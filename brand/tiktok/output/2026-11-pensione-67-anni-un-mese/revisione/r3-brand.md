# Giro 3 · brand · Il numero: 67 anni e 1 mese

Data: 2026-10-29 · File letti: `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt`, `didascalia.md`, `ricerca.md`, `README.md` (nessuna cartella `immagini/`: post solo script), `revisione/r2-brand.md`, `revisione/r2-redattore.md`, `revisione/stato.md`; regole: `CLAUDE.md`, `brand/mascotte/README.md`, `brand/tiktok/stile-tiktok.md`, `crea-post-tiktok/references/brand.md`, `didascalia.md`, `montaggio.md`, `rivedi-post-tiktok/references/rubrica.md` (sez. 3 e formato) · Rubrica e accento: **Il numero**, blu `#1F4FA3` (un solo accento, coerente in tutti i file)

## Coerenza fra i file
Confronto fatto con Python: testo ripulito dai tag, spazi normalizzati, `elevenlabs.txt` diviso per intestazione `=== VERSIONE n`, blocco voce di `copione.md` confrontato a parte.
- `scene_elevenlabs.json`: `text`, `text_v3` e `text_it` identici a meno dei tag in tutte e 5 le scene.
- `elevenlabs.txt`: la versione 1 contiene ogni `text_v3` e ha solo tag inglesi (`[surprised] [curious] [matter-of-fact] [calm] [thoughtful] [warm]`). La versione 2 contiene ogni `text_it` e ha solo tag italiani. La versione 3 contiene ogni `text` senza tag. Le intestazioni di scena (nome, secondi, stability, style) coincidono con il JSON.
- `copione.md`: il blocco voce contiene ogni `text_v3`, il production doc ogni `text`. Immagini previste, testo a schermo, espressione ed effetto sonoro sono identici al JSON, carattere per carattere.
- Nessuna cifra nella voce. Parole 13 + 23 + 6 + 19 + 14 = **75**, cioè **26,5 s** a 170/min: coincide con `copione.md`, testa di `elevenlabs.txt` e `r2-redattore.md`.
- Nessun residuo di «Per tutti»: hook, schermo («PER QUASI TUTTI») e prima riga della didascalia dicono «per quasi tutti». La lista delle eccezioni è uguale nel contenuto in didascalia e nel commento fissato. Il bloccante [brand-r2-1] è **risolto**.
- Numeri uguali ovunque (67a1m nel 2027, 67a3m dal 2028), fonti uguali (INPS circ. 28/2026, Istat, L. 199/2025, Cgil). La domanda finale è identica in voce, didascalia completa e breve («E tu, a che età pensi di andarci? 👇»).
- Unica differenza rimasta: il **commento fissato** chiude con un'altra domanda («Legare l'età della pensione a quanto si vive: giusto o no?»). Non contraddice nulla, ma divide i commenti su due domande (vedi [brand-r3-2]). Il commento aggiunge anche l'anticipata, che nel video non c'è: è un'aggiunta, non una contraddizione (`ricerca.md` riga 6).

## Tesi a confronto
| Tesi | Attribuita a | Parole | Formulazione equilibrata? |
|---|---|---|---|
| «Per chi difende la regola, tiene in equilibrio i conti.» (sc. 4, uguale in didascalia) | generico: "chi difende la regola" | 10 | Sì nello spazio e nel tono. L'attribuzione è senza nome: la fonte diretta non è confermata (rifiuto motivato del redattore in r2). |
| «Per la Cgil, allontana il traguardo di chi lavora.» (sc. 4, uguale in didascalia) | Cgil (nota di L. Ghiglione, 23/01/2026, in sintesi) | 9 | Sì. A schermo «CGIL (sindacato)». |
| A schermo: «CHI DIFENDE LA REGOLA» + «conti in equilibrio» / «CGIL (sindacato)» + «traguardo più lontano» | come sopra | 6 / 5 | Sì. Due righe ciascuna, stessa forza. Immagini simmetriche: salvadanaio e cassetta degli attrezzi, entrambe grigie. |
| Hook: «Un mese di lavoro in più. Per quasi tutti.» | pagina (scelta dell'utente) | 9 | Ora è un fatto esatto. La cornice resta "costo", bilanciata dalla regola spiegata in modo neutro (sc. 2) e dalla chiusura «Poco o tanto, un mese conta». |
| Commento fissato: «Legare l'età della pensione a quanto si vive: giusto o no?» | domanda al pubblico | 11 | Neutra: lascia la conclusione al pubblico. |

Il testo non si schiera. Resta la sola asimmetria lieve del nome (Cgil con nome, tesi favorevole generica), già discussa e accettata in mancanza di una fonte diretta.

## Punteggi
| # | Criterio | Voto | Motivazione (una riga) |
|---|---|---|---|
| B1 | Voce "commercialista al bar" | 5 | Frasi corte, tono calmo, chiusura calda. «Per quasi tutti» toglie l'assoluto all'hook e c'è un controllo d'ascolto se esce esclamato. |
| B2 | Neutralità, tesi con pari dignità | 4 | Tesi 10/9 parole, attribuite, simmetriche a schermo e in immagine. Resta l'asimmetria lieve del nome, motivata dalla fonte. |
| B3 | Nessuna consulenza | 5 | Nessun prodotto né marca. Il rinvio «chiedi all'INPS o a un patronato» indica enti pubblici o di assistenza, non è un consiglio finanziario. |
| B4 | Fatto / stima / ipotesi | 5 | Misure approvate dette come tali, eccezioni «a precise condizioni», ddl 2027 annotato «da ricontrollare il giorno dell'uscita». |
| B5 | Regole visive | 4 | Accento blu unico, inchiostro solo su 1 e 5, niente rosso o rosa, nessuna scritta, sagome grigie, € visibile. Nella stretta dell'hook (4,3 s) però non è detto quali righe restano. |
| B6 | Momento "Sai che…?" | 5 | In didascalia, su una riga sua, senza numeri nuovi. |
| B7 | Hashtag | 5 | `#butwhyfinance #maperché` in entrambe le versioni, più 3 o 2 pertinenti (5 e 4 in totale). |
| B8 | Etichetta IA | 5 | Presente in note di pubblicazione, copione e README. |
| B9 | Coerenza fra i file | 4 | Testi, tag, numeri, conteggi ed eccezioni coincidono ovunque. Il commento fissato pone però una domanda diversa da video e didascalia. |

Media: 42 / 9 = **4,7**

## Problemi bloccanti
Nessuno.

## Problemi migliorativi
1. **[brand-r3-1] (B5)** Scena 1: l'hook ha ora fino a cinque righe sopra la testa (PENSIONE · DAL 2027, 1 MESE, DI LAVORO IN PIÙ, PER QUASI TUTTI, ECCEZIONI? SCOPRI SE RIENTRI 👇). Al taglio stretto delle ~4,3 s (≤ 115%) la testa dell'orso sale e si ingrandisce. Lì arrivano anche «MA PERCHÉ?» (4,3 s) e il fumetto (4,6 s). Il copione non dice quali righe escono al taglio: se restano tutte, la pila scende sugli occhiali o entra nel 10% in alto. L'invito delle eccezioni (scelta dell'utente) va tenuto fino al taglio di scena: va precisato solo cosa esce.
2. **[brand-r3-2] (B9)** Commento fissato: chiude con «Legare l'età della pensione a quanto si vive: giusto o no? Una riga sola 👇», mentre video e didascalia chiedono «a che età pensi di andarci?». Con due domande diverse i commenti si dividono e il post non risponde più a un'unica domanda. Basta una variante della stessa domanda.
3. **[brand-r3-3] (B5)** Testo a schermo «ECCEZIONI? SCOPRI SE RIENTRI 👇»: IBM Plex Sans Condensed non ha glifi emoji. In montaggio il 👇 va reso come icona/emoji a colori separata o come freccia «↓» nel font. Se no esce un quadratino vuoto. Va annotato nelle note di montaggio.
4. **[brand-r3-4] (B2, nota)** L'asimmetria del nome nelle tesi resta. Non propongo nomi nuovi senza una dichiarazione confermata (decisione del giro 2, che condivido). Se il verificatore trova una citazione diretta, lo schema pronto è in `r2-brand.md` [brand-r2-3].

Valutazione delle scelte dell'utente (non da sostituire): l'hook «Un mese di lavoro in più. Per quasi tutti.» è ora vero e coerente con la didascalia; regge la voce da bar. «ECCEZIONI? SCOPRI SE RIENTRI 👇» e «Scopri se rientri in questi casi:» sono chiari, utili e senza tono da meme; rimandano a fonti pubbliche e non danno consulenza.

## Proposte di riscrittura (testo pronto)
- **[brand-r3-1] Scena 1, testo a schermo (aggiunta da mettere prima di «taglio su inquadratura stretta…»):** «al taglio stretto (~4,3 s) escono «1 MESE», «DI LAVORO IN PIÙ», «PER QUASI TUTTI» e «PENSIONE · DAL 2027»; restano solo «MA PERCHÉ?» sopra la testa e, in corpo piccolo, «ECCEZIONI? SCOPRI SE RIENTRI 👇» fino al taglio di scena; il fumetto «But Why Finance?» va di lato, lontano da occhiali e volto; nessuna riga nel 10% superiore né sugli occhiali a 115%». Stessa frase nella nota di montaggio dell'hook in `copione.md`.
- **[brand-r3-2] Commento fissato, ultima frase:** «Legare l'età della pensione a quanto si vive: e tu, a che età pensi di andarci? Una riga sola 👇»
- **[brand-r3-3] Note di montaggio (`copione.md`):** «Il 👇 di «ECCEZIONI? SCOPRI SE RIENTRI 👇» si inserisce come emoji/icona a parte (IBM Plex non ha emoji) oppure come «↓» nello stesso font; controllarlo nell'anteprima.»

## Note per il redattore
- Il bloccante [brand-r2-1] è risolto, come i migliorativi applicati del giro 2 ([brand-r2-2], [brand-r2-4], [brand-r2-5], [brand-r2-6]). [brand-r2-7] è giusto come controllo d'ascolto. Non trovo regressioni.
- Le proposte non toccano la voce (resta a 75 parole) e non introducono numeri nuovi. Le proposte [brand-r3-1] e [brand-r3-3] vanno scritte in parallelo in `scene_elevenlabs.json` (`testo_a_schermo` sc. 1) e `copione.md`, perché i due file oggi coincidono carattere per carattere.
- Per il verificatore: il commento fissato dice «il mese in più vale … anche per l'anticipata». Per l'anticipata il mese in più riguarda i contributi, non l'età (`ricerca.md` riga 6). Conviene controllare che la frase non lasci intendere un'età.

```json
{"ruolo": "brand", "giro": 3, "media": 4.7, "bloccanti": 0, "verdetto": "ok"}
```
