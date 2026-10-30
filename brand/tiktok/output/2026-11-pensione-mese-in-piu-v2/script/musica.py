#!/usr/bin/env python3
"""Base musicale sotto la voce (A8), solo se c'e' un file con licenza commerciale.

Uso: musica.py MIX.wav VOCE.wav MUSICA.(mp3|wav) OUT.wav DURATA [--sotto 20]
- misura il loudness integrato (EBU R128) della voce e della musica e porta la musica a --sotto dB
  (default 20) sotto la voce;
- la ripete se e' piu' corta del video e la taglia alla DURATA, con dissolvenza di 0,3 s in entrata e
  di 0,4 s in uscita;
- ducking leggero: compressore sidechain pilotato dalla voce (soglia -30 dBFS, rapporto 3:1, attacco
  20 ms, rilascio 250 ms): quando la voce parla la musica scende ancora di 2-4 dB;
- somma la musica a MIX.wav (voce + effetti) senza toccarlo. La normalizzazione a -14 LUFS si fa dopo.
Niente musica scaricata dal web: il file deve avere una licenza per uso commerciale (vedi README)."""
import argparse, json, re, subprocess


def lufs(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "loudnorm=print_format=json", "-f", "null",
                          "-"], capture_output=True, text=True).stderr
    return float(json.loads(re.search(r"\{[^{}]*\}", err, re.S).group(0))["input_i"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mix"); ap.add_argument("voce"); ap.add_argument("musica"); ap.add_argument("out")
    ap.add_argument("durata", type=float)
    ap.add_argument("--sotto", type=float, default=20)
    a = ap.parse_args()
    lv, lm = lufs(a.voce), lufs(a.musica)
    g = lv - a.sotto - lm
    d = a.durata
    filt = (f"[2:a]aformat=sample_rates=48000:channel_layouts=mono,atrim=0:{d},asetpts=N/SR/TB,volume={g:.2f}dB,"
            f"afade=t=in:d=0.3,afade=t=out:st={max(0, d - 0.4):.3f}:d=0.4[m];"
            "[1:a]aformat=sample_rates=48000:channel_layouts=mono[sc];"
            "[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=250[md];"
            "[0:a]aformat=sample_rates=48000:channel_layouts=mono[v];"
            "[v][md]amix=inputs=2:normalize=0:duration=first[out]")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", a.mix, "-i", a.voce, "-stream_loop", "-1", "-i",
                    a.musica, "-filter_complex", filt, "-map", "[out]", a.out], check=True)
    print(f"musica: voce {lv:.1f} LUFS, musica {lm:.1f} LUFS -> guadagno {g:+.1f} dB (musica {a.sotto:.0f} dB sotto "
          f"la voce, poi ducking sidechain)")


if __name__ == "__main__":
    main()
