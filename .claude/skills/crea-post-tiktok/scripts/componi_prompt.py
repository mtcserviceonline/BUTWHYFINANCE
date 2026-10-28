#!/usr/bin/env python3
"""Compone i prompt (in inglese) delle immagini del post con i blocchi fissi del brand.

Ingresso: un file JSON di scene scritto a mano, per esempio `immagini/scene.json`:

    {
      "accento": "ambra",                       # ambra | arancio | blu | viola | giallo | fucsia | verde
      "palette_extra": "",                      # facoltativo, es. "coffee browns"
      "immagini": [
        {"id": "01", "orso": true, "fondo": "inchiostro",
         "scena": "Medium-full shot of the bear, centered, looking SURPRISED ..."},
        {"id": "04", "orso": true, "fondo": "carta",
         "scena": "On the left, a full-body {SAGOMA} walking ..."},
        {"id": "08", "orso": true, "fondo": "inchiostro",
         "scena": "... WINKING exactly like the winking face in the second reference image ...",
         "riferimenti": ["brand/mascotte/mascotte-principale.jpg", "brand/mascotte/espressioni.jpg"]}
      ]
    }

Nella scena si possono usare i segnaposto {SAGOMA} e {SAGOME} (persona/e grigia/e senza volto)
e {ACCENTO} (nome + esadecimale del colore d'accento, es. "warm amber/golden yellow (#E9A400)").

Uscita: `prompts.json` nello stesso formato del post risparmio
    {"01": {"bear": true, "background": "inchiostro #111418", "riferimenti": [...], "scena": "...", "prompt": "..."}}
che `genera_immagine.py --prompts prompts.json --id 01` legge direttamente.

Uso: componi_prompt.py scene.json prompts.json [--senza-fascia-destra]
"""
import argparse
import json
import sys

ACCENTI = {
    # nome: (esadecimale, descrizione inglese per il prompt)
    "ambra": ("#E9A400", "warm amber/golden yellow"),
    "arancio": ("#B8420F", "burnt orange"),
    "blu": ("#1F4FA3", "deep cobalt blue"),
    "viola": ("#5B3FA8", "deep violet purple"),
    "giallo": ("#FFD60A", "bright lemon yellow"),
    "fucsia": ("#B0186E", "deep magenta fuchsia"),
    "verde": ("#006B3C", "deep brand green"),
}

INTRO = "Vertical 9:16 illustration for a short educational video."

BEAR = ("The character is EXACTLY the bear mascot shown in the reference image: a cartoon brown bear with "
        "copper-orange fur (#C2622A) with small fur tufts on cheeks and shoulders, round chubby body, light peach "
        "muzzle (#F6C78E), round ears with black inner ears, black rounded-triangle nose with a short vertical line "
        "to the mouth, ROUND BLACK SUNGLASSES with one white diagonal glare stripe on each lens (always worn, eyes "
        "never visible), dark green t-shirt (#0F5E3F) with a big yellow euro symbol (#F6C21C) in the center of the "
        "chest, clearly visible and not covered by props; plain short sleeves without any symbol. Keep the exact "
        "same character design, proportions and colors as the reference.")

STYLE = ("Flat 2D vector cartoon illustration, thick uniform black outlines, solid flat colors, no gradients, no "
         "shading, no photographic texture, simple and very readable, one strong prop, lots of empty space.")

FONDI = {
    "inchiostro": ("inchiostro #111418",
                   "Background: perfectly uniform flat solid very dark charcoal color (#111418), empty, no pattern, "
                   "no floor, no gradient."),
    "carta": ("carta #F4F1EA",
              "Background: perfectly uniform flat solid warm off-white paper color (#F4F1EA), empty, no pattern, no "
              "gradient, no wall decorations, at most a very thin simple floor line."),
}

COMPOSIZIONE = ("Composition: all characters and objects stay inside the central band of the image; the top 12% and "
                "the bottom 18% of the image are completely empty background (space for titles and subtitles added "
                "later), nothing touches the bottom edge.")
FASCIA_DESTRA = (" Keep the rightmost 10% of the image free of important details (app buttons will cover it); "
                 "nothing important is cut by the right edge.")

SAGOMA = ("faceless plain flat medium-grey silhouette person (#9A9A9A, no face, no eyes, no mouth, no hair details, "
          "smooth mannequin-like shape, thick black outline; the whole figure including the torso is plain flat grey "
          "with no clothes, no t-shirt, no logo)")
SAGOME = SAGOMA.replace("silhouette person", "silhouette people").replace("the whole figure", "each whole figure")

NOTEXT = ("Absolutely no text, no letters, no numbers, no words, no labels, no logo, no watermark anywhere in the "
          "image; any paper is blank or has only abstract grey lines.")

# occhiolino: formula che ha funzionato al primo colpo nella 08 del post risparmio (con espressioni.jpg come image[1])
WINK = ("The bear's winking eye: its sunglasses lens on that side is a see-through dark tinted lens (black outline, "
        "translucent smoky dark grey tint) so the closed, winking eye with a curved lid line is clearly visible "
        "through the lens; the other lens stays opaque solid black with the white diagonal glare stripe, exactly "
        "like the reference image. Both lenses present, same round size, joined by the black bridge.")

RIF_PRINCIPALE = "brand/mascotte/mascotte-principale.jpg"
RIF_ESPRESSIONI = "brand/mascotte/espressioni.jpg"


def palette(accento, extra=""):
    hexa, nome = ACCENTI[accento]
    s = (f"Color palette limited to: the bear's own colors, {nome} ({hexa}) accents, greys, white and black outlines"
         + (f", {extra}" if extra else "") + ". No red anywhere")
    if accento != "fucsia":
        s += ", no pink"
    if accento != "blu":
        s += ", no blue"
    if accento == "verde":
        s += f", no green except the bear's t-shirt and the {nome} ({hexa}) accent objects"
    else:
        s += ", no other green objects besides the bear's t-shirt"
    if accento == "arancio":
        s += "; accent objects must stay clearly distinct from the bear's fur color"
    if accento == "ambra":
        s += "; amber objects are golden yellow, not orange"
    return s + "."


def componi(spec, fascia_destra=True):
    accento = spec.get("accento", "ambra")
    if accento not in ACCENTI:
        sys.exit(f"accento sconosciuto: {accento} (validi: {', '.join(ACCENTI)})")
    hexa, nome = ACCENTI[accento]
    pal = palette(accento, spec.get("palette_extra", ""))
    comp = COMPOSIZIONE + (FASCIA_DESTRA if fascia_destra else "")
    out = {}
    for im in spec["immagini"]:
        iid = str(im["id"]).zfill(2)
        fondo = im.get("fondo", "carta")
        if fondo not in FONDI:
            sys.exit(f"{iid}: fondo sconosciuto {fondo} (validi: inchiostro, carta)")
        orso = bool(im.get("orso", True))
        scena = (im["scena"].replace("{SAGOMA}", SAGOMA).replace("{SAGOME}", SAGOME)
                 .replace("{ACCENTO}", f"{nome} ({hexa})"))
        rif = im.get("riferimenti")
        if rif is None:
            rif = [RIF_PRINCIPALE] if orso else []
            if orso and "wink" in scena.lower():
                rif.append(RIF_ESPRESSIONI)
                print(f"{iid}: occhiolino -> aggiunto {RIF_ESPRESSIONI} come secondo riferimento", file=sys.stderr)
        bear = BEAR
        if orso and "wink" in scena.lower():
            # per l'occhiolino l'occhio chiuso si vede attraverso una lente fume' (risparmio 08, terza versione)
            bear = BEAR.replace("(always worn, eyes never visible)",
                                "(always worn; eyes hidden, except the winking eye seen through its see-through "
                                "dark tinted lens)")
            if "tinted lens" not in scena:
                scena += " " + WINK
        parti = [INTRO] + ([bear] if orso else []) + [STYLE, "Scene: " + scena, FONDI[fondo][1], comp, pal, NOTEXT]
        out[iid] = {"bear": orso, "background": FONDI[fondo][0], "riferimenti": rif, "scena": im["scena"],
                    "prompt": " ".join(parti)}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scene")
    ap.add_argument("uscita")
    ap.add_argument("--senza-fascia-destra", action="store_true",
                    help="non chiedere la fascia destra libera (sconsigliato)")
    a = ap.parse_args()
    spec = json.load(open(a.scene, encoding="utf-8"))
    out = componi(spec, fascia_destra=not a.senza_fascia_destra)
    json.dump(out, open(a.uscita, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(out)} prompt scritti in {a.uscita}")


if __name__ == "__main__":
    main()
