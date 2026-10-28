#!/usr/bin/env python3
"""TTS ElevenLabs con timestamp. Uso: tts.py VOICE_ID TEXT_FILE OUT_PREFIX [MODEL] [SPEED]
Salva OUT_PREFIX.mp3 e OUT_PREFIX.json (allineamento dei caratteri)."""
import sys, json, base64, requests

voice, text_file, out = sys.argv[1], sys.argv[2], sys.argv[3]
model = sys.argv[4] if len(sys.argv) > 4 else "eleven_multilingual_v2"
speed = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
text = open(text_file, encoding="utf-8").read().strip()
body = {
    "text": text,
    "model_id": model,
    "language_code": "it",
    "voice_settings": {"stability": 0.65, "similarity_boost": 0.8, "style": 0.1,
                       "use_speaker_boost": True, "speed": speed},
}
r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128",
                  headers={"xi-api-key": "proxy", "Content-Type": "application/json"}, json=body, timeout=300)
if r.status_code != 200:
    print("HTTP", r.status_code, r.text[:1000]); sys.exit(1)
j = r.json()
open(out + ".mp3", "wb").write(base64.b64decode(j["audio_base64"]))
json.dump({"text": text, "model": model, "voice": voice, "body": body,
           "alignment": j.get("alignment"), "normalized_alignment": j.get("normalized_alignment")},
          open(out + ".json", "w"), ensure_ascii=False)
al = j["alignment"]
print("ok", out, "durata", al["character_end_times_seconds"][-1])
