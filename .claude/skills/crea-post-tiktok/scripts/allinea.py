#!/usr/bin/env python3
"""Stima i tempi di ogni parola senza modello di riconoscimento vocale.
Uso: allinea.py VOCE.wav FRASI.json OUT_PAROLE.json
FRASI.json: [{"text": "...", "start": s, "end": e}, ...] con inizio/fine di ogni frase presi dalle pause
(silencedetect). Dentro la frase i picchi di energia (300-2500 Hz) approssimano i nuclei sillabici:
le sillabe del testo vengono distribuite sui picchi e ogni parola parte al confine del suo primo picco."""
import json, re, sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfiltfilt, find_peaks

VOC = "aeiouàèéìíòóùú"


def sillabe(w):
    w = w.lower().replace("'", " ")
    n = 0
    for part in w.split():
        part = re.sub(r"[^a-zàèéìíòóùú0-9]", "", part)
        # dittonghi comuni contano una sillaba: gruppi di vocali = 1 (approssimazione)
        n += max(1, len(re.findall(f"[{VOC}]+", part))) if part else 0
    return max(1, n)


def picchi(x, sr):
    """Istanti (s) dei picchi di energia 300-2500 Hz, che approssimano i nuclei sillabici."""
    if x.ndim > 1:
        x = x.mean(axis=1)
    y = sosfiltfilt(butter(4, [300, 2500], btype="band", fs=sr, output="sos"), x)
    hop = int(0.01 * sr)
    env = np.array([np.sqrt(np.mean(y[i:i + hop] ** 2)) for i in range(0, len(y) - hop, hop)])
    env = np.convolve(env, np.hanning(7) / np.hanning(7).sum(), mode="same")
    db = 20 * np.log10(env + 1e-6)
    pk, _ = find_peaks(db, prominence=2.5, height=db.max() - 30, distance=8)
    return pk / 100.0


def main():
    x, sr = sf.read(sys.argv[1])
    pk = picchi(x, sr)
    frasi = json.load(open(sys.argv[2], encoding="utf-8"))
    out = []
    for fr in frasi:
        a, b = fr["start"], fr["end"]
        words = fr["text"].split()
        syl = [sillabe(w) for w in words]
        n = sum(syl)
        p = [t for t in pk if a <= t <= b] or [(a + b) / 2]
        m = len(p)
        # confini: inizio frase, punti medi tra picchi, fine frase -> m intervalli, uno per picco
        bounds = [a] + [(p[k] + p[k + 1]) / 2 for k in range(m - 1)] + [b]

        def at(q):  # q = posizione frazionaria in "picchi" (0..m)
            k = min(int(q), m - 1)
            return bounds[k] + (bounds[k + 1] - bounds[k]) * (q - k)
        acc = 0
        for w, s in zip(words, syl):
            st, en = at(acc * m / n), at((acc + s) * m / n)
            out.append({"w": w, "start": round(st, 3), "end": round(en, 3)})
            acc += s
        out[-1]["end"] = round(b, 3)
        print(f"{a:6.2f}-{b:5.2f} sillabe {n:2d} picchi {m:2d}  {fr['text']}")
    json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
