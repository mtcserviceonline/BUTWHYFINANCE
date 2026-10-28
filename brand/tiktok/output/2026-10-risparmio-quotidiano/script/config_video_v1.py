# Configurazione del montaggio "Risparmio quotidiano" (letta da montage.py).
#
# SHOTS: un'inquadratura per riga.
#   img      file in img/ (senza .png)
#   parola   indice (da 0) della parola di parole.json con cui parte l'inquadratura: il taglio cade
#            subito prima di quella parola (nella pausa, se c'e')
#   view     (cx, cy, zoom): punto dell'immagine sorgente che va al centro dello schermo e scala
#            (1 = immagine intera 1080x1920; <1 rimpicciolisce e riempie col colore del fondo;
#            >1 e' un primo piano ritagliato, massimo ~1,6 per non sgranare)
#   moto     "in" (zoom 100->106% durante l'inquadratura, default) o "out" (106->100%, per il loop)
#   ancora   (x, y) punto dello schermo attorno a cui cresce lo zoom (default centro); utile per non
#            spingere il soggetto sotto il titolo o dentro la fascia dei sottotitoli
#   pill     True: titolo su targhetta del colore del fondo (primi piani con il disegno dietro al titolo)
#   pan      (dx, dy) spostamento lento in px della sorgente durante l'inquadratura (facoltativo)
#   title    chiave di TITLES (None = nessun titolo); se e' uguale all'inquadratura prima non si rianima
#   sub_cy   centro verticale del sottotitolo (default SUB_CY in montage.py)
#   bubble   (x0, y0, tail_x, tail_y): fumetto "But Why Finance?" (facoltativo)
#
# TITLES: righe di "run" (testo, font, dimensione, colore). colori: "base" (carta su inchiostro,
#   inchiostro su carta) o "accent" (ambra).
#
# SUBS: un sottotitolo per riga. Ogni parola mostrata corrisponde a UNA parola parlata, in ordine
#   (serve per l'evidenziazione parola per parola). *...* = ambra.

TITLES = {
    "hook": [[("CAFFÈ AL GIORNO", "cond", 92, "base")],
             [("~470", "mono", 176, "accent"), (" ", "cond", 30, "accent"), ("€", "cond", 168, "accent"),
              (" ALL'ANNO", "cond", 92, "base")]],
    "perche": [[("MA ", "cond", 150, "base"), ("PERCHÉ?", "cond", 150, "accent")]],
    "piccole": [[("PICCOLE ", "cond", 120, "accent"), ("SPESE", "cond", 120, "base")]],
    "uno": [[("1", "mono", 120, "accent"), (" · ABBONAMENTI", "cond", 104, "base")]],
    "due": [[("2", "mono", 120, "accent"), (" · LISTA DELLA SPESA", "cond", 104, "base")]],
    "tre": [[("3", "mono", 120, "accent"), (" · LUCE E GAS", "cond", 104, "base")]],
    "fine": [[("BASTA GUARDARE LE", "cond", 92, "base")],
             [("PICCOLE SPESE", "cond", 124, "accent")]],
}

SHOTS = [
    {"img": "01", "parola": 0, "view": (540, 885, 0.76), "title": "hook", "sfx": "colpo"},
    {"img": "01", "parola": 8, "view": (520, 1290, 1.42), "title": None, "sfx": "moneta"},
    {"img": "02", "parola": 11, "view": (560, 980, 1.0), "title": "perche", "sfx": "pop"},
    {"img": "03", "parola": 17, "view": (540, 960, 0.86), "title": "piccole"},
    {"img": "04", "parola": 21, "view": (540, 1120, 0.92), "title": "piccole", "ancora": (540, 380)},
    {"img": "04", "parola": 25, "view": (610, 1260, 1.5), "title": "piccole", "pill": True, "pan": (0, 40), "sfx": "monetine"},
    {"img": "05", "parola": 29, "view": (540, 985, 0.82), "title": "uno", "sfx": "pop"},
    {"img": "05", "parola": 32, "view": (740, 1000, 1.5), "title": "uno", "pill": True, "sfx": "forbici"},
    {"img": "06", "parola": 36, "view": (520, 960, 1.0), "title": "due", "sfx": "pop"},
    {"img": "06", "parola": 40, "view": (700, 1080, 1.5), "title": "due", "pill": True, "sfx": "carta"},
    {"img": "07", "parola": 45, "view": (540, 960, 1.0), "title": "tre", "sfx": "pop"},
    {"img": "07", "parola": 49, "view": (330, 1150, 1.55), "title": "tre", "pill": True, "pan": (20, 0)},
    {"img": "08", "parola": 56, "view": (830, 1300, 1.5), "title": None, "sfx": "salvadanaio"},
    {"img": "08", "parola": 60, "view": (540, 1010, 0.82), "title": "fine", "moto": "out",
     "bubble": (600, 485, 585, 655), "sfx": "pop"},
]

SUBS = [
    "UN CAFFÈ AL BAR", "OGNI GIORNO", "COSTA CIRCA *470 EURO*", "ALL'ANNO.",
    "MA *PERCHÉ*", "NON CE NE ACCORGIAMO?",
    "PERCHÉ SONO", "*PICCOLE SPESE*,", "E LE PICCOLE SPESE", "NON LE *GUARDIAMO* MAI.",
    "*PRIMO*:", "CONTROLLA GLI", "*ABBONAMENTI*", "CHE NON USI.",
    "*SECONDO*:", "FAI LA *LISTA*", "PRIMA DI ANDARE", "AL *SUPERMERCATO*.",
    "*TERZO*:", "CONFRONTA LE *OFFERTE*", "DI *LUCE E GAS*", "UNA VOLTA ALL'ANNO.",
    "NON SERVE", "*CAMBIARE VITA*,", "BASTA INIZIARE", "A GUARDARE LE", "*PICCOLE SPESE*.",
]
