#!/bin/bash
# monta.sh VOCE.mp3 [CARTELLA_DEL_POST]
#
# Catena completa del montaggio, dalla voce registrata al video finale. Dalla radice del repository:
#   bash brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/script/monta.sh brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/voce.mp3
#
# PRIMA, con la nuova scena 1 registrata dall'utente (solo in questo post):
#   python3 brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/script/sostituisci_scena1.py NUOVA.mp3 \
#       --out brand/tiktok/output/2026-11-pensione-mese-in-piu-v2/voce.mp3
#
# Lavora in una cartella temporanea fuori dal repository (copia script, immagini e font), poi scrive nella
# cartella del post: video.mp4, tempi.json, trascrizione.md, sottotitoli.srt, anteprima_video.jpg,
# copertina.png e
# script/frasi.json + script/parole.json. ~3 minuti.
#
# Passi: mp3 -> wav -> frasi.py (testo noto da scene_elevenlabs.json, allineato alle pause) -> ritmo.py
# (pause > 0,4 s portate a 0,3 s, 0,36 s prima di "Ma perché?"; accelera solo se sotto 165 parole/min,
# qui nessuna accelerazione: VMAX=1.0, variabile VMAX) -> allinea.py (tempi di ogni parola) -> montage.py (controlli automatici + video muto) ->
# effetti.py -> [musica.py] -> norm.sh (-14 LUFS, true peak -2 dBTP) -> unione -> fotogrammi.py ->
# copertina.py -> trascrizione.py.
#
# Variabili facoltative:
#   MUSICA=base.mp3        base con licenza commerciale: 20 dB sotto la voce, ducking leggero (A8).
#                          Senza, niente musica.
#   RITMO=0                lascia pause e velocità come registrate
#   PAUSA_PRIMA="Ma perché?=0.36"   pausa (s) prima della frase che inizia così
#   LAVORO=cartella        cartella di lavoro (default: una nuova in $TMPDIR)
#   FONTS=cartella         font IBM Plex già scaricati (default ~/.cache/butwhy-fonts; se mancano si
#                          scaricano da github.com/google/fonts, licenza OFL)
#   FORZA=1                monta anche se i controlli automatici trovano errori (sconsigliato)
set -euo pipefail
S=$(cd "$(dirname "$0")" && pwd)
POST=$(cd "${2:-$S/..}" && pwd)
VOCE=$(realpath "$1")
L=${LAVORO:-$(mktemp -d -t montaggio-XXXX)}
FONTS=${FONTS:-$HOME/.cache/butwhy-fonts}
PAUSA_PRIMA=${PAUSA_PRIMA:-"Ma perché?=0.36"}
echo "cartella di lavoro: $L"
mkdir -p "$L/img" "$L/fonts" "$FONTS"
cp "$S"/*.py "$S"/norm.sh "$S"/scene_elevenlabs.json "$L"/
cp "$POST"/immagini/[0-9][0-9].png "$L/img/"
G=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in ibmplexsanscondensed/IBMPlexSansCondensed-Bold.ttf ibmplexsanscondensed/IBMPlexSansCondensed-SemiBold.ttf \
         ibmplexmono/IBMPlexMono-Bold.ttf; do
  n=$(basename "$f")
  [ -s "$FONTS/$n" ] || curl -sSfL -o "$FONTS/$n" "$G/$f"
  cp "$FONTS/$n" "$L/fonts/"
done
cd "$L"
ffmpeg -loglevel error -y -i "$VOCE" -ac 1 -ar 44100 voce_orig.wav
# pause da 0,12 s (non 0,08): con 0,08 una micro-pausa dentro "duemilaventisette" spostava "Ma perché?"
python3 frasi.py voce_orig.wav scene_elevenlabs.json frasi_orig.json --min "${FRASI_MIN:-0.12}"
if [ "${RITMO:-1}" != "0" ]; then
  python3 ritmo.py voce_orig.wav frasi_orig.json voce.wav frasi.json --pausa-prima "$PAUSA_PRIMA" --vmax "${VMAX:-1.0}"
else
  cp voce_orig.wav voce.wav; cp frasi_orig.json frasi.json
fi
python3 allinea.py voce.wav frasi.json parole.json
python3 montage.py voce.wav parole.json video_noaudio.mp4 ${FORZA:+--forza}
cp video_noaudio_tempi.json tempi.json
python3 effetti.py voce.wav tempi.json mix.wav effetti.wav
D=$(python3 -c "import json;print(json.load(open('tempi.json'))['durata'])")
if [ -n "${MUSICA:-}" ]; then
  python3 musica.py mix.wav voce.wav "$(realpath "$MUSICA")" mix_musica.wav "$D"
  mv mix_musica.wav mix.wav
fi
bash norm.sh mix.wav mix_norm.wav
ffmpeg -loglevel error -y -i video_noaudio.mp4 -i mix_norm.wav -map 0:v -map 1:a -c:v copy -af apad \
  -c:a aac -b:a 192k -ar 48000 -t "$D" -movflags +faststart video.mp4
LOUD=$(ffmpeg -hide_banner -i video.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A14 Summary)
echo "$LOUD" | grep -E "I:|Peak:"
python3 - "$VOCE" "$LOUD" "${MUSICA:-}" <<'EOF'
import json, re, sys, os
t = json.load(open("tempi.json", encoding="utf-8"))
r = json.load(open("frasi_ritmo.json", encoding="utf-8")) if os.path.exists("frasi_ritmo.json") else None
t["voce"] = {"file": os.path.basename(sys.argv[1]), "ritmo": r,
             "frasi_originali": json.load(open("frasi_orig.json", encoding="utf-8")),
             "frasi": json.load(open("frasi.json", encoding="utf-8"))}
t["audio"] = {"lufs_integrati": float(re.search(r"I:\s+(-?[\d.]+) LUFS", sys.argv[2]).group(1)),
              "true_peak_dbfs": float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", sys.argv[2]).group(1)),
              "musica": os.path.basename(sys.argv[3]) or None}
json.dump(t, open("tempi.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
EOF
python3 fotogrammi.py video.mp4 tempi.json fotogrammi anteprima_video.jpg
python3 copertina.py copertina.png --font-dir fonts --immagine img/01.png              # copertina: orso + «67 ANNI + 1 MESE»
python3 trascrizione.py parole.json "$D" trascrizione.md sottotitoli.srt --titolo "Trascrizione: pensione, 67 anni e 1 mese: cosa puoi fare" \
  --nota "Voce ElevenLabs ($(basename "$VOCE")), pause accorciate da ritmo.py (vedi tempi.json → voce.ritmo). Inizio di ogni frase dalle pause dell'audio; parole dentro le frasi stimate (errore atteso < 0,15 s)."
cp video.mp4 tempi.json trascrizione.md sottotitoli.srt anteprima_video.jpg copertina.png "$POST/"
cp frasi.json parole.json "$S/"
echo "fatto: $POST/video.mp4 ($D s). Fotogrammi di controllo in $L/fotogrammi"
