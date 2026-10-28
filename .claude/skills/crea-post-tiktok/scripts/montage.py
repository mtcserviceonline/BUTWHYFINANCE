#!/usr/bin/env python3
"""Montaggio di un video TikTok di But Why Finance (versione 3: "risparmio quotidiano" v2).

Uso:
  montage.py VOCE.wav PAROLE.json OUT.mp4 [--forza]          video completo (senza audio) + OUT_tempi.json
  montage.py VOCE.wav PAROLE.json OUT.mp4 --preview DIR [T1 T2 ...]
                                                          solo alcuni fotogrammi in DIR (default: 0 s,
                                                          ogni taglio +0,2 s, ogni riga di titolo che entra
                                                          e l'ultimo)
  montage.py VOCE.wav PAROLE.json OUT.mp4 --solo-controlli   solo i controlli automatici

PAROLE.json: [{"w", "start", "end"}, ...] una voce per parola parlata (da allinea.py o da ElevenLabs).
La configurazione (inquadrature, titoli, scritte, sottotitoli, box degli occhiali, effetti) e' in
config_video.py nella stessa cartella; le immagini in img/NN.png (1080x1920), i font in fonts/.

Cosa fa, fotogramma per fotogramma (Pillow -> ffmpeg, 1080x1920, 30 fps, H.264):
- inquadrature con taglio netto subito prima della parola indicata (o alla fine di una parola, per il
  loop); ognuna e' una "vista" sulla sorgente (centro + zoom) con un lento zoom 100->104% che cresce
  attorno agli occhiali (che quindi restano fermi); un solo ricampionamento dalla sorgente;
- una sola transizione possibile ("tenda", 0,2 s), il resto tagli netti;
- titolo in alto (sotto il 10%), riga per riga: ogni riga puo' entrare con un "pop" sulla parola detta;
- "scritte" stampate sulla sorgente (es. il conto sullo scontrino), che compaiono sulle parole;
- sottotitoli 1-2 righe ancorati in basso sopra il 15% (bordo basso del testo <= 1632), parola chiave in
  ambra, parole non ancora dette spente, pop 90->100%;
- fumetto "But Why Finance?" facoltativo;
- il video finisce CODA s dopo l'ultima parola (A6: entro 0,5 s).

Controlli automatici (prima del render; con errori si ferma, salvo --forza), scritti anche in OUT_tempi.json:
- per ogni inquadratura (inizio, meta', fine): volto dell'orso tutto in campo, occhiali fuori dalla
  fascia destra (120 px, pulsanti TikTok) e non coperti da titoli, sottotitoli, fumetto o scritte;
- zoom effettivo <= zoom_max (default 1,20);
- testi nelle zone sicure: niente nel 10% in alto, nel 15% in basso, nella fascia destra di 120 px;
- distanza massima tra due cambi visivi (tagli, righe di titolo e scritte che entrano) <= 2 s (avviso);
- loop: ultima inquadratura con la stessa vista della prima e titolo del loop nella stessa posizione
  della prima riga del titolo d'apertura.
"""
import json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
import config_video as C  # noqa: E402

SHOTS, SUBS, TITLES = C.SHOTS, C.SUBS, C.TITLES
SCRITTE = getattr(C, "SCRITTE", {})
OCCHIALI = getattr(C, "OCCHIALI", {})
EFFETTI = getattr(C, "EFFETTI", [])

W, H, FPS = 1080, 1920, 30
INK, PAPER, AMBER, BRAND, WHITE = (17, 20, 24), (244, 241, 234), (233, 164, 0), (0, 107, 60), (255, 255, 255)
GREY = (110, 110, 110)
TOP_SAFE, BOTTOM_SAFE, RIGHT_BAND = 192, 1632, 120   # 10% in alto, 15% in basso, pulsanti a destra
SAFE_L, SAFE_R = 60, W - 130
CX = (SAFE_L + SAFE_R) // 2
TITLE_TOP = 215
SUB_BOTTOM = 1600                     # bordo basso del blocco sottotitoli (testo + contorno <= 1632)
SUB_SIZE, SUB_STROKE = 90, 10
ZOOM_MOVE = 0.04                      # 100% -> 104% su ogni inquadratura
ZOOM_MAX = 1.20
CODA = 0.45                           # secondi dopo l'ultima parola (A6: entro 0,5 s)
TENDA = 0.2                           # durata della transizione "tenda"
DIM_MIX = 0.42
PAD = 900
F = {"cond": f"{S}/fonts/IBMPlexSansCondensed-Bold.ttf", "semi": f"{S}/fonts/IBMPlexSansCondensed-SemiBold.ttf",
     "mono": f"{S}/fonts/IBMPlexMono-Bold.ttf"}
COL = {"ink": INK, "amber": AMBER, "grey": GREY, "paper": PAPER, "white": WHITE}
_fc = {}


def font(kind, size):
    k = (kind, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(F[kind], size)
    return _fc[k]


# ---------- parole ----------
def norm(w):
    return re.sub(r"[^\w']", "", w.lower().replace("’", "'"))


def trova(words, spec, da=0):
    """Indice della parola: int, "testo" (prima occorrenza da `da` in poi) o "testo#n" (n-esima nel testo)."""
    if isinstance(spec, int):
        return spec
    t, _, n = spec.partition("#")
    cand = [i for i, w in enumerate(words) if norm(w["w"]) == norm(t)]
    if not cand:
        raise SystemExit(f"parola non trovata nel testo: {spec!r}")
    if n:
        return cand[int(n) - 1]
    for i in cand:
        if i >= da:
            return i
    raise SystemExit(f"parola {spec!r} non trovata dopo la parola {da} ({words[da]['w']!r})")


# ---------- sorgenti ----------
_base, _src = {}, {}


def base(img):
    """Immagine con un margine PAD del colore del fondo (per le viste rimpicciolite)."""
    if img not in _base:
        im = Image.open(f"{S}/img/{img}.png").convert("RGB")
        a = np.asarray(im)
        corner = tuple(int(v) for v in np.median(a[5:60, 5:60].reshape(-1, 3), axis=0))
        big = Image.new("RGB", (im.width + 2 * PAD, im.height + 2 * PAD), corner)
        r = 80                         # la grana del fondo sfuma nel colore pieno del margine
        ramp = np.minimum(1, np.minimum(np.arange(im.width), np.arange(im.width)[::-1]) / r)
        rampy = np.minimum(1, np.minimum(np.arange(im.height), np.arange(im.height)[::-1]) / r)
        m = np.outer(rampy, ramp)
        m[np.abs(a.astype(int) - np.array(corner)).sum(axis=2) > 45] = 1
        big.paste(im, (PAD, PAD), Image.fromarray((m * 255).astype(np.uint8)))
        lum = 0.299 * corner[0] + 0.587 * corner[1] + 0.114 * corner[2]
        _base[img] = (big, "ink" if lum < 100 else "paper")
    return _base[img]


def scritta_box(s):
    """Box (coordinate sorgente) di una scritta."""
    if "linea" in s:
        x0, y0, x1, y1 = s["linea"]
        return (x0, y0 - 4, x1, y1 + 4)
    f = font(s["font"], s["size"])
    return ImageDraw.Draw(Image.new("L", (1, 1))).textbbox(s["xy"], s["testo"], font=f, anchor="mm")


def source(img, visibili=()):
    """Sorgente con le scritte visibili (indici in SCRITTE[img]) stampate sopra."""
    key = (img, tuple(visibili))
    if key not in _src:
        big, bg = base(img)
        if visibili:
            big = big.copy()
            d = ImageDraw.Draw(big)
            for k in visibili:
                s = SCRITTE[img][k]
                if "linea" in s:
                    x0, y0, x1, y1 = s["linea"]
                    d.line([(PAD + x0, PAD + y0), (PAD + x1, PAD + y1)], fill=INK, width=5)
                else:
                    d.text((PAD + s["xy"][0], PAD + s["xy"][1]), s["testo"], font=font(s["font"], s["size"]),
                           fill=COL[s.get("colore", "ink")], anchor="mm")
        _src[key] = (big, bg)
    return _src[key]


def view_at(sh, p):
    """(cx, cy, z) effettivi dell'inquadratura alla frazione p (0..1)."""
    cx, cy, z0 = sh["view"]
    moto = sh.get("moto", "in")
    zf = 1 + ZOOM_MOVE * (p if moto == "in" else (1 - p) if moto == "out" else 0)
    z = z0 * zf
    dx, dy = sh.get("pan", (0, 0))
    cx, cy = cx + dx * p, cy + dy * p
    if "ancora" in sh:
        ax, ay = sh["ancora"]
    elif sh["img"] in OCCHIALI:
        g = OCCHIALI[sh["img"]]["occhiali"]
        ax, ay = ((g[0] + g[2]) / 2 - cx) * z0 + W / 2, ((g[1] + g[3]) / 2 - cy) * z0 + H / 2
    else:
        ax, ay = W / 2, H / 2
    sx, sy = cx + (ax - W / 2) / z0, cy + (ay - H / 2) / z0
    return sx - (ax - W / 2) / z, sy - (ay - H / 2) / z, z


def to_screen(box, v):
    cx, cy, z = v
    return ((box[0] - cx) * z + W / 2, (box[1] - cy) * z + H / 2, (box[2] - cx) * z + W / 2, (box[3] - cy) * z + H / 2)


def render_view(img, v, visibili=()):
    big, _ = source(img, visibili)
    cx, cy, z = v
    bw, bh = W / z, H / z
    box = (PAD + cx - bw / 2, PAD + cy - bh / 2, PAD + cx + bw / 2, PAD + cy + bh / 2)
    return big.resize((W, H), Image.LANCZOS if z > 1 else Image.BICUBIC, box=box)


# ---------- testo ----------
def parse(markup):
    """'IN MEDIA *1,29_€*{3}.' -> [(testo, ambra?, parole parlate), ...]"""
    out, hi = [], False
    for tok in markup.split(" "):
        n = 1
        m = re.search(r"\{(\d+)\}", tok)
        if m:
            n, tok = int(m.group(1)), tok.replace(m.group(0), "")
        h = hi
        if tok.startswith("*"):
            h, tok = True, tok[1:]
            hi = True
        if "*" in tok:
            tok = tok.replace("*", "")
            hi = False
        out.append((tok.replace("_", " "), h, n))
    return out


def title_lines(key):
    out = []
    for ln in TITLES[key]:
        out.append((ln["runs"], ln.get("parola")) if isinstance(ln, dict) else (ln, None))
    return out


def title_layers(key, bg, top, pill=False):
    """Un livello RGBA per riga del titolo. Ritorna [(livello, bbox)], y del bordo basso."""
    if key is None:
        return [], top
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    base_col, stroke_col = (PAPER, INK) if bg == "ink" else (INK, PAPER)
    lines = title_lines(key)
    maxw = SAFE_R - SAFE_L - 20
    k = 1.0
    for runs, _ in lines:
        wdt = sum(probe.textlength(t, font=font(f, s)) for t, f, s, _ in runs)
        k = min(k, maxw / wdt)
    y, out = top, []
    for runs, _ in lines:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(lay)
        sizes = [int(s * k) for _, _, s, _ in runs]
        fonts = [font(f, s) for (_, f, _, _), s in zip(runs, sizes)]
        widths = [d.textlength(t, font=fo) for (t, *_), fo in zip(runs, fonts)]
        asc = max(fo.getmetrics()[0] for fo in fonts)
        x = CX - sum(widths) / 2
        for (t, _, _, col), fo, wd in zip(runs, fonts, widths):
            d.text((x, y + asc), t, font=fo, fill=AMBER if col == "accent" else base_col, anchor="ls",
                   stroke_width=max(4, fo.size // 16), stroke_fill=stroke_col)
            x += wd
        y += int(max(sizes) * 1.12)
        if pill:
            bb = lay.getbbox()
            plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            fill = (INK if bg == "ink" else PAPER) + (238,)
            ImageDraw.Draw(plate).rounded_rectangle((bb[0] - 30, bb[1] - 16, bb[2] + 30, bb[3] + 16), radius=30,
                                                    fill=fill)
            plate.alpha_composite(lay)
            lay = plate
        out.append((lay, lay.getbbox()))
    return out, y


def sub_lines(words, d, f):
    full = " ".join(w for w, _, _ in words)
    if d.textlength(full, font=f) <= SAFE_R - SAFE_L - 40 or len(words) < 2:
        return [words]
    best = None
    for i in range(1, len(words)):
        a, b = words[:i], words[i:]
        m = max(d.textlength(" ".join(w for w, _, _ in a), font=f), d.textlength(" ".join(w for w, _, _ in b), font=f))
        if best is None or m < best[0]:
            best = (m, [a, b])
    return best[1]


def sub_layer(markup, lit, bottom):
    """Sottotitolo: prime `lit` parole mostrate piene, le altre spente. Blocco ancorato in basso."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", SUB_SIZE)
    lines = sub_lines(parse(markup), d, f)
    maxw = SAFE_R - SAFE_L - 20
    space = d.textlength(" ", font=f)
    larg = max(sum(d.textlength(w, font=f) for w, _, _ in ln) + space * (len(ln) - 1) for ln in lines)
    size = SUB_SIZE if larg <= maxw else int(SUB_SIZE * maxw / larg)   # riga troppo lunga: font piu' piccolo
    f = font("cond", size)
    lh = int(SUB_SIZE * 1.12)
    y0 = bottom - lh * len(lines)
    space = d.textlength(" ", font=f)
    stroke = max(6, round(SUB_STROKE * size / SUB_SIZE))
    n = 0
    for li, ln in enumerate(lines):
        widths = [d.textlength(w, font=f) for w, _, _ in ln]
        x = CX - (sum(widths) + space * (len(ln) - 1)) / 2
        for (w, hi, _), wd in zip(ln, widths):
            col = AMBER if hi else WHITE
            if n >= lit:
                col = tuple(int(c * (1 - DIM_MIX) + k * DIM_MIX) for c, k in zip(col, INK))
            d.text((x, y0 + li * lh + lh / 2), w, font=f, fill=col, anchor="lm", stroke_width=stroke,
                   stroke_fill=INK)
            x += wd + space
            n += 1
    return lay


def bubble_layer(x0, y0, tail, text="But Why Finance?", size=60):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", size)
    tw = d.textlength(text, font=f)
    x1, y1 = x0 + tw + 70, y0 + int(size * 1.9)
    if x1 > SAFE_R:
        x0, x1 = x0 - (x1 - SAFE_R), SAFE_R
    d.polygon([(x0 + 50, y1 - 4), (x0 + 130, y1 - 4), tail], fill=BRAND)
    d.line([(x0 + 50, y1), tail, (x0 + 130, y1)], fill=PAPER, width=5, joint="curve")
    d.rounded_rectangle((x0, y0, x1, y1), radius=40, fill=BRAND, outline=PAPER, width=5)
    d.polygon([(x0 + 55, y1 - 6), (x0 + 125, y1 - 6), tail], fill=BRAND)
    d.text(((x0 + x1) / 2, (y0 + y1) / 2), text, font=f, fill=WHITE, anchor="mm")
    return lay


def scaled(layer, s, cx, cy, alpha=1.0):
    if abs(s - 1) < 1e-3 and alpha >= 0.999:
        return layer
    big = layer.resize((round(W * s), round(H * s)), Image.BICUBIC)
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if s >= 1:
        out.alpha_composite(big, dest=(0, 0), source=(round(cx * s - cx), round(cy * s - cy)))
    else:
        out.alpha_composite(big, dest=(round(cx - cx * s), round(cy - cy * s)))
    if alpha < 0.999:
        a = np.asarray(out).copy()
        a[..., 3] = (a[..., 3] * alpha).astype(np.uint8)
        out = Image.fromarray(a)
    return out


def bbox_center(bb):
    return ((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2)


def pop(layer, bb, age, n=4):
    """Comparsa 90->100% e dissolvenza in n fotogrammi."""
    if age >= n / FPS:
        return layer
    q = max(0.0, age * FPS / n)
    return scaled(layer, 0.9 + 0.1 * q, *bbox_center(bb), alpha=0.35 + 0.65 * q)


# ---------- tempi ----------
def timeline(words):
    total = round(words[-1]["end"] + CODA, 3)
    starts, idx, prev = [], [], 0
    for k, sh in enumerate(SHOTS):
        if k == 0:
            starts.append(0.0)
            idx.append(0)
            continue
        if "dopo" in sh:
            i = trova(words, sh["dopo"], prev)
            starts.append(round(words[i]["end"] + sh.get("dopo_offset", 0.0), 3))
        else:
            i = trova(words, sh["parola"], prev + 1 if isinstance(sh["parola"], str) else 0)
            st = words[i]["start"]
            pause = st - words[i - 1]["end"] > 0.12
            starts.append(round(st - (0.08 if pause else 0.03), 3))
        idx.append(i)
        prev = i
    ends = starts[1:] + [total]
    for k in range(len(SHOTS)):
        if ends[k] <= starts[k]:
            raise SystemExit(f"inquadratura {k + 1} ({SHOTS[k]['img']}) di durata nulla: controlla le parole")
    subs, wi = [], 0
    for m in SUBS:
        toks = parse(m)
        n = sum(t[2] for t in toks)
        ws = words[wi:wi + n]
        if len(ws) < n:
            raise SystemExit(f"i sottotitoli hanno piu' parole del parlato (fino a {m!r})")
        tstart, j = [], 0
        for t in toks:
            tstart.append(ws[j]["start"])
            j += t[2]
        subs.append({"text": m, "start": ws[0]["start"], "words": tstart, "spoken": " ".join(w["w"] for w in ws)})
        wi += n
    if wi != len(words):
        raise SystemExit(f"i sottotitoli coprono {wi} parole su {len(words)}: SUBS e testo non tornano")
    for a, b in zip(subs, subs[1:]):
        a["end"] = b["start"]
    subs[-1]["end"] = total
    return starts, ends, idx, subs, total


def main():
    wav, pw, out = sys.argv[1], sys.argv[2], sys.argv[3]
    args = sys.argv[4:]
    forza = "--forza" in args
    solo_controlli = "--solo-controlli" in args
    preview, ptimes = None, []
    if "--preview" in args:
        k = args.index("--preview")
        preview = args[k + 1]
        ptimes = [float(x) for x in args[k + 2:] if not x.startswith("--")]
    words = json.load(open(pw, encoding="utf-8"))
    starts, ends, idx, subs, total = timeline(words)
    nfr = int(round(total * FPS))

    # titoli: livelli per riga, tempi d'ingresso delle righe
    t_since, chain_word = [], []
    for k, sh in enumerate(SHOTS):
        _, bg = base(sh["img"])
        sh["_bg"] = bg
        same = (k > 0 and sh.get("title") == SHOTS[k - 1].get("title") and bg == SHOTS[k - 1]["_bg"]
                and sh.get("title_y") == SHOTS[k - 1].get("title_y"))
        t_since.append(t_since[-1] if same else starts[k])
        chain_word.append(chain_word[-1] if same else idx[k])
    titles = []
    for k, sh in enumerate(SHOTS):
        lays, _ = title_layers(sh.get("title"), sh["_bg"], sh.get("title_y", TITLE_TOP), sh.get("pill", False))
        lines = title_lines(sh["title"]) if sh.get("title") else []
        tl = []
        for (lay, bb), (_, parola) in zip(lays, lines):
            t_in = t_since[k] if parola is None else max(t_since[k], words[trova(words, parola, chain_word[k])]["start"])
            tl.append((lay, bb, round(t_in, 3)))
        titles.append(tl)
    bubbles = [bubble_layer(sh["bubble"][0], sh["bubble"][1], sh["bubble"][2:]) if sh.get("bubble") else None
               for sh in SHOTS]
    bub_t = [max(starts[k], words[trova(words, sh["bubble_parola"], idx[k])]["start"]) if sh.get("bubble_parola")
             else starts[k] for k, sh in enumerate(SHOTS)]
    scr_t = {img: [None if s.get("parola") is None else words[trova(words, s["parola"])]["start"] for s in lst]
             for img, lst in SCRITTE.items()}

    def visibili(img, t):
        return tuple(k for k, ts in enumerate(scr_t.get(img, [])) if ts is None or ts <= t + 0.02)

    # ---------- controlli ----------
    errori, avvisi = [], []
    sub_bb = {}
    for s in subs:
        bottom = None
        for k in range(len(SHOTS)):          # il sottotitolo usa il sub_bottom dell'inquadratura in cui compare
            if starts[k] <= s["start"] + 0.02 < ends[k] or (k == len(SHOTS) - 1 and s["start"] >= starts[k]):
                bottom = SHOTS[k].get("sub_bottom", SUB_BOTTOM)
        s["_bottom"] = bottom or SUB_BOTTOM
        sub_bb[s["text"]] = sub_layer(s["text"], 99, s["_bottom"]).getbbox()
        bb = sub_bb[s["text"]]
        if bb[3] > BOTTOM_SAFE or bb[2] > W - RIGHT_BAND or bb[0] < 40:
            errori.append(f"sottotitolo {s['text']!r} fuori dalle zone sicure: {bb}")

    def inter(a, b, m=6):
        return not (a[2] + m <= b[0] or b[2] + m <= a[0] or a[3] + m <= b[1] or b[3] + m <= a[1])
    righe = []
    for k, sh in enumerate(SHOTS):
        nome = f"inq. {k + 1:2d} ({sh['img']}, {starts[k]:.2f}-{ends[k]:.2f} s)"
        for lay, bb, _ in titles[k]:
            if bb[1] < TOP_SAFE or bb[2] > W - RIGHT_BAND or bb[3] > BOTTOM_SAFE:
                errori.append(f"{nome}: titolo fuori dalle zone sicure {bb}")
        g = OCCHIALI.get(sh["img"])
        zmax = sh.get("zoom_max", ZOOM_MAX)
        shot_subs = [s for s in subs if s["start"] < ends[k] and s["end"] > starts[k]]
        info = {"n": k + 1, "img": sh["img"], "zoom_max_effettivo": 0}
        for p in (0.0, 0.5, 1.0):
            v = view_at(sh, p)
            info["zoom_max_effettivo"] = max(info["zoom_max_effettivo"], round(v[2], 3))
            if v[2] > zmax + 1e-6:
                errori.append(f"{nome}: zoom {v[2]:.2f} oltre il massimo {zmax:.2f}")
            t = starts[k] + p * (ends[k] - starts[k])
            for kk in visibili(sh["img"], t):
                s = SCRITTE[sh["img"]][kk]
                sb = to_screen(scritta_box(s), v)
                if sb[1] < TOP_SAFE or sb[3] > BOTTOM_SAFE or sb[2] > W - RIGHT_BAND or sb[0] < 0:
                    errori.append(f"{nome} p={p}: scritta {s.get('testo', 'linea')!r} fuori dalle zone sicure "
                                  f"({', '.join(str(round(c)) for c in sb)})")
            if not g:
                continue
            ob, vb = to_screen(g["occhiali"], v), to_screen(g["volto"], v)
            if p == 0.0:
                info["occhiali"] = [round(c) for c in ob]
            if vb[0] < 0 or vb[1] < 0 or vb[2] > W or vb[3] > H:
                errori.append(f"{nome} p={p}: volto tagliato dal bordo ({', '.join(str(round(c)) for c in vb)})")
            if ob[2] > W - RIGHT_BAND or ob[1] < TOP_SAFE * 0.5 or ob[3] > BOTTOM_SAFE:
                errori.append(f"{nome} p={p}: occhiali in una fascia coperta dall'interfaccia "
                              f"({', '.join(str(round(c)) for c in ob)})")
            ostacoli = [("titolo", bb) for _, bb, _ in titles[k]]
            ostacoli += [(f"sottotitolo {s['text']!r}", sub_bb[s["text"]]) for s in shot_subs]
            if bubbles[k] is not None:
                ostacoli.append(("fumetto", bubbles[k].getbbox()))
            for kk in visibili(sh["img"], t):
                s = SCRITTE[sh["img"]][kk]
                ostacoli.append((f"scritta {s.get('testo', 'linea')!r}", to_screen(scritta_box(s), v)))
            for nm, bb in ostacoli:
                if inter(ob, bb):
                    errori.append(f"{nome} p={p}: {nm} copre gli occhiali")
        righe.append(info)
    cambi = sorted(set([0.0] + starts + bub_t + [t for tl in titles for _, _, t in tl]
                       + [t for v in scr_t.values() for t in v if t is not None]))
    cambi = [c for c in cambi if c < total] + [total]
    gap = max(b - a for a, b in zip(cambi, cambi[1:]))
    gi = max(range(len(cambi) - 1), key=lambda i: cambi[i + 1] - cambi[i])
    if gap > 2.0 + 1e-6:
        avvisi.append(f"cambio visivo piu' lontano: {gap:.2f} s ({cambi[gi]:.2f}-{cambi[gi + 1]:.2f} s), oltre 2 s")
    # loop
    loop = {}
    if SHOTS[-1]["view"] != SHOTS[0]["view"] or SHOTS[-1]["img"] != SHOTS[0]["img"]:
        avvisi.append("loop: l'ultima inquadratura non ha la stessa vista della prima")
    if SHOTS[-1].get("moto") != "fermo" or SHOTS[0].get("moto", "in") == "out":
        avvisi.append("loop: l'ultima inquadratura dovrebbe essere ferma e uguale al primo fotogramma")
    if titles[0] and titles[-1]:
        c0, c1 = bbox_center(titles[0][0][1]), bbox_center(titles[-1][0][1])
        loop = {"centro_titolo_apertura": [round(c) for c in c0], "centro_titolo_loop": [round(c) for c in c1],
                "baseline_uguale": titles[0][0][1][3] - titles[-1][0][1][3]}
        if abs(c0[0] - c1[0]) > 4:
            avvisi.append(f"loop: titolo finale non centrato come quello d'apertura ({c0} vs {c1})")
    controlli = {"errori": errori, "avvisi": avvisi, "cambio_visivo_max_s": round(gap, 2),
                 "fine_dopo_ultima_parola_s": round(total - words[-1]["end"], 3), "loop": loop,
                 "inquadrature": righe}
    for e in errori:
        print("ERRORE:", e)
    for a in avvisi:
        print("avviso:", a)
    print(f"controlli: {len(errori)} errori, {len(avvisi)} avvisi; cambio visivo max {gap:.2f} s; "
          f"fine {total - words[-1]['end']:.2f} s dopo l'ultima parola")
    if solo_controlli:
        return
    if errori and not forza and not preview:
        raise SystemExit("controlli non superati: correggi config_video.py (o --forza)")

    # ---------- render ----------
    sub_cache = {}

    def compose(i, t, fi, with_sub=True, p_override=None):
        sh = SHOTS[i]
        p = (t - starts[i]) / max(0.01, ends[i] - starts[i]) if p_override is None else p_override
        v = view_at(sh, min(1.0, max(0.0, p)))
        frame = render_view(sh["img"], v, visibili(sh["img"], t)).convert("RGBA")
        if bubbles[i] is not None and t + 1e-6 >= bub_t[i]:
            age = t - bub_t[i]
            frame.alpha_composite(pop(bubbles[i], bubbles[i].getbbox(), age, 5) if fi > 0 else bubbles[i])
        for lay, bb, t_in in titles[i]:
            if t + 1e-6 < t_in:
                continue
            age = t - t_in
            frame.alpha_composite(pop(lay, bb, age) if fi > 0 else lay)
        if with_sub:
            cur = [s for s in subs if s["start"] <= t + 0.02 and t < s["end"]]
            if cur:
                s = cur[-1]
                lit = sum(1 for ws in s["words"] if ws <= t + 0.02)
                key = (s["text"], lit, s["_bottom"])
                if key not in sub_cache:
                    sub_cache[key] = sub_layer(s["text"], lit, s["_bottom"])
                lay = sub_cache[key]
                sage = t - s["start"]
                if fi > 0 and sage < 3 / FPS:
                    q = sage * FPS / 3
                    bb = sub_bb[s["text"]]
                    lay = scaled(lay, 0.9 + 0.1 * q, CX, (bb[1] + bb[3]) / 2, alpha=0.5 + 0.5 * q)
                frame.alpha_composite(lay)
        return frame

    if preview:
        os.makedirs(preview, exist_ok=True)
        if not ptimes:
            ptimes = [0.0] + [s + 0.2 for s in starts[1:]] + [t + 0.2 for tl in titles for _, _, t in tl] \
                     + [t + 0.2 for t in bub_t] \
                     + [total - 1 / FPS]
        frames = sorted({min(nfr - 1, int(round(t * FPS))) for t in ptimes})
        proc = None
    else:
        frames = range(nfr)
        proc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                 "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                                 "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
                                stdin=subprocess.PIPE)
    for fi in frames:
        t = fi / FPS
        i = max(k for k in range(len(SHOTS)) if starts[k] <= t + 1e-6)
        sh = SHOTS[i]
        if sh.get("transizione") == "tenda" and i > 0 and t - starts[i] < TENDA:
            q = (t - starts[i]) / TENDA
            q = q * q * (3 - 2 * q)
            old = compose(i - 1, starts[i] - 1 / FPS, fi, with_sub=False, p_override=1.0)
            new = compose(i, t, fi, with_sub=False)
            edge = int(H * (1 - q))
            mask = Image.new("L", (W, H), 0)
            ImageDraw.Draw(mask).rectangle((0, edge, W, H), fill=255)
            frame = Image.composite(new, old, mask)
            ImageDraw.Draw(frame).rectangle((0, edge - 6, W, edge), fill=AMBER + (255,))
            cur_s = [s for s in subs if s["start"] <= t + 0.02 and t < s["end"]]   # sottotitolo sopra la tenda
            if cur_s:
                s = cur_s[-1]
                lit = sum(1 for ws in s["words"] if ws <= t + 0.02)
                frame.alpha_composite(sub_layer(s["text"], lit, s["_bottom"]))
        else:
            frame = compose(i, t, fi)
        rgb = frame.convert("RGB")
        if preview:
            rgb.save(f"{preview}/t{t:06.2f}_s{i + 1:02d}.jpg", quality=90)
        else:
            proc.stdin.write(rgb.tobytes())
    if proc:
        proc.stdin.close()
        proc.wait()
    tempi = {
        "durata": total, "fps": FPS,
        "inquadrature": [{"n": k + 1, "img": SHOTS[k]["img"], "inizio": starts[k], "fine": round(ends[k], 3),
                          "durata": round(ends[k] - starts[k], 3), "vista": SHOTS[k]["view"],
                          "moto": SHOTS[k].get("moto", "in"), "titolo": SHOTS[k].get("title"),
                          "transizione": SHOTS[k].get("transizione")} for k in range(len(SHOTS))],
        "titoli": [{"titolo": SHOTS[k].get("title"), "riga": r + 1, "da": t_in}
                   for k in range(len(SHOTS)) for r, (_, _, t_in) in enumerate(titles[k])
                   if k == 0 or t_since[k] != t_since[k - 1]],
        "scritte": [{"img": img, "testo": s.get("testo", "linea"), "da": scr_t[img][k]}
                    for img, lst in SCRITTE.items() for k, s in enumerate(lst)],
        "sottotitoli": [{"testo": s["text"], "parlato": s["spoken"], "da": round(s["start"], 3),
                         "a": round(s["end"], 3), "parole": [round(x, 3) for x in s["words"]]} for s in subs],
        "effetti": [{"effetto": e, "parola": p, "t": round(words[trova(words, p)]["start"], 3)} for e, p in EFFETTI],
        "controlli": controlli,
    }
    json.dump(tempi, open(os.path.splitext(out)[0] + "_tempi.json", "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    print("inquadrature", len(SHOTS), "fotogrammi", len(frames), "durata", total)


if __name__ == "__main__":
    main()
