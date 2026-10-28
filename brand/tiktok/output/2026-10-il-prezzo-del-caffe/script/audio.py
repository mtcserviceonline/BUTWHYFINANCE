"""Audio: colpo 'scontrino' sintetizzato (numpy, nessun campione esterno) + voce."""
import sys, numpy as np, soundfile as sf
voice, sr = sf.read(sys.argv[1], dtype="float32")
t = np.arange(int(0.35 * sr)) / sr
f = 55 + 95 * np.exp(-t / 0.05)                       # tonfo grave che scende 150 -> 55 Hz
thud = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t / 0.07)
rng = np.random.default_rng(1)
noise = rng.standard_normal(len(t)); noise = np.diff(noise, prepend=0)   # fruscio "carta"
click = noise * np.exp(-t / 0.012) * 0.35
sfx = (thud * 0.8 + click).astype(np.float32)
sfx *= 0.5 * np.abs(voice).max() / np.abs(sfx).max()  # circa -6 dB sotto il picco della voce
mix = voice.copy(); mix[:len(sfx)] += sfx
sf.write(sys.argv[2], mix, sr)
sf.write(sys.argv[3], sfx, sr)
