# Configurazione del montaggio "Pensione: 67 anni e un mese, cosa puoi fare" (rubrica In 60 secondi,
# accento fucsia #B0186E), letta da montage.py. Testi a schermo dal production doc di ../copione.md.
#
# Regole generali (vedi .claude/skills/crea-post-tiktok/scripts/config_video_esempio.py e la config del post
# ../../2026-11-pensione-67-anni-un-mese/script/config_video.py, da cui questa e' presa):
#   parole indicate per TESTO ("pensione#2" = seconda occorrenza nel testo; senza "#n" = prima occorrenza
#   dopo la parola d'inizio dell'inquadratura precedente);
#   view (cx, cy, zoom) sulla sorgente 1080x1920; zoom effettivo <= zoom_max (qui 1,15 nelle strette);
#   righe di titolo {"runs", "parola"} che entrano sulla parola, "fino" = escono su quella parola,
#   "sopra" = prendono il posto della riga precedente;
#   colori "base" (carta su inchiostro, inchiostro su carta) o "accent" (fucsia, contorno carta).
#
# PREPARATA SENZA LA VOCE DEFINITIVA: inquadrature e titoli sono stati provati con montage.py
# (--solo-controlli e --preview) su tempi stimati dalle pause della registrazione del 30/10/2026
# (scena 1 a parte, che verra' rifatta). Con la voce nuova rilanciare monta.sh: se un controllo
# fallisce (di solito un cambio visivo > 2 s), spostare la parola d'inizio dell'inquadratura.

# Box degli occhiali (lenti + ponte) e del volto (orecchie comprese), pixel della sorgente, misurati su una
# griglia di 50 px e controllati disegnandoli (immagini del 30/10/2026).
OCCHIALI = {
    "01": {"occhiali": (240, 820, 425, 930), "volto": (160, 720, 460, 1030)},
    "02": {"occhiali": (190, 945, 390, 1040), "volto": (95, 845, 405, 1155)},
    "03": {"occhiali": (160, 640, 370, 760), "volto": (60, 550, 415, 855)},
    "04": {"occhiali": (190, 790, 445, 960), "volto": (45, 670, 530, 1060)},
    "05": {"occhiali": (260, 665, 495, 810), "volto": (130, 550, 590, 960)},
    "06": {"occhiali": (155, 725, 345, 835), "volto": (78, 640, 372, 910)},
    "07": {"occhiali": (190, 810, 420, 940), "volto": (90, 690, 455, 1040)},
    "08": {"occhiali": (205, 870, 450, 990), "volto": (128, 770, 498, 1105)},
}

INVITO = ("ECCEZIONI? LEGGI LA DIDASCALIA ↓", "semi", 48, "base")   # freccia nel font, niente emoji a schermo
AVVERTENZA = ("Informazione, non consulenza finanziaria", "semi", 44, "base")

TITLES = {
    # hook: «PENSIONE» piccolo + «67 ANNI» gigante dal fotogramma 0, «+ 1 MESE» sulla parola «mese»
    "hook": [
        [("PENSIONE", "cond", 70, "base")],
        [("67", "mono", 210, "accent"), (" ANNI", "cond", 190, "accent")],
        {"runs": [("+ ", "cond", 150, "accent"), ("1", "mono", 160, "accent"), (" MESE", "cond", 150, "accent")],
         "parola": "mese"},
    ],
    "perche": [[("MA PERCHÉ?", "cond", 130, "base")]],
    # il fatto, sul calendario: «DAL 2027» → «PER QUASI TUTTI» + invito alle eccezioni
    "anno": [
        [("DAL ", "cond", 110, "base"), ("2027", "mono", 112, "accent")],
        {"runs": [("PER ", "cond", 92, "base"), ("QUASI", "cond", 92, "accent"), (" TUTTI", "cond", 92, "base")],
         "parola": "quasi"},
        {"runs": [INVITO], "parola": "tutti,"},
    ],
    "vecchiaia": [
        [("PENSIONE DI VECCHIAIA", "cond", 70, "base")],
        {"runs": [("PIÙ IN LÀ →", "cond", 112, "accent")], "parola": "sposta"},
    ],
    "speranza": [
        [("SI VIVE PIÙ A LUNGO", "cond", 92, "base")],
        {"runs": [("→ L'ETÀ ", "cond", 100, "base"), ("SALE", "cond", 100, "accent")], "parola": "sale"},
        {"runs": [("adeguamento alla speranza di vita (Istat)", "semi", 46, "base")], "parola": "speranza"},
    ],
    "cosa": [[("COSA PUOI FARE?", "cond", 116, "base")]],
    "c1": [
        [("1", "mono", 112, "accent"), (" · ESTRATTO CONTO", "cond", 96, "base")],
        {"runs": [("MyINPS, gratis con SPID o CIE", "semi", 54, "base")], "parola": "estratto"},
    ],
    "c2": [
        [("2", "mono", 112, "accent"), (" · SIMULATORE INPS", "cond", 96, "base")],
        {"runs": [("«La mia pensione futura»", "semi", 56, "base")], "parola": "simulatore"},
    ],
    "c3": [
        [("3", "mono", 112, "accent"), (" · FONDO PENSIONE", "cond", 96, "base")],
        {"runs": [AVVERTENZA], "parola": "fondo"},
        {"runs": [("versamenti deducibili, con un tetto annuo", "semi", 50, "base")], "parola": "dedurre"},
    ],
    "prima": [
        [("PRIMA INIZI,", "cond", 120, "base")],
        {"runs": [("MEGLIO È", "cond", 132, "accent")], "parola": "meglio"},
    ],
    "domanda": [[("CI STAI GIÀ PENSANDO?", "cond", 96, "base")], [AVVERTENZA]],
    # loop: stessa composizione del fotogramma 0 con «?» al posto di «67 ANNI» (stessa riga, fucsia)
    "loop": [
        [("PENSIONE", "cond", 70, "base")],
        [("?", "mono", 210, "accent")],
    ],
}

V0 = (560, 880, 0.92)   # vista d'apertura: orso intero e sedia a dondolo, testa sotto le righe del titolo

SHOTS = [
    # 1 · hook su inchiostro: numero e colpo dal fotogramma 0, punch-in 112% in 0,7 s attorno agli occhiali
    {"img": "01", "parola": 0, "view": V0, "title": "hook", "punch": (1.12, 0.7)},
    # 2 · il fatto (carta, tenda inchiostro → carta): calendario con la pagina fucsia in più; titoli su
    # targhetta color carta ("pill") perche' passano sopra il calendario
    {"img": "02", "parola": "Dal", "view": (540, 950, 0.85), "title": "anno", "pill": True, "transizione": "tenda"},
    {"img": "02", "parola": "la#1", "view": (500, 935, 0.95), "title": "vecchiaia"},
    # «Ma perché?»: stretta su orso sorpreso + sedia, fumetto sopra la sedia
    {"img": "01", "parola": "Ma", "view": (520, 960, 1.10), "title": "perche", "zoom_max": 1.15,
     "bubble": (560, 440, 640, 600), "bubble_parola": "perché?"},
    # 3 · il perché: sentiero, sagoma col bastone, sedia spostata più in là
    {"img": "03", "parola": "Si", "view": (540, 1040, 0.92), "title": "speranza"},
    {"img": "03", "parola": "l'età", "view": (515, 930, 1.09), "title": "speranza", "zoom_max": 1.15},
    # 4 · consiglio 1: estratto conto
    {"img": "04", "parola": "Cosa", "view": (480, 1020, 0.95), "title": "cosa"},
    {"img": "04", "parola": "Primo:", "view": (480, 1020, 0.95), "title": "c1"},
    {"img": "04", "parola": "contributi", "view": (520, 1000, 1.03), "title": "c1", "zoom_max": 1.15},
    # 5 · consiglio 2: simulatore
    {"img": "05", "parola": "Secondo:", "view": (500, 1000, 0.95), "title": "c2"},
    {"img": "05", "parola": "pensione#2", "view": (560, 880, 1.08), "title": "c2", "zoom_max": 1.15},
    # 6 · consiglio 3: fondo pensione (avvertenza piccola a schermo)
    {"img": "06", "parola": "Terzo:", "view": (540, 1000, 1.0), "title": "c3"},
    {"img": "06", "parola": "Quello", "view": (560, 1000, 1.08), "title": "c3", "zoom_max": 1.15},
    # 7 · prima inizi, meglio è: clessidra
    {"img": "07", "parola": "Prima", "view": (520, 1000, 0.98), "title": "prima"},
    # 8 · domanda su inchiostro: occhiolino, sedia ferma (richiama l'hook)
    {"img": "08", "parola": "E", "view": (560, 1000, 0.95), "title": "domanda",
     "bubble": (520, 470, 600, 640), "bubble_parola": "già"},
    # loop: ultimo ~0,45 s = fotogramma 0 (vista prima del punch-in) con «?» al posto di «67 ANNI»
    {"img": "01", "dopo": "pensando?", "view": V0, "title": "loop", "moto": "fermo"},
]

SUBS = [
    "*67* ANNI", "E UN *MESE*.",
    "DAL *2027*,", "PER *QUASI* TUTTI,", "LA PENSIONE", "DI VECCHIAIA", "SI SPOSTA *PIÙ IN LÀ*.",
    "MA *PERCHÉ?*",
    "SI VIVE PIÙ A LUNGO:", "L'ETÀ *SALE*", "CON LA SPERANZA DI VITA.",
    "COSA PUOI *FARE?*", "PRIMO:", "CONTROLLA I *CONTRIBUTI*", "VERSATI, NEL TUO", "*ESTRATTO CONTO* INPS.",
    "SECONDO:", "STIMA LA TUA PENSIONE", "CON IL *SIMULATORE*", "GRATUITO DELL'INPS.",
    "TERZO:", "VALUTA UN *FONDO PENSIONE*.", "QUELLO CHE VERSI", "SI PUÒ *DEDURRE*", "DALLE TASSE.",
    "PRIMA INIZI,", "*MEGLIO* È.",
    "E TU, CI STAI", "GIÀ *PENSANDO?*",
]

# effetti solo sui numeri: colpo secco a 0,0 s (il numero e' la prima parola), tick su «mese» e sui tre
# numeri dei consigli
EFFETTI = [
    ("colpo", 0.0),
    ("tick", "mese"), ("tick", "Primo:"), ("tick", "Secondo:"), ("tick", "Terzo:"),
]
