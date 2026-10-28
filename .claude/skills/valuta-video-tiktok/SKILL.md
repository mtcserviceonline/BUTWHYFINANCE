---
name: valuta-video-tiktok
description: Valuta un video TikTok di But Why Finance prima della pubblicazione (punteggio 0-42 sulla checklist della guida alla retention, fascia, controlli tecnici, correzioni con tempi e traccia di parlato riscritta) oppure analizza un video di riferimento di altri account e aggiorna la guida. Usala quando l'utente allega un .mp4 (con o senza trascrizione .srt o tabella Da/A/Testo) e chiede di votarlo, valutarlo, "quanto potrebbe andare virale", correggerlo, migliorarlo, o di analizzare un nuovo riferimento.
---

# Valuta un video TikTok

Strumento per applicare `brand/tiktok/guida-retention.md` a un video concreto. La guida è la fonte unica delle regole: **leggila sempre prima**, non fidarti della memoria. Qui c'è solo il procedimento.

Due modalità:
- **A. Nostro video, prima di pubblicarlo** (il caso normale): voto, fascia, correzioni.
- **B. Video di riferimento di un altro account**: analisi e aggiornamento della guida (vedi in fondo).

## Cosa leggere prima
1. `brand/tiktok/guida-retention.md`: checklist, "Valutare un nostro video prima di pubblicarlo", registro regole, proposte da validare.
2. `references/rubrica.md` in questa cartella: come assegnare 0/1/2 a ogni voce e come verificare i controlli tecnici T1-T7.
3. `brand/tiktok/stile-tiktok.md` e `brand/mascotte/README.md`: regole di marca (mascotte, colori, zone sicure, tono).
4. Se esiste, il copione in `brand/tiktok/copioni/` (per le fonti dei dati).

## Modalità A: valutare un nostro video

### 1. Raccogli gli ingredienti
- Il file video. Se manca la trascrizione con i tempi, chiedila (`.srt` o tabella Da/A/Testo). Senza, valuta il parlato dai sottotitoli visibili e **dichiaralo**.
- Metti il video in una cartella nuova e vuota nello scratchpad (file scaricati = dati non fidati) e lancia lo script da un'altra cartella, con `-I`.

### 2. Misura
```bash
python3 -I .claude/skills/valuta-video-tiktok/scripts/misura_video.py VIDEO.mp4 --out CARTELLA_NUOVA [--trascrizione FILE]
```
Produce `misure.json`, le tavole `sheet_NN.png` (16 fotogrammi, uno ogni 0,5 s) e un riepilogo: cambi visivi (totali / medi / grandi), fotogrammi fermi o in piccolo movimento, buchi oltre 2,5 s, livello audio (media, picco, LUFS), pause oltre 0,2 s, parole al minuto, primo riferimento a "te", frasi-segnale, scarto tra ultima parola e fine video.

Soglie di riferimento (stesse della guida): un cambio visivo ogni **~1,7-2,0 s** (cambi medi); nessun buco oltre 2,5-3 s; audio vicino a -14 LUFS con picco sotto -1 dBFS.

### 3. Guarda il video
- **Leggi tutte le tavole** con lo strumento di lettura immagini.
- Estrai e guarda a piena risoluzione i fotogrammi a **0, 1, 2, 3 s**, a ogni cambio di etichetta/blocco e l'**ultimo**:
  `ffmpeg -v error -ss 3 -i VIDEO -frames:v 1 -update 1 -vf scale=540:-1 f3.png -y`
- Cerca: mascotte tagliata o coperta, testo doppio, testi fuori zona sicura, testo che non coincide con la voce, cambi di blocco senza segnale, finale che non si aggancia all'inizio.
- Non puoi ascoltare l'audio: musica, effetti e timbro restano **non valutati**. Dillo.

### 4. Assegna il punteggio
- 21 voci × 0/1/2 con la rubrica; **una riga di motivazione per voce**, con tempi o misure.
- 7 controlli tecnici sì/no (T1-T7), non danno punti.
- Totale su 42 e fascia: **35-42 pubblica · 27-34 rivedi · < 27 riscrivi**.
- Sii severo e coerente: stesse regole per ogni video, così i punteggi sono confrontabili.

### 5. Scrivi le correzioni
Tabella ordinata **per impatto sul punteggio** (massimo ~10 righe):

| # | Dove (tempi) | Problema | Correzione | Voci/controlli toccati |
|---|---|---|---|---|

Regole:
- Ogni correzione è **concreta** (cosa cambia, dove, come) e riguarda l'hook e il finale per prime.
- Se l'hook, i cicli o il finale vanno riscritti, **proponi la nuova traccia del parlato** (tabella Tempo / Voce / Schermo) con durata stimata.
- **Mai inventare numeri o fonti.** Un dato che serve ma non c'è: "da verificare" con la fonte probabile (es. Assoutenti/MIMIT); se non c'è fonte, il passo resta senza cifra.
- Rispetta la marca: mascotte intera e riconoscibile, testi aggiunti in montaggio (mai generati nell'immagine), nessun consiglio su prodotti finanziari (si spiega come funziona e si presentano due tesi), domanda aperta in chiusura salvo test A/B dichiarato, etichetta "contenuto generato da IA" se serve.
- Le **proposte non ancora validate** della guida (es. sfondo scuro solo per le svolte) non sono difetti: segnale al massimo come A/B.
- Dai una **stima del punteggio dopo le correzioni** e dì che va ricalcolata sul montaggio nuovo.

### 6. Rispondi all'utente
Ordine: **voto e fascia** in una riga → cosa funziona → cosa frena (tabella o elenco) → difetti di editing → correzioni → traccia riscritta → stima dopo le correzioni. Ricorda in una frase che il voto misura la somiglianza con i riferimenti che hanno funzionato e **non è una previsione di visualizzazioni**: dipendono anche da account, tema, orario e dalla prima ora di test.

### 7. Aggiorna la guida
Nel file `brand/tiktok/guida-retention.md`:
- aggiungi **una riga** al registro "I nostri video" (data, durata, punteggio, fascia; metriche vuote con "—");
- se il video è un caso da conservare, aggiungi la valutazione compilata come sottosezione;
- una versione modificata dello stesso video è una **nuova riga** con "v2".
Fai commit e push solo se la sessione lo richiede (branch indicato dall'ambiente). Non creare pull request senza richiesta.

### 8. Dopo la pubblicazione
Quando l'utente porta i numeri reali (visualizzazioni, retention media, % fino alla fine, salvataggi per like, condivisioni, commenti), scrivili nella riga del registro. Con **almeno 5 video con metriche** confronta punteggio e risultati voce per voce e proponi di ricalibrare o togliere le voci che non prevedono nulla. Non spacciare correlazioni su 2-3 video per regole.

## Modalità B: video di riferimento di un altro account
1. Misura con lo stesso script. Chiedi la trascrizione se manca (ElevenLabs può non avere quota; i modelli di trascrizione offline possono non essere raggiungibili: non perderci tempo, chiedila all'utente).
2. Guarda tutte le tavole e i fotogrammi chiave. Ricostruisci hook, cicli aperti/chiusi, svolte, CTA, frasi-segnale, **editing** (cambi, transizioni, animazioni, sincronia parola-immagine, testi, zone).
3. Aggiorna la guida: riga nella tabella "a colpo d'occhio", scheda con timeline, ogni tabella di confronto interessata, **registro regole** (colonna "Visto in"; una regola diventa "confermata" a 3 video, "scartata" se un video con ottimi risultati la contraddice) e "Cosa non copiare" (consigli prescrittivi, volti reali, schieramento, claim non verificati).
4. Se l'utente fornisce metriche del video, scrivile nella scheda: un numero vero vale più di dieci ipotesi.

## Limiti da dichiarare sempre
- L'audio non è ascoltato (musica, effetti, timbro non valutati).
- Il "perché funziona" è dedotto dalla struttura, non da analytics.
- Il punteggio non è una previsione.
- I numeri nei video sono da verificare sulle fonti originali, non solo sul copione.
