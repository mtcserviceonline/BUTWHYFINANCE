# 3 perché sui soldi che vedi ogni giorno — immagini TikTok

Immagini per il copione [`../../copioni/2026-11-03-tre-perche-soldi-quiz-tiktok.md`](../../copioni/2026-11-03-tre-perche-soldi-quiz-tiktok.md) (rubrica "Curiosità Economiche", quiz in 3 domande).

## File

| File | Contenuto |
|---|---|
| `immagini/01.png` … `15.png` | Le 15 illustrazioni, 1152x2016 (circa 9:16), senza testi |
| `audio/voce-originale.mp3` | Voce ElevenLabs ("Valerio") con il testo modificato, 57,5 s |
| `audio/voce-con-pause.mp3` | La stessa voce con 3 s di silenzio dopo ogni domanda (a 8,25 · 24,55 · 40,95 s), 67,7 s: è quella da usare nel montaggio |
| `prompt-montaggio.md` | Prompt per il montaggio: scene con tempi, opzioni delle domande, conto alla rovescia, regole |
| `script/make_prompts.py` | Scrive i prompt in inglese (`script/prompts.json`) |
| `script/gen.py` | Chiama l'API Meta `muse-image-1.0` (vedi il README del video sul caffè) |

Tutte le immagini contengono l'orso e sono state generate con `/v1/images/edits` passando `brand/mascotte/mascotte-principale.jpg` come riferimento, `size=1024x1792`.

## Immagini

| Img | Scena (tempo) | Sfondo | Contenuto |
|---|---|---|---|
| 01 | Hook (0:00) | giallo `#FFD23F` | Orso che fa il giocoliere con tre punti di domanda |
| 02 | Domanda 1 (0:03) | blu `#3A86FF` | Orso indica un cartellino del prezzo bianco appeso allo scaffale |
| 03 | RISPONDI! (0:06) | rosa `#FF4FA3` | Orso con cronometro in mano e zampa all'orecchio |
| 04 | Risposta 1 (0:08) | menta `#7CE0B5` | Cervello con lente sul lato sinistro, orso stupito |
| 05 | 9,99 (0:11) | arancio `#FF9F1C` | Orso che taglia a metà un cartellino con le forbici |
| 06 | Domanda 2 (0:14) | limone `#FFF05A` | Corsia del supermercato, latte e pane in fondo |
| 07 | RISPONDI! (0:17) | corallo `#FF6B6B` | Orso pensieroso, fumetto con latte e pane |
| 08 | Risposta 2 (0:19) | azzurro `#5BC0EB` | Cestino con latte e pane, calendario pieno di spunte |
| 09 | Attraversi tutto (0:22) | turchese `#2EC4B6` | Orso col carrello in una corsia lunghissima |
| 10 | Carrello pieno (0:25) | viola `#9B5DE5` | Carrello stracolmo, lista della spesa, orso colpevole |
| 11 | Domanda 3 (0:28) | pesca `#FFB997` | Orso detective con lente su una banconota viola |
| 12 | RISPONDI! (0:31) | rosa `#FF4FA3` | Orso a braccia conserte, cronometro accanto |
| 13 | 2016 BCE (0:33) | verde `#80ED99` | Pile di mazzette viola, valigetta piccola, edificio con colonne |
| 14 | Ancora valida (0:37) | giallo `#FFD23F` | Orso paga con la banconota a un cassiere (sagoma grigia), spunta verde |
| 15 | Chiusura (0:41) | blu `#3A86FF` | Orso con quattro carte: 0, 1, 2, 3 punti |

Sfondi a colore vivo come chiede il copione (nessun nero); 01/15 e 03/12 hanno lo stesso colore per richiamarsi.

## Note

- Nel copione l'orso ha "a white euro sign": nei prompt è stato usato il **€ giallo** della scheda `brand/mascotte/README.md`.
- 03, 06 e 15 sono state rigenerate: nella prima versione l'orso della 03 era tagliato a metà, in fondo alla corsia della 06 latte e pane non si vedevano e le carte della 15 avevano 0-1-3-4 punti invece di 0-1-2-3. I prompt in `make_prompts.py` sono quelli corretti.
- Nessun testo nelle immagini: cifre (9,99 €, 500 €, 2016, 2019), "RISPONDI!", il conto alla rovescia e il numero di domanda vanno aggiunti in montaggio.
- La banconota è viola ma senza cifre né disegni della vera banconota da 500 €.
- Immagini generate con IA: attivare l'etichetta TikTok.
