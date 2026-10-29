# Giro 3 · ritenzione · Il numero: 67 anni e 1 mese

Data: 2026-10-29 · File letti: `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt`, `didascalia.md`, `revisione/r2-ritenzione.md`, `revisione/r2-redattore.md`, `revisione/stato.md`; regole: `rubrica.md` (sez. 2, conteggio, formato), `crea-post-tiktok/references/montaggio.md`. Le altre regole (`stile-tiktok.md`, `analisi-riferimenti.md`, `copione.md` della skill) e il modello `2026-10-risparmio-quotidiano` (README v2b, scene) sono già stati letti nei giri 1-2 e non sono cambiati dopo (ultimo commit su `.claude/skills` e `brand/tiktok/*.md`: 5019bfd).

## Numeri del copione
- Parole: **75** (per scena: 13 · 23 · 6 · 19 · 14), contate con lo script della rubrica · durata stimata a 170/min: **26,5 s** (165-175: 25,7-27,3 s); con la pausa «…» (~0,4 s) ~26,9 s, con la coda del loop (+0,45 s) **~27,4 s**. Al tetto della fascia ideale (60-75).
- Secondi per scena, stimati parola per parola a 170/min (pausa inclusa): sc. 1 **0-5,0** · sc. 2 **5,0-13,1** · sc. 3 **13,1-15,2** · sc. 4 **15,2-21,9** · sc. 5 **21,9-26,9** (+ loop). Previsti: 0-5 / 5-13 / 13-15 / 15-22 / 22-27. **Tornano tutti** (scarti ≤ 0,1 s); anche i tempi interni del production doc coincidono con la stima («tutti» 2,8 · «Ma» 4,3 · «sessantasette» 6,0 · «Cgil» 19,5 · «che» 25,1).
- Primo secondo: voce «**Un mese** di lavoro…» (il numero come prima parola; «Un» è atono, ma c'è il controllo d'ascolto con «UN MESE» in `text_v3` come ripiego) · schermo a 0,0 s riga piccola «**PENSIONE**» sopra «**1 MESE**» gigante in blu, «DI LAVORO IN PIÙ» a ~1,1 s · immagine: fondo inchiostro, orso sorpreso a zampe alzate nella metà bassa, clessidra con sabbia blu, sedia a dondolo ben visibile · suono: colpo secco (clessidra girata) a 0,0 s, punch-in 100→112% nei primi 0,7 s, poi ticchettio basso. La parola chiave «pensione» ora è a schermo dal fotogramma 0.
- "Ma perché?" a **~4,3 s** (dopo «…», con [curious]) · risposta («La regola: se a sessantacinque anni si vive più a lungo, si va più tardi») a ~7,8-13,1 s · domanda finale: «E tu: a che età pensi di andarci?»

## Mappa dei cambi visivi
Tempi stimati a 170/min (0,353 s a parola). "Cambio max" = intervallo più lungo senza taglio o elemento che entra, con il piano attuale.

| Scena | Secondi stimati | Elementi che entrano | Cambio max | Esito / cosa aggiungere |
|---|---|---|---|---|
| 1 hook | 0-5,0 (5,0 s) | titolo «PENSIONE / 1 MESE» + colpo a 0,0 · punch-in fino a 0,7 · «DI LAVORO IN PIÙ» (1,1) · «PER QUASI TUTTI» (2,8) · «ECCEZIONI? SCOPRI SE RIENTRI 👇» (3,2) · «PENSIONE · DAL 2027» (3,5) · taglio stretto + «MA PERCHÉ?» (4,3) · fumetto (4,6) | ~1,7 s (1,1 → 2,8) | **Ritmo ok.** Problema nuovo di **affollamento**: a ~3,5 s sopra la testa ci sono 5 righe (PENSIONE · DAL 2027 / 1 MESE / DI LAVORO IN PIÙ / PER QUASI TUTTI / ECCEZIONI…), e dopo il taglio a 4,3 s, se restano, si aggiungono «MA PERCHÉ?», fumetto e sottotitolo, con l'inquadratura al 115% che riduce lo spazio. Snellire [rit-r3-1] |
| 2 la regola | 5,0-13,1 (8,1 s) | taglio + «PENSIONE DI VECCHIAIA» (5,0) · «67 ANNI + 1 MESE» + tick (6,0) · «OGNI 2 ANNI · Fonte: Istat» (7,8) · taglio sagoma + «A 65 ANNI» (9,2) · «SI VIVE DI PIÙ?» (10,3) · taglio sedia + «→ PENSIONE PIÙ TARDI» (11,7) | ~1,8 s (6,0 → 7,8) | ok (era 3,2 s nel giro 2). Precisare che ai tagli stretti le righe dell'inquadratura larga escono [rit-r3-2] |
| 3 2028 | 13,1-15,2 (2,1 s) | taglio + «2028» + «Fonte: INPS» (13,1) · taglio stretto + «67 ANNI + 3 MESI» + tick (13,8) | ~1,4 s | ok |
| 4 due tesi | 15,2-21,9 (6,7 s) | taglio largo (15,2) · taglio stretto + «CHI DIFENDE LA REGOLA» (15,9) · «conti in equilibrio» (17,7) · taglio stretto + «CGIL (sindacato)» (19,5) · «traguardo più lontano» (20,5) | ~1,8 s (15,9 → 17,7 e 17,7 → 19,5) | ok (era 3,5 s) |
| 5 chiusura | 21,9-26,9 + loop ~0,45 s | taglio carta→inchiostro + «POCO O TANTO?» (21,9) · «1 MESE CONTA» (23,3) · taglio stretto + «A CHE ETÀ IN PENSIONE?» (24,0) · fumetto (25,1) · loop «?» (~26,9) | ~1,8 s (25,1 → 26,9) | ok (era 2,1 s) |

## Punteggi
| # | Criterio | Voto | Motivazione (una riga) |
|---|---|---|---|
| R1 | Hook nel primo secondo sui tre canali | 5 | Numero come prima parola, «PENSIONE» + «1 MESE» gigante a 0,0 s, sedia visibile, colpo secco e punch-in; il rischio «Un» atono ha un controllo e un ripiego scritti. |
| R2 | Struttura "Ma perché?" | 5 | A ~4,3 s, dopo «…», con [curious], taglio stretto e fumetto; la risposta arriva subito nella scena 2. |
| R3 | Ritmo e durata | 5 | 75 parole, ~26,5 s, frasi corte, scene che tornano coi secondi previsti; non c'è margine per aggiungere nulla. |
| R4 | Cambio visivo ogni ≤ 2 s | 5 | Vuoto massimo ~1,8 s in tutte le scene; i buchi da 3,2-3,5 s del giro 2 sono chiusi. |
| R5 | Open loop e payoff | 4 | Il «perché» è pagato e il 2028 premia chi resta; «quasi tutti» apre una seconda domanda (chi è escluso?) che il video manda fuori, in didascalia, già a ~3 s. |
| R6 | Loop finale | 5 | Ultimo ~0,5 s = fotogramma 0 con «?» al posto del solo «1 MESE» e «PENSIONE» invariata; la voce che riparte («Un mese…») riempie il «?». |
| R7 | Chiusura: frase forte + domanda aperta | 5 | «Poco o tanto, un mese conta.» + «E tu: a che età pensi di andarci?», in seconda persona, ripetuta in didascalia. |
| R8 | Leggibilità dei testi a schermo | 3 | Le singole righe sono corte, ma nell'hook se ne impilano fino a 5 (più «MA PERCHÉ?», fumetto e sottotitolo dopo il taglio): nei 5 secondi più importanti il titolo non si legge in 1 s. |
| R9 | SEO TikTok | 4 | «Pensione» a schermo dal fotogramma 0, «pensione di vecchiaia» e «2027» dette, a schermo e in didascalia; «età pensionabile» solo in didascalia e «pensione» detta solo a ~5,0 s (vincolo dell'hook scelto). |

Media: (5+5+5+5+4+5+5+3+4)/9 = 41/9 = **4,6**.

## Controllo del giro 2
- Bloccanti miei del giro 2: nessuno.
- rit-r2-1 (scena 2 in cinque ingressi), rit-r2-2 (scena 4 in due tempi), rit-r2-4 (fumetto su «perché»), rit-r2-5 («1 MESE CONTA» + loop con «?» al posto del solo «1 MESE»), rit-r2-6 («Fonte: INPS»), rit-r2-7 (due righe in scena 2): **risolti**, verificati sui tempi parola per parola.
- rit-r2-3: risolto come proposto (sedia visibile, «PENSIONE» a 0,0 s, «UN MESE» solo se all'ascolto serve).
- «Per quasi tutti» (+1 parola, 75): resta nella fascia ideale, nessun effetto sul ritmo.
- **Problema nuovo**: con «PENSIONE», la divisione di «DI LAVORO IN PIÙ», «PER QUASI TUTTI» e l'invito «ECCEZIONI? SCOPRI SE RIENTRI 👇» il blocco di titolo dell'hook è cresciuto a 5 righe impilate [rit-r3-1].

## Problemi bloccanti
Nessuno. Prima parola = il numero, testo a 0,0 s, "Ma perché?" a ~4,3 s, 75 parole, domanda finale, nessuna scena oltre 4 s senza elementi che entrano.

## Problemi migliorativi
1. **[rit-r3-1] (R8, R1)** Hook affollato: le righe si **aggiungono** senza mai uscire. A ~3,5 s sopra la testa dell'orso ci sono «PENSIONE · DAL 2027» / «1 MESE» / «DI LAVORO IN PIÙ» / «PER QUASI TUTTI» / «ECCEZIONI? SCOPRI SE RIENTRI 👇», con il sottotitolo sotto; il piano dice che l'invito «resta fino al taglio di scena (~5,0 s)», quindi nell'inquadratura stretta al 115% (4,3-5,0 s) si sommerebbero anche «MA PERCHÉ?» e il fumetto. Chi scorre vede un muro di testo proprio nei secondi decisivi, e l'invito (scelta dell'utente) rischia di perdersi fra le altre righe. Non si tolgono parole né l'invito: si fanno **sostituire** le righe invece di impilarle (testo pronto sotto). Massimo 3 righe di titolo + la riga piccola dell'invito; al taglio di «Ma perché?» resta solo l'essenziale.
2. **[rit-r3-2] (R8)** Scene 2 e 4: il piano non dice se le righe della vista larga restano dopo i tagli stretti. Se restano, in scena 2 a ~10,3 s ci sarebbero 5 righe («PENSIONE DI VECCHIAIA», «67 ANNI + 1 MESE», «OGNI 2 ANNI · Fonte: Istat», «A 65 ANNI», «SI VIVE DI PIÙ?»). Scrivere esplicitamente: a ogni taglio stretto le righe precedenti escono, restano al massimo 2 righe a schermo.
3. **[rit-r3-3] (R5)** L'invito «SCOPRI SE RIENTRI 👇» a ~3,2 s manda lo sguardo in didascalia prima del «perché»: per chi apre la didascalia il video continua a girare, ma l'attenzione si sposta. Accettato (scelta dell'utente); per pagare il loop «quasi tutti» senza parole in più, tenere l'invito leggibile da solo nell'inquadratura stretta fino al taglio (vedi rit-r3-1) e pubblicare il commento fissato insieme al video (già nelle note).
4. **[rit-r3-4] (R9)** «Età pensionabile» è la ricerca più probabile ma non è né detta né a schermo; a schermo si può far entrare senza toccare la voce né aggiungere numeri: in chiusura «A CHE ETÀ IN PENSIONE?» la contiene già in parte. In didascalia aggiungere l'hashtag `#etàpensionabile` (versione completa) per coprire la parola chiave nella ricerca.

## Proposte di riscrittura (testo pronto)
L'hook a voce e l'invito «Scopri se rientri» restano quelli scelti dall'utente: le due varianti cambiano **solo la resa a schermo**, parole invariate (13 → 13), utilizzabili come A/B test.
- **[rit-r3-1] Hook, variante A (consigliata, `testo_a_schermo` scena 1):** «tutte le righe del titolo restano sopra la testa dell'orso, sotto il 10% superiore, mai sugli occhiali anche al 112% del punch-in; al massimo 3 righe di titolo + la riga piccola dell'invito · a 0,0 s: riga piccola «PENSIONE» sopra «1 MESE» gigante in blu · «DI LAVORO IN PIÙ» su «lavoro» (~1,1 s) · su «tutti» (~2,8 s) «PER QUASI TUTTI» **prende il posto** di «DI LAVORO IN PIÙ» (stessa riga; «QUASI» può essere più piccolo ma leggibile) · subito sotto, in corpo piccolo, «ECCEZIONI? SCOPRI SE RIENTRI 👇» su «Dal» (~3,2 s) · la riga piccola in alto diventa «PENSIONE · DAL 2027» su «duemilaventisette» (~3,5 s) · taglio su inquadratura stretta (orso + clessidra, ≤ 115%) su «Ma» (~4,3 s): **escono** «PENSIONE · DAL 2027», «1 MESE» e «PER QUASI TUTTI»; entra «MA PERCHÉ?» e l'invito «ECCEZIONI? SCOPRI SE RIENTRI 👇» resta, sotto «MA PERCHÉ?», fino al taglio di scena (~5,0 s) · fumetto «But Why Finance?» in verde marchio su «perché» (~4,6 s), di lato, fino al taglio». Righe a schermo: massimo 4 a ~3,5 s (oggi 5), 2 + fumetto dopo il taglio (oggi fino a 6).
- **[rit-r3-1] Hook, variante B (A/B test sul fotogramma 0):** come la variante A, ma a 0,0 s solo «1 MESE» gigante in blu (senza la riga «PENSIONE»), che entra piccola come «PENSIONE · DAL 2027» su «duemilaventisette» (~3,5 s); il contesto "pensione" nel primo secondo lo danno la sedia a dondolo e la clessidra. Prova se la sorpresa pura trattiene più della parola chiave a 0,0 s (la A è più forte per la ricerca, R9). Il loop resta coerente: fotogramma 0 e ultimo identici tranne «?».
- **[rit-r3-2] Scene 2 e 4, nota da aggiungere a `testo_a_schermo` e alle note di montaggio:** «a ogni taglio stretto le righe dell'inquadratura precedente escono: a schermo al massimo 2 righe di titolo + sottotitolo». (In scena 2: dopo il taglio a ~9,2 s restano solo «A 65 ANNI» e poi «SI VIVE DI PIÙ?»; dopo il taglio a ~11,7 s solo «→ PENSIONE PIÙ TARDI». In scena 4: dopo il taglio a ~19,5 s escono «CHI DIFENDE LA REGOLA» e «conti in equilibrio».)
- **[rit-r3-4] Didascalia, hashtag (versione completa):** «#butwhyfinance #maperché #pensioni #pensione2027 #etàpensionabile #inps».
- **Didascalia, prima riga:** invariata («Età pensionabile 2027: un mese di lavoro in più, per quasi tutti.»): ha due parole chiave e ripete l'hook.
- **Conteggio:** nessuna proposta cambia la voce: **75 parole**, ~26,5 s.

## Note per il redattore
- **Da non toccare:** la voce (75 parole, al tetto: niente parole in più), l'hook e l'invito dell'utente, «…» + [curious] prima di «Ma perché?», gli ingressi sulla parola di tutte le scene (il ritmo ≤ 2 s ora regge ovunque), il loop con «?» al posto del solo «1 MESE», la chiusura e la domanda finale, i tag v3 in inglese, il controllo d'ascolto su «Un» e sulla stability.
- **Priorità:** 1) [rit-r3-1] variante A nel JSON e nella riga 1 del production doc + note di montaggio (è l'unica cosa che alza R8); 2) [rit-r3-2] nota "le righe escono ai tagli"; 3) [rit-r3-4] hashtag. La variante B è solo per un eventuale A/B test dopo la pubblicazione.
- Nessun numero nuovo: le proposte spostano o fanno uscire righe esistenti.
- Aggiornare insieme `testo_a_schermo` del JSON, il production doc, la sezione "Hook: i tre canali" e le note di montaggio di `copione.md`.

```json
{"ruolo": "ritenzione", "giro": 3, "media": 4.6, "bloccanti": 0, "verdetto": "ok"}
```
