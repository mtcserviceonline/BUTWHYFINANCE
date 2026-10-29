# Giro 2 · brand · Il numero: 67 anni e 1 mese

Data: 2026-10-29 · File letti: `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt`, `didascalia.md`, `ricerca.md`, `README.md` (nessuna cartella `immagini/`: post solo script), `revisione/r1-brand.md`, `revisione/r1-redattore.md`; regole: `CLAUDE.md`, `brand/mascotte/README.md`, `brand/tiktok/stile-tiktok.md`, `crea-post-tiktok/references/brand.md`, `didascalia.md`, `montaggio.md`, `rivedi-post-tiktok/references/rubrica.md` (sez. 3 e formato) · Rubrica e accento: **Il numero**, blu `#1F4FA3` (un solo accento, coerente in tutti i file)

## Coerenza fra i file
Ho fatto il confronto con Python: testo ripulito dai tag e spazi normalizzati. Le versioni sono state separate per intestazione (`=== VERSIONE n`), e il blocco "Testo della voce" di `copione.md` è stato confrontato a parte.
- In `scene_elevenlabs.json`, `text`, `text_v3` e `text_it` sono identici in tutte e 5 le scene. Ogni `text_v3`/`text_it` comincia con il suo `tag_v3`/`tag_it`.
- In `elevenlabs.txt`, la versione 1 contiene `text_v3` con soli tag inglesi (`[surprised] [curious] [matter-of-fact] [calm] [thoughtful] [warm]`). La versione 2 contiene `text_it` con soli tag italiani. La versione 3 contiene `text` senza tag. Stability e style della versione 3 coincidono con il JSON in tutte le scene.
- In `copione.md`, il blocco voce coincide con `text_v3` e il production doc con `text`. Immagini previste, testo a schermo ed espressioni dell'orso sono identici al JSON.
- Nessuna cifra nel campo `text`. Parole: 12 + 23 + 6 + 19 + 14 = **74**, cioè **26,1 s** a 170 parole/min. Coincide con quanto dichiarato in `copione.md` e in testa a `elevenlabs.txt`.
- Didascalia: stessi numeri (67a1m nel 2027, 67a3m dal 2028), stesse fonti (INPS circ. 28/2026, Istat, Cgil), tesi uguali alla voce, domanda finale come variante accettata («E tu, a che età pensi di andarci? 👇»).
- **Una contraddizione di contenuto.** La voce e lo schermo della scena 1 dicono «Per tutti» / «PER TUTTI». La didascalia («Restano fuori dall'aumento, a precise condizioni, alcuni lavori gravosi e usuranti») e il commento fissato («con esclusioni, a precise condizioni, per alcuni lavori gravosi e usuranti») dicono il contrario. Chi guarda il video e poi legge la didascalia trova due affermazioni opposte nello stesso post (vedi [brand-r2-1]).

## Tesi a confronto
| Tesi | Attribuita a | Parole | Formulazione equilibrata? |
|---|---|---|---|
| «Per chi difende la regola, tiene in equilibrio i conti.» (sc. 4) | generico: "chi difende la regola" | 10 | Sì nello spazio. L'attribuzione però è più debole (nessun nome) e il registro è tecnico ("conti"). |
| «Per la Cgil, allontana il traguardo di chi lavora.» (sc. 4) | Cgil (nota di L. Ghiglione, 23/01/2026) | 9 | Sì nello spazio. Ha un soggetto con nome e un'immagine più emotiva ("traguardo di chi lavora"). |
| A schermo: «CHI DIFENDE LA REGOLA: conti in equilibrio» / «CGIL: traguardo più lontano» | come sopra | 6 / 4 | Sì |
| Hook (non è una tesi, ma inquadra il tema): «Un mese di lavoro in più. Per tutti.» | pagina (scelta dell'utente) | 8 | Parte dal costo, cioè dalla cornice della tesi critica. "Per tutti" amplifica. Lo bilanciano la scena 2 (il perché della regola, detto in modo neutro) e la chiusura neutra «Poco o tanto, un mese conta». |

Il bilancio complessivo regge: il testo non si schiera e la conclusione resta al pubblico. Restano due asimmetrie lievi, entrambe dalla stessa parte: l'hook ha la cornice "costo" e la tesi critica ha un nome. Proposta in [brand-r2-3].

## Punteggi
| # | Criterio | Voto | Motivazione (una riga) |
|---|---|---|---|
| B1 | Voce "commercialista al bar" | 4 | Calma, frasi corte, chiusura calda. L'hook a scatti («Per tutti.») con `[surprised]` e style 0.45 è al limite del registro, ma non è allarmista. |
| B2 | Neutralità, tesi con pari dignità | 4 | Tesi di lunghezza pari (10/9) e attribuite, chiusura neutra. Hook e attribuzione nominale pendono un po' verso la tesi critica. |
| B3 | Nessuna consulenza | 5 | Nessun consiglio, prodotto o marca. |
| B4 | Fatto / stima / ipotesi | 4 | Misure approvate dette come tali e controllo della manovra 2027 annotato. «Per tutti» è un'affermazione assoluta, già contata in B9 e da verificare. |
| B5 | Regole visive | 4 | Accento blu unico, inchiostro solo su 1 e 5, niente rosso, font, occhiali ed € tutelati. Mancano i colori di collina/sentiero e la moneta "liscia", e nelle scene 3-4 manca «Nessuna scritta». |
| B6 | Momento "Sai che…?" | 5 | Presente in didascalia, su una riga separata, senza numeri nuovi. |
| B7 | Hashtag | 5 | `#butwhyfinance #maperché` in entrambe le versioni, più 3 o 2 pertinenti (5 e 4 in totale). |
| B8 | Etichetta IA | 5 | Presente in note di pubblicazione, copione e README. |
| B9 | Coerenza fra i file | 2 | Testi, tag, numeri e conteggi sono identici ovunque, ma l'hook («Per tutti») contraddice didascalia e commento fissato (esclusioni). |

Media: 38 / 9 = **4,2**

## Problemi bloccanti
1. **[brand-r2-1] (B9)** L'hook dice «Per tutti» (voce sc. 1 e schermo «PER TUTTI»), mentre didascalia e commento fissato dicono che alcuni lavori gravosi e usuranti restano fuori dall'aumento, a precise condizioni. Dove: `scene_elevenlabs.json` sc. 1, `elevenlabs.txt` (3 versioni), `copione.md` contro `didascalia.md` (versione completa e commento fissato). Blocca perché nello stesso post due file affermano cose opposte. Per una pagina anonima che si regge solo sui dati, è la contraddizione più facile da far notare nei commenti. Non si risolve togliendo l'esclusione dalla didascalia, perché vorrebbe dire nascondere un fatto (`ricerca.md`, riga 4). L'hook è una scelta dell'utente e non propongo di sostituirlo. Serve però una decisione sua dopo l'esito del verificatore: tenere «Per tutti» (il post resta incoerente) oppure usare la variante minima già registrata nei file da lui stesso, «Per quasi tutti» (voce sc. 1, schermo «PER QUASI TUTTI»).

## Problemi migliorativi
1. **[brand-r2-2] (B2)** Didascalia: la frase delle tesi è senza virgole («Per chi difende la regola tiene in equilibrio i conti; per la Cgil allontana…»). Si legge male e la prima parte suona come "chi difende la regola tiene i conti", con un soggetto sbagliato. Basta la punteggiatura della voce.
2. **[brand-r2-3] (B2)** La tesi favorevole resta attribuita in modo generico, mentre la critica ha un nome. Con l'hook che parte dal costo, le due asimmetrie pendono dalla stessa parte. Nessuna riscrittura a voce senza una fonte confermata. Per il verificatore: `ricerca.md` cita dubbi sul blocco da parte di Ragioneria generale dello Stato e Banca d'Italia (letti in sintesi). Se una delle due posizioni si conferma con una dichiarazione diretta, si può nominare a voce (vedi proposte: stesse parole o meno, nessun numero).
3. **[brand-r2-4] (B5)** Scena 2: collina e sentiero non hanno colore. Il generatore tende a farli verdi come un prato, con un secondo colore forte accanto all'accento blu e un verde da rubrica diversa. Vanno fissati su toni neutri.
4. **[brand-r2-5] (B5)** Scena 4: la «moneta blu» rischia di uscire con cifre o simboli incisi. Va chiesta liscia. Nelle scene 3 e 4 manca la frase «Nessuna scritta», presente invece nelle scene 1, 2 e 5: va aggiunta per uniformità (scala e salvadanaio chiamano facilmente numeri ed etichette).
5. **[brand-r2-6] (B5)** Scena 1: solo il primo titolo ha la posizione dichiarata («sopra la testa dell'orso»). Le righe «PER TUTTI» e «PENSIONE · DAL 2027» si aggiungono sotto la prima e rischiano di scendere sugli occhiali durante il punch-in al 112%. Va precisato che tutte e tre restano sopra la testa e sotto il 10% superiore.
6. **[brand-r2-7] (B1)** Hook: con `[surprised]`, stability 0.35 e style 0.45, il «Per tutti.» isolato può uscire esclamato. In registrazione conviene una sorpresa contenuta (stability ≥ 0.4). Va controllato all'ascolto, senza cambiare il testo.

## Proposte di riscrittura (testo pronto)
- **[brand-r2-1] Hook, solo se l'utente lo decide dopo la verifica (variante registrata nei file):** voce sc. 1 «Un mese di lavoro in più. Per quasi tutti. Dal duemilaventisette. … Ma perché?» (13 parole, totale 75). Schermo «PER QUASI TUTTI» su «tutti». Da aggiornare in parallelo: `text`, `text_v3`, `text_it`, le 3 versioni di `elevenlabs.txt`, blocco voce e production doc di `copione.md`, conteggio in testa (75 parole, ~26,5 s a 170/min). Se l'utente tiene «Per tutti», la didascalia non va toccata e il bloccante resta a lui.
- **[brand-r2-2] Didascalia, frase delle tesi:** «Per chi difende la regola, tiene in equilibrio i conti; per la Cgil, allontana il traguardo di chi lavora.»
- **[brand-r2-3] Scena 4, voce, solo se il verificatore conferma la fonte:** «Per la Ragioneria dello Stato, tiene in equilibrio i conti. Per la Cgil, allontana il traguardo di chi lavora.» (9 + 9 parole). Schermo «RAGIONERIA DELLO STATO: conti in equilibrio». In alternativa «Per la Banca d'Italia, …» con lo stesso schema.
- **[brand-r2-4] Scena 2, immagine prevista:** «Fondo carta. Un sentiero grigio chiaro che sale dolcemente su una collina liscia beige chiaro, senza erba né alberi, con una piccola sagoma grigia senza volto che cammina; in cima una sedia a dondolo vuota grigia con un dettaglio blu; orso a lato che spiega con l'indice alzato. Nessun grafico, asse, cartello, numero o scritta.»
- **[brand-r2-5] Scena 3, immagine prevista:** «Fondo carta. Due gradini grigi di una scala, il secondo un po' più alto, una freccia blu senza segni; orso ai piedi della scala che guarda il gradino più alto. Nessuna scritta, numero o tacca sui gradini.»
- **[brand-r2-5] Scena 4, immagine prevista:** «Fondo carta. Due sagome grigie senza volto ai lati di un tavolo grigio chiaro: una tiene un salvadanaio grigio con una moneta blu liscia, senza cifre né simboli; l'altra una cassetta degli attrezzi grigia; nessun oggetto rosso o rosa. Orso pensieroso al centro, mano al mento, € della maglietta visibile. Nessuna scritta.»
- **[brand-r2-6] Scena 1, testo a schermo (aggiunta in testa):** «tutte le righe del titolo («1 MESE DI LAVORO IN PIÙ», «PER TUTTI», «PENSIONE · DAL 2027») restano sopra la testa dell'orso, sotto il 10% superiore, mai sugli occhiali anche al 112% del punch-in».

## Note per il redattore
- I bloccanti del giro 1 di mia competenza ([brand-r1-1], hashtag) e tutti i migliorativi applicati sono risolti. Non ho trovato regressioni.
- [brand-r2-1] è una decisione dell'utente, non tua. Riportalo nei "Bloccanti non risolvibili" insieme all'esito del verificatore su «Per tutti». Se l'utente sceglie «Per quasi tutti», applica la variante in tutti i file in parallelo e aggiorna il conteggio (75 parole).
- [brand-r2-3] dipende dal verificatore: niente nomi nuovi a voce senza una dichiarazione confermata.
- Le proposte non introducono numeri nuovi.

```json
{"ruolo": "brand", "giro": 2, "media": 4.2, "bloccanti": 1, "verdetto": "da_rivedere"}
```
