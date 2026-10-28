#!/usr/bin/env python3
"""Genera la voce del post con ElevenLabs, scena per scena, e i tempi per il montaggio.

!! SOLO su richiesta esplicita dell'utente o dopo che ha confermato il passaggio a un piano a pagamento.
   Sul piano gratuito le voci italiane della libreria rispondono 402 paid_plan_required e restano pochi crediti:
   per questo senza --conferma lo script non chiama l'API.

Per ogni scena di scene_elevenlabs.json:
  POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128
  modello eleven_multilingual_v2, language_code "it", stability/style della scena, similarity 0.8, speaker boost;
  header xi-api-key con valore fittizio (l'autenticazione la fa il proxy su api.elevenlabs.io).
Poi unisce le scene con una pausa (default 0,3 s) e scrive nella cartella di uscita:
  voce.mp3, voce.wav (PCM 16 bit, per montage.py), scene/NN.mp3, tempi_voce.json
tempi_voce.json ha "segments" = un segmento per IMMAGINE (formato di montage.py del post del caffe'):
le scene con piu' immagini ("immagini": [1, 2]) si dividono sul testo ai segni di punteggiatura
(prima . ? !, poi : ;, poi la virgola) oppure con "frasi_immagini": ["...", "..."] nella scena.

Uso:
  voce_elevenlabs.py script/scene_elevenlabs.json --out-dir voce --conferma [--voice-id ID] [--speed 1.0]
  voce_elevenlabs.py script/scene_elevenlabs.json --out-dir /tmp/x --simula   # niente rete: tempi finti, per provare
Voci italiane della libreria (richiedono il piano a pagamento):
  f8NAZK1ciwrVujah7clz  Valerio - Warm Italian Storyteller (default)
  wQAoCaUYKpd8fFWwtvnq  Valerio - Deep
  94VTtZwvNmsppde6nAW0  Achille Valerio
Errori 401/402: lo script si ferma subito (non ritenta, per non consumare crediti).
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys
import time
import wave

import numpy as np
import requests

URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128"
SR = 44100


def dividi(testo, k, frasi=None):
    """Divide il testo di una scena in k parti contigue (una per immagine)."""
    if frasi:
        if len(frasi) != k or " ".join(f.strip() for f in frasi) != " ".join(testo.split()):
            sys.exit(f"frasi_immagini non corrisponde al testo o al numero di immagini: {frasi}")
        return [f.strip() for f in frasi]
    if k <= 1:
        return [testo]
    for livello in (r"[.?!]", r"[.?!:;]", r"[.?!:;,]"):
        punti = [m.end() for m in re.finditer(livello + r"\s+", testo)]
        if len(punti) >= k - 1:
            scelti, usati = [], set()
            for j in range(1, k):
                bersaglio = len(testo) * j / k
                p = min((p for p in punti if p not in usati and (not scelti or p > scelti[-1])),
                        key=lambda p: abs(p - bersaglio))
                scelti.append(p)
                usati.add(p)
            tagli = [0] + scelti + [len(testo)]
            return [testo[a:b].strip() for a, b in zip(tagli[:-1], tagli[1:])]
    parole = testo.split()
    n = len(parole)
    return [" ".join(parole[round(n * j / k):round(n * (j + 1) / k)]) for j in range(k)]


def tts(voice, testo, scena, modello, speed, timeout=300):
    body = {"text": testo, "model_id": modello, "language_code": "it",
            "voice_settings": {"stability": scena["stability"], "similarity_boost": 0.8, "style": scena["style"],
                               "use_speaker_boost": True, "speed": speed}}
    for n in range(1, 5):
        try:
            r = requests.post(URL.format(voice=voice), headers={"xi-api-key": "proxy",
                                                                "Content-Type": "application/json"},
                              json=body, timeout=timeout)
        except requests.RequestException as e:
            print(f"scena {scena['id']}: errore di rete {e}", file=sys.stderr)
            r = None
        if r is not None and r.status_code == 200:
            return r.json()
        if r is not None and r.status_code < 500:
            print(f"scena {scena['id']}: HTTP {r.status_code} {r.text[:800]}", file=sys.stderr)
            if r.status_code in (401, 402):
                print("Piano gratuito o crediti finiti: fermati e avvisa l'utente (non ritentare).", file=sys.stderr)
            sys.exit(2)
        time.sleep(2 ** n)
    sys.exit("tentativi esauriti")


def decodifica_mp3(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16)


def allineamento_finto(testo, sec_per_car=0.065):
    n = len(testo)
    return {"characters": list(testo), "character_start_times_seconds": [i * sec_per_car for i in range(n)],
            "character_end_times_seconds": [(i + 1) * sec_per_car for i in range(n)]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scene")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--voice-id", default="f8NAZK1ciwrVujah7clz")
    ap.add_argument("--modello", default="eleven_multilingual_v2")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--pausa", type=float, default=0.3, help="silenzio tra una scena e l'altra (s)")
    ap.add_argument("--conferma", action="store_true", help="l'utente ha chiesto/confermato la generazione")
    ap.add_argument("--simula", action="store_true", help="nessuna chiamata: tempi finti per provare la catena")
    a = ap.parse_args()
    if not (a.conferma or a.simula):
        sys.exit("Serve --conferma (l'utente ha chiesto la voce o ha un piano a pagamento) oppure --simula.")
    scene = json.load(open(a.scene, encoding="utf-8"))
    os.makedirs(os.path.join(a.out_dir, "scene"), exist_ok=True)

    t, pezzi, scene_out, segmenti = 0.25, [np.zeros(int(0.25 * SR), dtype=np.int16)], [], []
    for s in scene:
        testo = s["text"].strip()
        if a.simula:
            al = allineamento_finto(testo)
            dur = al["character_end_times_seconds"][-1] + 0.1
            audio = np.zeros(int(dur * SR), dtype=np.int16)
        else:
            j = tts(a.voice_id, testo, s, a.modello, a.speed)
            mp3 = os.path.join(a.out_dir, "scene", f"{int(s['id']):02d}.mp3")
            open(mp3, "wb").write(base64.b64decode(j["audio_base64"]))
            al = j["alignment"]
            audio = decodifica_mp3(mp3)
            dur = len(audio) / SR
        chars = "".join(al["characters"])
        st, en = al["character_start_times_seconds"], al["character_end_times_seconds"]
        scene_out.append({"id": s["id"], "text": testo, "start": round(t, 3), "end": round(t + dur, 3)})
        # un segmento per immagine
        imm = s.get("immagini") or [None]
        pos = 0
        for img, parte in zip(imm, dividi(testo, len(imm), s.get("frasi_immagini"))):
            i = chars.index(parte, pos)
            jf = i + len(parte) - 1
            segmenti.append({"img": img, "scena": s["id"], "text": parte,
                             "start": round(t + st[i], 3), "end": round(t + en[jf], 3)})
            pos = jf + 1
        pezzi += [audio, np.zeros(int(a.pausa * SR), dtype=np.int16)]
        t += dur + a.pausa
        print(f"scena {s['id']}: {dur:.2f} s, {len(imm)} immagini")
    pezzi.append(np.zeros(int(0.4 * SR), dtype=np.int16))
    tutto = np.concatenate(pezzi)
    totale = len(tutto) / SR
    json.dump({"voice": a.voice_id, "model": a.modello, "simulato": a.simula, "scene": scene_out,
               "segments": segmenti, "total": round(totale, 3)},
              open(os.path.join(a.out_dir, "tempi_voce.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not a.simula:
        wav = os.path.join(a.out_dir, "voce.wav")
        with wave.open(wav, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SR)
            wf.writeframes(tutto.tobytes())
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-c:a", "libmp3lame", "-b:a", "128k",
                        os.path.join(a.out_dir, "voce.mp3")], check=True)
    print(f"totale {totale:.2f} s, {len(segmenti)} segmenti -> {a.out_dir}/tempi_voce.json"
          + (" (SIMULATO: nessun audio)" if a.simula else ""))


if __name__ == "__main__":
    main()
