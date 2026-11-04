#!/usr/bin/env python3
"""Montaggio del video TikTok di un episodio.
Uso: monta.py CARTELLA_EPISODIO [--anteprima]
Legge scene.json, voce/voce.wav, voce/tempi.json (da allinea.py) e immagini/ID.png.
Scrive CARTELLA/video.mp4 (1080x1920, 30 fps, H.264 + AAC, -14 LUFS) e CARTELLA/tempi-video.json.
Con --anteprima scrive solo un fotogramma per scena in CARTELLA/_lavoro/anteprima/ e un provino unico."""
import json, os, re, shutil, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comune import (BRAND, CX, FONTS, FPS, H, INK, PAPER, SAFE_L, SAFE_R, SUB_CY, TITLE_TOP, W, WHITE,  # noqa: E402
                    accento, carica_episodio, sillabe, tokens)

_fc = {}
ACC = (233, 164, 0)


def font(kind, size):
    k = (kind, size)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(FONTS[kind], size)
    return _fc[k]


def parse(markup):
    out, hi = [], False
    for part in re.split(r"(\*)", markup):
        if part == "*":
            hi = not hi
        elif part:
            out.append((part, hi))
    return out


def draw_rich(draw, cx, y, markup, fnt, base, stroke=0, stroke_fill=None):
    runs = parse(markup)
    widths = [draw.textlength(t, font=fnt) for t, _ in runs]
    x = cx - sum(widths) / 2
    for (t, hi), w in zip(runs, widths):
        draw.text((x, y), t, font=fnt, fill=ACC if hi else base, stroke_width=stroke, stroke_fill=stroke_fill)
        x += w


def righe_titolo(titolo):
    """Titolo: lista di righe. Ogni riga è "TESTO *ACCENTO*" oppure {"testo":..., "font":"mono", "dim":120}."""
    if isinstance(titolo, str):
        titolo = [titolo]
    base = {1: 150, 2: 115}.get(len(titolo), 95)
    out = []
    for r in titolo:
        if isinstance(r, dict):
            out.append((r["testo"], r.get("dim", base), r.get("font", "cond")))
        else:
            out.append((r, base, "mono" if re.fullmatch(r"[\s\d.,€%+\-→*]+", r) else "cond"))
    return out


# ---------- immagine di base ----------
def place(im, corner, sc, dy):
    canvas = Image.new("RGB", (W, H), corner)
    nw, nh = round(im.width * sc), round(im.height * sc)
    im2 = im.resize((nw, nh), Image.LANCZOS)
    x, y = (W - nw) // 2, H - nh + dy
    canvas.paste(im2, (x, y))
    return canvas


def content_top(canvas, corner):
    a = np.asarray(canvas).astype(int)
    diff = np.abs(a - np.array(corner)).sum(axis=2) > 90
    rows = np.where(diff.sum(axis=1) > 25)[0]
    return rows.min() if len(rows) else H


def base_canvas(path, title_bottom, scala=1.0):
    im = Image.open(path).convert("RGB")
    arr = np.asarray(im)
    corner = tuple(int(v) for v in np.median(arr[5:60, 5:60].reshape(-1, 3), axis=0))
    cover = max(W / im.width, H / im.height)
    rel, dy = scala, 0
    target = title_bottom + 45
    while True:                           # sposta in basso (max 320 px), poi rimpicciolisce
        canvas = place(im, corner, cover * rel, dy)
        if content_top(canvas, corner) >= target or rel < 0.7:
            return canvas
        if dy < 320:
            dy += 20
        else:
            rel -= 0.02


# ---------- livelli di testo ----------
def title_layer(scena):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    base = PAPER if scena["sfondo"] == "inchiostro" else INK
    righe = righe_titolo(scena["titolo"])
    maxw = SAFE_R - SAFE_L - 20
    k = 1.0
    for text, size, kind in righe:
        k = min(k, maxw / d.textlength(text.replace("*", ""), font=font(kind, size)))
    y = TITLE_TOP
    for text, size, kind in righe:
        size = int(size * k)
        draw_rich(d, CX, y, text, font(kind, size), base)
        y += int(size * 1.08)
    return lay, y


def sub_layer(markup):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = font("cond", 86)
    words = markup.split(" ")
    lines = [markup]
    if d.textlength(markup.replace("*", ""), font=f) > (SAFE_R - SAFE_L - 40):
        best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            if a.count("*") % 2:
                continue
            m = max(d.textlength(a.replace("*", ""), font=f), d.textlength(b.replace("*", ""), font=f))
            if best is None or m < best[0]:
                best = (m, [a, b])
        if best:
            lines = best[1]
    lh = 100
    y0 = SUB_CY - lh * len(lines) / 2 - 10
    for i, ln in enumerate(lines):
        draw_rich(d, CX, y0 + i * lh, ln, f, WHITE, stroke=9, stroke_fill=INK)
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


# ---------- tempi dei sottotitoli ----------
def silenzi_interni(audio, sr, a, b):
    seg = audio[int(a * sr):int(b * sr)]
    hop = int(0.01 * sr)
    if len(seg) <= hop:
        return []
    env = np.array([np.sqrt(np.mean(seg[i:i + hop] ** 2)) for i in range(0, len(seg) - hop, hop)])
    quiet = env < max(0.004, 0.07 * np.percentile(env, 95))
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


def tempi_sottotitoli(seg, subs, audio, sr):
    if seg.get("token_start"):            # tempi delle parole da Speech-to-Text
        ts, out, k = seg["token_start"], [], 0
        for disp, spoken in subs:
            out.append(ts[min(k, len(ts) - 1)])
            k += len(tokens(spoken or disp.replace("*", "")))
        out[0] = seg["start"]
        return out
    a, b = seg["start"], seg["end"]
    wts = [sum(sillabe(t) for t in tokens(sp or d.replace("*", ""))) + (1.5 if re.search(r"[,:.?!]$", d.strip()) else 0)
           for d, sp in subs]
    tot = sum(wts)
    starts, acc = [], a
    for w in wts:
        starts.append(acc)
        acc += (b - a) * w / tot
    sil = silenzi_interni(audio, sr, a, b)
    for k in range(1, len(subs)):
        if re.search(r"[,:.?!]$", subs[k - 1][0].strip()) and sil:
            near = min(sil, key=lambda s: abs(s - starts[k]))
            if abs(near - starts[k]) < 0.45:
                starts[k] = near
    return starts


# ---------- audio ----------
def colpo(sr, ref_peak):
    t = np.arange(int(0.35 * sr)) / sr
    f = 55 + 95 * np.exp(-t / 0.05)
    thud = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.07)
    noise = np.diff(np.random.default_rng(1).standard_normal(len(t)), prepend=0)
    sfx = thud * 0.8 + noise * np.exp(-t / 0.012) * 0.35
    return (sfx * 0.5 * ref_peak / np.abs(sfx).max()).astype(np.float32)


def loudnorm(inp, out, extra):
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", inp, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:"
          "linear=true,aresample=48000")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", inp, "-af", af] + extra + [out], check=True)


def main():
    global ACC
    ep = sys.argv[1]
    anteprima = "--anteprima" in sys.argv
    epi = carica_episodio(ep)
    ACC = accento(epi)
    SC = epi["scene"]
    T = json.load(open(os.path.join(ep, "voce", "tempi.json")))
    segs = T["segments"]
    assert len(segs) == len(SC), f"tempi per {len(segs)} scene, ma scene.json ne ha {len(SC)}: rilancia allinea.py"
    wav = os.path.join(ep, "voce", "voce.wav")
    with wave.open(wav) as wf:
        sr = wf.getframerate()
        audio = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    total = T["total"] + 0.4
    nfr = int(round(total * FPS))
    lav = os.path.join(ep, "_lavoro")
    os.makedirs(lav, exist_ok=True)

    shot_start = [0.0] + [max(0, s["start"] - 0.08) for s in segs[1:]]
    shot_end = shot_start[1:] + [total]
    sub_events = []
    for seg, sc in zip(segs, SC):
        for (disp, _), t in zip(sc["sottotitoli"], tempi_sottotitoli(seg, sc["sottotitoli"], audio, sr)):
            sub_events.append((t, disp))
    sub_events.sort()

    bases, titles, extras = [], [], []
    for sc in SC:
        tl, tb = title_layer(sc)
        img = os.path.join(ep, "immagini", f"{sc.get('immagine') or sc['id']}.png")
        bases.append(base_canvas(img, tb, sc.get("scala", 1.0)))
        titles.append(tl)
        extras.append(bubble_layer(500, tb + 60, (560, tb + 250), "But Why Finance?", 64) if sc.get("fumetto") else None)
    sub_cache = {}

    if anteprima:
        prev = os.path.join(lav, "anteprima")
        shutil.rmtree(prev, ignore_errors=True)
        os.makedirs(prev)
        frames = [int((shot_start[i] + shot_end[i]) / 2 * FPS) for i in range(len(SC))]
        proc = None
    else:
        muto = os.path.join(lav, "video_muto.mp4")
        proc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                 "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                                 "-crf", "18", "-pix_fmt", "yuv420p", muto], stdin=subprocess.PIPE)
        frames = range(nfr)
    salvati = []
    for fi in frames:
        t = fi / FPS
        i = max(k for k in range(len(SC)) if shot_start[k] <= t + 1e-6)
        p = (t - shot_start[i]) / max(0.01, shot_end[i] - shot_start[i])
        z = 1.0 + 0.04 * p                         # zoom lento 100% -> 104%
        bw, bh = W / z, H / z
        fx, fy = W / 2, H * 0.55
        box = (fx - bw * fx / W, fy - bh * fy / H, fx - bw * fx / W + bw, fy - bh * fy / H + bh)
        frame = bases[i].resize((W, H), Image.BICUBIC, box=box).convert("RGBA")
        if extras[i] is not None:
            frame.alpha_composite(extras[i])
        tl, age = titles[i], t - shot_start[i]
        if i == 0 and age < 0.2:                   # hook: piccolo "colpo" di scala
            s = 1.12 - 0.12 * (age / 0.2)
            tw, th = int(W * s), int(H * s)
            big = tl.resize((tw, th), Image.BICUBIC)
            cy = TITLE_TOP + 100
            ox = int((tw - W) * CX / W)
            oy = int(cy * s - cy)
            frame.alpha_composite(big.crop((ox, oy, ox + W, oy + H)))
        elif age < 4 / FPS and i > 0:              # dissolvenza del titolo in 4 fotogrammi
            a = np.asarray(tl).copy()
            a[..., 3] = (a[..., 3] * (age * FPS / 4)).astype(np.uint8)
            frame.alpha_composite(Image.fromarray(a))
        else:
            frame.alpha_composite(tl)
        cur = [d for (ts, d) in sub_events if ts <= t + 0.03]
        if cur:
            if cur[-1] not in sub_cache:
                sub_cache[cur[-1]] = sub_layer(cur[-1])
            frame.alpha_composite(sub_cache[cur[-1]])
        rgb = frame.convert("RGB")
        if anteprima:
            fp = os.path.join(prev, f"{i + 1:02d}.jpg")
            rgb.save(fp, quality=88)
            salvati.append(rgb)
        else:
            proc.stdin.write(rgb.tobytes())

    if anteprima:
        cols = 5
        rows = (len(salvati) + cols - 1) // cols
        tw, th = 270, 480
        sheet = Image.new("RGB", (cols * tw, rows * th), (60, 60, 60))
        for k, im in enumerate(salvati):
            sheet.paste(im.resize((tw, th)), ((k % cols) * tw, (k // cols) * th))
        sheet.save(os.path.join(prev, "provino.jpg"), quality=85)
        print("anteprima in", prev)
        return

    proc.stdin.close()
    proc.wait()
    # audio: colpo sull'hook + voce, normalizzato a -14 LUFS
    import soundfile as sf
    voice, vsr = sf.read(wav, dtype="float32")
    sfx = colpo(vsr, np.abs(voice).max())
    mix = np.concatenate([voice, np.zeros(int(1.0 * vsr), dtype=np.float32)])
    mix[:len(sfx)] += sfx
    sf.write(os.path.join(lav, "mix.wav"), mix, vsr)
    loudnorm(os.path.join(lav, "mix.wav"), os.path.join(lav, "mix_norm.wav"), [])
    loudnorm(wav, os.path.join(ep, "voce", "voce-normalizzata.mp3"), ["-b:a", "192k"])
    out = os.path.join(ep, "video.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.path.join(lav, "video_muto.mp4"), "-i",
                    os.path.join(lav, "mix_norm.wav"), "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    json.dump({"scene": [{"id": SC[k]["id"], "immagine": SC[k].get("immagine") or SC[k]["id"],
                          "inizio": round(shot_start[k], 3), "fine": round(shot_end[k], 3)} for k in range(len(SC))],
               "sottotitoli": [{"t": round(a, 3), "testo": b} for a, b in sub_events], "durata": round(total, 3),
               "metodo_allineamento": T.get("metodo")},
              open(os.path.join(ep, "tempi-video.json"), "w"), ensure_ascii=False, indent=1)
    print("video:", out, f"{total:.1f} s, {nfr} fotogrammi")


if __name__ == "__main__":
    main()
