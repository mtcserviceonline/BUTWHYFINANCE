#!/usr/bin/env python3
"""Divide il testo NOTO della voce in frasi allineate alle pause dell'audio (senza riconoscimento vocale).

Uso: frasi.py VOCE.wav TESTO OUT_FRASI.json [--soglia -35] [--min 0.08]
TESTO: scene_elevenlabs.json (si usa il campo "text" di ogni scena, in ordine) oppure un .txt.

Come funziona:
- silencedetect (soglia -35 dB, pause da 0,08 s) trova le pause vere dell'audio;
- ogni pausa ha una posizione "in sillabe": i picchi di energia (~nuclei sillabici, come in allinea.py)
  contati prima della pausa, riportati al numero di sillabe del testo; ogni spazio tra due parole ha la sua
  posizione contando le sillabe del testo;
- una programmazione dinamica abbina ogni pausa a uno spazio tra due parole, in ordine: abbinare costa
  quanto le due posizioni sono lontane (meno se nel testo li' c'e' punteggiatura); lasciare una
  pausa senza parola costa di piu' quanto piu' la pausa e' lunga (una pausa vera da 0,3 s cade quasi
  sempre tra due parole, una da 0,08 s puo' essere una consonante occlusiva);
- le parole tra due pause abbinate formano una frase: inizio = fine della pausa prima, fine = inizio
  della pausa dopo. allinea.py poi stima le parole dentro ogni frase.
Stampa le frasi con i tempi e lo scarto medio in sillabe: se e' grande (>3) il testo
letto e' probabilmente diverso da quello noto (trascrivi l'audio e controlla)."""
import argparse, json, re, subprocess, sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from allinea import sillabe, picchi  # noqa: E402
import soundfile as sf  # noqa: E402


def silenzi(wav, soglia, dmin):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", wav, "-af", f"silencedetect=n={soglia}dB:d={dmin}",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                         "csv=p=0", wav]).decode())
    if len(en) < len(st):
        en.append(dur)
    return list(zip(st, en)), dur


def testo(path):
    if path.endswith(".json"):
        return " ".join(s["text"] for s in json.load(open(path, encoding="utf-8")))
    return open(path, encoding="utf-8").read()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("wav")
    ap.add_argument("testo")
    ap.add_argument("out")
    ap.add_argument("--soglia", type=float, default=-35)
    ap.add_argument("--min", type=float, default=0.08)
    ap.add_argument("--sigma", type=float, default=2.5)
    a = ap.parse_args()
    # i segni senza lettere (es. la pausa "…" del testo per ElevenLabs) non sono parole parlate
    words = [w for w in testo(a.testo).split() if re.search(r"\w", w)]
    syl = [sillabe(w) for w in words]
    sil, dur = silenzi(a.wav, a.soglia, a.min)
    # inizio e fine del parlato
    t0 = sil[0][1] if sil and sil[0][0] < 0.02 else 0.0
    t1 = sil[-1][0] if sil and sil[-1][1] >= dur - 0.02 else dur
    pause = [(s, e) for s, e in sil if s > t0 + 0.01 and e < t1 - 0.01]
    # posizione di ogni pausa e di ogni spazio tra parole misurata in "sillabe":
    # pausa -> picchi di energia (~sillabe) prima di lei, riportati al totale delle sillabe del testo;
    # spazio dopo la parola j -> sillabe del testo fino a j. Cosi' le differenze di velocita' tra una
    # frase e l'altra non spostano l'abbinamento (con il tempo atteso si')
    x, sr = sf.read(a.wav)
    pk = [p for p in picchi(x, sr) if t0 <= p <= t1]
    tot = sum(syl)
    k_tot = max(1, len(pk))
    pos_pausa = [tot * sum(1 for p in pk if p < (s + e) / 2) / k_tot for s, e in pause]
    cum = 0
    pos_spazio = []
    for j in range(len(words) - 1):
        cum += syl[j]
        pos_spazio.append(cum)
    atteso = pos_spazio
    # 2 = punto/domanda/due punti, 1 = virgola, 0.5 = spazio prima di una congiunzione (in italiano si respira
    # spesso prima di "e", "ma", "che"... anche senza virgola; peso minore: "uno e ventinove"), 0 = niente
    CONG = {"e", "ed", "ma", "che", "perché", "però", "o", "oppure", "quindi"}
    punt = [2 if re.search(r"[.?!:]$", w) else 1 if w.endswith(",") else 0.5 if words[j + 1].lower() in CONG else 0
            for j, w in enumerate(words[:-1])]
    G, P = len(atteso), len(pause)
    INF = 1e18

    def costo_salta(d):
        return (d / 0.13) ** 2

    def costo_abbina(k, j):
        peso = min(1.0, (pause[k][1] - pause[k][0]) / 0.3)     # le pause lunghe "vogliono" la punteggiatura
        # 0.6 fisso: una pausa brevissima senza punteggiatura (spesso l'occlusione di una "p" o una "t"
        # dentro la parola) costa meno lasciarla senza abbinamento che metterla tra due parole
        return 0.6 + ((pos_pausa[k] - pos_spazio[j]) / a.sigma) ** 2 - peso * (3.0 if punt[j] == 2 else 1.5 if punt[j] == 1 else 1.0 if punt[j] == 0.5 else 0)

    def costo_vuoto(j):               # spazio con punteggiatura forte rimasto senza pausa
        return 0.8 if punt[j] == 2 else 0.2 if punt[j] == 1 else 0
    # dp[k][j]: prime k pause trattate, ultimo spazio "consumato" j (-1 = nessuno)
    dp = [[INF] * (G + 1) for _ in range(P + 1)]
    bk = [[None] * (G + 1) for _ in range(P + 1)]
    dp[0][0] = 0                      # indice j+1
    for k in range(P):
        d = pause[k][1] - pause[k][0]
        for jj in range(G + 1):
            c = dp[k][jj]
            if c >= INF:
                continue
            # salta la pausa
            v = c + costo_salta(d)
            if v < dp[k + 1][jj]:
                dp[k + 1][jj], bk[k + 1][jj] = v, (jj, None)
            # abbinala allo spazio j >= jj (spazi in mezzo restano senza pausa)
            vuoti = 0
            for j in range(jj, G):
                v = c + vuoti + costo_abbina(k, j)
                if v < dp[k + 1][j + 1]:
                    dp[k + 1][j + 1], bk[k + 1][j + 1] = v, (jj, j)
                vuoti += costo_vuoto(j)
    best = min(range(G + 1), key=lambda jj: dp[P][jj] + sum(costo_vuoto(j) for j in range(jj, G)))
    match, jj = {}, best
    for k in range(P, 0, -1):
        pj, j = bk[k][jj]
        if j is not None:
            match[j] = pause[k - 1]
        jj = pj
    frasi, cur, start = [], [], t0
    scarti = []
    for i, w in enumerate(words):
        cur.append(w)
        if i in match:
            s, e = match[i]
            scarti.append(abs(pos_pausa[pause.index((s, e))] - pos_spazio[i]))
            frasi.append({"text": " ".join(cur), "start": round(start, 3), "end": round(s, 3)})
            cur, start = [], e
    frasi.append({"text": " ".join(cur), "start": round(start, 3), "end": round(t1, 3)})
    saltate = [p for p in pause if p not in match.values()]
    for f in frasi:
        print(f"{f['start']:6.2f}-{f['end']:6.2f}  {f['text']}")
    print(f"{len(words)} parole, {len(pause)} pause, {len(match)} abbinate, saltate: "
          + ", ".join(f"{s:.2f}-{e:.2f}" for s, e in saltate))
    m = sum(scarti) / max(1, len(scarti))
    print(f"scarto medio pausa/posizione attesa {m:.1f} sillabe" + ("  ATTENZIONE: testo forse diverso dall'audio" if m > 3 else ""))
    json.dump(frasi, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
