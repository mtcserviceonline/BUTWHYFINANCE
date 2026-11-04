"""Costanti e funzioni condivise dalla pipeline dei video TikTok di But Why Finance."""
import json, os, re, unicodedata

P = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(P, "..", "..", ".."))
MASCOTTE = os.path.join(REPO, "brand", "mascotte", "mascotte-principale.jpg")

W, H, FPS = 1080, 1920, 30
INK, PAPER, BRAND, WHITE = (17, 20, 24), (244, 241, 234), (0, 107, 60), (255, 255, 255)
SAFE_L, SAFE_R = 60, W - 130          # fascia destra (pulsanti TikTok) libera
CX = (SAFE_L + SAFE_R) // 2
TITLE_TOP = 215                       # sotto il 10% in alto (192 px)
SUB_CY = 1440                         # sottotitoli sopra il 15% in basso (1632 px)
FONTS = {"cond": f"{P}/fonts/IBMPlexSansCondensed-Bold.ttf",
         "semi": f"{P}/fonts/IBMPlexSansCondensed-SemiBold.ttf",
         "mono": f"{P}/fonts/IBMPlexMono-Bold.ttf"}

# Rubriche -> colore d'accento (da brand/tiktok/stile-tiktok.md)
RUBRICHE = {
    "vero o falso?": "#FFD60A",
    "in 60 secondi": "#B0186E",
    "il numero": "#1F4FA3",
    "il prezzo di…": "#E9A400",
    "chi paga?": "#B8420F",
    "dietro la notizia": "#006B3C",
}
LIMITE_PAROLE = (80, 95, 100)          # minimo, obiettivo massimo, limite rigido (30-40 s)


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def carica_episodio(ep):
    path = os.path.join(ep, "scene.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def accento(epi):
    if epi.get("accento"):
        return hex2rgb(epi["accento"])
    r = RUBRICHE.get(epi.get("rubrica", "").strip().lower().replace("...", "…"))
    return hex2rgb(r or "#E9A400")


def tokens(testo):
    """Parole normalizzate (minuscole, senza accenti né punteggiatura, senza tag [..])."""
    testo = re.sub(r"\[[^\]]*\]", " ", testo)
    testo = unicodedata.normalize("NFD", testo.lower())
    testo = "".join(c for c in testo if unicodedata.category(c) != "Mn")
    testo = testo.replace("'", " ").replace("’", " ")
    return re.findall(r"[a-z0-9]+", testo)


def sillabe(t):
    return max(1, len(re.findall(r"[aeiouàèéìòóù]+", t.lower())))
