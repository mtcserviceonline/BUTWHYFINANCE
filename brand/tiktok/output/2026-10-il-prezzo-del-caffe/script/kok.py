import sys, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro(sys.argv[1] + "/kokoro-v1.0.onnx", sys.argv[1] + "/voices-v1.0.bin")
voice, speed, out = sys.argv[2], float(sys.argv[3]), sys.argv[4]
text = open(sys.argv[5], encoding="utf-8").read().strip()
s, sr = k.create(text, voice=voice, speed=speed, lang="it")
sf.write(out, s, sr); print(out, len(s)/sr)
