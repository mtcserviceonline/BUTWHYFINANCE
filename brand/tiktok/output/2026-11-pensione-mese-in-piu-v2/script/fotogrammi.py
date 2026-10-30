#!/usr/bin/env python3
"""Estrae i fotogrammi di controllo dal video finale e crea il contact sheet.
Uso: fotogrammi.py VIDEO.mp4 TEMPI.json DIR_FOTOGRAMMI ANTEPRIMA.jpg
Fotogrammi: 0,0 s, ogni taglio +0,12 s, il 60% di ogni inquadratura e l'ultimo. Nel contact sheet
(5 colonne) vanno 0,0 s, il 60% di ogni inquadratura e l'ultimo, con il tempo scritto sopra."""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

S = os.path.dirname(os.path.abspath(__file__))
video, tempi, d, out = sys.argv[1:5]
T = json.load(open(tempi, encoding="utf-8"))
os.makedirs(d, exist_ok=True)


def grab(t):
    p = f"{d}/t{t:06.2f}.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", video, "-frames:v", "1",
                    "-q:v", "2", p], check=True)
    return p


last = T["durata"] - 1.5 / T["fps"]
for s in T["inquadrature"][1:]:
    grab(s["inizio"] + 0.12)
key = [grab(0.0)] + [grab(s["inizio"] + s["durata"] * 0.6) for s in T["inquadrature"][1:]] + [grab(last)]
cols, w, h = 5, 360, 640
rows = (len(key) + cols - 1) // cols
sh = Image.new("RGB", (cols * w, rows * (h + 30)), (200, 200, 200))
dr = ImageDraw.Draw(sh)
f = ImageFont.truetype(f"{S}/fonts/IBMPlexMono-Bold.ttf", 22)
for k, p in enumerate(key):
    x, y = (k % cols) * w, (k // cols) * (h + 30)
    sh.paste(Image.open(p).resize((w, h)), (x, y + 30))
    dr.text((x + 6, y + 3), os.path.basename(p)[1:-4] + " s", fill=(0, 0, 0), font=f)
sh.save(out, quality=85, optimize=True)
print(len(os.listdir(d)), "fotogrammi;", len(key), "nel contact sheet")
