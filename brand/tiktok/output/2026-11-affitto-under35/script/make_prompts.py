#!/usr/bin/env python3
"""Scrive i prompt dei primi fotogrammi (uno per scena) in script/prompts/NN.txt."""
import json, pathlib
STYLE = ("Style: handmade paper-collage look, cut-paper textures, masking tape, ink stamps, hand-drawn doodles, "
         "warm cream paper background, deep navy ink accents, one accent color burnt orange (#B8420F) with soft peach tint (#ECD8CB), "
         "soft even studio light, gentle stop-motion feel, vertical 9:16.")
BEAR = ("The bear is EXACTLY the mascot in the reference image, rendered as a cut-paper collage character: brown cartoon bear "
        "with copper-orange fur, light peach muzzle, round ears with black inner ears, black rounded nose, "
        "black round sunglasses with a white diagonal glare on each lens always on (eyes never visible), "
        "dark green t-shirt with the euro sign in the center of the chest exactly as in the reference. "
        "Same design and proportions as the reference image, fully visible from head to feet.")
NOTEXT = "No text, no letters, no numbers, no logos, no flags anywhere in the image."
SCENES = {
 "01": "Wide shot. The bear stands in front of two IDENTICAL small paper houses side by side (same shape, same size, same colors, same roof, mirror copies of each other), holding a paper key in one paw, looking at the camera with a curious expression.",
 "02": "The bear stands a few steps away from a large blank paper document taped to the wall with masking tape, holding two blank paper price tags (one large, one small) in his paws and turning his head toward the document with a calm expression. Below the document, a small paper table with three paper ink stamps of decreasing size.",
 "03": "Wide shot, the whole scene visible with empty floor below the feet. The bear stands beside a paper desk and is about to sit down on a paper chair. On the desk lie two rolled-up long paper receipts (blank) and a paper magnifying glass. Thoughtful expression, one paw resting on the desk.",
 "04": "Wide shot from slightly further away, the whole bear visible including his feet under the desk, empty floor below. The bear sits on a paper chair at a small paper desk, the two long blank paper receipts (completely empty, no lines, no print) lying unrolled on it and the paper magnifying glass set aside; in front of him a loose scattered heap of plain paper coins with no markings. He looks at the coins with a light smile, about to stand up.",
 "05": "The bear stands next to two piles of plain paper coins on a paper desk, one very tall and one tiny, and turns his head toward a large paper public building with classical columns standing on the other side of the frame. A closed paper wallet lies on the ground in front of the building. Serious expression.",
 "06": "The bear stands centered in front of a small paper table on which lie two blank paper cards. Paws relaxed at his sides, friendly expression, looking at the camera, about to pick up the cards.",
}
out = pathlib.Path(__file__).parent / "prompts"
allp = {}
for k, s in SCENES.items():
    p = f"{STYLE} {BEAR} Scene: {s} {NOTEXT}"
    (out / f"{k}.txt").write_text(p, encoding="utf-8"); allp[k] = p
(pathlib.Path(__file__).parent / "prompts.json").write_text(json.dumps(allp, indent=1, ensure_ascii=False), encoding="utf-8")
