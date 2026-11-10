#!/usr/bin/env python3
"""Scrive i prompt dei primi fotogrammi (uno per scena) in script/prompts/NN.txt.
Riferimenti passati a gen.py: image[0] = mascotte, image[1] e image[2] = esempi di stile."""
import json, pathlib
REFS = ("Reference images: the FIRST image is the bear character to draw. The SECOND and THIRD images are ONLY examples of the "
        "art style to copy exactly: do NOT copy their people, characters, places, objects, text or composition.")
STYLE = ("Art style, identical to the style references: modern comic-book / cartoon illustration, bold clean black ink outlines, "
         "flat cel-shaded colors with soft simple shading, detailed semi-realistic background drawn in the same comic style, "
         "warm natural daylight, slightly saturated warm palette, vertical 9:16 frame.")
BEAR = ("The bear is EXACTLY the mascot of the first reference image: cartoon brown bear with copper-orange fur, light peach muzzle, "
        "round ears with dark inner ears, black rounded nose, black round sunglasses with a white diagonal glare on each lens "
        "always on (eyes never visible), dark green t-shirt with a big yellow euro sign in the center of the chest. "
        "Same design and proportions as the reference, fully visible from head to feet. He is the only bear in the image.")
NOTEXT = ("No other characters. No text, no letters, no numbers, no words, no logos, no flags, no signs with writing anywhere; "
          "all papers, tags, receipts and documents are blank.")
SCENES = {
 "01": "Sunny Italian residential street. The bear stands in front of two IDENTICAL small houses side by side (same shape, same size, same colors, same roof, same door). He holds a metal house key in one paw, raised slightly, and looks at the camera with a curious expression.",
 "02": "Inside a bright office. The bear stands a few steps away from a large blank document taped to the wall with strips of masking tape, holding two blank price tags (one large, one small) in his paws and turning his head toward the document with a calm expression. Below the document, a small wooden table with three rubber ink stamps of decreasing size.",
 "03": "Same bright office. The bear stands beside a wooden desk and is about to sit down on the chair. On the desk lie two rolled-up long blank receipts and a magnifying glass. Thoughtful expression, one paw resting on the desk.",
 "04": "Same bright office, wide shot. The bear sits on a chair at the wooden desk, the two long blank receipts lying unrolled on it and the magnifying glass set aside; on the desk in front of him a loose scattered heap of plain gold coins with no markings. He looks at the coins with a light smile, about to stand up. His whole body is visible including his feet under the desk.",
 "05": "Italian piazza in daylight. The bear stands next to a small outdoor table with two piles of plain gold coins, one very tall and one tiny, and turns his head toward a large public building with classical columns on the other side of the frame. A closed brown leather wallet lies on the pavement in front of the building. Serious expression.",
 "06": "Same Italian piazza. The bear stands centered behind a small outdoor table on which lie two blank white cards. Paws relaxed at his sides, friendly expression, looking at the camera, about to pick up the cards.",
}
out = pathlib.Path(__file__).parent / "prompts"
allp = {}
for k, s in SCENES.items():
    p = f"{REFS} {STYLE} {BEAR} Scene: {s} {NOTEXT}"
    (out / f"{k}.txt").write_text(p, encoding="utf-8"); allp[k] = p
(pathlib.Path(__file__).parent / "prompts.json").write_text(json.dumps(allp, indent=1, ensure_ascii=False), encoding="utf-8")
