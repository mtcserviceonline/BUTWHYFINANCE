#!/usr/bin/env python3
"""Copertina del video "In 60 secondi: pensione a 67 anni e un mese, cosa puoi fare": 1080x1920, fondo
inchiostro, immagine 01 (orso sorpreso, sedia a dondolo fucsia che si allontana) e il numero dell'hook.

Uso (dalla radice del repository):
  python3 brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/script/copertina.py \
      brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/copertina.png [--font-dir ~/.cache/butwhy-fonts]

Stessa idea di ../../2026-11-pensione-67-anni-un-mese/script/copertina.py, senza montage.py (la usa anche
monta.sh): legge immagini/01.png e scrive i titoli con Pillow (IBM Plex Sans Condensed Bold, numeri in
IBM Plex Mono Bold). Il titolo sta fra y=245 e y~660, sopra le orecchie dell'orso (y~720) e lo schienale della
sedia (y~740): tutto resta visibile anche nel ritaglio 3:4 della griglia del profilo (y 240-1680). Accento
fucsia #B0186E della rubrica "In 60 secondi" con contorno carta, perché il fucsia su inchiostro si legge poco."""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont

QUI = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(QUI)
INCHIOSTRO = (17, 20, 24)
CARTA = (244, 241, 234)
FUCSIA = (176, 24, 110)

RIGHE = [  # pezzi (testo, font), corpo, colore, contorno
    ([("PENSIONE", "cond")], 84, CARTA, INCHIOSTRO),
    ([("67", "mono"), (" ANNI", "cond")], 190, FUCSIA, CARTA),
    ([("+ ", "cond"), ("1", "mono"), (" MESE", "cond")], 150, FUCSIA, CARTA),
]
Y0, INTERLINEA = 245, 22
OCCHIALI_Y = 820  # bordo alto delle lenti nell'immagine 01 (griglia di 50 px, vedi config_video.py)
ORECCHIE_Y = 720  # cima delle orecchie dell'orso nell'immagine 01


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--font-dir", default=os.path.expanduser("~/.cache/butwhy-fonts"))
    ap.add_argument("--immagine", default=os.path.join(POST, "immagini", "01.png"))
    a = ap.parse_args()
    fp = {"cond": os.path.join(a.font_dir, "IBMPlexSansCondensed-Bold.ttf"),
          "mono": os.path.join(a.font_dir, "IBMPlexMono-Bold.ttf")}
    img = Image.open(a.immagine).convert("RGB")
    d = ImageDraw.Draw(img)
    y = Y0
    for pezzi, corpo, colore, contorno in RIGHE:
        sw = max(6, corpo // 16)
        fonti = [ImageFont.truetype(fp[f], corpo) for _, f in pezzi]
        larg = [d.textlength(t, font=f) for (t, _), f in zip(pezzi, fonti)]
        asc = max(f.getmetrics()[0] for f in fonti)
        h = max(d.textbbox((0, 0), t, font=f, anchor="ls", stroke_width=sw)[3] - d.textbbox((0, 0), t, font=f, anchor="ls", stroke_width=sw)[1] for (t, _), f in zip(pezzi, fonti))
        w = sum(larg)
        assert w <= 1080 - 2 * 60, f"riga troppo larga: {pezzi} ({w}px)"
        x = (1080 - w) / 2
        top = min(d.textbbox((0, y + asc), t, font=f, anchor="ls", stroke_width=sw)[1] for (t, _), f in zip(pezzi, fonti))
        dy = y - top
        for (t, _), f, lw in zip(pezzi, fonti, larg):
            d.text((x, y + asc + dy), t, font=f, fill=colore, anchor="ls", stroke_width=sw, stroke_fill=contorno)
            x += lw
        y += h + INTERLINEA
    assert y - INTERLINEA < ORECCHIE_Y - 30, f"il titolo scende fino a y={y}, troppo vicino all'orso"
    img.save(a.out)
    print(a.out, "fondo titolo", y)


if __name__ == "__main__":
    main()
