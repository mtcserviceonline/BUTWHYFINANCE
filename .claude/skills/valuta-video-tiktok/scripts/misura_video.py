#!/usr/bin/env python3
"""Misure oggettive di un video TikTok per la guida alla retention.

Uso:
  python3 -I misura_video.py VIDEO.mp4 --out CARTELLA [--trascrizione FILE]

Produce in CARTELLA: sheet_NN.png (fotogrammi ogni 0,5 s, 16 per tavola),
misure.json e stampa un riepilogo. Richiede ffmpeg, ffprobe e numpy.
La trascrizione puo' essere .srt oppure una tabella "Da  A  Testo"
(tempi m:ss.cc separati da tab o spazi).
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
import numpy as np


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(video):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
             "-of", "json", str(video)])
    j = json.loads(r.stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    return float(j["format"]["duration"]), v["width"], v["height"], any(s["codec_type"] == "audio" for s in j["streams"])


def audio_metrics(video, out):
    wav = out / "audio.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
    vol = run(["ffmpeg", "-i", str(wav), "-af", "volumedetect", "-f", "null", "-"]).stderr
    mean = re.search(r"mean_volume: (-?[\d.]+)", vol)
    peak = re.search(r"max_volume: (-?[\d.]+)", vol)
    lufs = run(["ffmpeg", "-i", str(wav), "-af", "ebur128", "-f", "null", "-"]).stderr
    integ = re.findall(r"I:\s+(-?[\d.]+) LUFS", lufs)
    sil = run(["ffmpeg", "-i", str(wav), "-af", "silencedetect=noise=-45dB:d=0.2", "-f", "null", "-"]).stderr
    return {
        "media_db": float(mean.group(1)) if mean else None,
        "picco_db": float(peak.group(1)) if peak else None,
        "lufs_integrato": float(integ[-1]) if integ else None,
        "pause_ge_0_2s_a_-45dB": len(re.findall("silence_start", sil)),
    }


def visual_events(video, dur):
    w, h = 72, 128
    raw = run_bytes(["ffmpeg", "-v", "error", "-i", str(video), "-vf", f"fps=15,scale={w}:{h},format=gray",
                     "-f", "rawvideo", "-"])
    f = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
    d = np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))
    t = np.arange(1, len(f)) / 15

    def events(th):
        ev = []
        for x, v in zip(t, d):
            if v > th and (not ev or x - ev[-1] > 0.35):
                ev.append(round(float(x), 2))
        return ev

    out = {}
    for name, th in (("cambi_totali", 3), ("cambi_medi", 8), ("cambi_grandi", 25)):
        ev = events(th)
        gaps = np.diff(ev) if len(ev) > 1 else np.array([0.0])
        out[name] = {"n": len(ev), "ogni_s": round(dur / max(len(ev), 1), 2),
                     "mediana_s": round(float(np.median(gaps)), 2), "max_s": round(float(gaps.max()), 2),
                     "tempi": ev}
    out["fotogrammi_fermi_%"] = round(float((d < 0.15).mean() * 100))
    out["fotogrammi_con_piccolo_movimento_%"] = round(float(((d >= 0.15) & (d <= 3)).mean() * 100))
    # buchi: intervalli piu' lunghi di 2,5 s senza alcun cambio sopra soglia 3
    ev = [0.0] + out["cambi_totali"]["tempi"] + [dur]
    out["buchi_oltre_2_5s"] = [[round(a, 1), round(b, 1)] for a, b in zip(ev, ev[1:]) if b - a > 2.5]
    return out


def run_bytes(cmd):
    return subprocess.run(cmd, capture_output=True).stdout


def sheets(video, out):
    pat = str(out / "sheet_%02d.png")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf",
         "fps=2,scale=240:-1,drawtext=text='%{pts\\:hms}':x=4:y=4:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,tile=8x2",
         pat])
    return sorted(p.name for p in out.glob("sheet_*.png"))


def ts(s):
    s = s.strip().replace(",", ".")
    parts = s.split(":")
    sec = 0.0
    for p in parts:
        sec = sec * 60 + float(p)
    return sec


def load_transcript(path):
    txt = Path(path).read_text(encoding="utf-8")
    seg = []
    if "-->" in txt:
        for b in re.split(r"\n\s*\n", txt.strip()):
            l = [x for x in b.split("\n") if x.strip()]
            m = next((re.match(r"([\d:.,]+)\s*-->\s*([\d:.,]+)", x) for x in l if "-->" in x), None)
            if m:
                text = " ".join(x for x in l if "-->" not in x and not x.strip().isdigit())
                seg.append((ts(m.group(1)), ts(m.group(2)), text))
    else:
        for line in txt.splitlines():
            m = re.match(r"\s*([\d:.]+)\s+([\d:.]+)\s+(.*\S)", line)
            if m and re.match(r"\d", m.group(1)):
                seg.append((ts(m.group(1)), ts(m.group(2)), m.group(3)))
    return seg


def transcript_metrics(seg):
    if not seg:
        return None
    words = sum(len(s[2].split()) for s in seg)
    dur = seg[-1][1] - seg[0][0]
    gaps = [round(b[0] - a[1], 2) for a, b in zip(seg, seg[1:])]
    first_you = next((round(s[0], 1) for s in seg if re.search(r"\b(te|tu|tuo|tua|tuoi|tue|ti|vuoi|hai|sai|devi|puoi|spendi|bevi|guardi|usi|paghi|compri|risparmi)\b", s[2], re.I)), None)
    txt = " ".join(s[2] for s in seg).lower()
    return {
        "parole": words, "durata_parlato_s": round(dur, 1), "parole_al_minuto": round(words / dur * 60),
        "segmenti": len(seg), "parole_per_segmento": round(words / len(seg), 1),
        "primo_riferimento_a_te_s": first_you,
        "domande": txt.count("?"),
        "frasi_segnale": {k: txt.count(k) for k in ["ma perch", "fermati", "e non è finita", "cioè", "la parte che riguarda", "primo", "secondo", "terzo", "ma la"]},
        "ultima_parola_s": round(seg[-1][1], 2),
        "pause_tra_segmenti_oltre_0_3s": sum(1 for g in gaps if g > 0.3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out", required=True)
    ap.add_argument("--trascrizione")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    dur, w, h, has_audio = probe(a.video)
    m = {"file": Path(a.video).name, "durata_s": round(dur, 1), "risoluzione": f"{w}x{h}", "audio": has_audio}
    if has_audio:
        m["audio_misure"] = audio_metrics(a.video, out)
    m["visivo"] = visual_events(a.video, dur)
    m["tavole"] = sheets(a.video, out)
    if a.trascrizione:
        seg = load_transcript(a.trascrizione)
        m["parlato"] = transcript_metrics(seg)
        if m["parlato"]:
            m["parlato"]["scarto_fine_video_s"] = round(dur - m["parlato"]["ultima_parola_s"], 2)
    (out / "misure.json").write_text(json.dumps(m, ensure_ascii=False, indent=2))
    v = m["visivo"]
    print(f"Durata {m['durata_s']} s, {m['risoluzione']}")
    print(f"Cambi visivi: totali {v['cambi_totali']['n']} (1 ogni {v['cambi_totali']['ogni_s']} s), "
          f"medi {v['cambi_medi']['n']} (1 ogni {v['cambi_medi']['ogni_s']} s), grandi {v['cambi_grandi']['n']}")
    print(f"Fermi {v['fotogrammi_fermi_%']}%, piccolo movimento {v['fotogrammi_con_piccolo_movimento_%']}%, buchi > 2,5 s: {v['buchi_oltre_2_5s']}")
    if "audio_misure" in m:
        print("Audio:", m["audio_misure"])
    if m.get("parlato"):
        print("Parlato:", {k: v for k, v in m["parlato"].items() if k != "frasi_segnale"})
    print(f"Tavole: {len(m['tavole'])} in {out} (16 fotogrammi ciascuna, 0,5 s l'uno)")


if __name__ == "__main__":
    sys.exit(main())
