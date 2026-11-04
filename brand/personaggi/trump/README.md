# Personaggio: caricatura di Donald Trump

Caricatura cartoon di Donald Trump da usare nei contenuti di But Why Finance quando si parla di temi legati a lui (dazi, dollaro, politica economica USA). Stesso stile grafico dell'orso: contorno nero spesso, colori piatti.

## File di riferimento

| File | Contenuto |
|---|---|
| [`principale.jpg`](principale.jpg) | Figura intera, posa di riferimento (immagine di partenza) |
| [`turnaround.jpg`](turnaround.jpg) | Model sheet: fronte, profilo, tre quarti, retro |
| [`espressioni.jpg`](espressioni.jpg) | Sei espressioni a mezzo busto: ride, sorpreso, pensieroso, arrabbiato, spiega (indice alzato), occhiolino con pollice in su |
| [`posa-annuncio.jpg`](posa-annuncio.jpg) | Dietro un leggio, mani alzate: "grande annuncio" |
| [`posa-indica.jpg`](posa-indica.jpg) | Indica di lato uno spazio vuoto (per un grafico o un numero aggiunto in montaggio) |
| [`posa-firma.jpg`](posa-firma.jpg) | Seduto alla scrivania, mostra un foglio firmato (decreti, accordi) |
| [`posa-moneta.jpg`](posa-moneta.jpg) | Guarda sorpreso una grande moneta d'oro |

## Aspetto
- Uomo basso e tozzo, testa grande e rotonda.
- Capelli biondo dorato voluminosi, pettinati all'indietro con un ricciolo davanti.
- Pelle pesca-arancio chiaro, sopracciglia folte e chiare, occhi piccoli.
- Abito blu scuro, camicia bianca, cravatta rossa lunga, spilla con bandiera USA sul bavero sinistro, scarpe nere.

## Come generarlo
Script in `script/`: `make_prompts.py` scrive i prompt, `gen.py` chiama l'API Meta (`/v1/images/edits`) passando `principale.jpg` come riferimento. Per nuove pose allegare `principale.jpg` (ed eventualmente `turnaround.jpg` o `espressioni.jpg`).

Il filtro dei contenuti di Meta ha bloccato una posa con una banconota in mano: con una moneta d'oro generica è passata.

## Regole d'uso
- È una persona reale: usarlo solo in chiave di commento o satira, chiaramente da cartone animato.
- Non fargli dire frasi che sembrino citazioni vere: le sue parole in un video vanno prese da fonti verificabili, oppure il testo deve far capire che è una battuta.
- Niente scene degradanti o che possano sembrare fatti reali.
- Su TikTok attivare l'etichetta "contenuto generato da IA".
