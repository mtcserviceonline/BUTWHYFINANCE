#!/usr/bin/env python3
"""Contact sheet: tutte le immagini del post affiancate in un unico JPEG (immagini/anteprima.jpg).

Prende i file NN.png della cartella (01.png, 02.png, ...) in ordine, li riduce a miniature 9:16
e li dispone in una griglia su fondo grigio chiaro. Con 8 immagini e i valori di default
(4 colonne, miniature 270x480, margine 10 px) produce un JPEG 1130x990, come nel post risparmio.

Uso:
  anteprima.py CARTELLA_IMMAGINI [--out CARTELLA_IMMAGINI/anteprima.jpg] [--colonne 4]
  anteprima.py 01.png 02.png ... --out anteprima.jpg
  [--numeri]   scrive il numero dell'immagine in un angolo di ogni miniatura (solo per l'anteprima)
"""
import argparse
import glob
import os
import re

from PIL import Image, ImageDraw, ImageFont


def elenco(ingressi):
    files = []
    for p in ingressi:
        if os.path.isdir(p):
            files += sorted(f for f in glob.glob(os.path.join(p, "*.png"))
                            if re.fullmatch(r"\d+\.png", os.path.basename(f)))
        else:
            files.append(p)
    return files


def contact_sheet(files, colonne=4, larghezza=270, margine=10, fondo=(200, 200, 200), numeri=False):
    altezza = round(larghezza * 16 / 9)
    righe = -(-len(files) // colonne)
    col = min(colonne, len(files))
    W = col * larghezza + (col + 1) * margine
    H = righe * altezza + (righe + 1) * margine
    sheet = Image.new("RGB", (W, H), fondo)
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.load_default(size=28)
    except TypeError:            # Pillow vecchio
        font = ImageFont.load_default()
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        # adatta a 9:16 senza deformare (ritaglio centrale se serve)
        r = larghezza / altezza
        w, h = im.size
        if abs(w / h - r) > 0.01:
            if w / h > r:
                nw = round(h * r)
                im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
            else:
                nh = round(w / r)
                im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
        im = im.resize((larghezza, altezza), Image.LANCZOS)
        x = margine + (i % colonne) * (larghezza + margine)
        y = margine + (i // colonne) * (altezza + margine)
        sheet.paste(im, (x, y))
        if numeri:
            etichetta = os.path.splitext(os.path.basename(f))[0]
            draw.rectangle((x, y, x + 46, y + 36), fill=(17, 20, 24))
            draw.text((x + 8, y + 3), etichetta, fill=(244, 241, 234), font=font)
    return sheet


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ingressi", nargs="+", help="cartella con NN.png oppure elenco di file")
    ap.add_argument("--out", help="JPEG di uscita (default: <cartella>/anteprima.jpg)")
    ap.add_argument("--colonne", type=int, default=4)
    ap.add_argument("--larghezza", type=int, default=270, help="larghezza di ogni miniatura in px")
    ap.add_argument("--margine", type=int, default=10)
    ap.add_argument("--numeri", action="store_true")
    a = ap.parse_args()
    files = elenco(a.ingressi)
    if not files:
        ap.error("nessuna immagine NN.png trovata")
    out = a.out or os.path.join(a.ingressi[0] if os.path.isdir(a.ingressi[0]) else ".", "anteprima.jpg")
    sheet = contact_sheet(files, a.colonne, a.larghezza, a.margine, numeri=a.numeri)
    sheet.save(out, quality=90)
    print(f"{len(files)} immagini -> {out} {sheet.size[0]}x{sheet.size[1]}")


if __name__ == "__main__":
    main()
