# Giro 2 · redattore · Il numero: 67 anni e 1 mese

Data: 2026-10-29 · Parole: prima 74 → dopo 75 · durata stimata a 170/min: 26,1 s → 26,5 s (~26,9 s con la pausa «…», ~27,4 s con il fotogramma del loop)

## Testo nuovo della voce (v3)
    [surprised] Un mese di lavoro in più. Per quasi tutti. Dal duemilaventisette. … [curious] Ma perché?
    [matter-of-fact] Pensione di vecchiaia: sessantasette anni e un mese. La regola: se a sessantacinque anni si vive più a lungo, si va più tardi.
    [calm] Nel duemilaventotto, sessantasette e tre mesi.
    [thoughtful] Per chi difende la regola, tiene in equilibrio i conti. Per la Cgil, allontana il traguardo di chi lavora.
    [warm] Poco o tanto, un mese conta. [curious] E tu: a che età pensi di andarci?

Parole per scena: 13 · 23 · 6 · 19 · 14 = 75. L'unica modifica alla voce è «quasi». L'invito «Scopri se rientri» chiesto dall'utente **non è detto a voce**: sarebbero almeno 4 parole in più (79 in tutto) per una frase che a schermo e in didascalia funziona meglio. Resta solo testo a schermo e didascalia, come chiesto.

## Tabella dei problemi (tutti i rapporti)
| ID | Ruolo | B/M | Proposta in breve | Esito |
|---|---|---|---|---|
| fatti-r2-1 | verifica fatti | B | «Per tutti» falso → «Per quasi tutti» (voce e schermo) | applicato (decisione dell'utente) |
| brand-r2-1 | brand | B | contraddizione hook / didascalia | applicato (stessa correzione) |
| pub-r2-1 | pubblico | B | «Per tutti» falso se tagliato da solo | applicato (stessa correzione) |
| (utente) | coordinatore | — | invito «Scopri se rientri» a schermo + lista delle eccezioni in didascalia e commento fissato | applicato |
| fatti-r2-2 | verifica fatti | M | controllo su circolare INPS e L. 199/2025 prima di registrare | applicato (Da verificare) |
| fatti-r2-3 | verifica fatti | M | ddl di bilancio 2027 da ricontrollare il giorno dell'uscita | applicato (Da verificare, ricerca riga 5) |
| fatti-r2-4 | verifica fatti | M | citazione testuale di Ghiglione | applicato (Da verificare; non trovabile da me) |
| fatti-r2-5 | verifica fatti | M | commento fissato: vecchiaia **e** anticipata | applicato |
| rit-r2-1 | ritenzione | M | scena 2 in cinque ingressi sulla parola | applicato |
| rit-r2-2 | ritenzione | M | scena 4, etichette in due tempi | applicato |
| rit-r2-3 | ritenzione | M | «Un» udibile, sedia visibile; variante B «PENSIONE» a 0,0 s | applicato in parte |
| rit-r2-4 | ritenzione | M | fumetto dell'hook su «perché» | applicato |
| rit-r2-5 | ritenzione | M | «1 MESE CONTA» + loop con «?» al posto del solo «1 MESE» | applicato |
| rit-r2-6 | ritenzione | M | scena 3: «Fonte: INPS» breve | applicato |
| rit-r2-7 | ritenzione | M | «A 65 ANNI» / «SI VIVE DI PIÙ?» in due righe | applicato (dentro rit-r2-1) |
| brand-r2-2 | brand | M | virgole nella frase delle tesi in didascalia | applicato |
| brand-r2-3 | brand | M | nominare Ragioneria o Banca d'Italia nella tesi favorevole | rifiutato |
| brand-r2-4 | brand | M | collina e sentiero neutri | applicato |
| brand-r2-5 | brand | M | moneta liscia, «Nessuna scritta» nelle scene 3 e 4 | applicato |
| brand-r2-6 | brand | M | tutte le righe dell'hook sopra la testa | applicato |
| brand-r2-7 | brand | M | hook con stability ≥ 0.4 | applicato come controllo d'ascolto |
| pub-r2-2 | pubblico | M | «mandalo a chi ci sta arrivando» | applicato |
| pub-r2-3 | pubblico | M | «CGIL (sindacato)» a schermo | applicato |
| pub-r2-4 | pubblico | M | «se chi ha sessantacinque anni vive più a lungo» | rifiutato |
| pub-r2-5 | pubblico | M | spiegare gravosi e usuranti in didascalia | applicato (superato dalla lista delle eccezioni) |
| pub (domanda) | pubblico | M | domande finali alternative A/B | rifiutato |
| pub (termini) | pubblico | M | «conti delle pensioni in equilibrio» a schermo | rifiutato |

## Cosa ho cambiato e perché
| ID | Ruolo | B/M | Modifica (file, scena) | Prima → dopo |
|---|---|---|---|---|
| fatti-r2-1, brand-r2-1, pub-r2-1 (utente) | verifica fatti, brand, pubblico | B | JSON `text`/`text_v3`/`text_it` sc. 1; `elevenlabs.txt` v1-v3; `copione.md` (voce, production doc, hook, controllo qualità) | «Un mese di lavoro in più. Per tutti. Dal duemilaventisette.» → «Un mese di lavoro in più. Per quasi tutti. Dal duemilaventisette.»; schermo «PER TUTTI» → «PER QUASI TUTTI» su «tutti» (~2,8 s) |
| (utente) | coordinatore | — | JSON `testo_a_schermo` sc. 1, `copione.md` | aggiunta, subito sotto «PER QUASI TUTTI», la riga piccola «ECCEZIONI? SCOPRI SE RIENTRI 👇» su «Dal» (~3,2 s), che resta fino al taglio di scena (~5,0 s, ~1,8 s di lettura). L'ho accorciata a 4 parole rispetto a «SCOPRI SE RIENTRI TRA LE ECCEZIONI 👇» (6): la ritenzione (R8) segnala che le righe da 6 parole non si leggono in meno di 2 s |
| (utente) + pub-r2-5 | coordinatore, pubblico | — | `didascalia.md` (completa, breve, commento fissato) | «Restano fuori dall'aumento, a precise condizioni, alcuni lavori gravosi e usuranti.» → lista «Scopri se rientri in questi casi:» con gravosi (dipendenti, ≥ 30 anni di contributi, mansione per 7 degli ultimi 10 anni o 6 degli ultimi 7, senza APE sociale), usuranti (requisiti ridotti), precoci in attività gravose o usuranti, alcune categorie di difesa e sicurezza; fonte L. 199/2025 e circolare INPS 28/2026; rinvio all'INPS o a un patronato per il proprio caso. Tutte le condizioni vengono da A5 / riga 4 di `r2-verifica-fatti.md` (letto in sintesi). Nella versione breve: rinvio alle eccezioni nel commento fissato |
| fatti-r2-5 + pub-r2-2 | verifica fatti, pubblico | M | `didascalia.md`, commento fissato e 📌 | «Riguarda chi va in pensione di vecchiaia dal 2027 (con esclusioni…)» → lista delle eccezioni + «Per tutti gli altri il mese in più vale dal 2027, per la pensione di vecchiaia e per l'anticipata: mandalo a chi ci sta arrivando.»; 📌 «Da salvare (e da mandare a chi ci sta arrivando)» |
| brand-r2-2 | brand | M | `didascalia.md` | «Per chi difende la regola tiene…; per la Cgil allontana…» → «Per chi difende la regola, tiene…; per la Cgil, allontana…» |
| (coerenza) | — | — | `didascalia.md`, prima riga | «Età pensionabile 2027: un mese di lavoro in più.» → «… un mese di lavoro in più, per quasi tutti.» (la didascalia dice la stessa cosa dell'hook) |
| rit-r2-3 (variante B, in parte) + brand-r2-6 | ritenzione, brand | M | JSON sc. 1 `testo_a_schermo` e `immagini_previste` | a 0,0 s riga piccola «PENSIONE» sopra «1 MESE» gigante; «DI LAVORO IN PIÙ» entra su «lavoro» (~1,1 s, così il vuoto 0,7 → 2,8 s si spezza); la riga piccola diventa «PENSIONE · DAL 2027» su «duemilaventisette» (~3,5 s); tutte le righe sopra la testa, sotto il 10% superiore, mai sugli occhiali al 112%; orso nella metà bassa, sedia a dondolo «ben visibile (non un puntino)» |
| rit-r2-3 (voce) + brand-r2-7 | ritenzione, brand | M | `copione.md`, note di montaggio | controllo d'ascolto: se «Un» sparisce, «UN MESE» in maiuscolo nel solo `text_v3`; se «Per quasi tutti.» esce esclamato, rigenerare con stability 0.4. Il JSON resta 0.35/0.45 (tabella di `voce-elevenlabs.md`) |
| rit-r2-4 | ritenzione | M | JSON sc. 1 | fumetto «dopo «Ma perché?»» → su «perché» (~4,6 s), fino al taglio |
| rit-r2-1, rit-r2-7 | ritenzione | M | JSON sc. 2 `testo_a_schermo`, `effetto_sonoro` | «PENSIONE DI VECCHIAIA» su «Pensione» (~5,0) · «67 ANNI + 1 MESE» su «sessantasette» (~6,0, tick) · «OGNI 2 ANNI · Fonte: Istat» su «La» (~7,8) · «A 65 ANNI» su «sessantacinque» (~9,2) · «SI VIVE DI PIÙ?» su «vive» (~10,3) · «→ PENSIONE PIÙ TARDI» su «si va» (~11,7). Vuoto massimo 3,2 s → 1,8 s |
| brand-r2-4 | brand | M | JSON sc. 2 `immagini_previste` | sentiero grigio chiaro, collina liscia beige chiaro senza erba né alberi, sedia grigia; «Nessun grafico, asse, cartello, numero o scritta» |
| rit-r2-6 | ritenzione | M | JSON sc. 3 | «Fonte: INPS, circ. 28/2026» → «Fonte: INPS» (il riferimento completo resta in didascalia) |
| brand-r2-5 | brand | M | JSON sc. 3 e 4 `immagini_previste` | gradini grigi, freccia blu senza segni, «Nessuna scritta, numero o tacca»; moneta blu «liscia, senza cifre né simboli», «Nessuna scritta» |
| rit-r2-2 + pub-r2-3 | ritenzione, pubblico | M | JSON sc. 4 `testo_a_schermo` | larga a inizio scena · «CHI DIFENDE LA REGOLA» su «difende» (~15,9) · «conti in equilibrio» su «equilibrio» (~17,7) · «CGIL (sindacato)» su «Cgil» (~19,5) · «traguardo più lontano» su «traguardo» (~20,5). Vuoto massimo 3,5 s → 1,8 s |
| rit-r2-5 | ritenzione | M | JSON sc. 5, note di montaggio | aggiunto «1 MESE CONTA» su «mese» (~23,3); fumetto su «che» (~25,1); loop: fotogramma 0 con «?» al posto del solo «1 MESE», «PENSIONE» invariato |
| (tempi) | — | — | JSON `testo_a_schermo`, `copione.md` | tutti i tempi interni ricalcolati a 170/min con «quasi» (+0,35 s dalla scena 1 in poi); campi `secondi` invariati (0-5 / 5-13 / 13-15 / 15-22 / 22-27) |
| fatti-r2-2/3/4 | verifica fatti | M | `ricerca.md`, `README.md` | righe 4 (nuova), 5 e 6 incollate; riga 4 del giro 1 tra le storiche "non più usata"; "Per tutti" segnato falso e "non più usato"; Da verificare aggiornato (circolare e c. 185-188 parola per parola contro la lista, ddl 2027, Ghiglione, domini da abilitare) |

## Cosa ho rifiutato e perché
| ID | Ruolo | Proposta | Motivo del rifiuto |
|---|---|---|---|
| (utente, a voce) | coordinatore | dire a voce l'invito «Scopri se rientri…» | con «quasi» siamo a 75 parole: l'invito ne aggiunge almeno 4 (79) e allunga l'hook, che deve arrivare a «Ma perché?» entro ~4,5 s. L'utente l'ha previsto solo se si resta entro 80: resta a schermo e in didascalia |
| brand-r2-3 | brand | «Per la Ragioneria dello Stato / Banca d'Italia, tiene in equilibrio i conti» | il verificatore ha trovato solo riserve e stime riportate in sintesi, nessuna dichiarazione diretta copiata: nessun nome nuovo a voce senza fonte confermata. Annotato in `ricerca.md` (Tesi a confronto) |
| pub-r2-4 | pubblico | «se chi ha sessantacinque anni vive più a lungo» (+1 parola) | con «quasi» si va a 76 parole, e lo stesso pubblico chiede di non applicarle insieme; la frase attuale è giudicata chiara (P1 = 4) |
| rit-r2-3 (variante A, maiuscole) | ritenzione | «UN MESE» in maiuscolo in `text_v3` subito | la ritenzione la propone solo se nella prova «Un» non si sente: rinviata al controllo d'ascolto (nota in `copione.md`), `text_v3` resta uguale a `text` |
| brand-r2-7 (nel JSON) | brand | stability ≥ 0.4 per l'hook | la tabella di `voce-elevenlabs.md` fissa sorpreso a 0.35/0.45: resta 0.35 nel JSON e in `elevenlabs.txt`; 0.4 è il ripiego se all'ascolto esce esclamato |
| pub (domanda) | pubblico | domande finali alternative A/B | la domanda attuale ha R7 = 5 e il pubblico stesso dice che va bene |
| pub (termini) | pubblico | «conti delle pensioni in equilibrio» a schermo | allunga la riga a 5 parole contro rit-r2-2 (righe brevi in due tempi); a voce va bene |
| (utente, testo) | coordinatore | «SCOPRI SE RIENTRI TRA LE ECCEZIONI 👇» | sostituita con «ECCEZIONI? SCOPRI SE RIENTRI 👇», stesso senso in 4 parole, perché con 6 parole non si legge nel tempo disponibile (R8). L'utente aveva lasciato libera la forma («o simile, breve») |

## Conflitti fra valutatori
- **Correzione dell'hook**: i tre bloccanti chiedevano la stessa cosa; la decisione dell'utente («Per quasi tutti») li risolve tutti. Nessun conflitto.
- **Ritenzione e invito a schermo**: l'hook ora ha più righe (PENSIONE, 1 MESE, DI LAVORO IN PIÙ, PER QUASI TUTTI, ECCEZIONI…, DAL 2027). Per non affollare lo spazio sopra la testa (brand-r2-6) ho fuso «PENSIONE» e «DAL 2027» in una sola riga piccola che cresce, ho messo l'invito in corpo piccolo, e ho lasciato all'invito ~1,8 s di lettura fino al taglio di scena. Nel montaggio va controllato che le righe non scendano sugli occhiali al 112%.
- **Stability dell'hook**: il brand chiede ≥ 0.4, la tabella della voce dice 0.35. Tengo la tabella e lascio 0.4 come ripiego d'ascolto.

## Bloccanti non risolvibili da me (per l'utente)
- Nessuno. I tre bloccanti del giro (fatti-r2-1, brand-r2-1, pub-r2-1) sono risolti con «Per quasi tutti».
- Resta da fare prima di registrare: tutte le cifre e le condizioni delle eccezioni sono "lette in sintesi". La lista «Scopri se rientri in questi casi» va confrontata parola per parola con la circolare INPS 28/2026 e con la L. 199/2025 c. 186-188 (vedi `ricerca.md`), perché è il punto su cui i commenti saranno più pignoli.

## Controlli eseguiti
- Conteggio parole (script di `rubrica.md`): 13 + 23 + 6 + 19 + 14 = **75**, 26,5 s a 170/min (25,7-27,3 s a 165-175). Lo stesso numero è riportato in `copione.md` e in testa a `elevenlabs.txt`.
- Coerenza (Python): per ogni scena `text_v3`/`text_it` sono uguali a `text` a meno dei tag e iniziano con `tag_v3`/`tag_it`. `text_v3` compare nella versione 1, `text_it` nella versione 2 e `text` nella versione 3 di `elevenlabs.txt`. `text_v3` e `text` compaiono nel blocco voce e nel production doc di `copione.md`. Le intestazioni di scena della v3 coincidono con nome, secondi, stability e style del JSON. Esito: OK.
- Nessuna cifra nel campo `text`: OK. Nessun tag italiano nella versione 1 e nessun tag nella versione 3: OK. Nessun residuo di «Per tutti.» o «PER TUTTI» nei file del post: OK.
- `python3 -m json.tool script/scene_elevenlabs.json`: JSON valido.
- Domanda finale identica in voce, didascalia completa e breve («E tu, a che età pensi di andarci? 👇»).
