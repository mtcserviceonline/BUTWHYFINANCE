#!/usr/bin/env python3
"""Genera UNA immagine del post con l'API Meta (muse-image-1.0) e la salva come PNG 1080x1920.

- Con riferimenti (default: brand/mascotte/mascotte-principale.jpg) usa
  POST https://api.meta.ai/v1/images/edits  (multipart, image[0], image[1], ...).
- Senza riferimenti (--senza-riferimento, o voce "bear": false in prompts.json) usa
  POST https://api.meta.ai/v1/images/generations (JSON).
- Nessuna chiave: l'autenticazione la fa il proxy dell'ambiente.
- Risposta WebP 1152x2016 -> ritaglio centrale 1134x2016 -> 1080x1920 (Lanczos), senza deformare.
- Ritenta da solo sui 5xx (es. "HTTP 502 upstream request failed") e sugli errori di rete
  (attese 5 s, 10 s, 20 s...). Sui 4xx NON ritenta: di solito e' il filtro dei contenuti -> riformulare il prompt.

Uso:
  genera_immagine.py --prompts immagini/prompts.json --id 03 --out immagini/03.png
  genera_immagine.py --prompt-file p.txt --out prova.png [--ref brand/mascotte/espressioni.jpg ...]
  genera_immagine.py --prompt "..." --out prova.png --senza-riferimento

Codici di uscita: 0 ok, 1 tentativi esauriti (5xx/rete), 2 rifiutata (4xx, es. filtro contenuti), 3 errore d'uso.
I percorsi relativi dei riferimenti si risolvono rispetto alla radice del repository.
"""
import argparse
import base64
import io
import json
import os
import sys
import time

import requests
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ritaglia_916 import a_916  # noqa: E402

API = "https://api.meta.ai/v1/images"
MODELLO = "muse-image-1.0"
RIF_DEFAULT = "brand/mascotte/mascotte-principale.jpg"


def radice_repo():
    """Cartella che contiene brand/mascotte (risale dalla cartella corrente e da quella dello script)."""
    for start in (os.getcwd(), os.path.dirname(os.path.abspath(__file__))):
        d = start
        while True:
            if os.path.isdir(os.path.join(d, "brand", "mascotte")):
                return d
            parent = os.path.dirname(d)
            if parent == d:
                break
            d = parent
    return os.getcwd()


def risolvi(percorso):
    if os.path.isabs(percorso) or os.path.exists(percorso):
        return percorso
    return os.path.join(radice_repo(), percorso)


def mime(p):
    p = p.lower()
    if p.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    if p.endswith(".webp"):
        return "image/webp"
    return "image/png"


def richiesta(prompt, refs, size, timeout):
    if refs:
        files = [(f"image[{i}]", (os.path.basename(r), open(r, "rb"), mime(r))) for i, r in enumerate(refs)]
        data = {"model": MODELLO, "prompt": prompt, "size": size, "n": "1", "response_format": "b64_json"}
        try:
            return requests.post(API + "/edits", data=data, files=files, timeout=timeout)
        finally:
            for _, (_, fh, _) in files:
                fh.close()
    body = {"model": MODELLO, "prompt": prompt, "size": size, "n": 1, "response_format": "b64_json"}
    return requests.post(API + "/generations", json=body, timeout=timeout)


def genera(prompt, refs, out, size="1024x1792", tentativi=4, timeout=600, originale=None):
    """Restituisce un dict con l'esito; solleva SystemExit con il codice giusto in caso di errore."""
    attesa = 5
    for n in range(1, tentativi + 1):
        t0 = time.time()
        try:
            r = richiesta(prompt, refs, size, timeout)
        except requests.RequestException as e:
            print(f"tentativo {n}/{tentativi}: errore di rete {type(e).__name__}: {e}", file=sys.stderr)
            r = None
        dt = time.time() - t0
        if r is not None and r.status_code == 200:
            j = r.json()
            d = j["data"][0]
            raw = base64.b64decode(d["b64_json"]) if d.get("b64_json") else requests.get(d["url"], timeout=120).content
            if originale:
                open(originale, "wb").write(raw)
            src = Image.open(io.BytesIO(raw))
            dim_orig = src.size
            a_916(src).save(out)
            return {"file": out, "originale": f"{dim_orig[0]}x{dim_orig[1]}", "finale": "1080x1920",
                    "secondi": round(dt, 1), "tentativi": n, "riferimenti": refs,
                    "revised_prompt": d.get("revised_prompt")}
        if r is not None and r.status_code < 500:
            print(f"HTTP {r.status_code} (non ritento): {r.text[:1500]}", file=sys.stderr)
            print("Se e' il filtro dei contenuti: riformula la scena (niente pesi che schiacciano, armi, "
                  "persone in difficolta' descritte in modo crudo) e riprova.", file=sys.stderr)
            raise SystemExit(2)
        if r is not None:
            print(f"tentativo {n}/{tentativi}: HTTP {r.status_code} {r.text[:300]}", file=sys.stderr)
        if n < tentativi:
            time.sleep(attesa)
            attesa *= 2
    print("tentativi esauriti", file=sys.stderr)
    raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt", help="testo del prompt")
    g.add_argument("--prompt-file", help="file di testo con il prompt")
    g.add_argument("--prompts", help="prompts.json scritto da componi_prompt.py (serve --id)")
    ap.add_argument("--id", help="id dell'immagine in prompts.json, es. 03")
    ap.add_argument("--out", required=True, help="PNG di uscita (1080x1920)")
    ap.add_argument("--ref", action="append", help="immagine di riferimento (ripetibile); default mascotte-principale")
    ap.add_argument("--senza-riferimento", action="store_true", help="usa /generations, senza mascotte")
    ap.add_argument("--size", default="1024x1792")
    ap.add_argument("--tentativi", type=int, default=4, help="tentativi totali sui 5xx/errori di rete")
    ap.add_argument("--originale", help="salva anche la risposta grezza (WebP) qui")
    a = ap.parse_args()

    refs = a.ref
    if a.prompts:
        if not a.id:
            ap.error("--prompts richiede --id")
        tutti = json.load(open(a.prompts, encoding="utf-8"))
        voce = tutti.get(a.id) or tutti.get(a.id.zfill(2))
        if voce is None:
            print(f"id {a.id} non trovato in {a.prompts}", file=sys.stderr)
            raise SystemExit(3)
        prompt = voce["prompt"]
        if refs is None:
            if "riferimenti" in voce:
                refs = voce["riferimenti"]
            elif voce.get("bear") is False:
                refs = []
    elif a.prompt_file:
        prompt = open(a.prompt_file, encoding="utf-8").read().strip()
    else:
        prompt = a.prompt
    if a.senza_riferimento:
        refs = []
    if refs is None:
        refs = [RIF_DEFAULT]
    refs = [risolvi(r) for r in refs]
    for r in refs:
        if not os.path.exists(r):
            print(f"riferimento non trovato: {r}", file=sys.stderr)
            raise SystemExit(3)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    esito = genera(prompt, refs, a.out, a.size, a.tentativi, originale=a.originale)
    print(json.dumps(esito, ensure_ascii=False))


if __name__ == "__main__":
    main()
