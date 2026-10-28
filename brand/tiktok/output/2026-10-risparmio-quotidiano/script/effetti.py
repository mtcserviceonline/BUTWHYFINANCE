#!/usr/bin/env python3
"""Effetti sonori sintetizzati (numpy, nessun campione esterno) e mix con la voce.
Uso: effetti.py VOCE.wav TEMPI.json MIX.wav EFFETTI.wav
TEMPI.json e' quello scritto da montage.py: la lista "effetti" ha {"effetto", "t"}.
La voce non viene toccata (ne' tagliata ne' compressa): gli effetti si sommano sotto, a volume basso.
Effetti disponibili: scontrino, tick, colpo, moneta, monetine, pop, forbici, carta, salvadanaio.
Regola v2 (A8): effetti leggeri solo sui numeri (scontrino sul "470", tick sugli altri numeri, pop su
Primo/Secondo/Terzo); quali e dove lo decide EFFETTI in config_video.py."""
import json, sys
import numpy as np, soundfile as sf

RNG = np.random.default_rng(7)


def env_exp(n, sr, tau):
    return np.exp(-np.arange(n) / sr / tau)


def tone(freqs, amps, dur, sr, tau):
    t = np.arange(int(dur * sr)) / sr
    s = sum(a * np.sin(2 * np.pi * f * t + RNG.uniform(0, 6.28)) for f, a in zip(freqs, amps))
    return s * env_exp(len(t), sr, tau)


def noise(dur, sr):
    return RNG.standard_normal(int(dur * sr))


def bandpass(x, sr, lo, hi):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / sr)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))


def fade_in(x, sr, ms=2):
    n = min(len(x), int(sr * ms / 1000))
    x[:n] *= np.linspace(0, 1, n)
    return x


def clink(sr, base=2600.0):
    """Moneta: parziali inarmoniche, attacco netto, coda breve."""
    r = [1.0, 1.52, 2.17, 2.79]
    s = tone([base * k for k in r], [1, .7, .45, .3], 0.35, sr, 0.07)
    s[: int(0.004 * sr)] += bandpass(noise(0.004, sr), sr, 3000, 9000) * 0.4
    return fade_in(s, sr, 1)


def place(dst, x, at, sr):
    i = int(at * sr)
    j = min(len(dst), i + len(x))
    dst[i:j] += x[: j - i]


def sfx(name, sr):
    if name == "colpo":            # tonfo morbido + fruscio di scontrino (hook)
        t = np.arange(int(0.35 * sr)) / sr
        f = 55 + 95 * np.exp(-t / 0.05)
        thud = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.07)
        click = np.diff(noise(0.35, sr), prepend=0) * np.exp(-t / 0.012) * 0.35
        return fade_in(thud * 0.8 + click, sr), 0.0
    if name == "scontrino":        # stampante di scontrini: raffica di scatti + strappo, con un colpo morbido sotto
        out = np.zeros(int(0.45 * sr))
        t = np.arange(int(0.3 * sr)) / sr
        f = 60 + 80 * np.exp(-t / 0.05)
        place(out, np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.06) * 0.7, 0, sr)
        for k in range(14):                       # scatti della testina, 18 ms l'uno
            n = noise(0.006, sr)
            place(out, bandpass(n, sr, 1800, 7000) * env_exp(len(n), sr, 0.0015) * (0.55 + 0.03 * k), 0.012 + k * 0.018, sr)
        n = noise(0.09, sr)                       # strappo della carta
        tear = bandpass(n, sr, 1500, 8000) * np.sin(np.linspace(0, np.pi, len(n))) * 0.6
        place(out, tear, 0.29, sr)
        return fade_in(out, sr, 1), 0.0
    if name == "tick":             # tasto di cassa/calcolatrice: clic breve e leggero (numeri)
        n = noise(0.012, sr)
        s = bandpass(n, sr, 2500, 9000) * env_exp(len(n), sr, 0.002)
        s = np.concatenate([s, np.zeros(int(0.02 * sr))])
        place(s, tone([1900], [0.4], 0.025, sr, 0.006), 0.0, sr)
        return fade_in(s, sr, 0.5), 0.0
    if name == "moneta":           # due tocchi di moneta
        out = np.zeros(int(0.5 * sr))
        place(out, clink(sr, 2600), 0, sr)
        place(out, clink(sr, 3100) * 0.7, 0.07, sr)
        return out, 0.0
    if name == "monetine":         # monetine che cadono, sempre piu' piano
        out = np.zeros(int(0.9 * sr))
        for k, at in enumerate([0.0, 0.11, 0.2, 0.31, 0.39, 0.5]):
            place(out, clink(sr, RNG.uniform(2300, 3600)) * (0.9 ** k) * RNG.uniform(.6, 1), at, sr)
        return out, 0.0
    if name == "pop":              # "pop" morbido sui titoli: sinusoide che scende 700 -> 250 Hz
        t = np.arange(int(0.09 * sr)) / sr
        f = 250 + 450 * np.exp(-t / 0.018)
        s = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.025)
        return fade_in(s, sr, 3), 0.0
    if name == "forbici":          # due "snip": rumore filtrato brevissimo + piccolo squillo metallico
        out = np.zeros(int(0.45 * sr))
        for at in (0.0, 0.17):
            n = noise(0.03, sr)
            snip = bandpass(n, sr, 2500, 9000) * env_exp(len(n), sr, 0.006)
            ring = tone([4200, 6100], [.25, .15], 0.08, sr, 0.015)
            place(out, fade_in(snip, sr, 0.5), at, sr)
            place(out, ring, at, sr)
        return out, 0.0
    if name == "carta":            # fruscio di carta
        n = noise(0.32, sr)
        s = bandpass(n, sr, 1200, 6000)
        am = np.interp(np.arange(len(s)), np.linspace(0, len(s), 12), RNG.uniform(.2, 1, 12))
        s *= am * np.sin(np.linspace(0, np.pi, len(s)))
        return s, 0.0
    if name == "salvadanaio":      # moneta che entra nel salvadanaio: tocco + "toc" vuoto di ceramica
        out = np.zeros(int(0.6 * sr))
        place(out, clink(sr, 2900), 0.0, sr)
        place(out, tone([620, 1180, 1750], [1, .5, .25], 0.25, sr, 0.05) * 0.8, 0.16, sr)
        return out, 0.0
    raise ValueError(name)


# livello di ogni effetto: picco in dB rispetto al picco della voce
LIVELLO = {"scontrino": -13, "tick": -22, "colpo": -12, "moneta": -17, "monetine": -19, "pop": -20, "forbici": -11, "carta": -20,
           "salvadanaio": -15}


def main():
    voice, sr = sf.read(sys.argv[1], dtype="float64")
    if voice.ndim > 1:
        voice = voice.mean(axis=1)
    tempi = json.load(open(sys.argv[2], encoding="utf-8"))
    n = int(tempi["durata"] * sr) + 1
    v = np.zeros(n)
    v[: len(voice)] = voice[:n]
    fx = np.zeros(n)
    vpk = np.abs(voice).max()
    for e in tempi["effetti"]:
        s, off = sfx(e["effetto"], sr)
        s = s / np.abs(s).max() * vpk * 10 ** (LIVELLO[e["effetto"]] / 20)
        place(fx, s, max(0, e["t"] + off), sr)
        e["livello_db_picco_voce"] = LIVELLO[e["effetto"]]
    sf.write(sys.argv[3], (v + fx).astype(np.float32), sr)
    sf.write(sys.argv[4], fx.astype(np.float32), sr)
    json.dump(tempi, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("effetti", len(tempi["effetti"]))


if __name__ == "__main__":
    main()
