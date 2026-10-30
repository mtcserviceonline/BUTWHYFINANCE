#!/usr/bin/env python3
"""Ritmo della voce: accorcia le pause lunghe tra le frasi e, se serve, accelera senza cambiare l'intonazione.

Uso: ritmo.py VOCE.wav FRASI.json OUT.wav OUT_FRASI.json [opzioni]
  --pausa-max 0.30        le pause tra frasi piu' lunghe di --oltre (0,40 s) diventano di 0,30 s
  --oltre 0.40
  --pausa-prima "Ma perché?=0.36"   la pausa prima della frase che inizia cosi' prende questa durata
                          (ripetibile; A2: 0,3-0,4 s prima di "Ma perché?")
  --attacco 0.05          silenzio lasciato prima della prima parola (il video parte con la voce)
  --wpm 170 --wpm-min 165 --vmax 1.12
                          se dopo le pause la voce e' sotto 165 parole/min (A3: 165-175) accelera fino a
                          ~170 parole/min, mai oltre 1,12x; se e' gia' nell'intervallo non la tocca
                          (--velocita X per un valore fisso; 1 = nessuna accelerazione)
Le parole non vengono mai tagliate: si tolgono solo pezzi di silenzio (dal centro della pausa, con
dissolvenze di 10 ms). L'accelerazione usa il filtro rubberband di ffmpeg (formanti preservate), oppure
atempo se rubberband non c'e'. FRASI.json (da frasi.py) viene riscritto con i tempi nuovi.
Stampa durata originale e finale, parole/min prima e dopo, pause cambiate."""
import argparse, json, subprocess, tempfile, os
import numpy as np, soundfile as sf


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav"); ap.add_argument("frasi"); ap.add_argument("out"); ap.add_argument("out_frasi")
    ap.add_argument("--pausa-max", type=float, default=0.30)
    ap.add_argument("--oltre", type=float, default=0.40)
    ap.add_argument("--pausa-prima", action="append", default=[])
    ap.add_argument("--attacco", type=float, default=0.05)
    ap.add_argument("--wpm", type=float, default=170)
    ap.add_argument("--wpm-min", type=float, default=165)
    ap.add_argument("--vmax", type=float, default=1.12)
    ap.add_argument("--velocita", type=float)
    a = ap.parse_args()
    x, sr = sf.read(a.wav)
    if x.ndim > 1:
        x = x.mean(axis=1)
    fr = json.load(open(a.frasi, encoding="utf-8"))
    n_parole = sum(len(f["text"].split()) for f in fr)
    prima = {}
    for p in a.pausa_prima:
        k, v = p.rsplit("=", 1)
        prima[k.strip().lower()] = float(v)
    # tagli: (inizio, fine) del silenzio da togliere, in secondi dell'originale
    tagli, log = [], []
    if fr[0]["start"] > a.attacco + 0.01:
        tagli.append((0.0, fr[0]["start"] - a.attacco))
        log.append(f"attacco {fr[0]['start']:.2f} -> {a.attacco:.2f} s")
    for f0, f1 in zip(fr, fr[1:]):
        d = f1["start"] - f0["end"]
        target = None
        for k, v in prima.items():
            if f1["text"].lower().startswith(k):
                target = v
        if target is None and d > a.oltre:
            target = a.pausa_max
        if target is not None and d > target + 0.01:
            mid = (f0["end"] + f1["start"]) / 2
            tagli.append((mid - (d - target) / 2, mid + (d - target) / 2))
            log.append(f"pausa {f0['end']:.2f}-{f1['start']:.2f} ({d:.2f} s) -> {target:.2f} s  prima di \"{f1['text'][:30]}\"")
        elif target is not None:
            log.append(f"pausa {f0['end']:.2f}-{f1['start']:.2f} ({d:.2f} s) lasciata (gia' <= {target:.2f} s) prima di \"{f1['text'][:30]}\"")
    # ricostruzione con dissolvenze di 10 ms ai tagli
    fade = int(0.01 * sr)
    pezzi, prev = [], 0
    for s, e in tagli:
        i, j = int(s * sr), int(e * sr)
        pezzi.append(x[prev:i].copy())
        prev = j
    pezzi.append(x[prev:].copy())
    y = pezzi[0]
    for p in pezzi[1:]:
        n = min(fade, len(y), len(p))
        r = np.linspace(0, 1, n)
        y = np.concatenate([y[:-n], y[-n:] * (1 - r) + p[:n] * r, p[n:]]) if n else np.concatenate([y, p])

    def mappa(t):                      # tempo originale -> tempo dopo i tagli
        tolto = 0
        for s, e in tagli:
            if t >= e:
                tolto += e - s
            elif t > s:
                tolto += t - s
        return t - tolto
    fr2 = [{"text": f["text"], "start": mappa(f["start"]), "end": mappa(f["end"])} for f in fr]
    parlato0 = fr[-1]["end"] - fr[0]["start"]
    parlato1 = fr2[-1]["end"] - fr2[0]["start"]
    wpm0, wpm1 = n_parole / parlato0 * 60, n_parole / parlato1 * 60
    v = a.velocita if a.velocita else (1.0 if wpm1 >= a.wpm_min else min(a.vmax, a.wpm / wpm1))
    tmp = tempfile.mktemp(suffix=".wav")
    sf.write(tmp, y.astype(np.float32), sr)
    filtri = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True).stdout
    if abs(v - 1) < 1e-3:
        filtro = "anull"
    elif " rubberband " in filtri:
        filtro = f"rubberband=tempo={v:.4f}:formant=preserved:pitchq=quality:transients=mixed:detector=compound"
    else:
        filtro = f"atempo={v:.4f}"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp, "-af", filtro, "-ar", str(sr), a.out], check=True)
    os.remove(tmp)
    fr3 = [{"text": f["text"], "start": round(f["start"] / v, 3), "end": round(f["end"] / v, 3)} for f in fr2]
    json.dump(fr3, open(a.out_frasi, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    d0 = len(x) / sr
    d1 = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                        "csv=p=0", a.out]).decode())
    for l in log:
        print(l)
    print(f"parole {n_parole}; durata {d0:.2f} s -> {d1:.2f} s; parlato {parlato0:.2f} -> {parlato1 / v:.2f} s; "
          f"parole/min {wpm0:.0f} -> {wpm1:.0f} (pause) -> {wpm1 * v:.0f} (velocita' {v:.3f}x, {filtro.split('=')[0]})")
    json.dump({"durata_originale": round(d0, 3), "durata_finale": round(d1, 3), "parole": n_parole,
               "wpm_originale": round(wpm0, 1), "wpm_dopo_pause": round(wpm1, 1), "velocita": round(v, 4),
               "wpm_finale": round(wpm1 * v, 1), "filtro": filtro, "tagli": [[round(s, 3), round(e, 3)] for s, e in tagli],
               "modifiche": log}, open(os.path.splitext(a.out_frasi)[0] + "_ritmo.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
