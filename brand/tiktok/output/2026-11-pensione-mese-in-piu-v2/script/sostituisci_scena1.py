#!/usr/bin/env python3
"""Sostituisce la scena 1 della voce con una nuova registrazione ElevenLabs (solo per questo post).

La voce del 30/10/2026 (voce.mp3, 30,04 s) ha la scena 1 diversa dal testo approvato (dice «per raggiungere la
pensione di vecchiaia, si dovrà lavorare un mese in più» invece di «per quasi tutti, la pensione di vecchiaia si
sposta più in là»); dal «Ma perché?» in poi è giusta. Questo script tiene la voce attuale da TAGLIO (7,70 s, nel
silenzio 7,34-7,77 s subito prima di «Ma perché?») alla fine e ci mette davanti la nuova scena 1.

Uso (dalla radice del repository):
  P=brand/tiktok/output/2026-11-pensione-mese-in-piu-v2
  python3 $P/script/sostituisci_scena1.py NUOVA.mp3 --out $P/voce.mp3        # poi: bash $P/script/monta.sh $P/voce.mp3

NUOVA.mp3 può essere:
- solo la scena 1 («Sessantasette anni e un mese. Dal duemilaventisette, per quasi tutti, … più in là.»):
  si usa tutta, tolti i silenzi all'inizio e alla fine;
- l'intero testo rigenerato: la scena 1 finisce nel silenzio prima di «Ma perché?». Lo script lo cerca da solo
  (il silenzio più lungo, >= 0,25 s a -35 dB, che inizia fra 4,5 e 10 s) e stampa i candidati: se sceglie
  male, indica la fine a mano con --fine SECONDI.

Poi: pareggia il volume della nuova scena sul resto (loudness integrata, solo se differisce più di 3 dB: nella voce attuale la scena 1 è già
~1,3 dB più forte del resto, ed è voluto), mette
PAUSA s di silenzio fra le due parti (ritmo.py la porta poi a 0,36 s prima di «Ma perché?»), dissolvenze di
10 ms alle giunzioni, e trascrive la nuova scena (muse-spark-1.3, transcribe.py) per controllare il testo.
La voce di partenza resta quella indicata da --voce (default: voce.mp3 del post): se --out è lo stesso file,
viene sovrascritta (la vecchia resta nella storia di git).
"""
import argparse, os, re, subprocess, sys, tempfile
import numpy as np

QUI = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(QUI)
SR = 44100


def leggi(path, da=None, a=None):
    cmd = ["ffmpeg", "-loglevel", "error"]
    if da is not None:
        cmd += ["-ss", f"{da:.3f}"]
    if a is not None:
        cmd += ["-to", f"{a:.3f}"]
    cmd += ["-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, check=True, capture_output=True).stdout, dtype=np.float32).copy()


def silenzi(path, soglia=-35, durata=0.25):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", f"silencedetect=n={soglia}dB:d={durata}",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", r)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    return list(zip(st, en + [None] * (len(st) - len(en))))


def durata(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True, check=True).stdout)


def lufs(x):
    with tempfile.NamedTemporaryFile(suffix=".wav") as t:
        scrivi(x, t.name)
        r = subprocess.run(["ffmpeg", "-hide_banner", "-i", t.name, "-af", "ebur128", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1])


def scrivi(x, path):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-"]
                   + (["-c:a", "libmp3lame", "-b:a", "192k"] if path.endswith(".mp3") else []) + [path],
                   input=x.astype(np.float32).tobytes(), check=True)


def sfuma(x, ms=10):
    n = int(SR * ms / 1000)
    x = x.copy()
    x[:n] *= np.linspace(0, 1, n)
    x[-n:] *= np.linspace(1, 0, n)
    return x


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("nuova")
    ap.add_argument("--voce", default=os.path.join(POST, "voce.mp3"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--taglio", type=float, default=7.70, help="da dove tenere la voce attuale (s)")
    ap.add_argument("--fine", type=float, help="fine della scena 1 nel file nuovo (s); default automatico")
    ap.add_argument("--pausa", type=float, default=0.40)
    ap.add_argument("--soglia-db", type=float, default=3.0,
                    help="pareggia il volume solo oltre questa differenza (la scena 1 'sorpresa' è di solito più forte)")
    ap.add_argument("--senza-trascrizione", action="store_true")
    a = ap.parse_args()

    dn = durata(a.nuova)
    sil = silenzi(a.nuova)
    inizio = sil[0][1] if sil and sil[0][0] <= 0.01 and sil[0][1] else 0.0
    if a.fine is not None:
        fine = a.fine
    elif dn <= 10:
        coda = [s for s in sil if s[1] is None or s[1] >= dn - 0.01]
        fine = coda[-1][0] if coda else dn
        print(f"file corto ({dn:.2f} s): lo prendo come sola scena 1")
    else:
        cand = [s for s in sil if 4.5 <= s[0] <= 10 and s[1]]
        if not cand:
            sys.exit("nessun silenzio fra 4,5 e 10 s: indica la fine della scena 1 con --fine")
        print("silenzi candidati (inizio-fine):", ", ".join(f"{s:.2f}-{e:.2f}" for s, e in cand))
        fine = max(cand, key=lambda s: s[1] - s[0])[0]
    print(f"scena 1 nuova: {inizio:.2f}-{fine:.2f} s ({fine - inizio:.2f} s)")

    s1 = leggi(a.nuova, max(0, inizio - 0.05), fine + 0.05)
    resto = leggi(a.voce, a.taglio)
    l1, l2 = lufs(s1), lufs(resto)
    if abs(l1 - l2) > a.soglia_db:
        s1 = s1 * 10 ** ((l2 - l1) / 20)
        print(f"volume: scena 1 {l1:.1f} LUFS, resto {l2:.1f} LUFS -> scena 1 corretta di {l2 - l1:+.1f} dB")
    else:
        print(f"volume: scena 1 {l1:.1f} LUFS, resto {l2:.1f} LUFS (ok)")
    x = np.concatenate([sfuma(s1), np.zeros(int(SR * a.pausa), np.float32), sfuma(resto)])
    picco = float(np.abs(x).max())
    if picco > 0.99:
        x = x * (0.99 / picco)
    scrivi(x, a.out)
    print(f"scritto {a.out}: {len(x) / SR:.2f} s (scena 1 fino a {len(s1) / SR:.2f} s, «Ma perché?» da "
          f"~{len(s1) / SR + a.pausa + 0.07:.2f} s)")

    if not a.senza_trascrizione:
        with tempfile.TemporaryDirectory() as d:
            w = os.path.join(d, "scena1.wav")
            scrivi(np.concatenate([np.zeros(SR, np.float32), s1, np.zeros(SR, np.float32)]), w)
            print("trascrizione della nuova scena 1 (deve essere: «Sessantasette anni e un mese. Dal duemilaventisette, "
                  "per quasi tutti, la pensione di vecchiaia si sposta più in là.»):")
            subprocess.run([sys.executable, "-I", os.path.join(QUI, "transcribe.py"), w], check=False)


if __name__ == "__main__":
    main()
