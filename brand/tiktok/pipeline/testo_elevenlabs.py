#!/usr/bin/env python3
"""Controlla scene.json e scrive voce-elevenlabs.txt (testo da incollare in ElevenLabs, Eleven v3).
Uso: testo_elevenlabs.py CARTELLA_EPISODIO
Esce con codice 1 se ci sono errori (testo troppo lungo, sottotitoli che non coprono la voce, ecc.)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comune import LIMITE_PAROLE, carica_episodio, tokens  # noqa: E402

ep = sys.argv[1]
epi = carica_episodio(ep)
scene = epi["scene"]
err, warn = [], []

ids = [s["id"] for s in scene]
if len(set(ids)) != len(ids):
    err.append("id delle scene duplicati")
for s in scene:
    sid = s["id"]
    if s.get("sfondo") not in ("inchiostro", "carta"):
        err.append(f"scena {sid}: sfondo deve essere 'inchiostro' o 'carta'")
    if not s.get("voce", "").strip():
        err.append(f"scena {sid}: voce vuota")
    if re.search(r"\d", s.get("voce", "")):
        err.append(f"scena {sid}: nella voce i numeri vanno scritti in lettere ({s['voce']!r})")
    if re.search(r"\[[^\]]*\]", s.get("voce", "")):
        err.append(f"scena {sid}: i tag v3 vanno nel campo 'tag', non dentro 'voce'")
    if not s.get("titolo"):
        err.append(f"scena {sid}: manca il titolo a schermo")
    subs = s.get("sottotitoli") or []
    if not subs:
        err.append(f"scena {sid}: mancano i sottotitoli")
        continue
    parlato = []
    for disp, spoken in subs:
        parlato += tokens(spoken or disp.replace("*", ""))
        n = len(tokens(disp.replace("*", "")))
        if n > 5:
            warn.append(f"scena {sid}: sottotitolo di {n} parole (max 5): {disp!r}")
        if disp.count("*") % 2:
            err.append(f"scena {sid}: asterischi non chiusi in {disp!r}")
    if parlato != tokens(s["voce"]):
        err.append(f"scena {sid}: i sottotitoli (testo parlato) non corrispondono alla voce\n"
                   f"   voce: {' '.join(tokens(s['voce']))}\n   sub:  {' '.join(parlato)}")
    if not s.get("immagine"):
        warn.append(f"scena {sid}: manca 'immagine' (uso l'id della scena)")

if scene and scene[0].get("sfondo") != "inchiostro":
    warn.append("la prima scena (hook) di solito è su fondo inchiostro")
if scene and not scene[-1].get("fumetto"):
    warn.append("l'ultima scena di solito ha il fumetto 'But Why Finance?' (\"fumetto\": true)")

n_parole = sum(len(tokens(s["voce"])) for s in scene)
lo, hi, hard = LIMITE_PAROLE
if n_parole > hard:
    err.append(f"testo troppo lungo: {n_parole} parole (limite {hard}, obiettivo {lo}-{hi})")
elif n_parole > hi or n_parole < lo:
    warn.append(f"{n_parole} parole: fuori dall'obiettivo {lo}-{hi}")

righe = []
for s in scene:
    tag = (s.get("tag") or "").strip()
    righe.append(f"{tag} {s['voce'].strip()}".strip())
testo = "\n".join(righe) + "\n"
open(os.path.join(ep, "voce-elevenlabs.txt"), "w", encoding="utf-8").write(testo)

for w in warn:
    print("ATTENZIONE:", w)
for e in err:
    print("ERRORE:", e)
print(f"\n{len(scene)} scene, {n_parole} parole, durata stimata {n_parole / 2.4:.0f} s (a ~145 parole/min)")
print("scritto", os.path.join(ep, "voce-elevenlabs.txt"))
sys.exit(1 if err else 0)
