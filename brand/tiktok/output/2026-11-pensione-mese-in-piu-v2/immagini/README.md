# Immagini: In 60 secondi · Pensione a 67 anni e un mese: cosa puoi fare (video TikTok)

Le 8 illustrazioni del video, una per idea, nell'ordine del production doc di `../copione.md`. Senza testi: «67 ANNI + 1 MESE», i titoli dei consigli, l'avvertenza, i sottotitoli e il fumetto "But Why Finance?" si aggiungono in montaggio.

![Anteprima delle 8 immagini](anteprima.jpg)

| File | Contenuto |
|---|---|
| `01.png` … `08.png` | Immagini finali, PNG 1080x1920 (9:16) |
| `scene.json` | Scene in inglese (ingresso di `componi_prompt.py`), versione finale |
| `prompts.json` | Prompt finale di ogni immagine, con fondo e riferimenti |
| `anteprima.jpg` | Contact sheet (4 colonne) |

La copertina (`../copertina.png`) non è un'immagine generata: è composta da `../script/copertina.py` con l'immagine 01 e IBM Plex Sans Condensed / Mono Bold.

**Tutte nuove (30/10/2026).** Le 8 immagini della versione "Vero o falso?" erano viola, con oggetti viola (timbro, ingranaggi, cubi, bilancia) pensati per un verdetto che non c'è più: nessuna è stata tenuta. Le idee del calendario (02) e del sentiero con la sedia a dondolo spostata (03) vengono da lì, rigenerate in fucsia.

## Le 8 immagini

| # | Voce | Fondo | Oggetto / scena | Orso | Tentativo usato |
|---|---|---|---|---|---|
| 01 | «Sessantasette anni e un mese.» · «Ma perché?» | inchiostro | sedia a dondolo fucsia che si allontana verso destra (linee di movimento bianche) | sorpreso, zampe aperte | 1° |
| 02 | «Dal duemilaventisette, per quasi tutti, … più in là» | carta | calendario a strappo grigio, pagine bianche, una pagina fucsia nuova in cima (il mese in più), sospeso | spiega, indice alzato | 2° |
| 03 | «Si vive più a lungo: l'età sale con la speranza di vita» | carta | sentiero in salita, sagoma grigia anziana con bastone, sedia fucsia spostata più in là (sagoma tratteggiata + freccia fucsia) | pensieroso, mano al mento | 1° |
| 04 | «Cosa puoi fare? Primo: … estratto conto Inps» | carta | foglio bianco con righe grigie astratte tenuto in alto, lente d'ingrandimento fucsia | legge, sorriso | 2° |
| 05 | «Secondo: … simulatore gratuito dell'Inps» | carta | smartphone alzato con grafico astratto fucsia che sale e barre grigie, nessun numero | contento | 2° |
| 06 | «Terzo: valuta un fondo pensione …» | carta | salvadanaio grigio, moneta fucsia che entra, tre pile di monete fucsia che crescono | spiega, indice alzato | 1° |
| 07 | «Prima inizi, meglio è» | carta | clessidra con telaio grigio e sabbia fucsia appena iniziata a scendere | spiega, indice verso la clessidra | 1° |
| 08 | «E tu, ci stai già pensando?» | inchiostro | la stessa sedia a dondolo fucsia, ferma, accanto all'orso | **occhiolino** (lente fumé), saluta | 1° |

Unico accento fucsia (`#B0186E`, rubrica In 60 secondi), nessun rosso, nessun blu, nessun verde oltre alla maglietta, nessuna scritta/lettera/numero (foglio a righe astratte, schermo con grafico senza assi né cifre, monete lisce). Inchiostro solo su 01 e 08 (loop: stesso set, la sedia che scappa → la sedia ferma).

## Come sono state generate

API Meta `POST /v1/images/edits`, `muse-image-1.0`, `size=1024x1792`, riferimento `brand/mascotte/mascotte-principale.jpg` (`image[0]`) + `brand/mascotte/espressioni.jpg` (`image[1]`) per l'occhiolino della 08; WebP 1152x2016 → 1134x2016 → 1080x1920. Script: `.claude/skills/crea-post-tiktok/scripts/` (`componi_prompt.py` → `genera_immagine.py` → `controlla_immagini.py` → `anteprima.py`).

**11 immagini generate** (8 prime prove + 3 seconde), nessuna richiesta fallita, nessun 5xx, nessun blocco del filtro. Le prove scartate sono nello scratchpad, non nel repository.

| Img | Problema della 1ª prova | Correzione (2ª, usata) |
|---|---|---|
| 02 | calendario appeso a un chiodo fino all'8,6% in alto (fascia del titolo), orso fino al 93,5% | calendario più piccolo, "floating", fra il 27% e il 47%; orso più piccolo: contenuto 21,1%-84,7% |
| 04 | foglio e lente tagliati dal bordo destro, orso grande fino al 93% | foglio tenuto con una zampa sola, lente entro l'80%: lente intera; l'orso resta fino all'88% |
| 05 | orso grande (~45% dell'altezza), piedi all'88% | orso piccolo e telefono medio: contenuto 20,7%-81,2% |

## Controlli fatti

Ogni immagine guardata intera con Read (anche le prove scartate) e ingrandita su volto, foglio e schermo: nessuna scritta, cifra o segno; occhiali tondi neri con riflesso bianco in tutte; € gialla al centro del petto e scoperta in tutte; sagoma grigia senza volto né vestiti (03); niente rosso. Box di occhiali, volto ed € misurati su una griglia di 50 px e disegnati per controllo (in `../script/config_video.py`). Misure di `controlla_immagini.py` sulle immagini finali:

| # | Dimensioni | Fondo misurato | Contenuto da… a… (altezza) | Destra fino a | Avvisi |
|---|---|---|---|---|---|
| 01 | 1080x1920 | `#0E1218` (inchiostro) | 38,6% – 77,1% | 99,0% | contenuto nel 10% a destra |
| 02 | 1080x1920 | `#F4F1E9` (carta) | 21,1% – 84,7% | 96,9% | contenuto nel 10% a destra |
| 03 | 1080x1920 | `#F4F1E9` (carta) | 28,8% – 74,6% | 100,0% | contenuto nel 10% a destra |
| 04 | 1080x1920 | `#F4F1EB` (carta) | 20,4% – 88,4% | 98,9% | contenuto nel 15% in basso; contenuto nel 10% a destra |
| 05 | 1080x1920 | `#F4F1E9` (carta) | 20,7% – 81,2% | 94,0% | contenuto nel 10% a destra |
| 06 | 1080x1920 | `#F4F1EA` (carta) | 29,7% – 100,0% | 100,0% | contenuto nel 15% in basso; contenuto nel 10% a destra |
| 07 | 1080x1920 | `#F4F1E9` (carta) | 19,7% – 83,8% | 98,3% | contenuto nel 10% a destra |
| 08 | 1080x1920 | `#0E1218` (inchiostro) | 40,4% – 85,1% | 98,1% | contenuto nel 15% in basso; contenuto nel 10% a destra |

## Difetti noti

- **06, "contenuto fino al 100%" in basso:** misura falsata; righe da y 1500 a 1920 controllate pixel per pixel: solo fondo carta. Nel 06 la pila di monete più alta arriva al bordo destro (zona pulsanti): niente di importante lì.
- **Fascia destra (tutte):** la sedia (01, 03, 08), il calendario (02), la lente (04), il salvadanaio (06) e la clessidra (07) arrivano al 94-100% della larghezza. Nessun elemento chiave (occhiali, €, volto) è in quella fascia; il montaggio controlla gli occhiali a ogni inquadratura.
- **Fascia bassa (04, 08):** i piedi dell'orso arrivano all'88% (04) e all'85% (08): in montaggio i sottotitoli passano sulle gambe, mai su € e occhiali (verificato con le coordinate).
- **02:** l'orso tocca quasi il bordo sinistro (~2%); nelle viste del montaggio (85-95%) resta in campo.
- **03:** il sentiero tocca i bordi sinistro e destro dell'immagine: le viste del montaggio sono ≥ 92% e centrate (si vede il taglio solo a zoom molto più piccoli).

**Coerenza dell'orso:** stessa pelliccia ramata, muso pesca, occhiali tondi con riflesso diagonale, maglietta verde con € gialla in tutte e 8; proporzioni coerenti con `mascotte-principale.jpg`.

**Su TikTok va attivata l'etichetta "contenuto generato da IA".**
