#!/usr/bin/env python3
"""Trascrizione con i tempi (Markdown) e sottotitoli SRT dalla voce montata.

Uso: trascrizione.py PAROLE.json DURATA_VIDEO OUT.md OUT.srt [--titolo "..."] [--nota "..."]
Le battute si dividono alla punteggiatura (, . : ? !) e comunque oltre ~42 caratteri; i tempi sono
quelli di parole.json (inizio di frase esatto dalle pause, parole dentro la frase stimate)."""
import argparse, json


def ts(t, srt=True):
    h, r = divmod(max(0.0, t), 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",") if srt else f"{int(m)}:{s:05.2f}"


def battute(words, maxc=42):
    out, cur = [], []
    for w in words:
        if cur and len(" ".join(x["w"] for x in cur + [w])) > maxc:
            out.append(cur)
            cur = []
        cur.append(w)
        if w["w"][-1] in ",.:?!":
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("parole"); ap.add_argument("durata", type=float); ap.add_argument("md"); ap.add_argument("srt")
    ap.add_argument("--titolo", default="Trascrizione")
    ap.add_argument("--nota", default="")
    a = ap.parse_args()
    words = json.load(open(a.parole, encoding="utf-8"))
    bt = battute(words)
    with open(a.srt, "w", encoding="utf-8") as f:
        for k, b in enumerate(bt, 1):
            fine = min(b[-1]["end"] + 0.15, bt[k][0]["start"] if k < len(bt) else a.durata)
            f.write(f"{k}\n{ts(b[0]['start'])} --> {ts(fine)}\n{' '.join(x['w'] for x in b)}\n\n")
    with open(a.md, "w", encoding="utf-8") as f:
        durata = f"{a.durata:.2f}".replace(".", ",")
        f.write(f"# {a.titolo}\n\n{a.nota}\n\nDurata del video: {durata} s.\n\n")
        f.write("| Da | A | Testo |\n|---|---|---|\n")
        for b in bt:
            f.write(f"| {ts(b[0]['start'], False)} | {ts(b[-1]['end'], False)} | {' '.join(x['w'] for x in b)} |\n")
        f.write("\nTesto completo:\n\n> " + " ".join(w["w"] for w in words) + "\n")
    print(f"{len(bt)} battute -> {a.md}, {a.srt}")


if __name__ == "__main__":
    main()
