# Risparmio quotidiano ("Il prezzo di… un caffè al giorno") — video TikTok

Realizzazione del copione [`../../copioni/2026-10-risparmio-quotidiano.md`](../../copioni/2026-10-risparmio-quotidiano.md).

Ci sono **due versioni** del video, da mettere a confronto (P-6):

- **v2** (`video.mp4`, 33,7 s): testo nuovo con la fonte Assoutenti, il conto sullo scontrino e la domanda finale, montaggio rifatto con tutte le correzioni dell'utente (28/10/2026).
- **v1** (`video_v1_24s.mp4`, 24,3 s): la prima versione, conservata per l'A/B test.

## Stato

| Cosa | Stato |
|---|---|
| Testo v2, scene ElevenLabs | pronti (`script/elevenlabs.txt`, `script/scene_elevenlabs.json`) |
| Voce v2 | **registrata** dall'utente su ElevenLabs ("Valerio – Warm Italian Storyteller"), `voce.mp3` (35,6 s grezza) |
| Video v2 | **montato** (`video.mp4`, 33,74 s, 1080x1920, 30 fps, H.264 + AAC 48 kHz), -14,7 LUFS, true peak -1,5 dBFS |
| Copertina | `copertina.png` (P-2) |
| Didascalia | `didascalia.md` (P-3 e P-4 alla lettera) |
| Fonte del 1,29 € | concordante su più testate; **comunicato originale da aprire a cura dell'utente** (vedi sotto) |
| Da fare | ascoltare il video (io non posso), aprire la fonte originale, checklist di pubblicazione qui sotto |

## Checklist di pubblicazione

- [ ] **P-1 / A7 Etichetta IA:** su TikTok attivare "Contenuto generato dall'IA" (immagini generate, voce sintetica).
- [ ] **P-2 Copertina:** caricare `copertina.png` (fondo inchiostro, orso intero sorpreso, "470 €" in ambra e "ALL'ANNO"; tutto tra y=260 e y=1650, quindi visibile anche nel ritaglio 3:4 della griglia del profilo).
- [ ] **P-3 Didascalia:** il testo esatto in `didascalia.md` ("Se ti bevi un caffè al bar ogni giorno, spendi circa 470 euro all'anno. Per Assoutenti l'espresso costa in media 1,29 euro. Qual è la piccola spesa che non guardi mai? 👇").
- [ ] **P-4 Hashtag:** `#caffè #prezzi #risparmio #finanzapersonale`.
- [ ] **P-5 Assoutenti nominata** a voce (0:07,4 "Per Assoutenti…"), a schermo ("Fonte: Assoutenti (dati MIMIT)" sullo scontrino, 7,5-14,8 s) e in didascalia: fatto nel video e nella didascalia.
- [ ] **Fonte:** aprire il comunicato originale Assoutenti/CRC (18/08/2026) e confermare 1,29 €. Se è diverso: correggere testo, rifare la voce e rilanciare `monta.sh`.
- [ ] **A8 Musica:** nessuna base nel file (vedi "Musica"). Se si vuole, aggiungerla in app.
- [ ] **P-6 A/B test:** (1) v1 da 24 s contro v2 da 33,7 s; (2) finale con domanda (v2) contro taglio netto sull'ultima frase. Per la variante (2) basta rimontare la v2 fermandola dopo "Basta guardare le piccole spese." (vedi "Varianti per l'A/B test").
- [ ] Ascoltare il video almeno una volta: voce, pause accorciate, effetti (vedi "Limiti").

## Verifica della fonte (prima di registrare)

- **Dato:** espresso al bar **1,29 € in media**, studio del *Centro di formazione e ricerca sui consumi (CRC) con Assoutenti*, 18 agosto 2026, su dati del Ministero delle Imprese e del Made in Italy (MIMIT).
- **Dove:** [Teleborsa, 18/08/2026](https://www.teleborsa.it/News/2026/08/18/prezzi_caffe_al_bar_%2b_24_2percento_in_cinque_anni-115.html) e ANSA ripresa da [il NordEst](https://www.ilnordest.it/italia-ed-esteri/e-caro-tazzina-espresso-in-media-a-1-29-euro-24-5-sul-2025-e7o8qk6d). Le due fonti concordano su 1,29 €; sulla percentuale no (+24,2% sul 2021 in Teleborsa, "+24,5% sul 2025" nel titolo dell'altra): **la percentuale non si usa**.
- **Stato:** concordante su più testate, **comunicato originale da aprire a cura dell'utente** (assoutenti.it da questa sessione risponde 403 del proxy).
- **Conto:** 1,29 × 365 = 470,85 € → "circa quattrocentosettanta" nell'apertura e "quattrocentosettantuno" nel conto (arrotondamento), regge.
- **T-5 / M-6 (cifre accanto ai consigli, frase di colpo di scena):** **non applicati**. Per "abbonamenti non usati", "lista della spesa" e "confronto luce e gas una volta all'anno" non ho una cifra con fonte verificata, quindi i tre passi restano senza numero e non c'è la frase di colpo di scena prima dei consigli.

## Voce v2 e ritmo

Trascrizione di controllo (`muse-spark-1.3`, intero e a spezzoni): testo **quello nuovo**, nessun tag letto ad alta voce, nessuna parola aggiunta. Due punti da ascoltare: il "Se" iniziale è breve e debole (il trascrittore ha sentito "Ti bevi" / "Te ti bevi"; nell'audio c'è una sillaba a 0,12-0,22 s con la "s" iniziale) e "Assoutenti" è stato trascritto una volta "assurdo è" e una volta "assutenti".

| | Prima | Dopo |
|---|---|---|
| Durata | 35,63 s | 33,39 s (video 33,74 s) |
| Parole | 93 | 93 |
| Parole/min (prima → ultima parola) | 158 | **168** (A3: 165-175) |

- `script/ritmo.py`: le 10 pause tra frasi oltre 0,4 s portate a 0,30 s, la pausa prima di "Ma perché?" da 0,42 a **0,36 s** (A2), attacco da 0,12 a 0,05 s. Si tolgono solo pezzi di silenzio dal centro delle pause (dissolvenze di 10 ms; ai tagli il livello è sotto -85 dB, nessun clic). Nessuna parola tagliata.
- **Nessuna accelerazione:** dopo le pause la voce è già a 168 parole/min, dentro A3. Per arrivare a ~27 s servirebbero ~205 parole/min (1,24x, oltre il massimo di 1,12x e fuori da A3): con 93 parole il testo a 165-175 parole/min dura 32-34 s. `ritmo.py` accelera (rubberband di ffmpeg, formanti preservate) solo se dopo le pause si resta sotto 165 parole/min.
- A2 (voce che sale su "Ma perché?", enfasi su "non te ne accorgi"): dipende dalla registrazione, non verificabile senza ascolto.

## Musica (A8)

Nel video **non c'è musica**: non abbiamo una traccia con licenza commerciale e non si scarica musica dal web. Due strade:

1. **In app:** su TikTok, con account Business, scegliere un brano dalla **Libreria musicale commerciale** (Commercial Music Library) e abbassarne il volume al minimo utile (la voce deve restare chiaramente sopra; l'obiettivo è circa -20 dB).
2. **File con licenza fornito dall'utente:** rilanciare il montaggio con `MUSICA=percorso/base.mp3` (vedi "Come rifarlo"). `script/musica.py` misura voce e musica in LUFS, mette la musica **20 dB sotto la voce**, la ripete o taglia alla durata del video, con dissolvenze, e aggiunge un **ducking leggero** (compressore sidechain pilotato dalla voce, 3:1). Provato con un file di prova: guadagno calcolato e mix corretti.

## Montaggio v2

### Correzioni applicate

| Punto | Cosa è stato fatto |
|---|---|
| A1 | testo nuovo, 7 scene (`script/scene_elevenlabs.json`) |
| A4 | -14,7 LUFS integrati, true peak -1,5 dBFS misurati sul `video.mp4` finale (loudnorm a -14 LUFS con tetto -2 dBTP: con -1,5 dBTP, dopo l'AAC il picco risaliva a -1,1) |
| A5 | numeri per esteso nel testo per la voce; a schermo in cifre ("470 EURO", "1,29 €", "365", "471 EURO") |
| A6 | il video finisce **0,45 s** dopo l'ultima parola ("mai?" finisce a 33,29 s) |
| A8 | effetti solo sui numeri: "scontrino" (stampante + strappo) su "quattrocentosettanta", tre "tick" leggeri su "uno e ventinove", "trecentosessantacinque", "quattrocentosettantuno", tre "pop" leggeri su Primo/Secondo/Terzo. Tolti forbici, monete, monetine, carta, salvadanaio. Effetti nel complesso a -36 LUFS contro -19,5 della voce. Musica: vedi sopra |
| T-1 / M-5 | apertura senza titolo; **"470 €"** (IBM Plex Mono, ambra, gigante) entra con il colpo di scontrino all'inizio di "quattrocentosettanta" (2,58 s); **"ALL'ANNO"** entra su "all'anno" (4,12 s); in basso solo la riga parlata |
| T-2 | da "e non te ne accorgi" (4,95 s) fino ai consigli nessun titolo in alto: "Ma perché?" è solo nel sottotitolo |
| T-3 / I-4 | immagine nuova **09** (orso con scontrino vuoto); sullo scontrino, in Mono, compaiono "1,29 €" (su "uno"), "× 365" (su "trecentosessantacinque"), riga e "= 471 €" (su "quattrocentosettantuno"); "Fonte: Assoutenti (dati MIMIT)" dall'inizio della scena, sopra il 15% in basso |
| T-4 | "1 ·", "2 ·", "3 ·" sopra la testa dell'orso in tutte le inquadrature (vista scelta perché la testa stia sotto il titolo) |
| T-6 | domanda finale intera nel sottotitolo, su due righe, con **"MAI?"** in ambra; resta fino all'ultimo fotogramma |
| T-7 | sottotitoli ancorati in basso: bordo basso del testo (contorno compreso) ≤ y=1632 in tutti, controllato |
| I-1 | apertura: orso intero sorpreso (01 al 70%), occhiali ben visibili, fondo inchiostro |
| I-2 | avvicinamenti sull'01: 90% su "spendi", **115%** sul volto per "e non te ne accorgi"; volto sempre intero |
| I-5 | 04 al massimo al 108% (+4% di movimento = 112%), titolo sopra la scena |
| I-6 | 06: due inquadrature con l'orso intero e la lista (100% e 112%), titolo sopra la testa |
| I-7 | 08: volto e salvadanaio insieme (112%) |
| I-8 | ultimi 0,45 s: **stessa vista del primo fotogramma** (01 al 70%, ferma), con **"?"** al posto di "470 €" (centro del titolo identico: 504, 384) |
| I-9 / M-1 / M-2 | vedi "Controlli automatici". Un solo effetto di passaggio: la "tenda" da inchiostro a carta (0,2 s) su "Ma perché?" (6,42 s); il resto tagli netti |
| M-3 | fondo inchiostro in apertura e chiusura |

**Non applicati:** T-5 e M-6 (nessuna cifra verificata per i consigli, vedi sopra). Durata ~27 s (A1): vedi "Voce v2 e ritmo".

### Inquadrature (22 in 33,7 s, una ogni 1,53 s in media)

| # | Tempo (s) | Img | Vista (zoom) | Titolo | Voce |
|---|---|---|---|---|---|
| 1 | 0,00-1,99 | 01 | orso intero (70%) | — | Se ti bevi un caffè al bar ogni giorno, |
| 2 | 1,99-4,95 | 01 | 90% | **470 €** (2,58) + ALL'ANNO (4,12) | spendi circa quattrocentosettanta euro all'anno |
| 3 | 4,95-6,42 | 01 | volto 115% | — | e non te ne accorgi. |
| 4 | 6,42-7,31 | 02 | 100%, entra con la tenda | — | Ma perché? |
| 5 | 7,31-9,25 | 09 | larga (80%) | scontrino: Fonte | Per Assoutenti un espresso costa in media |
| 6 | 9,25-10,42 | 09 | scontrino + orso (97%) | scontrino: 1,29 € | uno e ventinove. |
| 7 | 10,42-13,14 | 09 | 88% | scontrino: × 365 (11,26) | Moltiplicato per trecentosessantacinque giorni: |
| 8 | 13,14-14,82 | 09 | scontrino + orso (97%) | scontrino: = 471 € | quattrocentosettantuno euro. |
| 9 | 14,82-16,16 | 03 | 86% | PICCOLE SPESE | Sono piccole spese. |
| 10 | 16,16-17,16 | 04 | 92% | PICCOLE SPESE | E le piccole spese |
| 11 | 17,16-18,25 | 04 | 108% | PICCOLE SPESE | non le guardiamo mai. |
| 12 | 18,25-19,47 | 05 | 75% | 1 · ABBONAMENTI | Primo: controlla gli |
| 13 | 19,47-20,86 | 05 | 100% | 1 · ABBONAMENTI | abbonamenti che non usi. |
| 14 | 20,86-22,28 | 06 | 100% | 2 · LISTA DELLA SPESA | Secondo: fai la lista |
| 15 | 22,28-24,09 | 06 | orso intero + lista (112%) | 2 · LISTA DELLA SPESA | prima di andare al supermercato. |
| 16 | 24,09-25,46 | 07 | 95% | 3 · LUCE E GAS | Terzo: confronta le |
| 17 | 25,46-26,74 | 07 | orso + fiammella (112%) | 3 · LUCE E GAS | offerte di luce e gas |
| 18 | 26,74-27,90 | 07 | 100% | 3 · LUCE E GAS | una volta all'anno. |
| 19 | 27,90-29,39 | 08 | volto + salvadanaio (112%) | — | Non serve cambiare vita. |
| 20 | 29,39-31,24 | 08 | 85%, zoom all'indietro | BASTA GUARDARE LE + PICCOLE SPESE (30,23) | Basta guardare le piccole spese. |
| 21 | 31,24-33,29 | 08 | 92% | fumetto "But Why Finance?" (31,96) | E tu: qual è quella che non guardi mai? |
| 22 | 33,29-33,74 | 01 | **come il fotogramma 0** | **?** | — (ultima parola finita) |

Tempi esatti, sottotitoli parola per parola, effetti, controlli e ritmo della voce in `tempi.json`.

### Controlli automatici (in `montage.py`, prima di ogni render)

Per ogni inquadratura, all'inizio, a metà e alla fine (lo zoom si muove):

- **volto dell'orso tutto in campo** e **occhiali** fuori dalla fascia destra di 120 px e mai coperti da titolo, sottotitoli, fumetto o scritte sullo scontrino (box di occhiali e volto per ogni immagine in `script/config_video.py` → `OCCHIALI`, misurati a mano e verificati disegnandoli; lo zoom lento cresce attorno agli occhiali, che quindi non si spostano);
- zoom effettivo ≤ 120% (≤ 115% dove indicato);
- testi nelle zone sicure: niente nel 10% in alto (y < 192), nel 15% in basso (y > 1632), nella fascia destra (x > 960);
- **cambio visivo al massimo ogni 2 s** (tagli, righe di titolo, scritte e fumetto che entrano): massimo misurato **1,99 s**;
- loop: ultima inquadratura uguale alla prima, titolo "?" centrato come "470 €".

Risultato sul video finale: **0 errori, 0 avvisi**. Con errori `monta.sh` si ferma (salvo `FORZA=1`).

### Controlli a occhio

- [`anteprima_layout_v2.jpg`](anteprima_layout_v2.jpg): 0,0 s, ogni taglio +0,12 s e l'ultimo fotogramma, con le fasce sicure (magenta) e il box degli occhiali (azzurro). [`anteprima_video.jpg`](anteprima_video.jpg): un fotogramma a metà di ogni inquadratura. Guardati tutti, più a piena risoluzione l'ingresso di "470 €", la tenda (6,45 / 6,52 / 6,58 s) e lo scontrino completo (14,3 s): conto leggibile, occhiali sempre visibili e liberi, nessun testo nelle fasce, "?" nella posizione di "470 €".

### Limiti noti

- **Non ho potuto ascoltare** voce, tagli delle pause ed effetti: controllati solo con misure.
- Tempi delle parole **stimati** dentro ogni frase (picchi di energia ≈ sillabe, errore atteso < 0,15 s): "470 €" entra all'inizio stimato di "quattrocentosettanta" (2,58 s), non al fotogramma garantito.
- Inquadrature 16-18 (07): la testa dell'orso sfiora la fascia destra (gli occhiali no); nella 16 una parte del foglio con la lampadina è tagliata a sinistra, nella 17 la lampadina è fuori campo.
- Inquadratura 3 (volto al 115%): la € della maglietta è in parte sotto il sottotitolo. Inquadratura 4 (0,9 s) è la più breve.
- Inquadrature 2 (2,96 s), 7 (2,72 s) e 21 (2,05 s) durano più di 2 s: dentro ognuna entra qualcosa di grande ("470 €" e "ALL'ANNO"; "× 365"; il fumetto), quindi il cambio visivo più lontano resta 1,99 s. Se per M-1 vale solo il taglio d'inquadratura, vanno spezzate.
- Immagine 09: tratto dell'orso leggermente più liscio delle altre (vedi `immagini/README.md`).

### Varianti per l'A/B test (P-6)

- **v1 contro v2:** `video_v1_24s.mp4` contro `video.mp4`.
- **Domanda finale contro taglio netto:** in `script/scene_elevenlabs.json` togliere "E tu: qual è quella che non guardi mai?" dal testo della scena 7, in `script/config_video.py` togliere l'ultimo sottotitolo e le inquadrature 21-22 (il loop "?" si può tenere dopo "spese."), poi rilanciare `monta.sh` con la stessa voce tagliata dopo "spese." (da ~31,0 s del montato, ~33,1 s del file grezzo).

## File

| File | Contenuto |
|---|---|
| `video.mp4` | **v2**, 1080x1920, 30 fps, 33,74 s, -14,7 LUFS, true peak -1,5 dBFS |
| `voce.mp3` | voce v2 così come registrata (35,63 s, non modificata; le pause si accorciano in montaggio) |
| `tempi.json` | inquadrature, titoli, scritte, sottotitoli parola per parola, effetti, controlli, ritmo della voce, loudness |
| `trascrizione.md`, `sottotitoli.srt` | testo con i tempi del video v2 (SRT da caricare se servono sottotitoli chiusi) |
| `copertina.png` | copertina 1080x1920 (P-2) |
| `anteprima_video.jpg`, `anteprima_layout_v2.jpg` | contact sheet del video v2 (il secondo con fasce sicure e occhiali) |
| `didascalia.md` | didascalia v2 |
| `*_v1.*`, `video_v1_24s.mp4`, `voce_v1.mp3` | la versione 1 (24 s), per l'A/B test |
| `immagini/` | 9 illustrazioni con README, prompt e anteprima |
| `script/` | testi per ElevenLabs e catena di montaggio |

## Come rifarlo (un comando)

Dalla radice del repository, con la voce in `voce.mp3`:

```bash
bash brand/tiktok/output/2026-10-risparmio-quotidiano/script/monta.sh brand/tiktok/output/2026-10-risparmio-quotidiano/voce.mp3
# con una base musicale con licenza commerciale:
MUSICA=percorso/base.mp3 bash brand/tiktok/output/2026-10-risparmio-quotidiano/script/monta.sh brand/tiktok/output/2026-10-risparmio-quotidiano/voce.mp3
```

Circa 2 minuti. Lavora in una cartella temporanea (script, immagini, font IBM Plex scaricati da `google/fonts`, licenza OFL, una volta sola in `~/.cache/butwhy-fonts`) e riscrive nella cartella del post `video.mp4`, `tempi.json`, `trascrizione.md`, `sottotitoli.srt`, `anteprima_video.jpg`, `copertina.png` e `script/frasi.json` + `script/parole.json`. Se si registra di nuovo con un testo diverso, aggiornare prima `script/scene_elevenlabs.json` (campo `text`) e `SUBS` in `script/config_video.py`.

| Script | Cosa fa |
|---|---|
| `monta.sh` | catena completa (sopra) |
| `frasi.py` | divide il **testo noto** (da `scene_elevenlabs.json`) in frasi allineate alle pause dell'audio (silencedetect + picchi ≈ sillabe, programmazione dinamica) → `frasi.json`; provato anche sulla voce v1: stesse 13 frasi della trascrizione fatta a mano |
| `ritmo.py` | accorcia le pause lunghe, pausa prima di "Ma perché?", accelera solo se sotto 165 parole/min (max 1,12x) |
| `allinea.py` | tempi stimati di ogni parola dentro le frasi → `parole.json` |
| `config_video.py` | inquadrature (parole d'inizio per testo), titoli riga per riga, scritte sullo scontrino, sottotitoli, box degli occhiali, effetti |
| `montage.py` | controlli automatici + rendering (Pillow → ffmpeg); `--preview DIR` per alcuni fotogrammi, `--solo-controlli` |
| `effetti.py` | effetti sintetizzati in numpy (scontrino, tick, pop…) sotto la voce |
| `musica.py` | base musicale facoltativa a -20 dB con ducking |
| `norm.sh` | loudnorm a due passaggi: -14 LUFS, true peak -2 dBTP |
| `fotogrammi.py`, `copertina.py`, `trascrizione.py` | contact sheet, copertina, trascrizione e SRT |
| `transcribe.py` | trascrizione di controllo con `muse-spark-1.3` (API Meta), da lanciare a mano sulla voce nuova |
| `elevenlabs.txt`, `scene_elevenlabs.json` | testi per ElevenLabs (v3 con tag inglesi, tag italiani, per scene con stability/style) |
| `*_v1.*` | dati della v1; la v1 si rifà esattamente dal commit `f1e5c40` |
