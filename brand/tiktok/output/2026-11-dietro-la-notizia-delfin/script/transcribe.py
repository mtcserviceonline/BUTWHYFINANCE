import sys, base64, json, requests, subprocess, tempfile, os
TMP = os.path.join(tempfile.gettempdir(), "_trascrizione.wav")
f = sys.argv[1]; model = sys.argv[2] if len(sys.argv) > 2 else "muse-spark-1.3"
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",f,"-ac","1","-ar","16000",TMP], check=True)
b = base64.b64encode(open(TMP,"rb").read()).decode()
msgs = [{"role":"user","content":[{"type":"input_audio","input_audio":{"data":b,"format":"wav"}}]}]
if "transcribe" not in model:
    msgs[0]["content"].append({"type":"text","text":"Trascrivi esattamente questo audio in italiano."})
r = requests.post("https://api.meta.ai/v1/chat/completions", json={"model":model,"messages":msgs}, timeout=300)
print(r.status_code, r.text[:2000])
