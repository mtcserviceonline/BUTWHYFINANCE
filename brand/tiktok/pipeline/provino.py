#!/usr/bin/env python3
"""Provino di tutte le immagini di un episodio (griglia con l'id sotto ogni immagine), per il controllo visivo.
Uso: provino.py CARTELLA_EPISODIO  ->  CARTELLA/_lavoro/provino-immagini.jpg"""
import glob, os, sys
from PIL import Image, ImageDraw

ep = sys.argv[1]
files = sorted(glob.glob(os.path.join(ep, "immagini", "*.png")))
cols, tw, th = 5, 288, 504
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + 40)), (60, 60, 60))
d = ImageDraw.Draw(sheet)
for k, f in enumerate(files):
    x, y = (k % cols) * tw, (k // cols) * (th + 40)
    sheet.paste(Image.open(f).convert("RGB").resize((tw, th)), (x, y))
    d.text((x + 10, y + th + 8), os.path.splitext(os.path.basename(f))[0], fill=(255, 255, 255))
os.makedirs(os.path.join(ep, "_lavoro"), exist_ok=True)
out = os.path.join(ep, "_lavoro", "provino-immagini.jpg")
sheet.save(out, quality=85)
print("provino:", out, len(files), "immagini")
