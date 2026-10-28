#!/usr/bin/env python3
"""Scrive script/elevenlabs.txt (il testo unico da incollare in ElevenLabs) a partire da script/scene_elevenlabs.json.

Il file (stesso formato di brand/tiktok/output/2026-10-risparmio-quotidiano/script/elevenlabs.txt) contiene:
  1. testo con i tag in inglese per il modello eleven_v3 ([surprised], [curious], [calm], [thoughtful], [warm]);
  2. testo con i tag di tono in italiano, come li scrive l'utente ([sorpreso], [curioso], [calmo], [pensieroso], [caldo]);
  3. per eleven_multilingual_v2 (che non legge i tag): il testo di ogni scena SENZA tag con stability/style da impostare.

Schema di ogni scena (come nel post risparmio):
  {"id": 1, "secondi": "0-6", "espressione_orso": "...", "tono": "...", "tag_v3": "[surprised]",
   "stability": 0.35, "style": 0.45, "text": "...", "immagini": [1, 2]}
Facoltativo: "tag_it": "[sorpreso]" se il tag italiano non si ricava da tag_v3.

Uso: elevenlabs_txt.py script/scene_elevenlabs.json script/elevenlabs.txt [--titolo "Il prezzo di... un caffe'"]
Stampa anche il testo a schermo: va SEMPRE incollato anche nel messaggio in chat.
"""
import argparse
import json
import sys

EN_IT = {
    "[surprised]": "[sorpreso]",
    "[curious]": "[curioso]",
    "[calm]": "[calmo]",
    "[thoughtful]": "[pensieroso]",
    "[warm]": "[caldo]",
    # altri tag v3 che possono servire
    "[excited]": "[entusiasta]",
    "[serious]": "[serio]",
    "[concerned]": "[preoccupato]",
    "[amused]": "[divertito]",
}
SIMILARITY = 0.8


def tag_it(s):
    if s.get("tag_it"):
        return s["tag_it"]
    t = s.get("tag_v3", "")
    if t not in EN_IT:
        print(f"scena {s.get('id')}: tag {t!r} senza traduzione, aggiungi \"tag_it\" nel JSON", file=sys.stderr)
        return t
    return EN_IT[t]


def componi(scene, titolo=""):
    righe = []
    if titolo:
        righe += [f"TESTO PER ELEVENLABS · {titolo}", ""]
    parole = sum(len(s["text"].split()) for s in scene)
    righe += [f"{len(scene)} scene, {parole} parole (a 140-150 parole/min ~ {parole / 150 * 60:.0f}-"
              f"{parole / 140 * 60:.0f} s di voce).", ""]
    # stesso formato di brand/tiktok/output/2026-10-risparmio-quotidiano/script/elevenlabs.txt
    righe += ["=== VERSIONE 1: eleven_v3, tag di tono in inglese (da incollare così) ===", ""]
    righe += [f"{s['tag_v3']} {s['text']}" for s in scene]
    righe += ["", "", "=== VERSIONE 2: tag di tono in italiano ===", ""]
    righe += [f"{tag_it(s)} {s['text']}" for s in scene]
    righe += ["", "", "=== VERSIONE 3: eleven_multilingual_v2, una scena alla volta (senza tag) ===",
              f"(lingua italiano, similarity {SIMILARITY}, speaker boost attivo, velocità 0,95-1,0)", ""]
    for s in scene:
        imm = ", ".join(str(i) for i in s.get("immagini", []))
        righe.append(f"Scena {s['id']} | {tag_it(s).strip('[]')} | stability {s['stability']} | style {s['style']}"
                     + (f" | {s['secondi']} s" if s.get("secondi") else "") + (f" | immagini {imm}" if imm else ""))
        righe.append(s["text"])
        righe.append("")
    return "\n".join(righe).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scene")
    ap.add_argument("uscita")
    ap.add_argument("--titolo", default="")
    a = ap.parse_args()
    scene = json.load(open(a.scene, encoding="utf-8"))
    testo = componi(scene, a.titolo)
    open(a.uscita, "w", encoding="utf-8").write(testo)
    print(testo)


if __name__ == "__main__":
    main()
