# Giro 1 · brand · Il numero: 67 anni e 1 mese

Data: 2026-10-29 · File letti: `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt`, `didascalia.md`, `ricerca.md`, `README.md` (nessuna cartella `immagini/`: post solo script); regole: `CLAUDE.md`, `brand/mascotte/README.md`, `brand/tiktok/stile-tiktok.md`, `crea-post-tiktok/references/brand.md`, `didascalia.md`, `montaggio.md`, `rivedi-post-tiktok/references/rubrica.md` (sez. 3 e formato) · Rubrica e accento: **Il numero**, blu `#1F4FA3` (un solo accento, coerente in tutti i file)

## Coerenza fra i file
Confronto fatto con Python (testo ripulito dai tag, spazi normalizzati):
- `text`, `text_v3`, `text_it` di `scene_elevenlabs.json` identici fra loro per tutte e 5 le scene; ogni `text_v3`/`text_it` inizia con il proprio `tag_v3`/`tag_it`.
- Versione 1 di `elevenlabs.txt` = `text_v3` riga per riga (tag inglesi); versione 2 = `text_it` (tag italiani); versione 3 = `text` senza tag, con stability/style uguali al JSON per tutte le scene.
- Blocco "Testo della voce" di `copione.md` identico alla versione 1; immagini previste, testo a schermo ed espressioni del production doc identici al JSON.
- Parole: 14 + 15 + 12 + 15 + 19 = **75**, a 170 parole/min **~26,5 s**: coincide con quanto dichiarato in `copione.md` ed `elevenlabs.txt` (75 parole, ~26-27 s).
- Didascalia: stessi numeri (67a1m dal 2027, 67a3m dal 2028), stesse fonti (INPS, Istat), stessa domanda finale ("E tu, a che età pensi di andarci? 👇"), tesi allineate ("allontana" → "sposta in avanti": variante accettabile). In più c'è il dato su gravosi/usuranti, che si trova in `ricerca.md` (fatto 4).
- **Nessuna differenza di testo o numeri.** Unica incoerenza di regola: la nota "`#butwhyfinance`: da decidere con l'utente" in `didascalia.md` contraddice la regola degli hashtag obbligatori (vedi B7).

## Tesi a confronto
| Tesi | Attribuita a | Parole | Formulazione equilibrata? |
|---|---|---|---|
| "tiene in equilibrio i conti" | "chi la difende" (generico; il "la" non ha un referente esplicito: la regola non viene nominata) | 9 (5 senza attribuzione) | Parzialmente: attribuzione vaga, mentre l'altra parte ha un nome |
| "allontana il traguardo" | "i sindacati" | 6 (3 senza attribuzione) | Parzialmente: più corta; però la frase di chiusura ("è un mese di lavoro in più") riprende proprio questa tesi e chiude il video sul suo punto di vista |

## Punteggi
| # | Criterio | Voto | Motivazione (una riga) |
|---|---|---|---|
| B1 | Voce "commercialista al bar" | 4 | Calma, frasi corte, niente allarmismo; la chiusura "è un mese di lavoro in più" suona un po' come una battuta a effetto |
| B2 | Neutralità, tesi con pari dignità | 3 | Le tesi sono contrapposte ma squilibrate (una attribuita in modo vago, l'altra con un nome) e la chiusura riprende la tesi dei sindacati |
| B3 | Nessuna consulenza | 5 | Nessun consiglio, prodotto o marca |
| B4 | Fatto / stima / ipotesi | 5 | Misure già decise e attribuite ("Per l'Inps", "misurata dall'Istat"); nessuna stima presentata come fatto |
| B5 | Regole visive | 4 | Accento blu unico, inchiostro solo su 1 e 5, nessuna scritta chiesta; ci sono però oggetti a rischio (grafico, cassetta rossa, salvadanaio rosa) e mancano le note su occhiali/€ e sui font |
| B6 | Momento "Sai che…?" | 1 | Manca (migliorativo) |
| B7 | Hashtag obbligatori | 1 | Mancano sia `#butwhyfinance` sia `#maperché` in entrambe le versioni |
| B8 | Etichetta IA | 5 | Presente nelle note della didascalia, nel copione e nel README |
| B9 | Coerenza fra i file | 5 | Testo, tag, stability/style, numeri, domanda e conteggio identici ovunque |

Media: 33 / 9 = **3,7**

## Problemi bloccanti
1. **[brand-r1-1] (B7)** Mancano gli hashtag obbligatori `#butwhyfinance` e `#maperché` — `didascalia.md`, versione completa e versione breve; la nota "`#butwhyfinance`: da decidere con l'utente (non aggiunto)" va tolta — blocca perché la regola della skill editoriale li rende obbligatori in entrambe le versioni (supera la vecchia nota di `brand.md`).

## Problemi migliorativi
1. **[brand-r1-2] (B6)** Manca il momento "Sai che…?". Il punto adatto è la scena 2 (speranza di vita a 65 anni), con una riga a schermo in verde `#006B3C` separata dal sottotitolo, oppure un passaggio della didascalia o il commento fissato. Testo nelle proposte.
2. **[brand-r1-3] (B2)** Scena 4: "Per chi la difende" è un'attribuzione vaga e il "la" non ha referente (la regola non è mai nominata). La tesi favorevole ha 5 parole di contenuto, quella dei sindacati 3. Conviene nominare "la regola" e dare alle due frasi lunghezza simile. Nota per il verificatore: `ricerca.md` indica come esempio l'Osservatorio CPI, ma la fonte non è ancora stata aperta. Finché non è confermata, meglio non nominarla a voce.
3. **[brand-r1-4] (B2/B1)** La chiusura "Un mese sembra poco: è un mese di lavoro in più." arriva subito dopo le due tesi e riprende quella dei sindacati: l'ultima affermazione prima della domanda sposta la conclusione. Proposta di chiusura più neutra, che fa anche rientrare il conteggio parole (vedi proposte).
4. **[brand-r1-5] (B5)** Scena 2: un "grafico a linea" invita a generare assi, tacche e numeri. Va sostituito con un oggetto senza scritte, per esempio un sentiero in salita.
5. **[brand-r1-6] (B5)** Scena 4: le cassette degli attrezzi vengono quasi sempre generate **rosse** (vietato, e qui vicino alla maglietta verde) e i salvadanai **rosa**. Bisogna fissare i colori: entrambi grigi, al massimo un dettaglio blu d'accento.
6. **[brand-r1-7] (B5)** Scena 5: l'orso tiene la clessidra in mano, quindi va specificato che resti di lato, lontana dal petto (€ visibile) e dal viso (occhiali liberi). Scena 1: il «67 ANNI + 1 MESE» gigante va messo **sopra la testa** dell'orso, mai sugli occhiali, anche durante il punch-in al 112%. Nelle note di montaggio mancano i font: IBM Plex Sans Condensed per titoli e sottotitoli, IBM Plex Mono per "67", "2027", "2028".
7. **[brand-r1-8] (B5)** Scena 3: "calmo" non è nel set di `espressioni.jpg`. Meglio "spiega, indice alzato" o "pensieroso". La scena 2 usa già "spiega", quindi per la 3 propongo "felice/sorriso tranquillo" oppure "pensieroso".
8. **[brand-r1-9] (B5)** Il fumetto "But Why Finance?" è previsto solo in chiusura, mentre `stile-tiktok.md` lo prevede in apertura e in chiusura. Si può aggiungere nell'hook dopo "Ma perché?", fuori dalle zone sicure e lontano dagli occhiali.
9. **[brand-r1-10] (B2)** Testo a schermo della scena 4: conviene attribuire le tesi anche a schermo, così chi guarda senza audio non le legge come affermazioni della pagina.

## Proposte di riscrittura (testo pronto)
- **[brand-r1-1] Hashtag versione completa:** `#butwhyfinance #maperché #pensioni #inps #finanzapersonale`
- **[brand-r1-1] Hashtag versione breve:** `#butwhyfinance #maperché #pensioni #inps`
- **[brand-r1-1] Note per la pubblicazione:** al posto di "`#butwhyfinance`: da decidere con l'utente (non aggiunto)" scrivere «Hashtag obbligatori `#butwhyfinance` e `#maperché` presenti in entrambe le versioni.»
- **[brand-r1-2] "Sai che…?" (riga a schermo in verde `#006B3C` nella scena 2, oppure in didascalia o nel commento fissato):** «Sai che…? La speranza di vita a 65 anni non è quella alla nascita: indica quanti anni, in media, vive ancora chi ne ha già compiuti 65.» (nessun numero nuovo)
- **[brand-r1-3] Scena 4, voce (`text`, con `[thoughtful]`/`[pensieroso]` nelle altre versioni):** «Per chi difende la regola, tiene in equilibrio i conti. Per i sindacati, allontana il traguardo di chi lavora.» (10 + 9 parole: scena da 15 a 19)
- **[brand-r1-4] Scena 5, voce (`text`; v3: `[warm] … [curious] E tu: …`):** «Poco o tanto, un mese conta. E tu: a che età pensi di andarci?» (14 parole, prima 19; insieme alla scena 4 il totale va da 75 a **74**). Se si cambia solo la scena 4 si arriva a 79 parole: in quel caso la chiusura va accorciata comunque.
- **[brand-r1-3] Didascalia, frase delle tesi:** «Per chi difende la regola tiene in equilibrio i conti; per i sindacati allontana il traguardo di chi lavora.»
- **[brand-r1-10] Scena 4, testo a schermo:** «chi difende la regola: conti in equilibrio» · «sindacati: traguardo più lontano»
- **[brand-r1-5] Scena 2, immagine prevista:** «Fondo carta. Un sentiero che sale dolcemente su una collina liscia, con una piccola sagoma grigia senza volto che cammina; in cima una sedia a dondolo vuota con un dettaglio blu; orso a lato che spiega con l'indice alzato. Nessun grafico, asse, cartello o numero.»
- **[brand-r1-6] Scena 4, immagine prevista:** «Fondo carta. Due sagome grigie senza volto ai lati di un tavolo grigio chiaro: una tiene un salvadanaio grigio con una moneta blu, l'altra una cassetta degli attrezzi grigia; nessun oggetto rosso o rosa. Orso pensieroso al centro, mano al mento, € della maglietta visibile.»
- **[brand-r1-7] Scena 5, immagine prevista:** «Fondo inchiostro. Orso con l'occhiolino che tiene la clessidra dell'hook (sabbia blu) di lato, all'altezza del fianco, lontana dal petto e dal viso: occhiali ed € liberi; spazio in alto per il fumetto.»
- **[brand-r1-7] Note di montaggio, da aggiungere:** «Titoli in IBM Plex Sans Condensed Bold, cifre (67, 2027, 2028) in IBM Plex Mono; titolo dell'hook sopra la testa dell'orso, mai sugli occhiali, anche al 112% del punch-in; fumetto "But Why Finance?" in verde marchio in apertura e chiusura, mai sopra occhiali o volto.»
- **[brand-r1-8] Scena 3, espressione:** «pensieroso, sguardo verso il gradino più alto» (oppure «felice, sorriso tranquillo»).

## Note per il redattore
- Se si applicano [brand-r1-3] e [brand-r1-4], vanno aggiornati in parallelo `copione.md` (blocco voce e production doc), `scene_elevenlabs.json` (`text`, `text_v3`, `text_it`), le tre versioni di `elevenlabs.txt`, la didascalia e il conteggio dichiarato in testa (74 parole, ~26 s a 170/min).
- Le due proposte di voce non introducono numeri nuovi. Per il verificatore: la tesi favorevole resta da attribuire a una fonte verificata (Osservatorio CPI non ancora aperto). Se si conferma, si può nominarla a voce al posto di "chi difende la regola", senza superare le ~10 parole.
- Il "Sai che…?" può andare nel commento fissato se la scena 2 a schermo è già piena.

```json
{"ruolo": "brand", "giro": 1, "media": 3.7, "bloccanti": 1, "verdetto": "da_rivedere"}
```
