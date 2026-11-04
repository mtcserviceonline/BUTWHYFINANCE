# Personaggio: uomo con barba e occhiali

Personaggio cartoon nello stesso stile dell'orso (contorno nero spesso, colori piatti), creato a partire da `principale.jpg`.

## File di riferimento

| File | Contenuto |
|---|---|
| [`principale.jpg`](principale.jpg) | Figura intera, posa di riferimento (immagine di partenza) |
| [`turnaround.jpg`](turnaround.jpg) | Model sheet: fronte, profilo destro, profilo, retro |
| [`tre-quarti.jpg`](tre-quarti.jpg) | Vista di tre quarti, figura intera (nel model sheet il modello la disegnava sempre di profilo) |
| [`espressioni.jpg`](espressioni.jpg) | Sei espressioni a mezzo busto: ride, sorpreso, pensieroso, arrabbiato, spiega (indice alzato), occhiolino con pollice in su |
| [`posa-annuncio.jpg`](posa-annuncio.jpg) | Dietro un leggio, mani alzate |
| [`posa-indica.jpg`](posa-indica.jpg) | Indica di lato uno spazio vuoto (per un grafico o un numero aggiunto in montaggio) |
| [`posa-firma.jpg`](posa-firma.jpg) | Alla scrivania, mostra un foglio firmato |
| [`posa-moneta.jpg`](posa-moneta.jpg) | Guarda sorpreso una grande moneta d'oro |

## Aspetto
- Uomo basso e tozzo, testa grande.
- Capelli castano scuro mossi fino alle spalle, riga in mezzo.
- Barba piena e baffi castano scuro, curati.
- Occhiali rettangolari con montatura nera spessa.
- Pelle pesca-ambrata, occhi piccoli, sorriso gentile.
- Giacca e pantaloni blu scuro, camicia bianca con il collo aperto e senza cravatta, scarpe nere.

## Come generarlo
Script in `script/`: `make_prompts.py` scrive i prompt, `gen.py` chiama l'API Meta (`/v1/images/edits`) passando `principale.jpg` come riferimento. Per nuove pose allegare `principale.jpg` (ed eventualmente `turnaround.jpg` o `espressioni.jpg`).

Se il personaggio ritrae una persona reale, serve il suo consenso per usarlo nei contenuti. Su TikTok attivare l'etichetta "contenuto generato da IA".
