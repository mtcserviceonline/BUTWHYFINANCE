#!/usr/bin/env python3
"""Copertina 9:16 (1080x1920) del video TikTok.
Uso: copertina.py CARTELLA_EPISODIO
Usa il campo "copertina" di scene.json: {"immagine": "01", "titolo": ["MA PERCHÉ", "IL CAFFÈ *COSTA DI PIÙ?*"]}
(senza campo: immagine e titolo della prima scena). Scrive CARTELLA/copertina.png.
Il titolo sta tra il 10% in alto e la metà dello schermo, fuori dalla colonna dei pulsanti:
TikTok ritaglia la copertina 3:4 al centro nella griglia del profilo, quindi resta leggibile."""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import monta  # noqa: E402
from comune import accento, carica_episodio  # noqa: E402

ep = sys.argv[1]
epi = carica_episodio(ep)
monta.ACC = accento(epi)
prima = epi["scene"][0]
cop = epi.get("copertina") or {}
scena = {"sfondo": cop.get("sfondo", prima["sfondo"]), "titolo": cop.get("titolo", prima["titolo"])}
img = os.path.join(ep, "immagini", f"{cop.get('immagine') or prima.get('immagine') or prima['id']}.png")
tl, tb = monta.title_layer(scena)
canvas = monta.base_canvas(img, tb).convert("RGBA")
canvas.alpha_composite(tl)
if cop.get("fumetto", False):
    canvas.alpha_composite(monta.bubble_layer(500, tb + 60, (560, tb + 250), "But Why Finance?", 64))
out = os.path.join(ep, "copertina.png")
canvas.convert("RGB").save(out)
print("copertina:", out)
