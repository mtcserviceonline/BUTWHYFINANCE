# Correzioni al video "Il prezzo di… un caffè" (versione 24 s, 470 €)

Elenco completo, dall'audio alle immagini, ricavato dalla valutazione in `brand/tiktok/guida-retention.md` (punteggio di partenza **29/42**, stima dopo le correzioni **34-38/42**, da ricalcolare sul montaggio nuovo). Hook scelto dall'utente: *"Se ti bevi un caffè al bar ogni giorno, spendi circa 470 euro all'anno e non te ne accorgi. Ma perché?"* (470 € è il totale annuo).

## Da verificare prima di registrare la voce
| Dato | Fonte probabile | Stato |
|---|---|---|
| Espresso al bar 1,29 € in media; 1,29 × 365 = 471 € ≈ 470 € | Assoutenti su dati MIMIT (Teleborsa, 18 ago 2026), già nel copione `2026-10-il-prezzo-del-caffe.md` | Letto solo in sintesi: aprire la fonte originale |
| Un numero per ognuno dei tre consigli (abbonamenti, lista della spesa, luce e gas) | Da trovare | Se non c'è la fonte, il passo resta **senza cifra** |

## 1. Audio e voce
| # | Cosa | Perché | Correzione |
|---|---|---|---|
| A1 | Testo del parlato | Hook senza "tu", ciclo chiuso in 3 s, finale morale senza domanda | Usare la **nuova traccia** qui sotto (~27 s) |
| A2 | Pausa prima di "Ma perché?" | Oggi ~0,4 s; con la domanda dentro l'hook deve "atterrare" | **0,3-0,4 s** di pausa e voce che sale; "non te ne accorgi" con enfasi |
| A3 | Ritmo | 168 parole/min, 9 pause brevi a fine frase: va bene | Mantenere ~165-175 parole/min; pause **solo a fine frase** (0,3-0,5 s) |
| A4 | Livello | -14,4 LUFS, picco -1,4 dBFS: in regola | Non toccare; dopo il nuovo montaggio ricontrollare (picco sotto -1 dBFS) |
| A5 | Numeri a voce | "quattrocentosettanta" occupa ~1,5 s | Dire **"quattrocentosettanta"** (non "470") ma senza rallentare; "uno e ventinove" per 1,29 |
| A6 | Fine del parlato | Il video termina 0,47 s dopo l'ultima parola: bene | Tenere il taglio **dentro 0,5 s** dall'ultima parola per favorire il loop |
| A7 | Voce sintetica | Se è sintetica va dichiarata | Attivare l'etichetta "contenuto generato da IA" |
| A8 | Musica ed effetti | Non valutati (non ho ascoltato l'audio) | Base strumentale **-20 dB sotto la voce** con licenza commerciale; colpo di scontrino su "470", timbro/pop leggeri solo sui numeri. **Da ascoltare** |

### Nuova traccia del parlato
| Tempo | Voce |
|---|---|
| 0:00-0:03 | "Se ti bevi un caffè al bar ogni giorno, spendi circa quattrocentosettanta euro all'anno…" |
| 0:03-0:06 | "…e non te ne accorgi. Ma perché?" |
| 0:06-0:10 | "Per Assoutenti un espresso costa in media uno e ventinove. Moltiplicato per trecentosessantacinque giorni: quattrocentosettantuno euro." |
| 0:10-0:13 | "Sono piccole spese. E le piccole spese non le guardiamo mai." |
| 0:13-0:16 | "Primo: controlla gli abbonamenti che non usi." |
| 0:16-0:19 | "Secondo: fai la lista prima di andare al supermercato." |
| 0:19-0:23 | "Terzo: confronta le offerte di luce e gas una volta all'anno." |
| 0:23-0:27 | "Non serve cambiare vita. Basta guardare le piccole spese. E tu: qual è quella che non guardi mai?" |

*Opzione più in linea con la nostra regola "fatti, non consigli":* sostituire gli imperativi con la forma impersonale ("Di solito pesano tre cose: gli abbonamenti che non usi, la spesa senza lista, le bollette di luce e gas mai confrontate"). Perde "Primo/Secondo/Terzo" come frasi-segnale: da provare in A/B.

## 2. Testi a schermo
| # | Tempo | Problema | Correzione |
|---|---|---|---|
| T-1 | 0:00-0:03 | In alto "CAFFÈ AL GIORNO ~470€ ALL'ANNO" e in basso la stessa frase | In alto **solo il numero "470 €"** in ambra, gigante; "ALL'ANNO" appare quando la voce dice "all'anno"; in basso solo la riga parlata |
| T-2 | 0:04,5-0:06 | "MA PERCHÉ?" in alto e nel sottotitolo | Nei secondi della domanda **niente titolo in alto**: il messaggio lo porta il sottotitolo e l'immagine |
| T-3 | 0:06-0:10 | Nessun numero né fonte | Scontrino con **1,29 € × 365 = 471 €** in IBM Plex Mono; piccola etichetta "Fonte: Assoutenti" **fuori dal 15% in basso** e dalla colonna destra |
| T-4 | 0:13-0:23 | Titoli "1 · / 2 · / 3 ·" coprono il viso dell'orso | Spostare l'etichetta **sopra la testa**, mai sul viso; mantenere 3 titoli persistenti mentre cambia la riga parlata |
| T-5 | 0:13-0:23 | Nessuna cifra per i passi | Aggiungere una cifra **solo se verificata** (cartellino in ambra accanto all'oggetto); altrimenti nessuna |
| T-6 | 0:23-0:27 | Titolo "BASTA GUARDARE LE PICCOLE SPESE" ok, ma la domanda non è a schermo | Aggiungere nel sottotitolo la domanda "qual è quella che non guardi mai?" (parola-chiave **mai** evidenziata) |
| T-7 | Tutto | Sottotitoli a ~80% dell'altezza | Controllare che le due righe non scendano nel 15% in basso; se serve alzarli del 2-3% |

## 3. Immagini e inquadrature
| # | Tempo | Problema | Correzione |
|---|---|---|---|
| I-1 | 0:00-0:03 | Orso piccolo, scontrino in basso | Orso **intero e sorpreso** (spalle alzate, occhiali visibili), tazzina e scontrino accanto; sfondo inchiostro `#111418` (come da copione) |
| I-2 | 0:02-0:04 | Lo zoom taglia la faccia: gli occhiali escono dall'inquadratura | Zoom massimo **~120%, centrato sul volto**; oppure punch-in sul solo scontrino **mantenendo l'orso visibile** |
| I-3 | 0:03-0:06 | Il ciclo parte qui | Orso pensieroso con la fila di tazzine (già presente) |
| I-4 | 0:06-0:10 | Manca l'oggetto-numero | Inserire **lo scontrino 1,29 € × 365** (numero come oggetto, grande); la fila di tazzine può scorrere sullo sfondo |
| I-5 | 0:11,5-0:12,5 | Titolo sul viso, ritaglio a sinistra | Zoom ≤ 115% e titolo spostato (vedi T-4) |
| I-6 | 0:14,5-0:16,5 | Titolo "2 ·" sulle lenti, orso tagliato a sinistra | Orso intero con la lista; titolo sopra la testa |
| I-7 | 0:20,5-0:22 | L'orso è **fuori campo** (si vede solo il braccio che mette la moneta) | Inquadrare **il volto** e il salvadanaio insieme; niente taglio a sinistra |
| I-8 | 0:23-0:27 | Il finale non richiama l'inizio | Ultimo secondo: **stessa composizione del primo fotogramma** (orso, tazzina, scontrino) con "470 €" sostituito da "?" così il video riparte senza strappo |
| I-9 | Intero video | Mascotte tagliata o coperta in 4 punti (0:02-0:04, 0:11,5-0:12,5, 0:14,5-0:16,5, 0:20,5-0:22) | **Regola di montaggio:** in ogni inquadratura gli occhiali dell'orso restano visibili e liberi da testi |

## 4. Montaggio e ritmo
| # | Cosa | Stato | Correzione |
|---|---|---|---|
| M-1 | Cambi visivi | 13 cambi medi, uno ogni ~1,9 s; nessun buco | **Mantenere** uno ogni ≤ 2 s; i secondi nuovi (0:06-0:10) vanno divisi in **2 inquadrature** (scontrino, poi fonte/moltiplicazione) |
| M-2 | Transizioni | Solo tagli netti | **Mantenere**; un'unica transizione speciale, se serve, a 0:05 (taglio inchiostro → carta su "Ma perché?") |
| M-3 | Sfondo | Inchiostro nell'hook e nel finale, carta in mezzo | Mantenere (convenzione del vostro copione). La proposta "scuro solo per le svolte" resta **un'ipotesi da testare in A/B**, non un difetto |
| M-4 | Movimento | Zoom lento continuo e monete che cadono | Mantenere; limitare lo zoom (vedi I-2, I-5) |
| M-5 | Sincronia | Etichette 1/2/3 sincronizzate con "Primo/Secondo/Terzo" | Mantenere; far entrare **"470 €"** nell'istante della parola e "ALL'ANNO" su "all'anno" |
| M-6 | Colpo di scena | Nessuno | **Opzionale, solo con fonte:** una frase prima dei tre consigli ("Ma il caffè non è la voce che pesa di più sul budget"); senza dato non inserirla |

## 5. Pubblicazione
| # | Cosa | Correzione |
|---|---|---|
| P-1 | Etichetta IA | Attivare "contenuto generato da IA" |
| P-2 | Copertina | Fotogramma con **470 €** e orso intero (non un frame zoomato) |
| P-3 | Didascalia | "Se ti bevi un caffè al bar ogni giorno, spendi circa 470 euro all'anno. Per Assoutenti l'espresso costa in media 1,29 euro. Qual è la piccola spesa che non guardi mai? 👇" |
| P-4 | Hashtag | #caffè #prezzi #risparmio #finanzapersonale |
| P-5 | Fonti | Nominare Assoutenti a voce, a schermo e in didascalia; **aprire la fonte originale prima di pubblicare** |
| P-6 | Test | A/B: versione 24 s originale contro questa versione ~27 s; secondo test finale con domanda contro taglio netto sull'ultima frase |

## Controlli finali (rifare la valutazione con la skill)
T1 orso intero e occhiali visibili in ogni inquadratura · T2 nessun testo doppio · T3 zona sicura · T4 numeri = fonte, fonte nominata · T5 audio entro -16/-12 LUFS, picco sotto -1 dBFS · T6 etichetta IA · T7 il finale si aggancia all'inizio.
