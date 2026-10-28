#!/usr/bin/env python3
"""Montaggio del video TikTok "Il prezzo di... un caffè".
Uso: montage.py VOCE.wav TIMING.json OUT.mp4 [--preview DIR]
Rende ogni fotogramma con Pillow (immagine con zoom lento + titoli + sottotitoli) e lo passa a ffmpeg."""
import json, os, re, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from config_video import SHOTS  # noqa: E402

W, H, FPS = 1080, 1920, 30
INK, PAPER, AMBER, BRAND, WHITE = (17, 20, 24), (244, 241, 234), (233, 164, 0), (0, 107, 60), (255, 255, 255)
SAFE_L, SAFE_R = 60, W - 130          # fascia destra (pulsanti TikTok) libera
CX = (SAFE_L + SAFE_R) // 2
TITLE_TOP = 215                       # sotto il 10% in alto (192 px)
SUB_CY = 1440                         # sottotitoli: centro, sopra il 15% in basso (1632 px)
F = {"cond": f"{S}/fonts/IBMPlexSansCondensed-Bold.ttf", "semi": f"{S}/fonts/IBMPlexSansCondensed-SemiBold.ttf",
     "mono": f"{S}/fonts/IBMPlexMono-Bold.ttf"}
_fc = {}


def font(kind, size):
    k = (kind, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(F[kind], size)
    return _fc[k]


def parse(markup):
    """'COSTA *24%* IN' -> [(testo, ambra?), ...]"""
    out, hi = [], False
    for part in re.split(r"(\*)", markup):
        if part == "*":
            hi = not hi
        elif part:
            out.append((part, hi))
    return out


def draw_rich(draw, cx, y, markup, fnt, base, accent, stroke=0, stroke_fill=None):
    runs = parse(markup)
    widths = [draw.textlength(t, font=fnt) for t, _ in runs]
    x = cx - sum(widths) / 2
    for (t, hi), w in zip(runs, widths):
        draw.text((x, y), t, font=fnt, fill=accent if hi else base, stroke_width=stroke, stroke_fill=stroke_fill)
        x += w
    return sum(widths)


# ---------- immagini di base ----------
def place(im, corner, sc, dy):
    canvas = Image.new("RGB", (W, H), corner)
    nw, nh = round(im.width * sc), round(im.height * sc)
    im2 = im.resize((nw, nh), Image.LANCZOS)
    x = (W - nw) // 2
    y = H - nh + dy                      # ancorata in basso, spostata in giu' di dy
    canvas.paste(im2, (x, y))
    return canvas, x, y


def content_top(canvas, corner):
    a = np.asarray(canvas).astype(int)
    diff = np.abs(a - np.array(corner)).sum(axis=2) > 90
    rows = np.where(diff.sum(axis=1) > 25)[0]
    return rows.min() if len(rows) else H


def base_canvas(shot, title_bottom):
    im = Image.open(f"{S}/img/final/{shot['img']}.png").convert("RGB")
    arr = np.asarray(im)
    # colore reale del fondo dell'immagine (angolo in alto a sinistra) per non vedere giunture
    corner = tuple(int(v) for v in np.median(arr[5:60, 5:60].reshape(-1, 3), axis=0))
    cover = max(W / im.width, H / im.height)
    rel, dy = shot.get("scale", 1.0), shot.get("dy", 0)
    target = title_bottom + 45
    while True:                           # sposta in basso (max 320 px), poi rimpicciolisce
        canvas, x, y = place(im, corner, cover * rel, dy)
        if content_top(canvas, corner) >= target or rel < 0.7:
            break
        if dy < 320:
            dy += 20
        else:
            rel -= 0.02
    shot["_placed"] = (round(rel, 2), dy)
    return canvas, cover * rel, x, y


# ---------- livelli di testo (RGBA) ----------
def title_layer(shot):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    base = PAPER if shot["bg"] == "ink" else INK
    maxw = SAFE_R - SAFE_L - 20
    k = 1.0
    for text, size, kind in shot["title"]:
        wdt = d.textlength(text.replace("*", ""), font=font(kind, size))
        k = min(k, maxw / wdt)
    y = TITLE_TOP
    for text, size, kind in shot["title"]:
        size = int(size * k)
        f = font(kind, size)
        draw_rich(d, CX, y, text, f, base, AMBER)
        y += int(size * 1.08)
    return lay, y


def sub_layer(markup):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", 86)
    # al massimo due righe
    words = markup.split(" ")
    lines = [markup]
    if d.textlength(markup.replace("*", ""), font=f) > (SAFE_R - SAFE_L - 40):
        best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            # non spezzare dentro un *...*
            if a.count("*") % 2:
                continue
            m = max(d.textlength(a.replace("*", ""), font=f), d.textlength(b.replace("*", ""), font=f))
            if best is None or m < best[0]:
                best = (m, [a, b])
        lines = best[1]
    lh = 100
    y0 = SUB_CY - lh * len(lines) / 2 - 10
    for i, ln in enumerate(lines):
        draw_rich(d, CX, y0 + i * lh, ln, f, WHITE, AMBER, stroke=9, stroke_fill=INK)
    return lay


def receipts_layer(canvas_im):
    """Numeri sugli scontrini vuoti dell'immagine 04 (IBM Plex Mono)."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a = np.asarray(canvas_im).astype(int)
    white = (a.min(axis=2) > 247)
    boxes = []
    for x0, x1 in ((0, W // 2), (W // 2, W)):
        m = white[:, x0:x1]
        cols = np.where(m.sum(axis=0) > 200)[0]
        rows = np.where(m.sum(axis=1) > 60)[0]
        boxes.append((x0 + cols.min(), rows.min(), x0 + cols.max(), rows.max()))
    d = ImageDraw.Draw(lay)
    for (bx0, by0, bx1, by1), year, price, hi in zip(boxes, ("2021", "OGGI"), ("1,04 €", "1,29 €"), (False, True)):
        cx = (bx0 + bx1) / 2
        fs = font("mono", 34)
        fb = font("mono", 64)
        y = by0 + 40
        d.text((cx, y), "ESPRESSO", font=fs, fill=INK, anchor="mt")
        d.text((cx, y + 50), year, font=fs, fill=(110, 110, 110), anchor="mt")
        d.line((bx0 + 25, y + 110, bx1 - 25, y + 110), fill=(150, 150, 150), width=3)
        d.text((cx, y + 140), price, font=fb, fill=AMBER if hi else INK, anchor="mt")
    return lay


def labels_layer():
    """Etichette sopra le tre sagome dell'immagine 19."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", 44)
    for cx, t in LABEL_POS:
        wdt = d.textlength(t, font=f)
        cx = min(cx, SAFE_R - wdt / 2)
        cx = max(cx, SAFE_L + wdt / 2)
        d.text((cx, LABEL_Y), t, font=f, fill=INK, anchor="mb")
    return lay


def bubble_layer(x0, y0, tail, text, size):
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


LABEL_POS, LABEL_Y = [], 870


# ---------- tempi ----------
def syll(t):
    return max(1, len(re.findall(r"[aeiouàèéìòóù]+", t.lower())))


def internal_silences(audio, sr, a, b):
    seg = audio[int(a * sr):int(b * sr)]
    hop = int(0.01 * sr)
    env = np.array([np.sqrt(np.mean(seg[i:i + hop] ** 2)) for i in range(0, len(seg) - hop, hop)])
    quiet = env < 0.012
    out, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if j - i >= 7 and i > 0 and j < len(quiet):
                out.append(a + (i + j) / 2 * 0.01)
            i = j
        else:
            i += 1
    return out


def chunk_times(seg, subs, audio, sr):
    a, b = seg["start"], seg["end"]
    wts = []
    for disp, spoken in subs:
        t = spoken or disp.replace("*", "")
        wts.append(syll(t) + (1.5 if re.search(r"[,:.?]$", disp.strip()) else 0))
    tot = sum(wts)
    starts, acc = [], a
    for w in wts:
        starts.append(acc)
        acc += (b - a) * w / tot
    sil = internal_silences(audio, sr, a, b)
    for k in range(1, len(subs)):
        if re.search(r"[,:.?]$", subs[k - 1][0].strip()) and sil:
            near = min(sil, key=lambda s: abs(s - starts[k]))
            if abs(near - starts[k]) < 0.45:
                starts[k] = near
    return starts


def main():
    wav, timing, out = sys.argv[1], sys.argv[2], sys.argv[3]
    preview = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == "--preview" else None
    T = json.load(open(timing))
    segs = T["segments"]
    assert len(segs) == len(SHOTS), (len(segs), len(SHOTS))
    with wave.open(wav) as wf:
        sr = wf.getframerate()
        audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    total = T["total"] + 0.4
    nfr = int(round(total * FPS))

    # inizio delle inquadrature: 0,1 s prima della voce; il taglio cade nella pausa
    shot_start = [0.0] + [max(0, s["start"] - 0.08) for s in segs[1:]]
    shot_end = shot_start[1:] + [total]

    # eventi sottotitoli
    sub_events = []
    for seg, shot in zip(segs, SHOTS):
        st = chunk_times(seg, shot["subs"], audio, sr)
        for (disp, _), t in zip(shot["subs"], st):
            sub_events.append((t, disp))
    sub_events.sort()

    # precalcolo dei livelli
    bases, titles, extras = [], [], []
    for i, shot in enumerate(SHOTS):
        tl, tb = title_layer(shot)
        canvas, sc, ox, oy = base_canvas(shot, tb)
        print("inquadratura", i + 1, "immagine", shot["img"], "scala/dy", shot["_placed"])
        bases.append(canvas)
        titles.append(tl)
        ex = None
        if shot.get("receipts"):
            ex = receipts_layer(canvas)
        if shot.get("labels"):
            global LABEL_POS
            LABEL_POS = [(ox + fx * sc * 1152, t) for fx, t in ((0.18, "CLIENTE"), (0.48, "BAR"), (0.775, "TORREFATTORE"))]
            ex = labels_layer()
        if shot.get("bubble"):
            ex = bubble_layer(500, tb + 60, (560, tb + 250), "But Why Finance?", 64)
        extras.append(ex)
    sub_cache = {}

    if preview:
        os.makedirs(preview, exist_ok=True)

    proc = None
    if not preview:
        proc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                 "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                                 "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    frames = range(nfr) if not preview else [int((shot_start[i] + shot_end[i]) / 2 * FPS) for i in range(len(SHOTS))]
    for fi in frames:
        t = fi / FPS
        i = max(k for k in range(len(SHOTS)) if shot_start[k] <= t + 1e-6)
        p = (t - shot_start[i]) / max(0.01, shot_end[i] - shot_start[i])
        z = 1.0 + 0.04 * p                       # zoom lento 100% -> 104%
        bw, bh = W / z, H / z
        fx, fy = W / 2, H * 0.55                 # punto fisso dello zoom
        box = (fx - bw * fx / W, fy - bh * fy / H, fx - bw * fx / W + bw, fy - bh * fy / H + bh)
        frame = bases[i].resize((W, H), Image.BICUBIC, box=box).convert("RGBA")
        if extras[i] is not None:
            frame.alpha_composite(extras[i])
        # titolo: dissolvenza in 4 fotogrammi; sull'hook un piccolo "colpo" di scala
        tl = titles[i]
        age = t - shot_start[i]
        if SHOTS[i].get("pop") and age < 0.2:
            s = 1.12 - 0.12 * (age / 0.2)
            tw, th = int(W * s), int(H * s)
            big = tl.resize((tw, th), Image.BICUBIC)
            cy = TITLE_TOP + 100
            big = big.crop((int((tw - W) * CX / W), int(cy * s - cy), int((tw - W) * CX / W) + W, int(cy * s - cy) + H))
            frame.alpha_composite(big)
        elif age < 4 / FPS and i > 0:
            a = np.asarray(tl).copy()
            a[..., 3] = (a[..., 3] * (age * FPS / 4)).astype(np.uint8)
            frame.alpha_composite(Image.fromarray(a))
        else:
            frame.alpha_composite(tl)
        # sottotitolo corrente
        cur = [d for (ts, d) in sub_events if ts <= t + 0.03]
        if cur:
            key = cur[-1]
            if key not in sub_cache:
                sub_cache[key] = sub_layer(key)
            frame.alpha_composite(sub_cache[key])
        rgb = frame.convert("RGB")
        if preview:
            rgb.save(f"{preview}/f_{i + 1:02d}.jpg", quality=88)
        else:
            proc.stdin.write(rgb.tobytes())
    if proc:
        proc.stdin.close()
        proc.wait()
    json.dump({"shots": [{"n": k + 1, "img": SHOTS[k]["img"], "start": round(shot_start[k], 3),
                          "end": round(shot_end[k], 3)} for k in range(len(SHOTS))],
               "subs": [{"t": round(a, 3), "text": b} for a, b in sub_events], "duration": total},
              open(os.path.splitext(out)[0] + "_tempi.json", "w"), ensure_ascii=False, indent=1)
    print("fotogrammi", len(frames), "durata", total)


if __name__ == "__main__":
    main()
