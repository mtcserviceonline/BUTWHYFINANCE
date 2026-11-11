# Poster A3 per Vinted

Set di 5 poster A3 (297 × 420 mm) con scritte grandi e tondeggianti e colori vividi.

## Contenuti

- `stampa/` — PDF A3 vettoriali, font incorporati. Questi sono i file da stampare.
- `vinted/<poster>/design.jpg` — immagine pulita del poster (1754 × 2481 px, 150 dpi).
- `vinted/<poster>/mockup-bianca.jpg`, `mockup-antracite.jpg` — poster incorniciato su parete.
- `vinted/set/mockup-bianca.jpg`, `mockup-beige.jpg`, `mockup-antracite.jpg` — set di 5 poster.
- `fonts/` — font usati (Titan One, Chango, Pacifico, Righteous) con le licenze SIL OFL 1.1.
- `script/make_posters.py` — genera tutto da zero. Per rigenerare, dalla radice del repo:

```bash
python3 poster/script/make_posters.py
```

Richiede `reportlab`, `Pillow` e `pdftoppm` (poppler-utils).

## Poster

| File | Frase | Font | Palette |
|---|---|---|---|
| 01-non-decidere | Oggi decido di non decidere. | Titan One | giallo, blu cobalto, rosa |
| 02-caffe-prima | Caffè prima, poi si vede. | Chango | rosso, crema, giallo |
| 03-modalita-aereo | Modalità aereo, anche di domenica. | Righteous | azzurro, blu notte, bianco |
| 04-cinque-minuti | Ancora 5 minuti (sono 40). | Pacifico | menta, verde scuro, arancio |
| 05-talento-rimandare | Il mio talento? Rimandare. | Titan One | viola, lime, rosa |

Le frasi sono scritte da zero per questo set. Prima di pubblicare, controllale rispetto al catalogo già in uso per evitare doppioni.

## Stampa

- Stampa il PDF a **dimensione reale A3**, senza "adatta alla pagina" né ridimensionamenti.
- Usa carta opaca e, se possibile, stampa fotografica a getto d'inchiostro.
- I colori su carta sono sempre più spenti che sullo schermo: fai una prova di stampa di almeno un poster prima di metterlo in vendita.

## Annuncio Vinted

- I mockup sono immagini digitali. Nel testo dell'annuncio scrivi che il poster è **venduto non incorniciato** e che la cornice nelle foto è solo illustrativa.
- Le foto dell'annuncio sono `design.jpg` e i mockup; non usare file scaricati da altri siti.

## Regole di contenuto

- Frasi e soggetti originali: niente versi di canzoni, titoli o copertine di riviste, loghi, scene di film.
- Vinted ammette la vendita occasionale di oggetti fatti da sé, non la produzione in serie. Per una vendita continuativa valuta Etsy o un negozio online. Vinted Pro richiede un'attività registrata (in Italia, partita IVA): chiedi conferma all'assistenza Vinted e a un commercialista.

## Dittico "buco nero"

Due poster A3 complementari in bianco e nero: affiancati ricompongono un buco nero intero. L'immagine è calcolata da zero da `script/make_dittico.py` (nessuna immagine di partenza), a 300 dpi.

- `stampa/dittico-buco-nero-sinistra.pdf`, `stampa/dittico-buco-nero-destra.pdf` — file di stampa A3.
- `vinted/dittico-buco-nero/` — immagini pulite (singole e insieme) e mockup su tre pareti.

Per rigenerare (circa 10 minuti): `python3 poster/script/make_dittico.py`. Anteprima veloce: aggiungi `40`.
