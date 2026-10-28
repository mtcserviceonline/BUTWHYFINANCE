# Risparmio quotidiano ("Il prezzo di… un caffè al giorno") — video TikTok

Realizzazione del copione [`../../copioni/2026-10-risparmio-quotidiano.md`](../../copioni/2026-10-risparmio-quotidiano.md).

## Stato del post

| Cosa | Stato |
|---|---|
| Copione, fatti e didascalia | pronti (nel copione) |
| 8 immagini | pronte ([`immagini/`](immagini/README.md)) |
| Voce | **registrata** con ElevenLabs (voce "Valerio – Warm Italian Storyteller"), 24,0 s |
| Video | **montato** (`video.mp4`, 24,3 s) |
| Da fare prima di pubblicare | 1) verificare il prezzo medio dell'espresso (1,29 €) sulla fonte originale Assoutenti/MIMIT (vedi copione); 2) attivare su TikTok l'etichetta **"contenuto generato da IA"** (immagini generate, voce sintetica); 3) guardare e **ascoltare** il video almeno una volta (io non ho potuto ascoltarlo) |

**Testo cambiato rispetto al copione:** la voce registrata chiude con *"Non serve cambiare vita, basta iniziare a guardare le piccole spese."* invece di *"E tu, quale piccola spesa taglieresti per prima?"*. Ho aggiornato copione, `script/elevenlabs.txt` e `script/scene_elevenlabs.json`. La domanda per i commenti non è più nel video: resta nella didascalia (bozza nel copione).

## File

| File | Contenuto |
|---|---|
| `video.mp4` | Video finale: 1080x1920, 30 fps, H.264 + AAC 48 kHz, **24,33 s** (voce + 0,3 s), audio a **-14,4 LUFS**, picco -1,4 dBFS |
| `voce.mp3` | La voce ElevenLabs così come caricata (24,03 s, non modificata) |
| `tempi.json` | Testo e frasi della voce, inquadrature (immagine, vista, inizio/fine), titoli, sottotitoli (con i tempi di ogni parola), effetti sonori |
| `anteprima_video.jpg` | Contact sheet: 0,0 s, un fotogramma per inquadratura e l'ultimo |
| `immagini/` | Le 8 illustrazioni (1080x1920), con il loro README |
| `script/` | Script di montaggio riutilizzabili (vedi "Come rifarlo") e testi per ElevenLabs |

## Testo parlato (trascritto dall'audio)

> Un caffè al bar ogni giorno costa circa quattrocentosettanta euro all'anno. Ma perché non ce ne accorgiamo? Perché sono piccole spese, e le piccole spese non le guardiamo mai. Primo, controlla gli abbonamenti che non usi. Secondo, fai la lista prima di andare al supermercato. Terzo, confronta le offerte di luce e gas una volta all'anno. Non serve cambiare vita, basta iniziare a guardare le piccole spese.

Trascrizione con `muse-spark-1.3` (API Meta, `script/transcribe.py`), ripetuta due volte sull'intero audio e su spezzoni di 4-6 s per controllare i punti dubbi: testo identico. faster-whisper non è utilizzabile qui (il download del modello da Hugging Face è bloccato dalla rete) e `muse-voice-transcribe-1.0` risponde `model_not_found`.

## Montaggio

### Cosa ho preso dai riferimenti

Ho riguardato i quattro video di riferimento a 4 fotogrammi al secondo (primi 5 s) e a 2 al secondo (5-15 s), con il rilevamento dei tagli di ffmpeg e l'analisi del volume:

- **Video 2 (@cashfoxclub0, riferimento principale):** 37 tagli in 66 s, **un taglio ogni ~1,8 s**; immagini ferme o quasi, tagli netti; sottotitoli al centro-basso (~70-75% dell'altezza), bianchi con contorno scuro, 2 righe al massimo, e **le parole non ancora dette sono spente** (grigie) e si "accendono" mentre la voce le dice; ogni tanto una parola gigante in alto ("Asset"). Audio: solo voce, **nessuna musica** (19 pause in silenzio vero).
- **Video 0 e 1 (Coniglio/Furetto furbo):** una parola alla volta, base musicale continua ~8-10 dB sotto la voce.
- **Video 3 (Primo Milione):** parole chiave in giallo, ritmo lento (un taglio ogni ~6 s), musica di sottofondo.

### Scelte per la ritenzione

- **Primo fotogramma = hook pieno:** a 0,00 s ci sono già l'immagine 01, il titolo "CAFFÈ AL GIORNO / **~470 €** ALL'ANNO" (numero gigante in ambra, IBM Plex Mono) e il primo sottotitolo; la voce parte subito. Nessuna dissolvenza, nessun logo.
- **14 inquadrature in 24,3 s: un taglio ogni 1,74 s in media** (da 1,1 a 2,5 s), come il riferimento principale. Da ogni immagine ricavo due inquadrature (02 e 03 una sola, perché le loro frasi durano meno di 2 s): **larga** + **primo piano ritagliato** sul dettaglio che la voce sta nominando. Tagli netti all'inizio della frase o della parola chiave, mai a metà parola (il taglio cade 0,08 s prima della parola, nella pausa se c'è).
- **Primi piani senza sgranare:** ogni fotogramma è ricampionato una sola volta dall'originale 1080x1920 (Lanczos), zoom massimo 1,55x (+6% di movimento = 1,64x); ricontrollati a piena risoluzione: contorni puliti.
- **Movimento continuo lento** su ogni inquadratura (zoom 100→106%, in due casi un piccolo pan); niente shake, glitch o zoom bruschi.
- **Sottotitoli** IBM Plex Sans Condensed Bold 90 px, bianchi con contorno inchiostro di 10 px, 2-4 parole (al massimo 2 righe), parola chiave in ambra `#E9A400`, comparsa "pop" (90→100% in 3 fotogrammi) e, come nel riferimento principale, **parole non ancora dette spente** che si accendono a tempo di voce. Centro a y=1535: per ogni inquadratura ho scelto vista e scala in modo che lì ci sia fondo, pavimento o un dettaglio secondario, **mai la € della maglietta** (controllato in tutti i fotogrammi). Sempre dentro le zone sicure: sotto y=1628 (15% in basso libero), x tra 60 e 950 (fascia destra libera).
- **Titoli** del copione in alto (da y=215, sotto il 10%), con comparsa "pop" solo quando cambiano: "~470 €", "MA PERCHÉ?", "PICCOLE SPESE", "**1** · ABBONAMENTI", "**2** · LISTA DELLA SPESA", "**3** · LUCE E GAS" (numeri in IBM Plex Mono ambra), "BASTA GUARDARE LE **PICCOLE SPESE**". Nei primi piani, dove dietro c'è il disegno, il titolo sta su una targhetta del colore del fondo. Nel primo piano della tazzina (1,98-4,44 s) il titolo dell'hook è tolto, perché avrebbe coperto la €: il "470 EURO" resta nel sottotitolo, in ambra.
- **Chiusura e loop:** immagine 08 (occhiolino) con fumetto "But Why Finance?" (verde `#006B3C`, testo bianco) nello spazio libero in alto a destra e la frase finale come titolo (carta + ambra su inchiostro: leggibile). L'ultima inquadratura fa lo zoom al contrario (106→100%) e si ferma sulla stessa scala e posizione dell'apertura (orso intero al centro, fondo inchiostro, titolo in alto): negli ultimi 0,3 s non c'è sottotitolo, poi il video riparte dal primo fotogramma senza strappo.
- **Effetti sonori** sintetizzati in numpy (`script/effetti.py`, nessun campione esterno), sotto la voce: colpo morbido + fruscio di scontrino a 0,0 s; due tocchi di moneta sul primo piano "470 euro" (1,98 s); "pop" morbido su "Ma perché?" e sui tre consigli e sul finale (4,44 / 10,29 / 13,03 / 16,48 / 21,85 s); monetine che cadono (8,96 s); forbici (11,50 s); fruscio di carta (14,54 s); moneta nel salvadanaio (20,39 s). Livelli misurati: 8-26 dB sotto la voce (RMS su 150 ms), solo effetti -35 LUFS contro -18,9 LUFS della voce.
- **Niente base musicale**, per scelta: il riferimento principale non ne ha, e una base sintetizzata senza poterla ascoltare rischiava di suonare male. Se si vuole, si aggiunge su TikTok dalla Commercial Music Library a volume molto basso.
- **Voce intatta:** né tagliata né accelerata; solo normalizzazione dell'intero mix a -14 LUFS (loudnorm a due passaggi, true peak -1,5 dBTP).

### Inquadrature

| # | Tempo (s) | Immagine | Inquadratura | Titolo | Voce |
|---|---|---|---|---|---|
| 1 | 0,00-1,98 | 01 | larga (orso intero, 76%) | CAFFÈ AL GIORNO ~470 € ALL'ANNO | Un caffè al bar ogni giorno costa circa |
| 2 | 1,98-4,44 | 01 | primo piano tazzina, scontrino, € | — | quattrocentosettanta euro all'anno. |
| 3 | 4,44-6,28 | 02 | larga | MA PERCHÉ? | Ma perché non ce ne accorgiamo? |
| 4 | 6,28-7,86 | 03 | larga | PICCOLE SPESE | Perché sono piccole spese, |
| 5 | 7,86-8,96 | 04 | larga | PICCOLE SPESE | e le piccole spese |
| 6 | 8,96-10,29 | 04 | primo piano monetine che cadono | PICCOLE SPESE (targhetta) | non le guardiamo mai. |
| 7 | 10,29-11,50 | 05 | larga | 1 · ABBONAMENTI | Primo, controlla gli |
| 8 | 11,50-13,03 | 05 | primo piano forbici e tessera | 1 · ABBONAMENTI (targhetta) | abbonamenti che non usi. |
| 9 | 13,03-14,54 | 06 | larga | 2 · LISTA DELLA SPESA | Secondo, fai la lista |
| 10 | 14,54-16,48 | 06 | primo piano carrello | 2 · LISTA DELLA SPESA (targhetta) | prima di andare al supermercato. |
| 11 | 16,48-18,17 | 07 | larga | 3 · LUCE E GAS | Terzo, confronta le offerte |
| 12 | 18,17-20,39 | 07 | primo piano bilancia, lampadina e fiammella | 3 · LUCE E GAS (targhetta) | di luce e gas una volta all'anno. |
| 13 | 20,39-21,85 | 08 | primo piano moneta e salvadanaio | — | Non serve cambiare vita, |
| 14 | 21,85-24,33 | 08 | larga, zoom all'indietro fino alla scala dell'apertura | BASTA GUARDARE LE PICCOLE SPESE + fumetto | basta iniziare a guardare le piccole spese. |

### Sincronia dei sottotitoli

La voce non ha l'allineamento parola per parola di ElevenLabs (è stata caricata come mp3). Ho diviso il testo trascritto in 13 frasi usando le pause rilevate (silencedetect -35 dB, 0,08 s) e, dentro ogni frase, ho stimato l'inizio di ogni parola con `script/allinea.py`: i picchi di energia nella banda 300-2500 Hz approssimano le sillabe, e le sillabe del testo vengono distribuite sui picchi. Il conteggio dei picchi torna con le sillabe nelle frasi brevi ("Primo" 2/2, "Secondo" 3/3, "Terzo" 2/2, "Non serve cambiare vita" 7/7). L'inizio di ogni frase è esatto; dentro la frase l'errore atteso è sotto 0,15 s. Controllo sul video finale: le pause dell'audio cadono agli stessi istanti della voce originale (±0,03 s).

### Controlli fatti

- 28 fotogrammi estratti dal video finale (0,0 s, ogni taglio +0,12 s, il 60% di ogni inquadratura, l'ultimo) e guardati, alcuni a piena risoluzione: titoli e sottotitoli leggibili e nelle zone sicure, nessun sottotitolo sulla €, orso coerente, primi piani nitidi, titolo finale leggibile, nessun sottotitolo negli ultimi 0,3 s.
- Bordo delle immagini rimpicciolite: la grana del fondo delle illustrazioni sfuma nel colore pieno (prima si vedeva un leggero rettangolo).
- Durata 24,333 s = voce (24,03 s) + 0,3 s; 730 fotogrammi; audio e video della stessa lunghezza.
- Loudness: -14,4 LUFS integrati, picco -1,4 dBFS.

### Limiti noti

- **Non ho potuto ascoltare** né la voce né gli effetti: livelli e timbri sono controllati solo con le misure (ebur128, RMS). Da ascoltare, soprattutto il "colpo" all'inizio e le forbici.
- I tempi delle parole dentro le frasi sono stimati (vedi sopra): l'accensione parola per parola può anticipare o ritardare di un paio di fotogrammi.
- Inquadrature 8, 10 e 13: il primo piano taglia l'orso al bordo (si vedono metà muso o metà maglietta). È una scelta di inquadratura, ma l'orso intero si vede solo nelle larghe.
- Inquadratura 5 dura 1,1 s (la più breve): si legge, ma è al limite.
- Immagine 03 rimpicciolita (86%): il piano grigio del tavolo finisce prima dei bordi dello schermo.
- Testo a schermo "~470 €": stima (1,29 € × 365), da verificare sulla fonte prima di pubblicare (vedi copione).

## Come rifarlo

In una cartella di lavoro **fuori dal repository**: copia tutti i file di `script/`, `voce.mp3`, le immagini in `img/01.png`…`08.png` e i font IBM Plex Sans Condensed (Bold, SemiBold) e IBM Plex Mono (Bold) dal repository GitHub `google/fonts` (licenza OFL) in `fonts/`. Poi `./monta.sh` (circa 1,5 minuti).

| Script | Cosa fa |
|---|---|
| `monta.sh` | catena completa: wav → `allinea.py` → `montage.py` → `effetti.py` → `norm.sh` → unione audio/video → `fotogrammi.py` |
| `transcribe.py` | trascrizione dell'audio con `muse-spark-1.3` (API Meta, autenticazione del proxy) |
| `frasi.json` | testo trascritto diviso in frasi, con inizio/fine presi dalle pause |
| `allinea.py` | tempi stimati di ogni parola → `parole.json` |
| `config_video.py` | inquadrature (immagine, parola d'inizio, vista, zoom, titolo, effetto), titoli e sottotitoli |
| `montage.py` | rende i fotogrammi (Pillow) e li passa a ffmpeg; `--preview DIR [tempi]` salva solo alcuni fotogrammi |
| `effetti.py` | effetti sonori sintetizzati e mix con la voce |
| `norm.sh` | loudnorm a due passaggi: -14 LUFS, true peak -1,5 dBTP, 48 kHz |
| `fotogrammi.py` | fotogrammi di controllo e `anteprima_video.jpg` |
| `elevenlabs.txt`, `scene_elevenlabs.json` | testi per ElevenLabs (aggiornati con la frase finale registrata) |
