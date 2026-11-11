#!/usr/bin/env python3
"""Dittico "buco nero": due poster A3 complementari, in bianco e nero.

L'immagine è calcolata da zero: per ogni pixel si segue un raggio di luce
attorno a un buco nero (metrica di Schwarzschild) e si somma la luce del disco
di materia che il raggio attraversa. Nessuna immagine di partenza.

Output:
- poster/stampa/dittico-buco-nero-sinistra.pdf / -destra.pdf   (A3)
- poster/vinted/dittico-buco-nero/design-sinistra.jpg, design-destra.jpg,
  design-insieme.jpg, mockup-<parete>.jpg

Uso (dalla radice del repo):  python3 poster/script/make_dittico.py [dpi]
dpi predefinito 300 (qualche minuto di calcolo); 40 per un'anteprima veloce.
"""

import math
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
STAMPA = ROOT / "poster" / "stampa"
OUT = ROOT / "poster" / "vinted" / "dittico-buco-nero"
NAME = "dittico-buco-nero"

# --- scena (unità: raggio dell'orizzonte = 1) ---
HALF_W = 10.0                 # metà larghezza del dittico
CAM_DIST = 50.0
INCL = math.radians(83.5)     # inclinazione della vista rispetto all'asse del disco
ROLL = math.radians(-24.0)    # rotazione dell'inquadratura
R_IN, R_OUT = 2.3, 11.5
STREAM_PHI, STREAM_LEN, STREAM_W = 2.25, 12.0, 0.55   # scia di materia
SPIRAL = 1.4
BETA = 0.30                   # asimmetria di luminosità dovuta alla rotazione
EXPOSURE = 1.9

rng = np.random.default_rng(7)
LOG_MIN, LOG_MAX = math.log(R_IN * 0.9), math.log(R_OUT + STREAM_LEN + 2)
TABLES = [(rng.standard_normal((nr, nphi)), w)
          for nr, nphi, w in [(40, 7, 0.9), (220, 11, 0.8), (1100, 17, 0.7), (5200, 23, 0.6)]]


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def texture(rho, phi):
    """Filamenti: rumore molto allungato lungo la rotazione, con leggera spirale."""
    lr = np.log(rho)
    x = np.clip((lr - LOG_MIN) / (LOG_MAX - LOG_MIN), 0, 0.99999)
    ang = (phi + SPIRAL * lr) / (2 * math.pi)
    tot = np.zeros_like(rho)
    for tab, w in TABLES:
        nr, nphi = tab.shape
        fx = x * (nr - 1)
        i0 = fx.astype(np.int64)
        tx = fx - i0
        fy = (ang % 1.0) * nphi
        j0 = fy.astype(np.int64) % nphi
        ty = fy - np.floor(fy)
        ty = ty * ty * (3 - 2 * ty)
        j1 = (j0 + 1) % nphi
        a = tab[i0, j0] * (1 - tx) + tab[i0 + 1, j0] * tx
        b = tab[i0, j1] * (1 - tx) + tab[i0 + 1, j1] * tx
        tot += w * (a * (1 - ty) + b * ty)
    return np.exp(0.75 * tot)


def emission(rho, phi):
    dphi = np.angle(np.exp(1j * (phi - STREAM_PHI)))
    r_out = R_OUT + STREAM_LEN * np.exp(-(dphi / STREAM_W) ** 2)
    mask = smoothstep(R_IN, R_IN * 1.25, rho) * (1 - smoothstep(r_out * 0.45, r_out, rho))
    base = (rho / R_IN) ** -1.6
    beta = BETA * np.sqrt(R_IN / rho)
    doppler = (1.0 / (1.0 + beta * np.cos(phi) * math.sin(INCL))) ** 3
    e = mask * base * texture(rho, phi) * doppler
    return e, 0.8 * mask


def camera_dirs(u, v):
    cam = CAM_DIST * np.array([0.0, -math.sin(INCL), math.cos(INCL)])
    fwd = -cam / CAM_DIST
    right = np.array([1.0, 0.0, 0.0])
    up = np.cross(right, fwd)
    cr, sr = math.cos(ROLL), math.sin(ROLL)
    r2, u2 = cr * right + sr * up, -sr * right + cr * up
    d = fwd[None, :] * CAM_DIST + u[:, None] * r2[None, :] + v[:, None] * u2[None, :]
    d /= np.linalg.norm(d, axis=1, keepdims=True)
    return cam, d


def trace(args):
    u, v = args
    n = u.size
    cam, vel = camera_dirs(u, v)
    pos = np.repeat(cam[None, :], n, axis=0)
    h2 = np.sum(np.cross(pos, vel) ** 2, axis=1)
    light = np.zeros(n)
    trans = np.ones(n)
    idx = np.arange(n)
    for step in range(900):
        r = np.sqrt(np.sum(pos * pos, axis=1))
        dt = np.clip(0.04 * r, 0.01, 2.0)[:, None]
        acc = (-1.5 * h2 / r ** 5)[:, None] * pos
        vel = vel + acc * dt * 0.5
        new = pos + vel * dt
        rn = np.sqrt(np.sum(new * new, axis=1))
        vel = vel + (-1.5 * h2 / rn ** 5)[:, None] * new * dt * 0.5

        cross = pos[:, 2] * new[:, 2] < 0
        if cross.any():
            t = pos[cross, 2] / (pos[cross, 2] - new[cross, 2])
            p = pos[cross] + t[:, None] * (new[cross] - pos[cross])
            rho = np.hypot(p[:, 0], p[:, 1])
            ok = rho > 1.0
            e, op = emission(np.maximum(rho, 1.0), np.arctan2(p[:, 1], p[:, 0]))
            ci = idx[cross]
            light[ci] += trans[ci] * e * ok
            trans[ci] *= 1 - op * ok
        pos = new

        if step % 8 == 7:
            outward = np.sum(pos * vel, axis=1) > 0
            alive = (rn > 1.02) & ~((rn > CAM_DIST + 5) & outward)
            if not alive.any():
                break
            pos, vel, h2, idx = pos[alive], vel[alive], h2[alive], idx[alive]
    return light.astype(np.float32)


def render(width, height):
    half_h = HALF_W * height / width
    us = (np.arange(width) + 0.5) / width * 2 * HALF_W - HALF_W
    vs = half_h - (np.arange(height) + 0.5) / height * 2 * half_h
    rows_per = max(1, 400_000 // width)
    jobs = []
    for y0 in range(0, height, rows_per):
        vv = vs[y0:y0 + rows_per]
        uu, vv2 = np.meshgrid(us, vv)
        jobs.append((uu.ravel(), vv2.ravel()))
    with Pool() as pool:
        parts = pool.map(trace, jobs, chunksize=1)
    return np.concatenate(parts).reshape(height, width)


def gaussian_fft(img, sigma):
    h, w = img.shape
    fy = np.fft.fftfreq(h)[:, None]
    fx = np.fft.rfftfreq(w)[None, :]
    kernel = np.exp(-2 * (math.pi * sigma) ** 2 * (fx ** 2 + fy ** 2))
    return np.fft.irfft2(np.fft.rfft2(img) * kernel, s=img.shape)


def resize_f(arr, size):
    return np.asarray(Image.fromarray(arr.astype(np.float32), "F").resize(size, Image.BICUBIC))


def finish(light):
    h, w = light.shape
    # alone luminoso attorno alle zone più chiare
    sw, sh = max(64, w // 8), max(64, h // 8)
    small = resize_f(np.minimum(light, 6.0), (sw, sh))
    pad = sw // 4
    small = np.pad(small, pad, mode="edge")
    glow = 0.5 * gaussian_fft(small, sw * 0.012) + 0.35 * gaussian_fft(small, sw * 0.05) \
        + 0.15 * gaussian_fft(small, sw * 0.15)
    glow = glow[pad:-pad, pad:-pad]
    light = light + 0.30 * np.maximum(resize_f(glow, (w, h)), 0)
    img = 1 - np.exp(-EXPOSURE * light)
    img = img ** 0.9

    # pianeta solitario nel poster di destra, con un filo di luce verso il buco nero
    cx, cy, pr = w * 0.845, h * 0.80, h * 0.012
    yy, xx = np.mgrid[int(cy - 3 * pr):int(cy + 3 * pr), int(cx - 3 * pr):int(cx + 3 * pr)]
    dx, dy = (xx - cx) / pr, (yy - cy) / pr
    d = np.hypot(dx, dy)
    to_bh = np.array([w / 2 - cx, h / 2 - cy])
    to_bh /= np.linalg.norm(to_bh)
    lit = np.clip((dx * to_bh[0] + dy * to_bh[1]) / np.maximum(d, 1e-6), 0, 1)
    inside = np.clip((1 - d) * pr / 1.5, 0, 1)
    rim = smoothstep(0.80, 1.0, d) * lit ** 1.5 * 0.95
    sl = (slice(yy[0, 0], yy[-1, 0] + 1), slice(xx[0, 0], xx[0, -1] + 1))
    img[sl] = img[sl] * (1 - inside) + inside * (0.015 + rim)

    # grana fotografica
    g = np.random.default_rng(3).standard_normal((h // 2 + 1, w // 2 + 1)).astype(np.float32)
    grain = resize_f(g, (w, h))
    img = img + grain * (0.022 + 0.03 * img * (1 - img))
    img = 0.02 + 0.98 * np.clip(img, 0, 1)
    return Image.fromarray((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8), "L")


def save_pdf(jpg, pdf, title):
    c = canvas.Canvas(str(pdf), pagesize=A3)
    c.setTitle(title)
    c.drawImage(str(jpg), 0, 0, width=A3[0], height=A3[1])
    c.showPage()
    c.save()


def mockup(left, right, out, wall, frame, shadow):
    size = (1800, 1500)
    ph = 1000
    pw = round(ph / math.sqrt(2))
    t = round(ph * 0.018)
    gap = 60
    img = Image.new("RGB", size, wall).convert("RGBA")
    glow = Image.new("L", size, 0)
    ImageDraw.Draw(glow).ellipse([-500, -700, 1700, 900], fill=70)
    img = Image.composite(Image.new("RGBA", size, (255, 255, 255, 255)), img,
                          glow.filter(ImageFilter.GaussianBlur(350)))
    total = 2 * (pw + 2 * t) + gap
    x = (size[0] - total) // 2
    top = (size[1] - ph - 2 * t) // 2
    for panel in (left, right):
        fw, fh = pw + 2 * t, ph + 2 * t
        sh = Image.new("RGBA", size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle([x + 10, top + 18, x + fw + 10, top + fh + 18],
                                     fill=(0, 0, 0, int(255 * shadow)))
        img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(16)))
        ImageDraw.Draw(img).rectangle([x, top, x + fw - 1, top + fh - 1], fill=frame)
        img.paste(panel.resize((pw, ph), Image.LANCZOS).convert("RGBA"), (x + t, top + t))
        x += fw + gap
    img.convert("RGB").save(out, quality=90, optimize=True)


def main():
    dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    pw, ph = round(297 / 25.4 * dpi), round(420 / 25.4 * dpi)
    full = finish(render(2 * pw, ph))
    left, right = full.crop((0, 0, pw, ph)), full.crop((pw, 0, 2 * pw, ph))

    STAMPA.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    preview = dpi < 150
    tmp = OUT / "_tmp.jpg"
    for side, panel in (("sinistra", left), ("destra", right)):
        if not preview:
            panel.save(tmp, quality=90, dpi=(dpi, dpi))
            save_pdf(tmp, STAMPA / f"{NAME}-{side}.pdf", f"Poster {NAME} {side}")
        small = panel.resize((1754, 2481), Image.LANCZOS) if not preview else panel
        small.save(OUT / f"design-{side}.jpg", quality=90)
    tmp.unlink(missing_ok=True)
    both = full.resize((2400, round(2400 * ph / (2 * pw))), Image.LANCZOS)
    both.save(OUT / "design-insieme.jpg", quality=90)
    for wall, (wc, fc, s) in {"bianca": ("#F4F2EC", "#1B1B1B", 0.30),
                              "beige": ("#E3D3B8", "#1B1B1B", 0.32),
                              "antracite": ("#2E3033", "#E9E4DA", 0.60)}.items():
        mockup(left, right, OUT / f"mockup-{wall}.jpg", wc, fc, s)
    print("ok", full.size, "dpi", dpi)


if __name__ == "__main__":
    main()
