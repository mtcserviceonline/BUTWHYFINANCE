#!/usr/bin/env python3
"""Prompt (in inglese) delle immagini del video "Dietro la notizia: Delfin". Scrive prompts/NN.txt e prompts.json."""
import json, os

S = os.path.dirname(os.path.abspath(__file__))

BEAR = ("The character is EXACTLY the bear mascot shown in the reference image: a cartoon brown bear with copper-orange fur "
        "(#C2622A) with small fur tufts on cheeks and shoulders, round chubby body, light peach muzzle (#F6C78E), round ears "
        "with black inner ears, black rounded-triangle nose with a short vertical line to the mouth, ROUND BLACK SUNGLASSES "
        "with one white diagonal glare stripe on each lens (always worn, eyes never visible), dark green t-shirt (#0F5E3F) "
        "with a big yellow euro symbol (#F6C21C) in the center of the chest. Keep the exact same character design, "
        "proportions and colors as the reference.")
STYLE = ("Flat 2D vector cartoon illustration, thick uniform black outlines, solid flat colors, no gradients, no shading, "
         "no photographic texture, simple and very readable, one strong prop, lots of empty space.")
INK = "Background: perfectly uniform flat solid very dark charcoal color (#111418), empty, no pattern, no floor, no gradient."
PAPER = ("Background: perfectly uniform flat solid warm off-white paper color (#F4F1EA), empty, no pattern, no gradient, "
         "no wall decorations, at most a very thin simple floor line.")
TOPSPACE = "Keep the top quarter of the image completely empty background (space for a title added later)."
PERSON = ("faceless plain flat medium-grey silhouette person (#9A9A9A, no face, no eyes, no mouth, no hair details, "
          "smooth mannequin-like shape, wearing no clothes details, no logos, thick black outline)")
PEOPLE = PERSON.replace("silhouette person", "silhouette people")
SAFE = ("a big old-fashioned steel safe (cast-iron strongbox) in light and medium grey with a round dial and a big "
        "handle on the door")
PALETTE = ("Color palette limited to: the bear's own colors, warm amber/golden yellow (#E9A400) accents, steel greys, "
           "white, black outlines. No red anywhere, no other green objects besides the bear's t-shirt.")
NOTEXT = "Absolutely no text, no letters, no numbers, no words, no labels, no logo, no flags, no watermark anywhere in the image."

# (id, orso, fondo, scena)
SHOTS = [
 ("01", True, INK, "The bear, full body, in the lower part of the frame on the right, looking SURPRISED: mouth open in a "
  "small round 'o', eyebrows raised above the sunglasses, both paws raised in astonishment. Next to him on the left "
  + SAFE + ", closed, taller than the bear, with a few plain golden amber coins on the floor in front of it."),
 ("02", False, PAPER, "Exactly EIGHT " + PEOPLE + " standing in two rows, clearly separated and easy to count: four on "
  "the left and four on the right, with space between each figure. All of them have their arms crossed and turn their "
  "heads away from the center, clearly in disagreement. In the middle, between the two groups, a small closed grey safe "
  "on the floor. All figures identical in size and grey color. No animals, no other characters."),
 ("03", True, PAPER, "Waist-up shot of the bear, centered, THOUGHTFUL and puzzled: one paw on his chin, mouth twisted to "
  "one side, one eyebrow raised above the sunglasses, head slightly tilted. No props. The background must be exactly the "
  "flat off-white paper color #F4F1EA, not peach, not orange, not beige."),
 ("04", False, PAPER, "A torn newspaper clipping pinned to the paper background with two strips of beige tape, tilted "
  "slightly. The clipping is off-white with a black outline; instead of text it has only plain thick grey horizontal "
  "bars, and a large picture box in the middle showing " + SAFE + ". No readable text, only grey bars. The clipping is "
  "centered in the image and is the only object: no animals, no teddy bears, no characters anywhere."),
 ("05", False, PAPER, "Close-up of " + SAFE + " with the door wide open. Inside the safe, filling about a third of the "
  "interior shelves, there is one big pair of classic black-framed eyeglasses with clear lenses (normal eyeglasses, "
  "not sunglasses) lying on a plain golden amber cushion; the rest of the shelves are empty."),
 ("06", False, PAPER, "Close-up of " + SAFE + " with the door wide open. Inside, on two shelves, a small classical bank "
  "building with columns and a triangular roof (grey), and next to it a plain golden amber shield shape (insurance "
  "symbol). Both small, like trophies on a shelf."),
 ("07", False, PAPER, "A big round golden amber coin seen from the front, drawn very large and centered, cut into EIGHT "
  "exactly equal pie slices that are slightly separated from each other with thin gaps, like a pizza. Plain coin with "
  "no symbols or engravings. The coin is the only object in the image: no animals, no teddy bears, no characters."),
 ("08", False, PAPER, "On the left a single " + PERSON + " standing behind a simple table, pushing forward with both "
  "hands a very tall stack of plain golden amber coins toward the right. On the right side of the table seven small "
  "round coin slices (pie-slice shapes) lined up. Calm, determined pose."),
 ("09", False, PAPER, "A big classical bank building with columns and a triangular roof (grey) on the left. From its "
  "open door a long thick amber arrow goes to the right toward a " + PERSON + " who receives a huge bulging burlap money "
  "sack. The sack has no symbols."),
 ("10", True, PAPER, "On the left a " + PERSON + " in a long coat holding a briefcase in one hand and dragging an "
  "enormous bulging burlap money sack with the other, walking toward the right. On the right the bear, waist-up, looking "
  "at him SURPRISED, mouth in a small round 'o', eyebrows raised. The sack has no symbols."),
 ("11", False, PAPER, "A big round coin seen from the front, drawn very large and centered, divided into eight equal pie "
  "slices with thin gaps: four adjacent slices (the left half) are plain grey and each has a small black padlock on it; "
  "the other four slices (the right half) are golden amber. No symbols, no engravings."),
 ("12", False, PAPER, "One very large " + PERSON.replace("silhouette person", "silhouette hand and forearm") + " coming "
  "from the bottom of the frame, holding up on its open palm " + SAFE + ", closed, like a trophy. Only the hand and "
  "forearm are visible."),
 ("13", False, PAPER, "In the center " + SAFE + ", closed, staying in place. From the safe, several small items fly out in "
  "different directions along dotted lines: a small grey classical bank building, a plain golden amber shield, a small "
  "grey house, a stack of plain amber coins, each going toward a small " + PERSON + " standing around the edges."),
 ("14", True, INK, "Waist-up shot of the bear placed in the LOWER LEFT part of the frame, WINKING: one eye closed visible "
  "through the sunglasses lens, confident friendly closed-mouth smile, holding a small grey strongbox (mini safe) in one "
  "paw. The upper right part of the image is empty dark space."),
]


def build(shot):
    sid, bear, bg, scene = shot
    parts = ["Vertical 9:16 illustration for a short educational video."]
    if bear:
        parts.append(BEAR)
    parts += [STYLE, "Scene: " + scene, bg, TOPSPACE, PALETTE, NOTEXT]
    return " ".join(parts)


if __name__ == "__main__":
    os.makedirs(os.path.join(S, "prompts"), exist_ok=True)
    out = {}
    for sh in SHOTS:
        p = build(sh)
        out[sh[0]] = {"bear": sh[1], "prompt": p}
        open(os.path.join(S, "prompts", sh[0] + ".txt"), "w").write(p)
    json.dump(out, open(os.path.join(S, "prompts.json"), "w"), indent=1)
    print(len(out), "prompt")
