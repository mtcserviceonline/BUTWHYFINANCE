#!/usr/bin/env python3
"""Genera un'immagine con l'API Meta (muse-image-1.0).
Uso: gen.py OUT.png PROMPT_FILE SIZE [REF1 REF2 ...]
Con riferimenti usa /v1/images/edits (multipart), altrimenti /v1/images/generations."""
import sys, json, base64, time, requests

out, prompt_file, size = sys.argv[1], sys.argv[2], sys.argv[3]
refs = sys.argv[4:]
prompt = open(prompt_file, encoding="utf-8").read().strip()
base = "https://api.meta.ai/v1/images"
t0 = time.time()
if refs:
    files = [(f"image[{i}]", (r.split("/")[-1], open(r, "rb"), "image/jpeg" if r.endswith("jpg") else "image/png")) for i, r in enumerate(refs)]
    data = {"model": "muse-image-1.0", "prompt": prompt, "size": size, "n": "1", "response_format": "b64_json"}
    r = requests.post(base + "/edits", data=data, files=files, timeout=600)
else:
    r = requests.post(base + "/generations", json={"model": "muse-image-1.0", "prompt": prompt, "size": size, "n": 1,
                                                    "response_format": "b64_json"}, timeout=600)
dt = time.time() - t0
if r.status_code != 200:
    print("HTTP", r.status_code, r.text[:1500]); sys.exit(1)
j = r.json()
d = j["data"][0]
if d.get("b64_json"):
    open(out, "wb").write(base64.b64decode(d["b64_json"]))
else:
    open(out, "wb").write(requests.get(d["url"], timeout=120).content)
meta = {k: v for k, v in j.items() if k != "data"}
meta["revised_prompt"] = d.get("revised_prompt")
print("ok", out, f"{dt:.1f}s", json.dumps(meta)[:600])
