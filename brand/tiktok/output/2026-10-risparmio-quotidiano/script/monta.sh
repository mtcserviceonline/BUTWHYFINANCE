#!/bin/bash
# monta.sh: catena completa del montaggio, da lanciare nella cartella di lavoro (fuori dal repository) che
# contiene questi script, img/01.png..08.png, fonts/ (IBM Plex Sans Condensed Bold/SemiBold, IBM Plex Mono Bold)
# e voce.mp3. Scrive video.mp4, tempi.json, anteprima_video.jpg e fotogrammi/.
set -e
cd "$(dirname "$0")"
ffmpeg -loglevel error -y -i voce.mp3 -ac 1 -ar 44100 voce.wav
python3 allinea.py voce.wav frasi.json parole.json             # tempi parola per parola (stimati)
python3 montage.py voce.wav parole.json video_noaudio.mp4      # video muto + video_noaudio_tempi.json
cp video_noaudio_tempi.json tempi.json
python3 effetti.py voce.wav tempi.json mix.wav effetti.wav     # voce + effetti sintetizzati
bash norm.sh mix.wav mix_norm.wav                              # -14 LUFS, true peak -1,5 dBTP, 48 kHz
D=$(python3 -c "import json;print(json.load(open('tempi.json'))['durata'])")
ffmpeg -loglevel error -y -i video_noaudio.mp4 -i mix_norm.wav -map 0:v -map 1:a -c:v copy -af apad \
  -c:a aac -b:a 192k -ar 48000 -t "$D" -movflags +faststart video.mp4
ffmpeg -hide_banner -i video.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A14 Summary | grep -E "I:|Peak:"
python3 fotogrammi.py video.mp4 tempi.json fotogrammi anteprima_video.jpg
