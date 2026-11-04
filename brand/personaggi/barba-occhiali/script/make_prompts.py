#!/usr/bin/env python3
"""Prompt per i riferimenti del personaggio con barba e occhiali (stile But Why Finance). Scrive prompts/<nome>.txt"""
import os, json
S = os.path.dirname(os.path.abspath(__file__))
CHAR = ("The character is EXACTLY the cartoon man shown in the reference image: short chubby cartoon man with a big head, "
        "shoulder-length wavy chocolate-brown hair parted in the middle, full well-groomed dark brown beard and mustache, "
        "rectangular thick black glasses, light peach-tan skin, small kind eyes, gentle smile, navy blue suit jacket and "
        "trousers, white shirt with open collar and no tie, black shoes. Keep the exact same character design, proportions, "
        "colors and line style as the reference.")
STYLE = ("Flat 2D cartoon illustration, thick uniform black outlines, solid flat colors with minimal soft cel shading, "
         "plain white background, no shadows on the ground.")
NOTEXT = "Absolutely no text, no letters, no numbers, no labels, no logos, no watermark anywhere in the image."
SHOTS = {
 "turnaround": ("1792x1024", "Character model sheet / turnaround on a wide horizontal canvas: the same character drawn four "
   "times side by side, full body, same size, neutral standing pose with arms relaxed at the sides, evenly spaced: "
   "1) front view, 2) right profile view, 3) three-quarter front view (body and head turned only 45 degrees to the left, BOTH eyes and both lenses of the glasses visible, clearly different from the profile), 4) back view (showing the back of the hair and suit). "
   "Neutral friendly expression."),
 "espressioni": ("1792x1024", "Expression sheet on a wide horizontal canvas: six waist-up portraits of the same character "
   "in a 3x2 grid, same size, each clearly separated by white space: 1) happy laughing with open mouth, 2) surprised "
   "with mouth in an 'o' and raised eyebrows, 3) thoughtful with hand on chin and mouth twisted, 4) angry frowning with "
   "furrowed eyebrows and pouting lips, 5) explaining with index finger raised, 6) friendly wink with a thumbs up."),
 "tre-quarti": ("1024x1792", "Full body, neutral standing pose with arms relaxed, seen in a three-quarter front view: "
   "body and head turned about 45 degrees toward the left of the image, so the face is still mostly visible with BOTH "
   "eyes and both lenses of the glasses showing, the far side of the face partly hidden. Calm friendly smile."),
 "posa-annuncio": ("1024x1792", "Full body, standing behind a simple wooden podium without any emblem, both hands raised "
   "open as if making a big announcement, mouth open, very confident."),
 "posa-indica": ("1024x1792", "Full body, pointing with one index finger at an empty space on the side (for a chart added "
   "later), other hand on his hip, confident grin."),
 "posa-firma": ("1024x1792", "Waist-up, sitting at a simple desk, proudly holding up a blank signed sheet of paper toward "
   "the viewer with both hands (the paper shows only a scribbled signature line, no readable text), big smile."),
 "posa-moneta": ("1024x1792", "Full body, holding up a big shiny plain golden coin (no symbols) in one hand and looking "
   "at it with a surprised expression, eyebrows raised, mouth in an 'o'."),
}
os.makedirs(os.path.join(S, "prompts"), exist_ok=True)
out = {}
for k, (size, scene) in SHOTS.items():
    p = " ".join([CHAR, STYLE, "Scene: " + scene, NOTEXT])
    open(os.path.join(S, "prompts", k + ".txt"), "w").write(p); out[k] = {"size": size, "prompt": p}
json.dump(out, open(os.path.join(S, "prompts.json"), "w"), indent=1)
print(len(out))
