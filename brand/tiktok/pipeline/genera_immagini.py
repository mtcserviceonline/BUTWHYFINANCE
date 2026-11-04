#!/usr/bin/env python3
"""Genera le immagini di un episodio con l'API Meta (muse-image-1.0), autenticata dal proxy.
Uso: genera_immagini.py CARTELLA_EPISODIO [ID ...] [--forza]
Legge CARTELLA/immagini/prompts.json:
  {"01": {"orso": true, "sfondo": "inchiostro", "sagoma": false, "scena": "..."}, ...}
Compone il prompt completo con i blocchi fissi del brand (orso, stile, fondo, palette, niente testo),
lo salva in immagini/prompt/ID.txt e scrive immagini/ID.png (1152x2016).
Senza ID genera solo le immagini mancanti; con ID (o --forza) le rigenera."""
import base64, io, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
import requests
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comune import MASCOTTE, accento, carica_episodio  # noqa: E402

ORSO = ("The character is EXACTLY the bear mascot shown in the reference image: a cartoon brown bear with "
        "copper-orange fur (#C2622A) with small fur tufts on cheeks and shoulders, round chubby body, light peach "
        "muzzle (#F6C78E), round ears with black inner ears, black rounded-triangle nose with a short vertical line "
        "to the mouth, ROUND BLACK SUNGLASSES with one white diagonal glare stripe on each lens (always worn, eyes "
        "never visible), dark green t-shirt (#0F5E3F) with a big yellow euro symbol (#F6C21C) in the center of the "
        "chest, plain short sleeves without any symbol. Keep the exact same character design, proportions and "
        "colors as the reference.")
STILE = ("Flat 2D vector cartoon illustration, thick uniform black outlines, solid flat colors, no gradients, no "
         "shading, no photographic texture, simple and very readable, one strong prop, lots of empty space.")
FONDO = {
    "inchiostro": "Background: perfectly uniform flat solid very dark charcoal color (#111418), empty, no pattern, "
                  "no floor, no gradient.",
    "carta": "Background: perfectly uniform flat solid warm off-white paper color (#F4F1EA), empty, no pattern, no "
             "gradient, no wall decorations, at most a very thin simple floor line.",
}
SPAZIO = "Keep the top quarter of the image completely empty background (space for a title added later)."
SAGOMA = ("Any other person is a faceless plain flat medium-grey silhouette (#9A9A9A, no face, no eyes, no mouth, no "
          "hair details, no clothes logos, smooth mannequin-like shape, thick black outline).")
NO_TESTO = ("Absolutely no text, no letters, no numbers, no words, no labels, no logo, no watermark anywhere in the "
            "image.")


def palette(acc_hex):
    return (f"Color palette limited to: the bear's own colors, {acc_hex} accents, greys, white, black outlines and "
            "the natural colors of the props. No red anywhere, no other green objects besides the bear's t-shirt.")


def componi(p, acc_hex):
    parti = ["Vertical 9:16 illustration for a short educational video."]
    if p.get("orso"):
        parti.append(ORSO)
    parti += [STILE, "Scene: " + p["scena"].strip()]
    if p.get("sagoma"):
        parti.append(SAGOMA)
    parti += [FONDO[p.get("sfondo", "carta")], SPAZIO, palette(acc_hex), NO_TESTO]
    return " ".join(parti)


def genera(out_png, prompt, ref=None, size="1024x1792", tentativi=3):
    base = "https://api.meta.ai/v1/images"
    for k in range(tentativi):
        t0 = time.time()
        try:
            if ref:
                with open(ref, "rb") as fh:
                    files = [("image[0]", (os.path.basename(ref), fh, "image/jpeg"))]
                    data = {"model": "muse-image-1.0", "prompt": prompt, "size": size, "n": "1",
                            "response_format": "b64_json"}
                    r = requests.post(base + "/edits", data=data, files=files, timeout=600)
            else:
                r = requests.post(base + "/generations", json={"model": "muse-image-1.0", "prompt": prompt,
                                                                "size": size, "n": 1, "response_format": "b64_json"},
                                  timeout=600)
        except requests.RequestException as e:
            print("  errore di rete:", e)
            time.sleep(5 * (k + 1))
            continue
        if r.status_code == 200:
            d = r.json()["data"][0]
            raw = base64.b64decode(d["b64_json"]) if d.get("b64_json") else requests.get(d["url"], timeout=120).content
            Image.open(io.BytesIO(raw)).convert("RGB").save(out_png)
            return True, f"{time.time() - t0:.0f}s"
        msg = r.text[:400]
        if r.status_code in (400, 403) or "safety" in msg.lower() or "policy" in msg.lower():
            return False, f"HTTP {r.status_code} (probabile filtro: riformulare la scena) {msg}"
        time.sleep(5 * (k + 1))
    return False, f"HTTP {r.status_code} {msg}"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    forza = "--forza" in sys.argv
    ep, scelti = args[0], args[1:]
    epi = carica_episodio(ep)
    acc = accento(epi)
    acc_hex = "#%02X%02X%02X" % acc
    d = os.path.join(ep, "immagini")
    os.makedirs(os.path.join(d, "prompt"), exist_ok=True)
    prompts = json.load(open(os.path.join(d, "prompts.json"), encoding="utf-8"))
    lavori = []
    for iid, p in prompts.items():
        out = os.path.join(d, f"{iid}.png")
        if scelti and iid not in scelti:
            continue
        if not scelti and not forza and os.path.exists(out):
            continue
        testo = componi(p, acc_hex)
        open(os.path.join(d, "prompt", f"{iid}.txt"), "w", encoding="utf-8").write(testo)
        lavori.append((iid, out, testo, MASCOTTE if p.get("orso") else None))
    print(len(lavori), "immagini da generare")

    def job(j):
        iid, out, testo, ref = j
        ok, info = genera(out, testo, ref)
        print(("ok    " if ok else "FALLITA ") + iid, info, flush=True)
        return iid, ok

    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(job, lavori))
    falliti = [i for i, ok in res if not ok]
    if falliti:
        print("Da riformulare:", " ".join(falliti))
        sys.exit(1)


if __name__ == "__main__":
    main()
