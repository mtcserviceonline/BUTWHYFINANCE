#!/usr/bin/env python3
"""Scrive i prompt (in inglese) delle 15 immagini del quiz "3 perché sui soldi" in prompts/NN.txt e prompts.json.
Sfondi a colore vivo come da copione (niente nero). L'orso segue la scheda di brand/mascotte (€ giallo)."""
import json, os

S = os.path.dirname(os.path.abspath(__file__))

BEAR = ("The character is EXACTLY the bear mascot shown in the reference image: a cartoon brown bear with copper-orange fur "
        "(#C2622A) with small fur tufts on cheeks and shoulders, round chubby body, light peach muzzle (#F6C78E), round ears "
        "with black inner ears, black rounded-triangle nose with a short vertical line to the mouth, ROUND BLACK SUNGLASSES "
        "with one white diagonal glare stripe on each lens (always worn, eyes never visible), dark green t-shirt (#0F5E3F) "
        "with a big yellow euro symbol (#F6C21C) in the center of the chest. Keep the exact same character design, "
        "proportions and colors as the reference.")
STYLE = ("2D cartoon illustration, thick uniform black outlines, flat colors with soft cel shading, simple and very "
         "readable, one strong prop.")
LAYOUT = ("Vertical 9:16. Main subject in the lower and central part of the frame; keep the top fifth of the image and "
          "the area just above the center fairly empty (space for captions added later).")
BG = ("Background: bright saturated flat {name} color ({hex}) filling the whole frame, uniform, no pattern, no gradient, "
      "absolutely no black background, no dark background, no black bars, no dark vignette.")
PERSON = ("faceless plain flat medium-grey silhouette person (#9A9A9A, no face, no eyes, no mouth, no hair details, "
          "smooth mannequin-like shape, thick black outline)")
NOTEXT = ("Absolutely no text, no letters, no numbers, no digits, no words, no labels, no logos, no watermark anywhere "
          "in the image (the euro symbol on the bear's t-shirt is the only symbol allowed).")

# (id, usa_orso, nome colore, hex, scena)
SHOTS = [
 ("01", True, "sunny yellow", "#FFD23F", "Waist-up shot of the bear, centered, juggling three oversized glowing white "
  "question marks with thick black outlines floating above his paws; he looks at the camera with a confident smile and "
  "one eyebrow raised above the sunglasses."),
 ("02", True, "bright blue", "#3A86FF", "A simple cartoon store shelf on the left with a big BLANK white price tag hanging "
  "from it on a string (completely empty tag, no print). The bear, waist-up on the right, points at the tag with one "
  "paw, PUZZLED: mouth twisted to one side, one eyebrow raised."),
 ("03", True, "hot pink", "#FF4FA3", "Full body shot of the bear standing, centered, complete figure from ears to feet. "
  "In one paw he holds up at chest height a big round cartoon stopwatch (plain white face, two hands, no numbers) and taps "
  "its button; his other paw is cupped behind his ear as if listening for an answer; he looks at the camera with a small "
  "expectant smile."),
 ("04", True, "mint green", "#7CE0B5", "A large pink cartoon brain floating in the center-left; a small magnifying glass "
  "slides over the LEFT side of the brain, with small motion lines. The bear, waist-up on the right, watches it "
  "IMPRESSED: mouth open in a small round 'o', eyebrows raised."),
 ("05", True, "bright orange", "#FF9F1C", "Waist-up shot of the bear, centered, holding a BLANK white price tag "
  "(completely empty, no print) in one paw and a tiny pair of scissors in the other, as if cutting the tag in half; "
  "surprised grin with open mouth."),
 ("06", True, "lemon yellow", "#FFF05A", "Front view of the entrance of a cartoon supermarket: a long straight aisle "
  "with colorful shelves stretches far away into the distance in strong perspective; at the far end of the aisle, on a "
  "spotlighted shelf against the back wall, a clearly visible oversized white milk carton and a big golden loaf of bread, "
  "glowing slightly so they stand out. The bear, full body, stands in the foreground at the "
  "entrance on the left, looking down the aisle with a paw over his sunglasses like a visor."),
 ("07", True, "coral red", "#FF6B6B", "Waist-up shot of the bear, centered, THOUGHTFUL: scratching his chin with one paw, "
  "mouth twisted, one eyebrow raised. Above his head a white cartoon thought bubble containing a drawn white milk "
  "carton and a loaf of bread (drawings only, no text on the carton)."),
 ("08", True, "sky blue", "#5BC0EB", "Waist-up shot of the bear, centered, holding a plain yellow shopping "
  "basket containing a white milk carton and a loaf of bread, tapping them proudly with his other paw, big smile. "
  "Behind him floats a small simple wall calendar page with many green tick marks in a grid (no numbers)."),
 ("09", True, "teal", "#2EC4B6", "The bear, full body, pushes a shopping cart along a very long supermarket aisle seen "
  "in perspective, shelves full of colorful plain boxes and jars on both sides (no labels, no text), looking around "
  "wide-eyed and amazed."),
 ("10", True, "purple", "#9B5DE5", "The bear, waist-up, stands behind an overflowing shopping cart with plain colorful "
  "products sticking out (boxes, bottles, snacks, a toy, chips bags, all without labels); in one paw he holds a tiny "
  "BLANK white shopping list (empty paper); he looks GUILTY with a sheepish smile and a small sweat drop."),
 ("11", True, "peach", "#FFB997", "Waist-up shot of the bear, centered, holding up a large plain purple banknote "
  "(rectangular, plain purple with a simple lighter purple border and an empty oval in the middle, no numbers, no text) "
  "with both paws against the light, squinting at it like a detective, a magnifying glass held in one paw over the "
  "note."),
 ("12", True, "hot pink", "#FF4FA3", "Waist-up shot of the bear, centered, arms crossed on his chest, one eyebrow raised "
  "above the sunglasses, skeptical half smile, looking at the camera. A big round cartoon stopwatch (plain white face, "
  "two hands, no numbers) floats beside him on the left."),
 ("13", True, "bright green", "#80ED99", "The bear sits on a tall pile of thick plain purple banknote bundles (no numbers, "
  "no text) next to a tiny open brown briefcase that contains the same huge pile packed tight; a big magnifying glass "
  "hovers over the briefcase. In the background on the horizon a small simple grey classical bank building with "
  "columns and a triangular roof (no flag, no text). The bear looks at the briefcase with a raised eyebrow."),
 ("14", True, "sunny yellow", "#FFD23F", "A simple shop counter seen from the side. On the left the bear, waist-up, "
  "happily hands a large plain purple banknote (no numbers, no text) over the counter. On the right behind the counter "
  "a cashier drawn as a " + PERSON + " accepts it with both hands. A big green check mark floats above the banknote."),
 ("15", True, "bright blue", "#3A86FF", "Waist-up shot of the bear, centered, holding up four white paper cards side "
  "by side in a fan with both paws, facing the viewer, like dice faces counting up from zero: card 1 is completely EMPTY "
  "(zero dots), card 2 has exactly ONE black dot, card 3 has exactly TWO black dots, card 4 has exactly THREE black dots "
  "in a diagonal line. Never four or more dots on any card. Dots only, no digits. He looks at the camera with a "
  "questioning smile, one eyebrow raised. Same composition and mood as a quiz host."),
]


def build(shot):
    sid, bear, name, hx, scene = shot
    parts = ["Vertical 9:16 illustration for a short educational quiz video."]
    if bear:
        parts.append(BEAR)
    parts += [STYLE, "Scene: " + scene, BG.format(name=name, hex=hx), LAYOUT, NOTEXT]
    return " ".join(parts)


if __name__ == "__main__":
    os.makedirs(os.path.join(S, "prompts"), exist_ok=True)
    out = {}
    for sh in SHOTS:
        p = build(sh)
        out[sh[0]] = {"bear": sh[1], "background": sh[3], "prompt": p}
        open(os.path.join(S, "prompts", sh[0] + ".txt"), "w").write(p)
    json.dump(out, open(os.path.join(S, "prompts.json"), "w"), indent=1)
    print(len(out), "prompt")
