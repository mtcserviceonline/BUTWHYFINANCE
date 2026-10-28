#!/usr/bin/env python3
"""Controlli automatici sulle immagini del post (non sostituiscono lo sguardo: ogni immagine va guardata con Read).

Per ogni NN.png misura:
- dimensioni (attese 1080x1920);
- colore del fondo (mediana dei quattro angoli) e fondo piu' vicino tra inchiostro #111418 e carta #F4F1EA;
- ingombro del contenuto: dalla prima all'ultima riga "piena", in % dell'altezza dall'alto,
  e colonna piu' a destra con contenuto, in % della larghezza;
- avvisi: contenuto nel 10% in alto, nel 15% in basso, nel 10% a destra; fondo lontano dal colore atteso.

Stampa una tabella Markdown da incollare in immagini/README.md ("Controlli fatti").

Uso: controlla_immagini.py CARTELLA_IMMAGINI [--prompts prompts.json]
     (con --prompts confronta il fondo misurato con quello richiesto per ogni immagine)
"""
import argparse
import glob
import json
import os
import re

import numpy as np
from PIL import Image

FONDI = {"inchiostro": (17, 20, 24), "carta": (244, 241, 234)}


def hexa(c):
    return "#{:02X}{:02X}{:02X}".format(*c)


def misura(path, soglia=60, min_frac=0.01):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(int)
    h, w, _ = a.shape
    k = max(8, min(h, w) // 40)
    angoli = np.concatenate([a[:k, :k].reshape(-1, 3), a[:k, -k:].reshape(-1, 3),
                             a[-k:, :k].reshape(-1, 3), a[-k:, -k:].reshape(-1, 3)])
    fondo = tuple(int(v) for v in np.median(angoli, axis=0))
    diff = np.abs(a - np.array(fondo)).sum(axis=2) > soglia
    righe = np.where(diff.sum(axis=1) > w * min_frac)[0]
    # linee sottili isolate (es. la linea del pavimento): si segnalano a parte e non contano nell'ingombro
    linee = []
    if len(righe):
        tratti, inizio = [], righe[0]
        for prev, cur in zip(righe[:-1], righe[1:]):
            if cur - prev > 1:
                tratti.append((inizio, prev))
                inizio = cur
        tratti.append((inizio, righe[-1]))
        tenuti = []
        for i, (r0, r1) in enumerate(tratti):
            gap_su = r0 - tratti[i - 1][1] if i else r0
            gap_giu = tratti[i + 1][0] - r1 if i + 1 < len(tratti) else h - r1
            if r1 - r0 < 8 and gap_su > 20 and gap_giu > 20:
                linee.append(100 * r0 / h)
            else:
                tenuti.append((r0, r1))
        if tenuti:
            righe = np.array([tenuti[0][0], tenuti[-1][1]])
    colonne = np.where(diff.sum(axis=0) > h * min_frac)[0]
    vicino = min(FONDI, key=lambda n: sum((x - y) ** 2 for x, y in zip(fondo, FONDI[n])))
    dist = max(abs(x - y) for x, y in zip(fondo, FONDI[vicino]))
    return {
        "file": os.path.basename(path), "dim": f"{w}x{h}", "fondo": hexa(fondo), "fondo_tipo": vicino,
        "fondo_scarto": dist, "linee": linee,
        "alto": 100 * righe.min() / h if len(righe) else None,
        "basso": 100 * (righe.max() + 1) / h if len(righe) else None,
        "destra": 100 * (colonne.max() + 1) / w if len(colonne) else None,
    }


def avvisi(m, atteso=None):
    out = []
    if m["dim"] != "1080x1920":
        out.append(f"dimensioni {m['dim']}")
    if atteso and atteso != m["fondo_tipo"]:
        out.append(f"fondo {m['fondo_tipo']} invece di {atteso}")
    if m["fondo_scarto"] > 12:
        out.append(f"fondo lontano da {m['fondo_tipo']} ({m['fondo_scarto']} livelli)")
    if m["alto"] is not None and m["alto"] < 10:
        out.append("contenuto nel 10% in alto")
    if m["basso"] is not None and m["basso"] > 85:
        out.append("contenuto nel 15% in basso")
    if m["destra"] is not None and m["destra"] > 90:
        out.append("contenuto nel 10% a destra")
    for y in m["linee"]:
        out.append(f"linea sottile a {y:.1f}% (pavimento?) non contata".replace(".", ","))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cartella")
    ap.add_argument("--prompts", help="prompts.json per sapere il fondo richiesto")
    a = ap.parse_args()
    attesi = {}
    if a.prompts:
        for k, v in json.load(open(a.prompts, encoding="utf-8")).items():
            attesi[k.zfill(2)] = v.get("background", "").split(" ")[0] or None
    files = sorted(f for f in glob.glob(os.path.join(a.cartella, "*.png"))
                   if re.fullmatch(r"\d+\.png", os.path.basename(f)))
    if not files:
        ap.error("nessuna immagine NN.png")
    print("| # | Dimensioni | Fondo misurato | Contenuto da… a… (altezza) | Destra fino a | Avvisi |")
    print("|---|---|---|---|---|---|")
    n_avvisi = 0
    for f in files:
        m = misura(f)
        nid = os.path.splitext(m["file"])[0].zfill(2)
        av = avvisi(m, attesi.get(nid))
        n_avvisi += any(not x.startswith("linea") for x in av)
        fmt = lambda v: "-" if v is None else f"{v:.1f}%".replace(".", ",")  # noqa: E731
        print(f"| {nid} | {m['dim']} | `{m['fondo']}` ({m['fondo_tipo']}) | {fmt(m['alto'])} – {fmt(m['basso'])} "
              f"| {fmt(m['destra'])} | {'; '.join(av) or 'ok'} |")
    print(f"\n{len(files)} immagini, {n_avvisi} con avvisi. Ricorda: guardale comunque tutte con Read "
          "(scritte, € coperta o sulla manica, sagome colorate, colori d'accento sbagliati non si misurano qui).")


if __name__ == "__main__":
    main()
