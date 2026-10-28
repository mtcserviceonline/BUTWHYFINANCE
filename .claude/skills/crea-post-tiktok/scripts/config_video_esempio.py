# Configurazione del montaggio v2 "Risparmio quotidiano" (letta da montage.py).
#
# Le parole si indicano col TESTO (non con l'indice): "quattrocentosettanta", "mai#2" (seconda occorrenza
# nel testo), oppure senza "#n" = prima occorrenza dopo la parola d'inizio dell'inquadratura precedente.
# Il testo e' quello noto delle scene (scene_elevenlabs.json -> frasi.py -> allinea.py -> parole.json).
#
# SHOTS: un'inquadratura per riga.
#   img      file in img/ (senza .png)
#   parola   il taglio cade subito prima di questa parola (nella pausa, se c'e'); la prima parte da 0
#   dopo     in alternativa a "parola": il taglio cade alla FINE di questa parola (per il loop finale)
#   view     (cx, cy, zoom): punto della sorgente al centro dello schermo e scala (1 = immagine intera;
#            <1 rimpicciolisce col fondo esteso; >1 ingrandisce). Limite: zoom effettivo <= zoom_max
#   zoom_max default 1.20 (I-2); 1.15 dove richiesto (I-5)
#   moto     "in" (zoom 100->104% durante l'inquadratura, default), "out" (104->100%), "fermo"
#   ancora   (x, y) punto dello schermo attorno a cui cresce lo zoom; default: centro degli occhiali
#            dell'immagine (cosi' gli occhiali non si spostano mai durante lo zoom)
#   pan      (dx, dy) spostamento lento della sorgente in px (facoltativo)
#   title    chiave di TITLES (None = nessun titolo); uguale all'inquadratura prima = non si rianima
#   title_y  bordo alto del titolo (default 215, sotto il 10% in alto)
#   pill     True: titolo su targhetta del colore del fondo
#   sub_bottom  bordo basso del blocco sottotitoli (default 1600: il testo resta sopra y=1632, 85%)
#   bubble   (x0, y0, tail_x, tail_y): fumetto "But Why Finance?"; bubble_parola = entra su quella parola
#   transizione  "tenda": la nuova inquadratura sale dal basso in 0,2 s (una sola nel video, M-2)
#
# TITLES: righe; ogni riga e' una lista di "run" (testo, font, dimensione, colore) oppure un dict
#   {"runs": [...], "parola": "..."} = la riga entra (pop) quando la voce dice quella parola.
#   colori: "base" (carta su inchiostro, inchiostro su carta) o "accent" (ambra).
#
# SCRITTE: testi stampati SOPRA l'immagine sorgente (si muovono e si ingrandiscono con lei), es. lo
#   scontrino. {"testo", "font", "size", "colore" (ink/amber/grey), "xy" (centro, coordinate sorgente),
#   "parola" (da quando si vedono; None = sempre)} oppure {"linea": (x0, y0, x1, y1), "parola"}.
#
# SUBS: un sottotitolo per riga. Ogni parola mostrata = UNA parola parlata, in ordine. *...* = ambra.
#   "_" = spazio che non separa (es. "1,29_€"); "{n}" alla fine di una parola = copre n parole parlate
#   (es. "*1,29_€*{3}" per "uno e ventinove").
#
# OCCHIALI: per ogni immagine, box degli occhiali e del volto (x0, y0, x1, y1) in pixel della sorgente
#   1080x1920, misurati a mano su una griglia e controllati disegnandoli. montage.py verifica per ogni
#   inquadratura (inizio, meta', fine) che il volto sia tutto in campo, che gli occhiali siano fuori dalla
#   fascia destra e che nessun titolo, sottotitolo, fumetto o scritta li copra.
#
# EFFETTI: (effetto, parola). Solo sui numeri (A8): scontrino sul "470", tick leggeri sugli altri numeri.

OCCHIALI = {
    "01": {"occhiali": (280, 430, 710, 610), "volto": (240, 290, 770, 800)},
    "02": {"occhiali": (620, 680, 840, 790), "volto": (610, 585, 965, 910)},
    "03": {"occhiali": (230, 560, 700, 735), "volto": (180, 370, 760, 920)},
    "04": {"occhiali": (715, 925, 950, 1025), "volto": (700, 860, 975, 1100)},
    "05": {"occhiali": (170, 455, 600, 630), "volto": (110, 270, 620, 790)},
    "06": {"occhiali": (265, 640, 610, 775), "volto": (230, 520, 665, 880)},
    "07": {"occhiali": (725, 1030, 975, 1140), "volto": (700, 930, 1010, 1220)},
    "08": {"occhiali": (190, 575, 590, 730), "volto": (130, 440, 660, 900)},
    "09": {"occhiali": (250, 560, 510, 725), "volto": (80, 420, 560, 900)},
}

TITLES = {
    "hook": [{"runs": [("470", "mono", 250, "accent"), (" ", "mono", 110, "accent"), ("€", "cond", 236, "accent")],
              "parola": "quattrocentosettanta"},
             {"runs": [("ALL'ANNO", "cond", 104, "base")], "parola": "all'anno"}],
    "loop": [[("?", "mono", 250, "accent")]],
    "piccole": [[("PICCOLE ", "cond", 120, "accent"), ("SPESE", "cond", 120, "base")]],
    "uno": [[("1", "mono", 120, "accent"), (" · ABBONAMENTI", "cond", 104, "base")]],
    "due": [[("2", "mono", 120, "accent"), (" · LISTA DELLA SPESA", "cond", 104, "base")]],
    "tre": [[("3", "mono", 120, "accent"), (" · LUCE E GAS", "cond", 104, "base")]],
    "fine": [[("BASTA GUARDARE LE", "cond", 92, "base")],
             {"runs": [("PICCOLE SPESE", "cond", 124, "accent")], "parola": "piccole"}],
}

# scontrino dell'immagine 09 (interno bianco: x 680-1030, y 600-1290)
SCRITTE = {
    "09": [
        {"testo": "1,29 €", "font": "mono", "size": 70, "colore": "ink", "xy": (845, 760), "parola": "uno"},
        {"testo": "× 365", "font": "mono", "size": 70, "colore": "ink", "xy": (845, 870),
         "parola": "trecentosessantacinque"},
        {"linea": (705, 945, 985, 945), "parola": "quattrocentosettantuno"},
        {"testo": "= 471 €", "font": "mono", "size": 70, "colore": "ink", "xy": (845, 1025),
         "parola": "quattrocentosettantuno"},
        {"testo": "Fonte: Assoutenti", "font": "mono", "size": 30, "colore": "grey", "xy": (845, 1222),
         "parola": "Assoutenti"},
        {"testo": "(dati MIMIT)", "font": "mono", "size": 28, "colore": "grey", "xy": (845, 1264),
         "parola": "Assoutenti"},
    ],
}

SHOTS = [
    # 0:00 hook su inchiostro: orso intero (I-1), poi due avvicinamenti (I-2: mai oltre 120%, volto intero)
    {"img": "01", "parola": 0, "view": (515, 760, 0.70), "title": "hook"},
    {"img": "01", "parola": "spendi", "view": (515, 690, 0.90), "title": "hook"},
    # "e non te ne accorgi": primo piano sul volto (115%), il numero sparisce (e non c'e' titolo fino ai consigli
    # sul "Ma perche'?", T-2); con il titolo il primo piano avrebbe messo "ALL'ANNO" sulle orecchie
    {"img": "01", "parola": "e", "view": (505, 690, 1.15), "title": None},
    # "Ma perche'?": carta, nessun titolo (T-2), unica transizione (M-2)
    {"img": "02", "parola": "Ma", "view": (700, 960, 1.0), "title": None, "transizione": "tenda"},
    # numero e fonte: scontrino 09, alternando largo e primo piano sullo scontrino con l'orso in campo (M-1, I-4, T-3)
    {"img": "09", "parola": "Per", "view": (560, 1010, 0.80), "title": None},
    {"img": "09", "parola": "uno", "view": (606, 900, 0.97), "title": None},
    {"img": "09", "parola": "Moltiplicato", "view": (565, 990, 0.88), "title": None},
    {"img": "09", "parola": "quattrocentosettantuno", "view": (610, 870, 0.97), "title": None},
    # piccole spese
    {"img": "03", "parola": "Sono", "view": (500, 1000, 0.86), "title": "piccole"},
    {"img": "04", "parola": "E", "view": (560, 1100, 0.92), "title": "piccole"},
    {"img": "04", "parola": "non", "view": (700, 1060, 1.08), "title": "piccole", "zoom_max": 1.15},
    # tre consigli: titolo sopra la testa (T-4)
    {"img": "05", "parola": "Primo", "view": (450, 1070, 0.75), "title": "uno"},
    {"img": "05", "parola": "abbonamenti", "view": (470, 880, 1.0), "title": "uno"},
    {"img": "06", "parola": "Secondo", "view": (500, 1080, 1.0), "title": "due"},
    {"img": "06", "parola": "prima", "view": (455, 1040, 1.12), "title": "due"},
    {"img": "07", "parola": "Terzo", "view": (590, 1150, 0.95), "title": "tre"},
    {"img": "07", "parola": "offerte", "view": (700, 1160, 1.12), "title": "tre"},
    {"img": "07", "parola": "una", "view": (640, 1170, 1.0), "title": "tre"},
    # chiusura su inchiostro: volto + salvadanaio (I-7), frase finale, domanda con fumetto
    {"img": "08", "parola": "Non", "view": (565, 1080, 1.12), "title": None},
    {"img": "08", "parola": "Basta", "view": (560, 990, 0.85), "title": "fine", "moto": "out"},
    {"img": "08", "parola": "E", "view": (560, 1010, 0.92), "title": None, "bubble": (600, 300, 520, 470), "bubble_parola": "qual"},
    # ultimo mezzo secondo: stessa composizione del primo fotogramma con "?" al posto di "470 €" (I-8)
    {"img": "01", "dopo": "mai?", "view": (515, 760, 0.70), "title": "loop", "moto": "fermo"},
]

SUBS = [
    "SE TI BEVI", "UN CAFFÈ AL BAR", "OGNI GIORNO,", "SPENDI CIRCA", "*470 EURO*", "ALL'ANNO",
    "E *NON TE NE ACCORGI*.", "MA *PERCHÉ?*",
    "PER *ASSOUTENTI*", "UN ESPRESSO COSTA", "IN MEDIA *1,29_€*{3}.",
    "MOLTIPLICATO PER", "*365* GIORNI:", "*471 EURO*.",
    "SONO *PICCOLE SPESE*.", "E LE PICCOLE SPESE", "NON LE GUARDIAMO *MAI*.",
    "*PRIMO*:", "CONTROLLA GLI", "*ABBONAMENTI*", "CHE NON USI.",
    "*SECONDO*:", "FAI LA *LISTA*", "PRIMA DI ANDARE", "AL *SUPERMERCATO*.",
    "*TERZO*:", "CONFRONTA LE *OFFERTE*", "DI *LUCE E GAS*", "UNA VOLTA ALL'ANNO.",
    "NON SERVE", "*CAMBIARE VITA*.", "BASTA GUARDARE", "LE *PICCOLE SPESE*.",
    "E TU: QUAL È QUELLA CHE NON GUARDI *MAI?*",
]

EFFETTI = [
    ("scontrino", "quattrocentosettanta"),
    ("tick", "uno"), ("tick", "trecentosessantacinque"), ("tick", "quattrocentosettantuno"),
    ("pop", "Primo"), ("pop", "Secondo"), ("pop", "Terzo"),
]
