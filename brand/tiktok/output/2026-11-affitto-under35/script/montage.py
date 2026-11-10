#!/usr/bin/env python3
"""Montaggio del reel: clip di Flow (video) + voce ElevenLabs (audio) + sottotitoli.
Uso (dalla cartella del reel): python3 script/montage.py FONTDIR
FONTDIR deve contenere IBMPlexSansCondensed-Bold.ttf."""
import subprocess, sys, os
FONTDIR = sys.argv[1]
FPS = 30
VOICE = "audio/voce-elevenlabs.mp3"
PAUSE_AT, PAUSE = 44.6, 1.5   # pausa aggiunta dopo "Rinuncia a 2.424 euro", per vedere cadere la moneta
TAIL = 2.5                    # fermo finale dopo "Scrivilo nei commenti"

def t(x):  # tempo della voce originale -> tempo nel video
    return x + (PAUSE if x >= PAUSE_AT else 0)

# clip, inizio dentro la clip (s), inizio e fine nella voce originale (s)
SHOTS = [("1", 1.69, 0.0, 5.0), ("2A", 0.09, 5.0, 11.75), ("2B", 0.16, 11.75, 16.7),
         ("3A", 0.05, 16.7, 23.37), ("3B", 3.0, 23.37, 28.28), ("4", 0.15, 28.28, 34.3),
         ("5A", 0.3, 34.3, 41.4), ("5B", 3.2, 41.4, None), ("6A", 0.5, 44.6, 50.7), ("6B", 0.3, 50.7, None)]
END = 54.2
# sottotitoli: (inizio, fine) nella voce originale, testo; *parola* = evidenziata
SUBS = [
 (0.0, 1.9, "Affittare una casa a *800 €*"), (1.9, 3.84, "può rendere più che affittarla a *1.000*"),
 (4.21, 4.74, "Ma *perché?*"),
 (5.40, 6.9, "La manovra propone:"), (6.9, 8.4, "tasse all'*1%*"), (8.4, 9.9, "su chi affitta a *canone concordato*"),
 (9.9, 11.42, "a chi ha fino a *35 anni*"),
 (12.09, 13.70, "Oggi sono al *10%*"), (14.20, 15.2, "Sul mercato libero,"), (15.2, 16.40, "al *21%*"),
 (17.01, 17.84, "Facciamo un *esempio*"),
 (18.48, 20.0, "A *1.000 €* sul libero,"), (20.0, 21.5, "al proprietario restano"), (21.5, 23.03, "*9.480 €* l'anno"),
 (23.71, 25.9, "A *800 €* a un under 35,"), (25.9, 28.03, "ne restano *9.504*"),
 (28.53, 29.9, "L'inquilino risparmia"), (29.9, 31.38, "*2.400 €* l'anno"),
 (31.96, 32.9, "Il proprietario"), (32.9, 34.01, "ne guadagna *24*"),
 (34.59, 35.2, "E la differenza"), (35.2, 35.88, "chi la *mette?*"),
 (36.52, 37.06, "Lo *Stato:*"), (37.56, 39.3, "incassa *96 €*"), (39.3, 41.14, "invece di *2.520*"),
 (41.65, 44.23, "Rinuncia a *2.424 €*"),
 (44.99, 46.28, "Aiuto giusto ai giovani,"), (46.77, 46.98, "*A*"),
 (47.59, 48.5, "o tasse in meno"), (48.5, 49.36, "pagate da tutti,"), (49.79, 50.08, "*B?*"),
 (51.31, 52.40, "È ancora una *proposta*"), (52.96, 54.2, "Scrivilo nei *commenti*"),
]

def run(cmd): subprocess.run(cmd, check=True)
os.makedirs("build", exist_ok=True)

# 1) segmenti video: 1080x1920, 30 fps, senza audio, durata esatta in fotogrammi
bounds = [t(s[2]) for s in SHOTS] + [t(END) + TAIL]
bounds[8] = t(44.6)  # 6A parte dopo la pausa
frames_tot = 0; lst = []
for i, (name, off, a, _) in enumerate(SHOTS):
    start_f = round(bounds[i] * FPS); end_f = round(bounds[i + 1] * FPS); n = end_f - start_f
    out = f"build/{i:02d}_{name}.mp4"
    run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(off), "-i", f"clip/{name}.mp4", "-an",
         "-vf", f"scale=1080:1920:flags=lanczos,setsar=1,fps={FPS},tpad=stop_mode=clone:stop_duration=2",
         "-frames:v", str(n), "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", out])
    lst.append(f"file '{os.path.basename(out)}'"); frames_tot += n
    print(name, f"{bounds[i]:.2f}-{bounds[i+1]:.2f}s", n, "fotogrammi")
open("build/list.txt", "w").write("\n".join(lst) + "\n")
run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", "build/list.txt", "-c", "copy", "build/video_noaudio.mp4"])
total = frames_tot / FPS

# 2) audio: voce con pausa inserita e coda, normalizzata a -14 LUFS
run(["ffmpeg", "-loglevel", "error", "-y", "-i", VOICE, "-filter_complex",
     f"[0:a]atrim=0:{PAUSE_AT},asetpts=PTS-STARTPTS,apad=pad_dur={PAUSE}[a1];"
     f"[0:a]atrim={PAUSE_AT},asetpts=PTS-STARTPTS[a2];[a1][a2]concat=n=2:v=0:a=1,"
     f"apad=whole_dur={total:.3f},atrim=0:{total:.3f},aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
     "-map", "[a]", "-ar", "48000", "-c:a", "pcm_s16le", "build/voce.wav"])

# 3) sottotitoli ASS: testo carta su riquadro inchiostro, parola chiave in arancio "Chi paga?"
def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Sub,IBM Plex Sans Condensed,96,&H00EAF1F4,&H00EAF1F4,&H26181411,&H00000000,-1,0,0,0,100,100,0,0,3,16,0,2,70,150,310,1", "",
       "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for k, (a, b, txt) in enumerate(SUBS):
    nxt = SUBS[k + 1][0] if k + 1 < len(SUBS) else END + TAIL
    end = nxt if nxt - b < 0.7 else b + 0.3
    if k == len(SUBS) - 1: end = END + TAIL
    parts = txt.split("*")
    body = "".join(p if j % 2 == 0 else "{\\c&H0F42B8&}" + p + "{\\c&H00EAF1F4&}" for j, p in enumerate(parts))
    ass.append(f"Dialogue: 0,{ts(t(a))},{ts(t(end) if k < len(SUBS)-1 else t(END)+TAIL)},Sub,,0,0,0,,{body}")
open("build/sub.ass", "w", encoding="utf-8").write("\n".join(ass) + "\n")

# 4) video finale
run(["ffmpeg", "-loglevel", "error", "-y", "-i", "build/video_noaudio.mp4", "-i", "build/voce.wav",
     "-vf", f"ass=build/sub.ass:fontsdir={FONTDIR}", "-map", "0:v", "-map", "1:a",
     "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
     "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", "video.mp4"])
print("ok video.mp4", f"{total:.2f}s")
