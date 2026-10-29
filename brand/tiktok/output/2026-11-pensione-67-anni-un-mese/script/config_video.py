# Configurazione del montaggio "Pensione: 67 anni e 1 mese" (rubrica Il numero, accento blu #1F4FA3),
# letta da montage.py. Testi a schermo dal production doc di copione.md (giro 3).
#
# Regole generali (vedi .claude/skills/crea-post-tiktok/scripts/config_video_esempio.py per tutti i campi):
#   parole indicate per TESTO ("sessantasette#2" = seconda occorrenza nel testo; senza "#n" = prima
#   occorrenza dopo la parola d'inizio dell'inquadratura precedente);
#   view (cx, cy, zoom) sulla sorgente 1080x1920; zoom effettivo <= zoom_max (qui 1,15 nelle strette);
#   righe di titolo {"runs", "parola"} che entrano sulla parola, "fino" = escono su quella parola,
#   "sopra" = prendono il posto della riga precedente (aggiunte di questo post in montage.py);
#   colori "base" (carta su inchiostro, inchiostro su carta) o "accent" (blu, contorno carta).

# Box degli occhiali (lenti + ponte) e del volto (orecchie comprese), pixel della sorgente, misurati su una
# griglia di 50 px e controllati disegnandoli.
OCCHIALI = {
    "01": {"occhiali": (190, 830, 420, 940), "volto": (125, 745, 495, 1070)},
    "02": {"occhiali": (100, 1055, 340, 1140), "volto": (80, 960, 350, 1245)},
    "03": {"occhiali": (240, 700, 460, 850), "volto": (90, 605, 500, 955)},
    "04": {"occhiali": (420, 660, 620, 770), "volto": (335, 575, 705, 910)},
    "05": {"occhiali": (285, 570, 600, 730), "volto": (165, 435, 625, 875)},
}

INVITO = ("ECCEZIONI? SCOPRI SE RIENTRI ↓", "semi", 50, "base")   # freccia nel font, niente emoji a schermo

TITLES = {
    # hook: «PENSIONE» piccolo + «1 MESE» gigante dal fotogramma 0; le righe si sostituiscono
    "hook": [
        {"runs": [("PENSIONE", "cond", 70, "base")], "fino": "duemilaventisette"},
        {"runs": [("PENSIONE · DAL ", "cond", 70, "base"), ("2027", "mono", 66, "accent")],
         "parola": "duemilaventisette", "sopra": True},
        [("1", "mono", 250, "accent"), (" MESE", "cond", 236, "accent")],
        {"runs": [("DI LAVORO IN PIÙ", "cond", 100, "base")], "parola": "lavoro", "fino": "tutti"},
        {"runs": [("PER ", "cond", 100, "base"), ("QUASI", "cond", 82, "base"), (" TUTTI", "cond", 100, "base")],
         "parola": "tutti", "sopra": True},
        {"runs": [INVITO], "parola": "Dal"},
    ],
    "perche": [[("MA PERCHÉ?", "cond", 130, "base")], [INVITO]],
    "vecchiaia": [
        [("PENSIONE DI VECCHIAIA", "cond", 74, "base")],
        {"runs": [("67", "mono", 110, "accent"), (" ANNI + ", "cond", 104, "accent"), ("1", "mono", 110, "accent"),
                  (" MESE", "cond", 104, "accent")], "parola": "sessantasette"},
        {"runs": [("OGNI ", "semi", 56, "base"), ("2", "mono", 54, "base"), (" ANNI · Fonte: Istat", "semi", 56, "base")],
         "parola": "La"},
    ],
    "regola": [
        [("A ", "cond", 120, "base"), ("65", "mono", 124, "accent"), (" ANNI", "cond", 120, "base")],
        {"runs": [("SI VIVE DI PIÙ?", "cond", 104, "base")], "parola": "vive"},
    ],
    "tardi": [[("→ PENSIONE ", "cond", 78, "base"), ("PIÙ TARDI", "cond", 78, "accent")]],
    "2028": [
        [("2028", "mono", 170, "accent")],
        [("Fonte: INPS", "semi", 52, "base")],
        {"runs": [("67", "mono", 110, "accent"), (" ANNI + ", "cond", 104, "accent"), ("3", "mono", 110, "accent"),
                  (" MESI", "cond", 104, "accent")], "parola": "sessantasette#2"},
    ],
    "difende": [
        {"runs": [("CHI DIFENDE LA REGOLA", "cond", 96, "base")], "parola": "difende"},
        {"runs": [("conti pubblici in ", "semi", 66, "base"), ("equilibrio", "semi", 66, "accent")],
         "parola": "equilibrio"},
    ],
    "cgil": [
        [("CGIL", "cond", 112, "accent"), (" (sindacato)", "semi", 70, "base")],
        {"runs": [("traguardo più lontano", "semi", 70, "base")], "parola": "traguardo"},
    ],
    "fine": [
        [("POCO O TANTO?", "cond", 110, "base")],
        {"runs": [("1", "mono", 136, "accent"), (" MESE CONTA", "cond", 128, "accent")], "parola": "mese#3"},
    ],
    "domanda": [[("A CHE ETÀ IN PENSIONE?", "cond", 100, "base")]],
    # loop: stessa composizione del fotogramma 0 con «?» al posto di «1 MESE» (stessa riga, blu, stessa grandezza)
    "loop": [
        [("PENSIONE", "cond", 70, "base")],
        [("?", "mono", 250, "accent")],
    ],
}

V0 = (560, 880, 0.92)   # vista d'apertura (orso intero, clessidra, sedia; testa sotto le righe del titolo)

SHOTS = [
    # 1 · hook su inchiostro: numero e colpo dal fotogramma 0, punch-in 112% in 0,7 s attorno agli occhiali
    {"img": "01", "parola": 0, "view": V0, "title": "hook", "punch": (1.12, 0.7)},
    # «Ma perché?»: stretta su orso + clessidra (<= 115%), fumetto di lato sopra la sedia
    {"img": "01", "parola": "Ma", "view": (500, 960, 1.10), "title": "perche", "zoom_max": 1.15,
     "bubble": (560, 440, 640, 600), "bubble_parola": "perché"},
    # 2 · la regola (carta): larga, media, stretta sulla sagoma che cammina, sedia in cima. Zoom >= 1 e cx
    # centrato: collina e sentiero toccano i bordi dell'immagine, una vista rimpicciolita ne mostrerebbe il taglio.
    # La € della maglietta resta sopra i sottotitoli (su una riga sola in questa scena);
    # titoli su targhetta color carta ("pill") perche' nelle viste ravvicinate passano sopra sedia e sagoma.
    {"img": "02", "parola": "Pensione", "view": (540, 900, 1.0), "title": "vecchiaia", "pill": True, "transizione": "tenda"},
    {"img": "02", "parola": "mese#2", "view": (495, 1150, 1.10), "title": "vecchiaia", "pill": True, "zoom_max": 1.15},
    {"img": "02", "parola": "sessantacinque", "view": (520, 950, 1.10), "title": "regola", "pill": True, "zoom_max": 1.15},
    {"img": "02", "parola": "si#2", "view": (560, 1000, 1.04), "title": "tardi", "pill": True},
    # 3 · 2028: scala, stretta sul gradino piu' alto, poi di nuovo l'orso che guarda in su
    {"img": "03", "parola": "Nel", "view": (540, 1060, 0.85), "title": "2028"},
    {"img": "03", "parola": "sessantasette#2", "view": (590, 1000, 1.05), "title": "2028", "zoom_max": 1.15},
    {"img": "03", "parola": "tre", "view": (520, 1060, 0.92), "title": "2028"},
    # 4 · due tesi: larga, poi una sagoma per volta (orso sempre in campo); zoom >= 1 per non mostrare
    # la fine della linea del pavimento
    {"img": "04", "parola": "Per#2", "view": (540, 900, 1.0), "title": "difende"},
    {"img": "04", "parola": "tiene", "view": (380, 900, 1.10), "title": "difende", "zoom_max": 1.15},
    {"img": "04", "parola": "Cgil", "view": (720, 900, 1.10), "title": "cgil", "zoom_max": 1.15},
    # 5 · chiusura su inchiostro: occhiolino con la clessidra, poi stretta con la domanda e il fumetto
    {"img": "05", "parola": "Poco", "view": (540, 860, 0.92), "title": "fine"},
    {"img": "05", "parola": "E", "view": (480, 900, 1.08), "title": "domanda", "zoom_max": 1.15,
     "bubble": (500, 345, 600, 520), "bubble_parola": "che"},
    # loop: ultimo ~0,45 s = fotogramma 0 (vista prima del punch-in) con «?» al posto di «1 MESE»
    {"img": "01", "dopo": "andarci?", "view": V0, "title": "loop", "moto": "fermo"},
]

SUBS = [
    "UN *MESE* DI LAVORO", "IN PIÙ.", "PER *QUASI* TUTTI.", "DAL *2027*.", "MA *PERCHÉ?*",
    "PENSIONE", "DI VECCHIAIA:", "*67* ANNI", "E UN MESE.",
    "LA *REGOLA*:", "SE A *65* ANNI", "SI VIVE PIÙ", "A LUNGO,", "SI VA *PIÙ TARDI*.",
    "NEL *2028*,", "*67* E TRE MESI.",
    "PER CHI DIFENDE LA REGOLA,", "TIENE IN *EQUILIBRIO* I CONTI.",
    "PER LA *CGIL*,", "ALLONTANA IL *TRAGUARDO*", "DI CHI LAVORA.",
    "POCO O TANTO,", "UN *MESE* CONTA.", "E TU: A CHE ETÀ", "PENSI DI *ANDARCI?*",
]

# effetti solo sui numeri: colpo secco a 0,0 s (il numero e' la prima parola), tick sui due «67»
EFFETTI = [
    ("colpo", 0.0),
    ("tick", "sessantasette"), ("tick", "sessantasette#2"),
]
