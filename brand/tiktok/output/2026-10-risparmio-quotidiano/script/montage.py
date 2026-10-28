#!/usr/bin/env python3
"""Montaggio di un video TikTok di But Why Finance (versione 2, "risparmio quotidiano").

Uso:
  montage.py VOCE.wav PAROLE.json OUT.mp4                 video completo (senza audio) + OUT_tempi.json
  montage.py VOCE.wav PAROLE.json OUT.mp4 --preview DIR [T1 T2 ...]
                                                          solo alcuni fotogrammi in DIR (default: 0 s,
                                                          ogni taglio +0,2 s e l'ultimo)

PAROLE.json: [{"w", "start", "end"}, ...] una voce per parola parlata (da allinea.py o da ElevenLabs).
La configurazione (inquadrature, titoli, sottotitoli) e' in config_video.py nella stessa cartella,
le immagini in img/NN.png (1080x1920), i font in fonts/.

Cosa fa, fotogramma per fotogramma (Pillow -> ffmpeg, 1080x1920, 30 fps, H.264):
- inquadrature con taglio netto subito prima della parola indicata; ognuna e' una "vista" sulla
  sorgente (centro + zoom: <1 immagine intera rimpicciolita, >1 primo piano ritagliato), con un lento
  zoom continuo 100->106% (o 106->100% sull'ultima, per il loop) e un eventuale piccolo pan;
  un solo ricampionamento dalla sorgente (niente doppio ingrandimento);
- titolo in alto (zona sicura), con comparsa "pop" (90->100% e dissolvenza in 4 fotogrammi) solo quando
  cambia; al fotogramma 0 e' gia' pieno;
- sottotitoli 2-4 parole, bianchi con contorno inchiostro, parola chiave in ambra, comparsa pop
  90->100% in 3 fotogrammi, parole non ancora dette semitrasparenti (come nel riferimento principale);
- fumetto "But Why Finance?" facoltativo.
"""
import json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from config_video import SHOTS, SUBS, TITLES  # noqa: E402

W, H, FPS = 1080, 1920, 30
INK, PAPER, AMBER, BRAND, WHITE = (17, 20, 24), (244, 241, 234), (233, 164, 0), (0, 107, 60), (255, 255, 255)
SAFE_L, SAFE_R = 60, W - 130          # fascia destra (pulsanti TikTok) libera
CX = (SAFE_L + SAFE_R) // 2
TITLE_TOP = 215                       # sotto il 10% in alto (192 px)
SUB_CY = 1535                         # centro sottotitoli; il bordo basso resta sopra 1632 (15% in basso)
SUB_MAX_BOTTOM = 1628
SUB_SIZE, SUB_STROKE = 90, 10
ZOOM_MOVE = 0.06                      # 100% -> 106% su ogni inquadratura
DIM_MIX = 0.42                        # parole non ancora dette: bianco/ambra mescolato al 42% con l'inchiostro
PAD = 700                             # margine col colore del fondo attorno alla sorgente
F = {"cond": f"{S}/fonts/IBMPlexSansCondensed-Bold.ttf", "semi": f"{S}/fonts/IBMPlexSansCondensed-SemiBold.ttf",
     "mono": f"{S}/fonts/IBMPlexMono-Bold.ttf"}
_fc = {}


def font(kind, size):
    k = (kind, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(F[kind], size)
    return _fc[k]


# ---------- sorgenti ----------
_src = {}


def source(img):
    """Immagine con un margine PAD del colore del fondo (per le viste rimpicciolite)."""
    if img not in _src:
        im = Image.open(f"{S}/img/{img}.png").convert("RGB")
        a = np.asarray(im)
        corner = tuple(int(v) for v in np.median(a[5:60, 5:60].reshape(-1, 3), axis=0))
        big = Image.new("RGB", (im.width + 2 * PAD, im.height + 2 * PAD), corner)
        # bordo sfumato (80 px, solo sui pixel di fondo): la grana del fondo dell'immagine sfuma nel colore pieno del margine,
        # cosi' nelle viste rimpicciolite non si vede il rettangolo dell'immagine
        r = 80
        ramp = np.minimum(1, np.minimum(np.arange(im.width), np.arange(im.width)[::-1]) / r)
        rampy = np.minimum(1, np.minimum(np.arange(im.height), np.arange(im.height)[::-1]) / r)
        m = np.outer(rampy, ramp)
        m[np.abs(a.astype(int) - np.array(corner)).sum(axis=2) > 45] = 1   # il disegno non si sfuma mai
        mask = Image.fromarray((m * 255).astype(np.uint8))
        big.paste(im, (PAD, PAD), mask)
        lum = 0.299 * corner[0] + 0.587 * corner[1] + 0.114 * corner[2]
        _src[img] = (big, "ink" if lum < 100 else "paper")
    return _src[img]


def render_view(img, cx, cy, z, anchor=(W / 2, H / 2), z0=None):
    """Vista con zoom z; se z0 e' dato, il punto della sorgente che con zoom z0 sta in `anchor`
    resta fermo (lo zoom "cresce" attorno a quel punto dello schermo)."""
    big, _ = source(img)
    if z0 is not None:
        ax, ay = anchor
        sx, sy = cx + (ax - W / 2) / z0, cy + (ay - H / 2) / z0
        cx, cy = sx - (ax - W / 2) / z, sy - (ay - H / 2) / z
    bw, bh = W / z, H / z
    box = (PAD + cx - bw / 2, PAD + cy - bh / 2, PAD + cx + bw / 2, PAD + cy + bh / 2)
    return big.resize((W, H), Image.LANCZOS if z > 1 else Image.BICUBIC, box=box)


# ---------- testo ----------
def parse(markup):
    """'COSTA *24%* IN' -> [(parola, ambra?), ...] parola per parola"""
    out, hi = [], False
    for tok in markup.split(" "):
        h = hi
        if tok.startswith("*"):
            h, tok = True, tok[1:]
            hi = True
        if "*" in tok:
            tok = tok.replace("*", "")
            hi = False
        out.append((tok, h))
    return out


def title_layer(key, bg, pill=False):
    """Titolo centrato in alto. Ritorna (livello RGBA, y del bordo basso).
    pill=True: su una targhetta del colore del fondo (per i primi piani, dove dietro c'e' il disegno)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if key is None:
        return lay, TITLE_TOP
    d = ImageDraw.Draw(lay)
    base, stroke_col = (PAPER, INK) if bg == "ink" else (INK, PAPER)
    lines = TITLES[key]
    maxw = SAFE_R - SAFE_L - 20
    k = 1.0
    for runs in lines:
        wdt = sum(d.textlength(t, font=font(f, s)) for t, f, s, _ in runs)
        k = min(k, maxw / wdt)
    y = TITLE_TOP
    for runs in lines:
        sizes = [int(s * k) for _, _, s, _ in runs]
        fonts = [font(f, s) for (_, f, _, _), s in zip(runs, sizes)]
        widths = [d.textlength(t, font=fo) for (t, *_), fo in zip(runs, fonts)]
        asc = max(fo.getmetrics()[0] for fo in fonts)
        x = CX - sum(widths) / 2
        for (t, _, _, col), fo, wd in zip(runs, fonts, widths):
            d.text((x, y + asc), t, font=fo, fill=AMBER if col == "accent" else base, anchor="ls",
                   stroke_width=max(4, fo.size // 16), stroke_fill=stroke_col)
            x += wd
        y += int(max(sizes) * 1.12)
    if pill:
        bb = lay.getbbox()
        plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        fill = (INK if bg == "ink" else PAPER) + (238,)
        ImageDraw.Draw(plate).rounded_rectangle((bb[0] - 30, bb[1] - 22, bb[2] + 30, bb[3] + 22), radius=34, fill=fill)
        plate.alpha_composite(lay)
        lay = plate
    return lay, y


def sub_lines(markup, d, f):
    words = parse(markup)
    full = " ".join(w for w, _ in words)
    if d.textlength(full, font=f) <= SAFE_R - SAFE_L - 40 or len(words) < 2:
        return [words]
    best = None
    for i in range(1, len(words)):
        a, b = words[:i], words[i:]
        m = max(d.textlength(" ".join(w for w, _ in a), font=f), d.textlength(" ".join(w for w, _ in b), font=f))
        if best is None or m < best[0]:
            best = (m, [a, b])
    return best[1]


def sub_layer(markup, lit, cy):
    """Sottotitolo con le prime `lit` parole piene e le altre semitrasparenti."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", SUB_SIZE)
    lines = sub_lines(markup, d, f)
    lh = int(SUB_SIZE * 1.12)
    y0 = cy - lh * len(lines) / 2
    y0 = min(y0, SUB_MAX_BOTTOM - lh * len(lines))
    space = d.textlength(" ", font=f)
    n = 0
    for li, ln in enumerate(lines):
        widths = [d.textlength(w, font=f) for w, _ in ln]
        x = CX - (sum(widths) + space * (len(ln) - 1)) / 2
        for (w, hi), wd in zip(ln, widths):
            col = AMBER if hi else WHITE
            if n >= lit:                  # parola non ancora detta: stesso contorno, riempimento spento
                col = tuple(int(c * (1 - DIM_MIX) + k * DIM_MIX) for c, k in zip(col, INK))
            a = 255
            word = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(word).text((x, y0 + li * lh + lh / 2), w, font=f, fill=col, anchor="lm",
                                      stroke_width=SUB_STROKE, stroke_fill=INK + (a,))
            lay.alpha_composite(word)
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
    """Livello scalato di s attorno a (cx, cy), con opacita' alpha."""
    if abs(s - 1) < 1e-3 and alpha >= 0.999:
        return layer
    big = layer.resize((round(W * s), round(H * s)), Image.BICUBIC)
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.alpha_composite(big, dest=(0, 0), source=(round(cx * s - cx), round(cy * s - cy))) if s >= 1 else \
        out.alpha_composite(big, dest=(round(cx - cx * s), round(cy - cy * s)))
    if alpha < 0.999:
        a = np.asarray(out).copy()
        a[..., 3] = (a[..., 3] * alpha).astype(np.uint8)
        out = Image.fromarray(a)
    return out


def bbox_center(layer):
    bb = layer.getbbox()
    return ((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2) if bb else (W / 2, H / 2)


# ---------- tempi ----------
def timeline(words, total):
    starts = []
    for k, sh in enumerate(SHOTS):
        i = sh["parola"]
        if i == 0:
            starts.append(0.0)
            continue
        st = words[i]["start"]
        pause = st - words[i - 1]["end"] > 0.12
        starts.append(round(st - (0.08 if pause else 0.03), 3))
    ends = starts[1:] + [total]
    subs, wi = [], 0
    for m in SUBS:
        n = len(parse(m))
        ws = words[wi:wi + n]
        subs.append({"text": m, "start": ws[0]["start"], "words": [w["start"] for w in ws],
                     "spoken": " ".join(w["w"] for w in ws)})
        wi += n
    assert wi == len(words), f"i sottotitoli coprono {wi} parole su {len(words)}"
    for a, b in zip(subs, subs[1:]):
        a["end"] = b["start"]
    subs[-1]["end"] = min(total - 0.25, words[-1]["end"] + 0.15)
    return starts, ends, subs


def main():
    wav, pw, out = sys.argv[1], sys.argv[2], sys.argv[3]
    preview = None
    ptimes = []
    if len(sys.argv) > 5 and sys.argv[4] == "--preview":
        preview = sys.argv[5]
        ptimes = [float(x) for x in sys.argv[6:]]
    words = json.load(open(pw, encoding="utf-8"))
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                         "csv=p=0", wav]).decode())
    total = round(dur + 0.3, 3)
    nfr = int(round(total * FPS))
    starts, ends, subs = timeline(words, total)

    titles, tbottom = [], []
    for sh in SHOTS:
        _, bg = source(sh["img"])
        sh["_bg"] = bg
        tl, tb = title_layer(sh.get("title"), bg, sh.get("pill", False))
        titles.append(tl)
        tbottom.append(tb)
    bubbles = [bubble_layer(sh["bubble"][0], sh["bubble"][1], sh["bubble"][2:]) if sh.get("bubble") else None
               for sh in SHOTS]
    # da quando e' visibile il titolo (se uguale all'inquadratura prima, non si rianima)
    t_since = []
    for k, sh in enumerate(SHOTS):
        same = k > 0 and sh.get("title") == SHOTS[k - 1].get("title") and sh["_bg"] == SHOTS[k - 1]["_bg"]
        t_since.append(t_since[-1] if same else starts[k])
    sub_cache = {}

    if preview:
        os.makedirs(preview, exist_ok=True)
        if not ptimes:
            ptimes = [0.0] + [s + 0.2 for s in starts[1:]] + [total - 1 / FPS]
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
        p = (t - starts[i]) / max(0.01, ends[i] - starts[i])
        cx, cy, z = sh["view"]
        zf = 1 + ZOOM_MOVE * (1 - p if sh.get("moto") == "out" else p)
        dx, dy = sh.get("pan", (0, 0))
        frame = render_view(sh["img"], cx + dx * p, cy + dy * p, z * zf, sh.get("ancora", (W / 2, H / 2)), z).convert("RGBA")
        if bubbles[i] is not None:
            age = t - starts[i]
            frame.alpha_composite(scaled(bubbles[i], 0.9 + 0.1 * min(1, age / 0.15), *bbox_center(bubbles[i]),
                                         alpha=min(1, age / 0.1)) if age < 0.15 else bubbles[i])
        # titolo
        age = t - t_since[i]
        tl = titles[i]
        if fi > 0 and age < 4 / FPS:
            q = age * FPS / 4
            frame.alpha_composite(scaled(tl, 0.9 + 0.1 * q, CX, (TITLE_TOP + tbottom[i]) / 2, alpha=0.35 + 0.65 * q))
        else:
            frame.alpha_composite(tl)
        # sottotitolo
        cur = [s for s in subs if s["start"] <= t + 0.02 and t < s["end"]]
        if cur:
            s = cur[-1]
            lit = sum(1 for ws in s["words"] if ws <= t + 0.02)
            cyy = sh.get("sub_cy", SUB_CY)
            key = (s["text"], lit, cyy)
            if key not in sub_cache:
                sub_cache[key] = sub_layer(s["text"], lit, cyy)
            lay = sub_cache[key]
            sage = t - s["start"]
            if fi > 0 and sage < 3 / FPS:
                q = sage * FPS / 3
                lay = scaled(lay, 0.9 + 0.1 * q, CX, cyy, alpha=0.5 + 0.5 * q)
            frame.alpha_composite(lay)
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
                          "moto": SHOTS[k].get("moto", "in"), "titolo": SHOTS[k].get("title")}
                         for k in range(len(SHOTS))],
        "titoli": [{"titolo": SHOTS[k].get("title"), "da": t_since[k]} for k in range(len(SHOTS))
                   if k == 0 or t_since[k] != t_since[k - 1]],
        "sottotitoli": [{"testo": s["text"], "parlato": s["spoken"], "da": round(s["start"], 3),
                         "a": round(s["end"], 3), "parole": [round(x, 3) for x in s["words"]]} for s in subs],
        "effetti": [{"effetto": SHOTS[k]["sfx"], "t": starts[k]} for k in range(len(SHOTS)) if SHOTS[k].get("sfx")],
    }
    json.dump(tempi, open(os.path.splitext(out)[0] + "_tempi.json", "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    print("inquadrature", len(SHOTS), "fotogrammi", len(frames), "durata", total)


if __name__ == "__main__":
    main()
