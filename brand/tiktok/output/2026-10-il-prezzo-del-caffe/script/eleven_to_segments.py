#!/usr/bin/env python3
"""Converte l'allineamento di ElevenLabs (/with-timestamps) nel formato dei tempi usato da montage.py.
Uso: eleven_to_segments.py ELEVEN.json SHOTS_VOICE.json OUT_TIMING.json
ELEVEN.json e' il file scritto da tts.py; il testo inviato a ElevenLabs deve essere la concatenazione
(con uno spazio) dei testi di SHOTS_VOICE.json, nello stesso ordine."""
import json, sys

el = json.load(open(sys.argv[1], encoding="utf-8"))
shots = json.load(open(sys.argv[2], encoding="utf-8"))
al = el["alignment"]
chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
full = "".join(chars)
pos, segs = 0, []
for text, _pause in shots:
    i = full.index(text, pos)
    j = i + len(text) - 1
    segs.append({"text": text, "start": round(st[i], 3), "end": round(en[j], 3)})
    pos = j + 1
json.dump({"voice": el["voice"], "model": el["model"], "segments": segs, "total": en[-1] + 0.5},
          open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
print(len(segs), "segmenti, durata", en[-1])
