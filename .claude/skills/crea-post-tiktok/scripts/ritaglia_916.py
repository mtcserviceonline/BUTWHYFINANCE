#!/usr/bin/env python3
"""Porta un'immagine a 9:16 esatto (1080x1920) senza deformarla.

Ritaglio centrale al rapporto 9:16, poi ridimensionamento Lanczos.
La risposta di muse-image-1.0 con size=1024x1792 e' un WebP 1152x2016:
ritaglio a 1134x2016 (9 px per lato) -> 1080x1920.

Uso da riga di comando:
    ritaglia_916.py INGRESSO USCITA.png [--larghezza 1080 --altezza 1920]
Uso come modulo:
    from ritaglia_916 import a_916
    a_916(Image.open("x.webp")).save("x.png")
"""
import argparse

from PIL import Image


def a_916(im, larghezza=1080, altezza=1920):
    """Restituisce una nuova immagine RGB larghezza x altezza (default 1080x1920)."""
    im = im.convert("RGB")
    w, h = im.size
    rapporto = larghezza / altezza
    if w / h > rapporto:            # troppo larga: taglia ai lati
        nw = round(h * rapporto)
        x0 = (w - nw) // 2
        box = (x0, 0, x0 + nw, h)
    else:                           # troppo alta: taglia sopra e sotto
        nh = round(w / rapporto)
        y0 = (h - nh) // 2
        box = (0, y0, w, y0 + nh)
    return im.crop(box).resize((larghezza, altezza), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ingresso")
    ap.add_argument("uscita")
    ap.add_argument("--larghezza", type=int, default=1080)
    ap.add_argument("--altezza", type=int, default=1920)
    a = ap.parse_args()
    src = Image.open(a.ingresso)
    out = a_916(src, a.larghezza, a.altezza)
    out.save(a.uscita)
    print(f"{a.ingresso} {src.size[0]}x{src.size[1]} -> {a.uscita} {out.size[0]}x{out.size[1]}")


if __name__ == "__main__":
    main()
