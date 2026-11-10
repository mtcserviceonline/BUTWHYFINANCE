# Affittare a 800 € rende più che a 1.000 €? — fotogrammi iniziali

Primo fotogramma di ognuna delle 6 scene del reel (canone concordato under 35, tassa all'1%).

| File | Scena | Cosa mostra |
|---|---|---|
| `fotogrammi/01.png` | 1 · Il paradosso | Via italiana: orso con la chiave davanti a due case identiche, espressione curiosa |
| `fotogrammi/02.png` | 2 · La proposta | Ufficio: orso con i due cartellini del prezzo, si gira verso il grande foglio attaccato al muro col nastro; tavolino con tre timbri di misura decrescente |
| `fotogrammi/03.png` | 3 · I conti del proprietario | Ufficio: orso alla scrivania, sopra due scontrini arrotolati e la lente |
| `fotogrammi/04.png` | 4 · Chi ci guadagna | Ufficio: orso seduto con gli scontrini srotolati e un mucchio di monete d'oro da impilare |
| `fotogrammi/05.png` | 5 · Chi paga | Piazza: orso accanto a due pile di monete (alta e bassa), serio, si gira verso l'edificio pubblico con le colonne; portafoglio chiuso a terra |
| `fotogrammi/06.png` | 6 · La domanda | Piazza: orso dietro un tavolino con due cartoncini bianchi, guarda in camera |

Ogni primo fotogramma riprende la fine della scena precedente, così le scene si legano.

## Stile

Fumetto/cartoon: contorni neri netti, colori pieni con ombre semplici, sfondi semi-realistici disegnati nello stesso stile, luce calda di giorno. È lo stile indicato dall'utente con due immagini di esempio (`script/stile/stile-1.png`, `stile-2.png`), usate **solo** come riferimento di stile. Sostituisce lo stile "paper-collage" del copione: gli oggetti "paper" del copione sono diventati oggetti normali.

## Come sono fatti

- API Meta `muse-image-1.0`, `POST /v1/images/edits` con tre riferimenti: `image[0]` = `brand/mascotte/mascotte-principale.jpg`, `image[1]`/`image[2]` = i due esempi di stile. `size=1024x1792` → 1152x2016 (9:16).
- Prompt = istruzioni sui riferimenti + stile + orso + scena + "no text". Testi completi in `script/prompts.json` (da `script/make_prompts.py`); `script/gen.py OUT PROMPT SIZE REF...` genera un'immagine.
- Con 6 richieste in parallelo l'API dà spesso `502 upstream request failed`: meglio 2 alla volta.

## Note

- € gialla, come la mascotte ufficiale (il vecchio STILE del copione diceva "white euro sign").
- Scontrini e documenti hanno solo righe grigie illeggibili, nessuna scritta né numero.
- Scena 3: l'orso è già seduto (il copione parte da "sits at a paper desk", va bene).
- Scena 5: la pila piccola di monete è molto bassa, vicino a quella alta sul tavolino.
- Su TikTok/Instagram va attivata l'etichetta "contenuto generato con IA".
