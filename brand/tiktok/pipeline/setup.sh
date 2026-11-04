#!/bin/bash
# Prepara l'ambiente per la pipeline dei video TikTok (da lanciare una volta per sessione).
# Uso: bash brand/tiktok/pipeline/setup.sh
set -e
P="$(cd "$(dirname "$0")" && pwd)"

command -v ffmpeg >/dev/null || { echo "ERRORE: ffmpeg non installato"; exit 1; }
python3 -c "import PIL, numpy, requests, soundfile" 2>/dev/null || pip install -q pillow numpy requests soundfile

mkdir -p "$P/fonts"
base=https://raw.githubusercontent.com/google/fonts/main/ofl
for f in ibmplexsanscondensed/IBMPlexSansCondensed-Bold.ttf \
         ibmplexsanscondensed/IBMPlexSansCondensed-SemiBold.ttf \
         ibmplexmono/IBMPlexMono-Bold.ttf; do
  n=$(basename "$f")
  [ -s "$P/fonts/$n" ] || curl -sSfL -o "$P/fonts/$n" "$base/$f"
done
echo "setup ok: ffmpeg, python (pillow, numpy, requests, soundfile), font in $P/fonts"
