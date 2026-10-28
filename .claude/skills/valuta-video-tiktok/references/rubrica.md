# Rubrica di valutazione (0 / 1 / 2)

Le voci sono quelle della checklist in `brand/tiktok/guida-retention.md`. Qui i criteri per assegnare il punteggio in modo ripetibile. In caso di dubbio tra due livelli, assegna il più basso e scrivi il motivo.

| # | Voce | 2 punti | 1 punto | 0 punti |
|---|---|---|---|---|
| 1 | Prima frase su di te o su un dato che fa male | Seconda persona o dato che tocca lo spettatore, con bersaglio o paradosso, entro 3 s | Dato o domanda senza "tu" | Titolo neutro, presentazione, saluto |
| 2 | Voce a 0:00, nessun logo | Prima parola entro 0,3 s, nessun logo né saluto | Parte entro 1 s, o logo/intro brevissimo | Intro oltre 1 s o saluto |
| 3 | Cambio visivo entro 4-5 s | Cambio grande entro 4,5 s | Entro 6 s | Dopo 6 s |
| 4 | Ciclo lungo promesso nell'hook | Promessa dell'hook chiusa dopo almeno il 60% della durata | Chiusa tra il 30% e il 60% | Nessuna promessa, o chiusa subito |
| 5 | Mini-cicli domanda → risposta | Almeno uno ogni ~10-12 s (video lunghi) / due in un video sotto i 30 s | Uno solo | Nessuno |
| 6 | Gradino buona notizia → clausola | Due o più ribaltamenti ("ma…", "cioè", "fermati") | Uno | Nessuno |
| 7 | Nuova immagine ogni ≤ 2 s | **Cambi medi** (misure.json) ogni ≤ 2,0 s e nessun buco > 3 s | Ogni ≤ 2,5 s o un buco | Oltre 2,5 s o più buchi |
| 8 | Concetto astratto = oggetto | Quasi ogni concetto ha un oggetto | Circa la metà | Grafica generica o solo testo |
| 9 | Un numero per schermata, grande | Ogni cifra principale è l'immagine, grande, una per schermata | Alcune cifre sì, altre no | Nessun numero o piccoli |
| 10 | Un solo colore d'accento | Un accento coerente (più i colori base) | Due accenti | Più accenti |
| 11 | Svolta segnalata dal cambio di sfondo | Le svolte hanno cambio di sfondo o transizione | Cambio sfondo senza svolta, o video senza svolte | Svolta senza alcun segnale |
| 12 | Testi in zona sicura, ≤ 2 righe, parola-chiave | Tutti nei limiti (10% alto, 15% basso, colonna destra) con parola evidenziata | Una violazione | Più violazioni |
| 13 | Nessun tempo morto | Nessun buco > 2,5 s e nessuna schermata ferma | Un buco | Più buchi |
| 14 | Numero o formula finale | Riepilogo numerico, formula o 3 parole nel finale | Riepilogo senza cifra | Nessun riepilogo |
| 15 | Chiusura | Domanda vera o quotidiano che nasce dall'ultimo payoff; oppure taglio netto con punch (test dichiarato) | Chiusura generica o morale | Nessuna chiusura o CTA estranea |
| 16 | Frasi-segnale a voce (≥ 3) | Tre tipi o più ("ma perché?", "ma fermati", "e non è finita", "cioè?", "la parte che riguarda te", "primo/secondo/terzo") | Uno o due tipi | Nessuno |
| 17 | Sostantivo-chiave nell'istante in cui è detto | Entro ±0,3 s dal parlato | Scarti fino a 0,5 s in alcuni punti | Scollegato dal parlato |
| 18 | Transizioni solo ai cambi di blocco | Tagli netti; effetti speciali solo ai cambi di blocco | Effetti ripetuti senza logica | Effetti ovunque |
| 19 | Movimento: entrata oggetti + riposo | Oggetti che entrano **e** movimento di riposo | Uno dei due | Fermo |
| 20 | Titolo in alto persistente | Titolo/dato resta mentre cambia la riga parlata | Parziale | Un solo livello che cambia tutto |
| 21 | Beat di autorità a ~2/3 | Fonte nominata a voce **e** a schermo tra il 50% e il 75% | Fonte solo a voce o fuori posizione | Nessuna fonte |

**Totale massimo 42.** Fasce: 35-42 pubblica · 27-34 rivedi · < 27 riscrivi.

## Controlli tecnici (sì / no)

| # | Controllo | Come verificarlo |
|---|---|---|
| T1 | Mascotte intera e riconoscibile nell'hook (occhiali visibili), non coperta da testi | Fotogrammi a 0, 1, 2, 3 s e a ogni cambio |
| T2 | Nessuna frase ripetuta tra titolo, testo centrale e sottotitolo nello stesso fotogramma | Fotogrammi nei primi 5 s |
| T3 | Testi nella zona sicura | Posizione di titoli e sottotitoli rispetto a 10% alto / 15% basso / colonna destra |
| T4 | Numeri coerenti con la fonte del copione; fonte nominata | Copione + fonti originali |
| T5 | Audio ~ -16/-12 LUFS, picco sotto -1 dBFS, nessuna pausa lunga | `misure.json` |
| T6 | Etichetta "contenuto generato da IA" se serve | Promemoria |
| T7 | Prima e ultima inquadratura si agganciano (loop) | Fotogrammi 0 e finale; `scarto_fine_video_s` vicino a 0 se il taglio è sull'ultima parola |

## Note di misura
- "Cambi medi" (soglia 8) è la metrica da confrontare con la soglia di 1,7-2,0 s; "totali" conta anche gli elementi che entrano uno a uno (utile per i video a tela bianca); "grandi" sono i tagli di scena.
- I fotogrammi in piccolo movimento sono respiro, rimbalzo e zoom lenti; i video con zoom continuo risultano quasi senza fotogrammi fermi.
- Le misure sono su fotogrammi a 15 al secondo ridotti: cambi molto brevi o sfumati possono sfuggire. Confrontale con le tavole.
