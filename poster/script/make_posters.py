#!/usr/bin/env python3
"""Genera i poster A3 per Vinted.

Per ogni poster:
- poster/stampa/<slug>.pdf                   PDF A3 vettoriale (297 x 420 mm), font incorporati
- poster/vinted/<slug>/design.jpg            immagine pulita, rasterizzata dal PDF
- poster/vinted/<slug>/mockup-<parete>.jpg   poster incorniciato su parete (mockup)

Per il set:
- poster/vinted/set/mockup-<parete>.jpg      tutti i poster insieme

Uso (dalla radice del repo):  python3 poster/script/make_posters.py
Richiede: reportlab, Pillow, pdftoppm (poppler-utils).
"""

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A3
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
POSTER = ROOT / "poster"
FONTS = POSTER / "fonts"
STAMPA = POSTER / "stampa"
VINTED = POSTER / "vinted"

W, H = A3  # punti: 841.89 x 1190.55 = 297 x 420 mm
DPI_DESIGN = 150
A3_RATIO = 1 / math.sqrt(2)  # larghezza / altezza del formato A3

FONT_FILES = {
    "Titan": "TitanOne_400Regular.ttf",
    "Chango": "Chango_400Regular.ttf",
    "Pacifico": "Pacifico_400Regular.ttf",
    "Righteous": "Righteous_400Regular.ttf",
}
for _name, _file in FONT_FILES.items():
    pdfmetrics.registerFont(TTFont(_name, str(FONTS / _file)))

# box = (x0, y0, x1, y1) come frazioni della pagina, origine in basso a sinistra
POSTERS = [
    {
        "slug": "01-non-decidere",
        "text": "Oggi decido di non decidere.",
        "font": "Titan", "leading": 1.05,
        "bg": "#FFD23F", "fg": "#2233FF",
        "box": (0.08, 0.06, 0.92, 0.46),
        "motif": "target",
    },
    {
        "slug": "02-caffe-prima",
        "text": "Caffè prima, poi si vede.",
        "font": "Chango", "leading": 1.08,
        "bg": "#FF4E36", "fg": "#FFF3D6",
        "box": (0.08, 0.05, 0.92, 0.46),
        "motif": "sunrise",
    },
    {
        "slug": "03-modalita-aereo",
        "text": "Modalità aereo, anche di domenica.",
        "font": "Righteous", "leading": 1.10,
        "bg": "#3DD5F3", "fg": "#14213D",
        "box": (0.08, 0.06, 0.92, 0.58),
        "motif": "clouds",
    },
    {
        "slug": "04-cinque-minuti",
        "text": "Ancora 5 minuti (sono 40).",
        "font": "Pacifico", "leading": 1.25,
        "bg": "#6FE3B0", "fg": "#0B3D2E",
        "box": (0.08, 0.40, 0.92, 0.94),
        "motif": "horizon",
    },
    {
        "slug": "05-talento-rimandare",
        "text": "Il mio talento? Rimandare.",
        "font": "Titan", "leading": 1.05,
        "bg": "#8E5CFF", "fg": "#C8FF2E",
        "box": (0.08, 0.20, 0.92, 0.68),
        "motif": "zzz",
    },
]

WALLS = {
    # parete: colore muro, colore cornice, intensità ombra
    "bianca": {"wall": "#F4F2EC", "frame": "#1B1B1B", "shadow": 0.30},
    "beige": {"wall": "#E3D3B8", "frame": "#9C7449", "shadow": 0.32},
    "antracite": {"wall": "#2E3033", "frame": "#E9E4DA", "shadow": 0.60},
}


# ---------- disegno vettoriale ----------

def rect(c, x, y, w, h, color):
    c.setFillColor(HexColor(color))
    c.rect(x, y, w, h, stroke=0, fill=1)


def circle(c, x, y, r, color):
    c.setFillColor(HexColor(color))
    c.circle(x, y, r, stroke=0, fill=1)


def rays(c, cx, cy, r_in, r_out, n, color):
    c.setFillColor(HexColor(color))
    half = math.pi / n * 0.45
    for k in range(n):
        a = 2 * math.pi * k / n
        p = c.beginPath()
        p.moveTo(cx + r_out * math.cos(a), cy + r_out * math.sin(a))
        p.lineTo(cx + r_in * math.cos(a - half), cy + r_in * math.sin(a - half))
        p.lineTo(cx + r_in * math.cos(a + half), cy + r_in * math.sin(a + half))
        p.close()
        c.drawPath(p, stroke=0, fill=1)


def cloud(c, x, y, s, color):
    c.setFillColor(HexColor(color))
    c.circle(x, y, 60 * s, stroke=0, fill=1)
    c.circle(x + 70 * s, y + 25 * s, 85 * s, stroke=0, fill=1)
    c.circle(x + 150 * s, y, 60 * s, stroke=0, fill=1)
    c.rect(x, y - 60 * s, 150 * s, 60 * s, stroke=0, fill=1)


def wave(c, y, amp, period, color, width):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(width)
    c.setLineCap(1)
    p = c.beginPath()
    steps = 300
    for i in range(steps + 1):
        x = W * i / steps
        yy = y + amp * math.sin(2 * math.pi * x / period)
        if i == 0:
            p.moveTo(x, yy)
        else:
            p.lineTo(x, yy)
    c.drawPath(p, stroke=1, fill=0)


def draw_motif(c, p):
    m = p["motif"]
    if m == "target":
        cx, cy = W / 2, 0.74 * H
        for r, col in [(290, "#FF5FA2"), (225, "#2233FF"), (160, "#FF5FA2"),
                       (95, "#2233FF"), (35, "#FF5FA2")]:
            circle(c, cx, cy, r, col)
    elif m == "sunrise":
        cx, cy = W / 2, 0.76 * H
        rays(c, cx, cy, 140, 265, 18, "#FFD23F")
        circle(c, cx, cy, 160, "#FFD23F")
    elif m == "clouds":
        cloud(c, 0.20 * W, 0.80 * H, 1.4, "#FFFFFF")
        cloud(c, 0.52 * W, 0.66 * H, 1.0, "#FFFFFF")
    elif m == "horizon":
        cx, cy = W / 2, 0.18 * H
        circle(c, cx, cy, 190, "#FF9F1C")
        rect(c, 0, 0, W, cy, p["bg"])  # copre la metà inferiore del sole
        wave(c, 0.12 * H, 18, 220, p["fg"], 14)
        wave(c, 0.06 * H, 18, 220, p["fg"], 14)
    elif m == "zzz":
        c.setFillColor(HexColor("#FF5FA2"))
        for x, y, size in [(0.10, 0.74, 100), (0.22, 0.81, 150), (0.38, 0.87, 185)]:
            c.setFont("Titan", size)
            c.drawString(x * W, y * H, "Z")
        wave(c, 0.09 * H, 26, 260, "#FF5FA2", 24)
        wave(c, 0.04 * H, 26, 260, "#FF5FA2", 24)


# ---------- testo ----------

def wrap(text, font, size, max_w):
    lines, cur = [], ""
    for word in text.split():
        test = word if not cur else f"{cur} {word}"
        if pdfmetrics.stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_text(text, font, max_w, max_h, leading, hi=520, lo=20):
    """Trova la dimensione più grande che entra nel riquadro."""
    size = hi
    while size >= lo:
        lines = wrap(text, font, size, max_w)
        fits_w = all(pdfmetrics.stringWidth(ln, font, size) <= max_w for ln in lines)
        if fits_w and len(lines) * size * leading <= max_h:
            return size, lines
        size -= 2
    raise ValueError(f"Testo troppo lungo per il riquadro: {text!r}")


def check_glyphs(font_name, text):
    face = pdfmetrics.getFont(font_name).face
    missing = sorted({ch for ch in text if not ch.isspace() and ord(ch) not in face.charToGlyph})
    if missing:
        raise SystemExit(f"Glifi mancanti in {font_name}: {missing}")


def draw_text_block(c, p):
    check_glyphs(p["font"], p["text"])
    x0f, y0f, x1f, y1f = p["box"]
    x0, y0, x1, y1 = x0f * W, y0f * H, x1f * W, y1f * H
    size, lines = fit_text(p["text"], p["font"], x1 - x0, y1 - y0, p["leading"])
    block_h = len(lines) * size * p["leading"]
    top = y1 - ((y1 - y0) - block_h) / 2
    c.setFillColor(HexColor(p["fg"]))
    c.setFont(p["font"], size)
    for i, line in enumerate(lines):
        baseline = top - size * 0.8 - i * size * p["leading"]
        c.drawCentredString((x0 + x1) / 2, baseline, line)


# ---------- output ----------

def render_pdf(p):
    STAMPA.mkdir(parents=True, exist_ok=True)
    out = STAMPA / f"{p['slug']}.pdf"
    c = canvas.Canvas(str(out), pagesize=A3)
    c.setTitle(f"Poster {p['slug']}")
    rect(c, 0, 0, W, H, p["bg"])
    draw_motif(c, p)
    draw_text_block(c, p)
    c.showPage()
    c.save()
    return out


def rasterize(pdf, slug):
    outdir = VINTED / slug
    outdir.mkdir(parents=True, exist_ok=True)
    base = outdir / "design"
    subprocess.run(
        ["pdftoppm", "-r", str(DPI_DESIGN), "-jpeg", "-jpegopt", "quality=90",
         "-singlefile", str(pdf), str(base)],
        check=True,
    )
    return base.with_suffix(".jpg")


def make_wall(size, color):
    w, h = size
    base = Image.new("RGB", size, color)
    light = Image.new("L", size, 0)
    ImageDraw.Draw(light).ellipse([-w * 0.3, -h * 0.4, w * 1.0, h * 0.7], fill=110)
    light = light.filter(ImageFilter.GaussianBlur(w * 0.25))
    base = Image.composite(Image.new("RGB", size, (255, 255, 255)), base, light)
    vig = Image.new("L", size, 0)
    ImageDraw.Draw(vig).ellipse([-w * 0.2, -h * 0.2, w * 1.2, h * 1.2], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(w * 0.3))
    darker = Image.blend(base, Image.new("RGB", size, (0, 0, 0)), 0.12)
    return Image.composite(base, darker, vig)


def place_poster(img, design, x0, top, pw, ph, frame_hex, shadow_alpha):
    t = round(ph * 0.022)  # spessore cornice
    fw, fh = pw + 2 * t, ph + 2 * t
    # ombra morbida
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rectangle(
        [x0 + 10, top + 18, x0 + fw + 10, top + fh + 18],
        fill=(0, 0, 0, int(255 * shadow_alpha)),
    )
    layer = layer.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img.convert("RGBA"), layer)
    ImageDraw.Draw(img).rectangle([x0, top, x0 + fw - 1, top + fh - 1], fill=frame_hex)
    img.paste(design.resize((pw, ph), Image.LANCZOS).convert("RGBA"), (x0 + t, top + t))
    return img


def mockup_single(design_path, out, wall_name):
    spec = WALLS[wall_name]
    size = (1200, 1500)
    ph = 1040
    pw = round(ph * A3_RATIO)
    t = round(ph * 0.022)
    fw, fh = pw + 2 * t, ph + 2 * t
    img = make_wall(size, spec["wall"])
    design = Image.open(design_path).convert("RGB")
    img = place_poster(img, design, (size[0] - fw) // 2, (size[1] - fh) // 2,
                       pw, ph, spec["frame"], spec["shadow"])
    img.convert("RGB").save(out, quality=90, optimize=True)


def mockup_set(design_paths, out, wall_name):
    spec = WALLS[wall_name]
    size = (1800, 1400)
    ph = 500
    pw = round(ph * A3_RATIO)
    t = round(ph * 0.022)
    fw, fh = pw + 2 * t, ph + 2 * t
    gap = 70
    rows = [design_paths[:3], design_paths[3:]]
    img = make_wall(size, spec["wall"])
    top0 = 140
    for r, row in enumerate(rows):
        row_w = len(row) * fw + (len(row) - 1) * gap
        x = (size[0] - row_w) // 2
        top = top0 + r * (fh + gap)
        for path in row:
            design = Image.open(path).convert("RGB")
            img = place_poster(img, design, x, top, pw, ph, spec["frame"], spec["shadow"])
            x += fw + gap
    img.convert("RGB").save(out, quality=90, optimize=True)


def main():
    for p in POSTERS:
        pdf = render_pdf(p)
        design = rasterize(pdf, p["slug"])
        for wall in ("bianca", "antracite"):
            mockup_single(design, VINTED / p["slug"] / f"mockup-{wall}.jpg", wall)
        print(f"ok  {p['slug']}")

    set_dir = VINTED / "set"
    set_dir.mkdir(parents=True, exist_ok=True)
    designs = [VINTED / p["slug"] / "design.jpg" for p in POSTERS]
    for wall in ("bianca", "beige", "antracite"):
        mockup_set(designs, set_dir / f"mockup-{wall}.jpg", wall)
    print("ok  set")


if __name__ == "__main__":
    main()
