#!/usr/bin/env python3
"""Allinea l'audio di ElevenLabs alle scene di scene.json (dove inizia e finisce ogni scena, e ogni parola).
Uso: allinea.py CARTELLA_EPISODIO [AUDIO] [--locale]
- AUDIO: file caricato dall'utente (mp3/wav/m4a). Se manca usa CARTELLA/voce/voce-originale.*
- Scrive CARTELLA/voce/voce.wav (mono 44,1 kHz) e CARTELLA/voce/tempi.json.

Metodo 1 (se ci sono crediti): ElevenLabs Speech-to-Text (scribe_v1) con i tempi di ogni parola.
Metodo 2 (--locale o se il primo fallisce): pause nell'audio + numero di sillabe di ogni scena.
Funziona bene se tra una scena e l'altra c'è una pausa udibile (in ElevenLabs: una riga per scena)."""
import difflib, glob, json, os, subprocess, sys, wave
import numpy as np
import requests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comune import carica_episodio, sillabe, tokens  # noqa: E402


def leggi_wav(path):
    with wave.open(path) as wf:
        sr = wf.getframerate()
        a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return a, sr


def scribe(audio_path):
    with open(audio_path, "rb") as fh:
        r = requests.post("https://api.elevenlabs.io/v1/speech-to-text", headers={"xi-api-key": "proxy"},
                          data={"model_id": "scribe_v1", "language_code": "it", "timestamps_granularity": "word",
                                "tag_audio_events": "false"},
                          files={"file": (os.path.basename(audio_path), fh)}, timeout=300)
    if r.status_code != 200:
        print("Speech-to-Text ElevenLabs non disponibile:", r.status_code, r.text[:200])
        return None
    j = r.json()
    words = [w for w in j.get("words", []) if w.get("type", "word") == "word"]
    return {"text": j.get("text"), "words": [{"text": w["text"], "start": w["start"], "end": w["end"]} for w in words]}


def con_parole(scene, stt):
    """Mappa i token delle scene sui token trascritti (difflib) e ricava i tempi."""
    sc_tok, sc_idx = [], []
    for k, s in enumerate(scene):
        for t in tokens(s["voce"]):
            sc_tok.append(t)
            sc_idx.append(k)
    st_tok, st_time = [], []
    for w in stt["words"]:
        for t in tokens(w["text"]):
            st_tok.append(t)
            st_time.append((w["start"], w["end"]))
    sm = difflib.SequenceMatcher(None, sc_tok, st_tok, autojunk=False)
    mapped = [None] * len(sc_tok)
    for a, b, n in sm.get_matching_blocks():
        for i in range(n):
            mapped[a + i] = st_time[b + i]
    match = sum(m is not None for m in mapped) / max(1, len(mapped))
    # interpola i token non trovati (es. numeri trascritti in cifre)
    known = [i for i, m in enumerate(mapped) if m]
    if len(known) < 2:
        return None, match
    starts = np.interp(range(len(mapped)), known, [mapped[i][0] for i in known])
    ends = np.interp(range(len(mapped)), known, [mapped[i][1] for i in known])
    segs = []
    for k, s in enumerate(scene):
        ii = [i for i, x in enumerate(sc_idx) if x == k]
        segs.append({"id": s["id"], "start": round(float(starts[ii[0]]), 3), "end": round(float(ends[ii[-1]]), 3),
                     "token_start": [round(float(starts[i]), 3) for i in ii]})
    return segs, match


def pause(audio, sr, min_dur=0.14):
    hop = int(0.01 * sr)
    env = np.array([np.sqrt(np.mean(audio[i:i + hop] ** 2)) for i in range(0, len(audio) - hop, hop)])
    thr = max(0.004, 0.07 * np.percentile(env, 95))
    quiet = env < thr
    voiced = np.where(~quiet)[0]
    t0, t1 = voiced[0] * 0.01, (voiced[-1] + 1) * 0.01
    out, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if (j - i) * 0.01 >= min_dur and i * 0.01 > t0 and j * 0.01 < t1:
                out.append((i * 0.01, j * 0.01))
            i = j
        else:
            i += 1
    return out, t0, t1


def con_pause(scene, audio, sr):
    sil, t0, t1 = pause(audio, sr)
    w = [sum(sillabe(t) for t in tokens(s["voce"])) + 2 for s in scene]
    cum = np.cumsum(w)[:-1] / sum(w)
    exp = t0 + (t1 - t0) * cum
    n, m = len(exp), len(sil)
    span = t1 - t0
    if m < n:
        print(f"ATTENZIONE: trovate solo {m} pause per {n} tagli: tagli stimati in proporzione al testo")
        bounds = [(e - 0.05, e + 0.05) for e in exp]
    else:
        mid = [(a + b) / 2 for a, b in sil]
        dur = [b - a for a, b in sil]
        cost = lambda k, j: 400 * ((mid[j] - exp[k]) / span) ** 2 - 2.0 * min(dur[j], 0.7)  # noqa: E731
        INF = 1e18
        dp = np.full((n, m), INF)
        bk = np.zeros((n, m), dtype=int)
        for j in range(m):
            dp[0][j] = cost(0, j)
        for k in range(1, n):
            best, arg = INF, -1
            for j in range(m):
                if j - 1 >= 0 and dp[k - 1][j - 1] < best:
                    best, arg = dp[k - 1][j - 1], j - 1
                if best < INF:
                    dp[k][j] = best + cost(k, j)
                    bk[k][j] = arg
        j = int(np.argmin(dp[n - 1]))
        sel = [j]
        for k in range(n - 1, 0, -1):
            j = bk[k][j]
            sel.append(j)
        bounds = [sil[j] for j in reversed(sel)]
    segs = []
    starts = [t0] + [b for _, b in bounds]
    ends = [a for a, _ in bounds] + [t1]
    for s, a, b in zip(scene, starts, ends):
        segs.append({"id": s["id"], "start": round(float(a), 3), "end": round(float(b), 3)})
    return segs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ep = args[0]
    vd = os.path.join(ep, "voce")
    os.makedirs(vd, exist_ok=True)
    src = args[1] if len(args) > 1 else (sorted(glob.glob(os.path.join(vd, "voce-originale.*"))) or [None])[0]
    if not src:
        sys.exit("Manca l'audio: passa il file o mettilo in voce/voce-originale.mp3")
    ext = os.path.splitext(src)[1]
    orig = os.path.join(vd, "voce-originale" + ext)
    if os.path.abspath(src) != os.path.abspath(orig):
        subprocess.run(["cp", src, orig], check=True)
    wav = os.path.join(vd, "voce.wav")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", orig, "-ac", "1", "-ar", "44100", "-sample_fmt", "s16",
                    wav], check=True)
    audio, sr = leggi_wav(wav)
    durata = len(audio) / sr
    scene = carica_episodio(ep)["scene"]

    segs, metodo = None, "pause"
    if "--locale" not in sys.argv:
        stt = scribe(orig)
        if stt:
            json.dump(stt, open(os.path.join(vd, "trascrizione.json"), "w"), ensure_ascii=False, indent=1)
            segs, match = con_parole(scene, stt)
            print(f"trascrizione: {match:.0%} delle parole del copione ritrovate")
            if segs and match >= 0.6:
                metodo = "parole"
            else:
                segs = None
    if segs is None:
        segs = con_pause(scene, audio, sr)
    json.dump({"metodo": metodo, "durata_audio": round(durata, 3), "segments": segs,
               "total": round(min(durata, segs[-1]["end"] + 0.6), 3)},
              open(os.path.join(vd, "tempi.json"), "w"), ensure_ascii=False, indent=1)
    print(f"metodo: {metodo}; audio {durata:.1f} s")
    for s, sc in zip(segs, scene):
        print(f"  {s['id']:>4} {s['start']:6.2f}-{s['end']:6.2f}  {sc['voce'][:60]}")
    if durata > 42:
        print(f"ATTENZIONE: l'audio dura {durata:.0f} s (obiettivo 30-40 s)")


if __name__ == "__main__":
    main()
