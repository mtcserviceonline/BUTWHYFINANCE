#!/usr/bin/env python3
"""Copertina del video "Vero o falso? Il governo alza l'età pensionabile": 1080x1920, fondo inchiostro,
immagine 01 (orso sorpreso con il timbro viola sopra il foglio bianco) e il titolo dell'hook.

Uso (dalla radice del repository):
  python3 brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/script/copertina.py \
      brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/copertina.png [--font-dir ~/.cache/butwhy-fonts]

Stessa idea di ../../2026-11-pensione-67-anni-un-mese/script/copertina.py, ma senza montage.py (questo post non
è ancora montato): legge immagini/01.png e scrive i titoli con Pillow in IBM Plex Sans Condensed Bold.
Il titolo sta fra y=245 e y~570, sopra il manico del timbro (y~585) e la testa dell'orso (occhiali a y~880 nell'immagine 01): tutto resta
visibile anche nel ritaglio 3:4 della griglia del profilo (y 240-1680). Accento viola #5B3FA8 della rubrica
"Vero o falso?" con contorno carta, perché il viola puro su inchiostro si legge poco."""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont

QUI = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(QUI)
INCHIOSTRO = (17, 20, 24)
CARTA = (244, 241, 234)
VIOLA = (91, 63, 168)

RIGHE = [  # testo, corpo, colore, contorno
    ("VERO O FALSO?", 124, VIOLA, CARTA),
    ("«IL GOVERNO ALZA", 84, CARTA, INCHIOSTRO),
    ("L'ETÀ PENSIONABILE»", 84, CARTA, INCHIOSTRO),
]
Y0, INTERLINEA = 245, 22
OCCHIALI_Y = 820  # bordo alto delle lenti nell'immagine 01 (misurato a occhio sul PNG 1080x1920)
TIMBRO_Y = 585  # cima del manico del timbro nell'immagine 01


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--font-dir", default=os.path.expanduser("~/.cache/butwhy-fonts"))
    a = ap.parse_args()
    font_path = os.path.join(a.font_dir, "IBMPlexSansCondensed-Bold.ttf")
    img = Image.open(os.path.join(POST, "immagini", "01.png")).convert("RGB")
    d = ImageDraw.Draw(img)
    y = Y0
    for testo, corpo, colore, contorno in RIGHE:
        f = ImageFont.truetype(font_path, corpo)
        bb = d.textbbox((0, 0), testo, font=f, stroke_width=6)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        x = (1080 - w) // 2 - bb[0]
        assert w <= 1080 - 2 * 60, f"riga troppo larga: {testo} ({w}px)"
        d.text((x, y - bb[1]), testo, font=f, fill=colore, stroke_width=6, stroke_fill=contorno)
        y += h + INTERLINEA
    assert y < OCCHIALI_Y - 40, f"il titolo scende fino a y={y}, troppo vicino agli occhiali"
    assert y - INTERLINEA < TIMBRO_Y - 10, f"il titolo tocca il timbro (y={y})"
    img.save(a.out)
    print(a.out, "fondo titolo", y)


if __name__ == "__main__":
    main()
