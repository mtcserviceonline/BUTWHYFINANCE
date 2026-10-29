#!/bin/bash
# norm.sh IN OUT EXTRA_ARGS... : loudnorm a due passaggi a -14 LUFS, true peak -2 dBTP (dopo AAC il picco risale di ~0,4 dB)
in=$1; out=$2; shift 2
m=$(ffmpeg -hide_banner -i "$in" -af loudnorm=I=-14:TP=-2:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g() { echo "$m" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -loglevel error -y -i "$in" -af "loudnorm=I=-14:TP=-2:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" "$@" "$out"
