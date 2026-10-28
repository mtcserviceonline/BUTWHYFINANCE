#!/usr/bin/env python3
"""Scrive i prompt (in inglese) delle immagini in prompts/NN.txt e prompts.json."""
import json, os, sys

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
          "smooth mannequin-like shape, thick black outline)")
PALETTE = ("Color palette limited to: the bear's own colors, warm amber/golden yellow (#E9A400) accents, greys, white, "
           "black outlines and coffee browns. No red anywhere, no other green objects besides the bear's t-shirt.")
NOTEXT = "Absolutely no text, no letters, no numbers, no words, no labels, no logo, no watermark anywhere in the image."

# (id, usa_orso, fondo, scena)
SHOTS = [
 ("01", True, INK, "Medium-full shot of the bear, centered in the lower two thirds of the frame, looking SURPRISED: mouth "
  "open in a small round 'o' shape, eyebrows raised above the sunglasses, both paws raised slightly in astonishment. On "
  "the floor in front of him a small white espresso cup on a saucer and a long BLANK white paper receipt curling down "
  "(completely empty paper, no print)."),
 ("02", True, PAPER, "Waist-up shot of the bear, centered, THOUGHTFUL and puzzled: one paw on his chin, mouth twisted to "
  "one side, one eyebrow raised above the sunglasses, head slightly tilted. No props."),
 ("03", True, PAPER, "Waist-up shot of the bear, centered, holding up a small white espresso cup on a saucer in one paw "
  "and looking at it with curiosity, gentle closed-mouth smile, slightly nostalgic mood."),
 ("04", False, PAPER, "Still life, no characters: two BLANK white paper shop receipts standing straight side by side, "
  "facing the viewer, flat and rectangular with zigzag torn bottom edges, completely empty paper with no print at all. "
  "The left receipt is a bit shorter than the right one. In front of them, centered, a small white espresso cup on a "
  "saucer. Receipts placed in the middle of the image, large."),
 ("05", True, PAPER, "The bear seen waist-up behind a simple flat wooden bar counter, front view, the euro symbol "
  "visible on the chest of his t-shirt (plain short sleeves without any symbol). With one paw he is placing a small "
  "stack of plain golden amber coins (#E9A400) on the counter, next to a small white espresso cup on a saucer; he looks "
  "down at the coins with a slightly surprised face. The coins are plain discs with no symbols."),
 ("06", True, PAPER, "A simple coffee bar counter seen from the front. Behind the counter stands a barista drawn as a "
  + PERSON + ", next to a simple grey espresso machine. In front of the counter, on the right side, the bear seen "
  "waist-up in three-quarter view, THOUGHTFUL: paw on his chin, looking at the barista with a puzzled face."),
 ("07", True, PAPER, "Waist-up shot of the bear, centered, explaining: one index finger raised up ('I have an idea' "
  "pose), open smiling mouth. On the left side of the bear a small burlap sack of coffee beans, on the right side a "
  "small grey espresso machine, both floating at shoulder height like two options."),
 ("08", True, PAPER, "The bear, full body, standing on the right, pointing with one paw at a big open burlap sack full "
  "of pale beige raw coffee beans standing on the left. Curious expression, small smile."),
 ("09", True, PAPER, "A big open burlap sack of coffee beans in the center; behind it a very large bold solid amber "
  "(#E9A400) arrow pointing straight up, with black outline. The bear on the right side, waist-up, looking up at the "
  "arrow SURPRISED, mouth in a small round 'o'."),
 ("10", False, PAPER, "Still life, no characters: an old-fashioned brass balance scale with two hanging pans, drawn large "
  "and centered. The left pan holds a heavy burlap sack of coffee beans and hangs much LOWER; the right pan holds a tiny "
  "white espresso cup on a saucer and is much HIGHER. The scale beam is clearly tilted. Brass in warm amber tones."),
 ("11", True, PAPER, "On the left, behind a simple bar counter, a barista drawn as a " + PERSON + " wearing a plain "
  "grey apron, holding a big burlap sack of coffee beans in both arms, the sack looks heavy. On the right the bear, "
  "waist-up, looking at the barista with a sympathetic expression (eyebrows tilted, small closed-mouth frown)."),
 ("12", False, PAPER, "Interior of a simple small coffee bar seen from the front: a bar counter with a grey cash "
  "register and an espresso machine; behind the counter a barista drawn as a " + PERSON + ", the whole figure including the torso is plain flat grey "
  "with no clothes, no t-shirt, no logo. A single bare light bulb "
  "hangs from the top on a cord, glowing amber. A long BLANK white paper bill hangs over the edge of the counter "
  "(empty paper, no print)."),
 ("13", True, PAPER, "Waist-up shot of the bear, centered, WORRIED: a light-blue sweat drop on his temple, eyebrows "
  "tilted, mouth turned down, holding with both paws a very long BLANK white paper bill that unrolls down to the floor "
  "(completely empty paper, no print). Beside him floats a simple amber lightning bolt symbol and a grey electric plug "
  "with cable."),
 ("14", True, PAPER, "The bear, waist-up, slightly leaning forward, examining with a big magnifying glass a long BLANK "
  "white paper receipt that he holds in his other paw (completely empty paper, no print). Concentrated, curious "
  "expression, mouth slightly twisted."),
 ("15", True, PAPER, "On a simple flat wooden bar counter, three stacks of plain golden amber coins (#E9A400) of very "
  "different heights side by side: one short, one medium, one tall. The coins are plain discs without symbols. The bear "
  "is on the right side, waist-up behind the counter, looking at the stacks THOUGHTFUL with a paw on his chin."),
 ("16", True, PAPER, "A big simple blank presentation board on an easel showing only a thick amber (#E9A400) line chart "
  "that first rises high and then clearly drops down at the end; plain board with no axis labels, no grid numbers. The "
  "bear stands on the right, waist-up, pointing at the falling part of the line with his index finger, curious face."),
 ("17", True, PAPER, "Concrete metaphor: on the left a burlap sack of coffee beans sliding down a simple grey slope; on "
  "the right a small white espresso cup on a saucer sitting firmly on top of a tall plain grey pedestal, not moving. The "
  "bear, small, full body, stands between them looking up at the cup, THOUGHTFUL with paw on chin."),
 ("18", True, PAPER, "A coffee bar counter. On the left a customer drawn as a " + PERSON + " holding a small white "
  "espresso cup. On the right the bear, waist-up, facing the customer with a curious questioning face. On the counter "
  "between them lies a long BLANK white paper receipt (completely empty paper, no print)."),
 ("19", False, PAPER, "Three " + PERSON.replace("person", "people") + " standing in a row, evenly spaced, full body, "
  "same size: the left one holds a small white espresso cup (the customer), the middle one wears a plain grey apron and "
  "holds a small cloth (the barista), the right one carries a burlap sack of coffee beans on the shoulder (the roaster)."),
 ("20", True, INK, "Waist-up shot of the bear placed in the LOWER LEFT part of the frame, WINKING: one eye closed visible "
  "through the sunglasses lens, confident friendly closed-mouth smile, holding a small white espresso cup on a saucer in "
  "one paw. The upper right part of the image is empty dark space."),
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
