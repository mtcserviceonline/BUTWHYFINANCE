import sys, json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
S = sys.argv[1]; voice = sys.argv[2]; speed = float(sys.argv[3]); out = sys.argv[4]
k = Kokoro(S + "/kokoro/kokoro-v1.0.onnx", S + "/kokoro/voices-v1.0.bin")
segs = json.load(open(S + "/shots_voice.json", encoding="utf-8"))
audio = []; t = 0.25; times = []; sr = 24000
audio.append(np.zeros(int(0.25 * sr), dtype=np.float32))
for text, pause in segs:
    s, sr = k.create(text, voice=voice, speed=speed, lang="it")
    s = np.asarray(s, dtype=np.float32)
    thr = 0.01; idx = np.where(np.abs(s) > thr)[0]
    a, b = max(0, idx[0] - int(0.03 * sr)), min(len(s), idx[-1] + int(0.06 * sr))
    s = s[a:b]
    dur = len(s) / sr
    times.append({"text": text, "start": round(t, 3), "end": round(t + dur, 3)})
    audio.append(s); audio.append(np.zeros(int(pause * sr), dtype=np.float32))
    t += dur + pause
audio.append(np.zeros(int(0.6 * sr), dtype=np.float32))
full = np.concatenate(audio)
sf.write(out + ".wav", full, sr)
json.dump({"voice": voice, "speed": speed, "segments": times, "total": len(full) / sr}, open(out + ".json", "w"), ensure_ascii=False, indent=1)
print("totale", len(full) / sr)
