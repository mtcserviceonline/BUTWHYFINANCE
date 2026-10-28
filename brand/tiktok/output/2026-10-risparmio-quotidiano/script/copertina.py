#!/usr/bin/env python3
"""Copertina del video (P-2): 1080x1920, fondo inchiostro, orso intero sorpreso (immagine 01) e "470 €" in ambra.

Uso (nella cartella di lavoro di monta.sh, con img/ e fonts/): copertina.py OUT.png
Stessi font, colori e vista dell'apertura del video (montage.py), cosi' copertina e primo fotogramma si
somigliano. Tutto il contenuto sta tra y=260 e y=1650: resta visibile anche nel ritaglio 3:4 della griglia
del profilo (y 240-1680)."""
import sys
import montage as M

M.TITLES["copertina"] = [
    [("UN CAFFÈ AL BAR AL GIORNO", "cond", 84, "base")],
    [("470", "mono", 270, "accent"), (" ", "mono", 110, "accent"), ("€", "cond", 255, "accent")],
    [("ALL'ANNO", "cond", 120, "base")],
]


def main():
    out = sys.argv[1]
    sh = {"img": "01", "view": (515, 600, 0.70), "moto": "fermo"}
    frame = M.render_view("01", M.view_at(sh, 0)).convert("RGBA")
    layers, _ = M.title_layers("copertina", "ink", 260)
    for lay, bb in layers:
        frame.alpha_composite(lay)
    # controllo: gli occhiali non devono stare sotto il titolo
    occ = M.to_screen(M.OCCHIALI["01"]["occhiali"], M.view_at(sh, 0))
    fondo_titolo = max(bb[3] for _, bb in layers)
    assert occ[1] > fondo_titolo + 10, (occ, fondo_titolo)
    frame.convert("RGB").save(out)
    print(out, "occhiali", [round(c) for c in occ], "fondo titolo", fondo_titolo)


if __name__ == "__main__":
    main()
