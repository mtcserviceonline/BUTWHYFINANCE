# Copione TikTok: "In 60 secondi · Pensione a 67 anni e un mese: cosa puoi fare"

**Rubrica:** In 60 secondi (accento fucsia `#B0186E` su oggetti, numeri dei titoli e parole chiave dei sottotitoli; unico accento)
**Formato:** illustrato con l'orso + voce narrante; hook (01) e chiusura (08) su inchiostro `#111418`, le altre 6 immagini su carta `#F4F1EA`
**Durata:** **80 parole** (conteggio di `elevenlabs_txt.py`; 79 per `frasi.py`, che non conta «…»). Registrazione attuale 30,04 s → con le pause > 0,4 s portate a 0,3 s e al più 1,05x **~28 s, ~170 parole/min** (prova della catena sulla voce del 30/10); 8 scene voce, 8 immagini, 16 inquadrature (un cambio visivo ogni ≤ 2 s)
**Obiettivo:** salvataggi (tre cose da fare, con il «come» in didascalia) e commenti (domanda personale «ci stai già pensando?")
**Suono:** voce narrante; base strumentale leggera a -20 dB solo dalla libreria commerciale di TikTok; effetti: colpo secco a 0,0 s, «tick» su «mese» e sui numeri dei consigli
**Etichetta IA:** attivare "contenuto generato da IA" (immagini e voce). Testi solo in montaggio, mai nelle immagini.
**Stato:** testo **approvato dall'utente** (30/10/2026) e registrato; la scena 1 registrata è diversa dal testo e va rifatta (vedi `README.md`).
**Fatti e fonti:** [`ricerca.md`](ricerca.md) · **Scene per la voce:** [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json) · **Testo da incollare:** [`script/elevenlabs.txt`](script/elevenlabs.txt) · **Montaggio:** [`script/config_video.py`](script/config_video.py)

## Testo della voce (approvato, eleven_v3, tag inglesi)

```
[surprised] Sessantasette anni e un mese. Dal duemilaventisette, per quasi tutti, la pensione di vecchiaia si sposta più in là. … [curious] Ma perché?
[matter-of-fact] Si vive più a lungo: l'età sale con la speranza di vita.
[calm] Cosa puoi fare? Primo: controlla i contributi versati, nel tuo estratto conto Inps.
[calm] Secondo: stima la tua pensione con il simulatore gratuito dell'Inps.
[thoughtful] Terzo: valuta un fondo pensione. Quello che versi si può dedurre dalle tasse.
[warm] Prima inizi, meglio è. [curious] E tu, ci stai già pensando?
```

**Scena 1 da rifare** (la sola cosa da registrare di nuovo):

```
[surprised] Sessantasette anni e un mese. Dal duemilaventisette, per quasi tutti, la pensione di vecchiaia si sposta più in là.
```

La registrazione del 30/10 dice invece «Dal duemilaventisette, per raggiungere la pensione di vecchiaia, si dovrà lavorare un mese in più» (5 trascrizioni su 5): manca «per quasi tutti», la correzione chiave del post precedente.

## Production doc

Tempi della voce del 30/10 dopo `ritmo.py` (scena 1 stimata sulla durata attuale, ~7,3 s): conta la parola su cui entra ogni elemento, il secondo è indicativo. Le inquadrature sono in `script/config_video.py`.

| # | Tempo | Immagine / inquadratura | Testo a schermo (entra sulla parola) | Voce (tono) | Suono |
|---|---|---|---|---|---|
| 1 | 0,0-2,2 | **01 · Hook.** Inchiostro; orso intero sorpreso, zampe aperte; sedia a dondolo fucsia che **si allontana** (linee di movimento). Vista larga + punch-in 112% in 0,7 s | **a 0,0 s**, come la copertina: «PENSIONE» piccolo + **«67 ANNI»** gigante fucsia (cifre Mono) · su «mese» (~1,3): **«+ 1 MESE»** | *(sorpreso)* "Sessantasette anni e un mese." | **colpo** a 0,0 s, tick su «mese» |
| 2 | 2,2-4,6 | **02.** Carta; calendario a strappo grigio, pagine bianche, **una pagina fucsia nuova** in cima; orso che spiega, indice alzato. Larga (85%), **tenda** inchiostro → carta | **«DAL 2027»** · su «quasi»: **«PER QUASI TUTTI»** (QUASI in fucsia) · su «tutti»: **«ECCEZIONI? LEGGI LA DIDASCALIA ↓»** (targhetta carta: le righe passano sopra il calendario) | *(chiaro)* "Dal duemilaventisette, per quasi tutti," | — |
| 3 | 4,6-7,4 | 02, media (95%) | «PENSIONE DI VECCHIAIA» · su «sposta»: **«PIÙ IN LÀ →»** fucsia | "la pensione di vecchiaia si sposta più in là. …" | — |
| 4 | 7,4-8,4 | 01, stretta (110%) su orso sorpreso + sedia | **«MA PERCHÉ?»** gigante · fumetto «But Why Finance?» su «perché», sopra la sedia | *(curioso)* "Ma perché?" | — |
| 5 | 8,4-9,7 | **03.** Carta; sentiero in salita, sagoma grigia con bastone, **sedia fucsia spostata più in là** (sagoma tratteggiata + freccia fucsia); orso pensieroso, mano al mento. Larga (92%) | **«SI VIVE PIÙ A LUNGO»** | *(chiaro)* "Si vive più a lungo:" | — |
| 6 | 9,7-11,9 | 03, stretta (109%) | su «sale»: **«→ L'ETÀ SALE»** · su «speranza»: «adeguamento alla speranza di vita (Istat)» | "l'età sale con la speranza di vita." | — |
| 7 | 11,9-13,1 | **04.** Carta; orso che tiene in alto un **foglio bianco a righe grigie astratte** (l'estratto conto) e una **lente fucsia**. Larga | **«COSA PUOI FARE?»** | *(calmo)* "Cosa puoi fare?" | — |
| 8 | 13,1-14,5 | 04, larga (stessa vista, cambia il titolo) | **«1 · ESTRATTO CONTO»** (1 in Mono fucsia) sopra la testa | "Primo:" | tick su «Primo» |
| 9 | 14,5-16,9 | 04, media (103%) | su «estratto»: «MyINPS, gratis con SPID o CIE» | "controlla i contributi versati, nel tuo estratto conto Inps." | — |
| 10 | 16,9-18,4 | **05.** Carta; orso contento con uno **smartphone** alzato: grafico astratto fucsia che sale, barre grigie, **nessun numero**. Larga | **«2 · SIMULATORE INPS»** | *(calmo)* "Secondo: stima la tua" | tick su «Secondo» |
| 11 | 18,4-21,0 | 05, media (108%) | su «simulatore»: ««La mia pensione futura»» | "pensione con il simulatore gratuito dell'Inps." | — |
| 12 | 21,0-23,4 | **06.** Carta; **salvadanaio** grigio, moneta fucsia che entra, **tre pile di monete fucsia che crescono**; orso che spiega. Larga | **«3 · FONDO PENSIONE»** · su «fondo»: **«Informazione, non consulenza finanziaria»** (piccola, resta fino al taglio) | *(pensieroso)* "Terzo: valuta un fondo pensione." | tick su «Terzo» |
| 13 | 23,4-25,8 | 06, media (108%) | + su «dedurre»: «versamenti deducibili, con un tetto annuo» (nessuna cifra a schermo) | "Quello che versi si può dedurre dalle tasse." | — |
| 14 | 25,8-27,4 | **07.** Carta; **clessidra** con sabbia fucsia appena iniziata a scendere; orso con l'indice alzato verso la clessidra | **«PRIMA INIZI,»** · su «meglio»: **«MEGLIO È»** fucsia | *(caldo)* "Prima inizi, meglio è." | — |
| 15 | 27,4-28,9 | **08 · Chiusura.** Inchiostro; orso con l'**occhiolino** che saluta, **la stessa sedia fucsia, ferma** accanto a lui | **«CI STAI GIÀ PENSANDO?»** + sotto, piccola, «Informazione, non consulenza finanziaria» · fumetto «But Why Finance?» su «già» | *(curioso)* "E tu, ci stai già pensando?" | — |
| 16 | ultimi ~0,45 s | **loop:** 01, la vista del fotogramma 0 (prima del punch-in), ferma | «PENSIONE» + **«?»** fucsia al posto di «67 ANNI», stessa posizione | — | — |

Note di montaggio:
- **Fotogramma 0 = copertina**: stesse righe di `copertina.png` (`script/copertina.py`), numero a schermo e colpo a 0,0 s.
- «Ma perché?» senza titolo di rubrica: solo la domanda e il fumetto.
- **Titoli dei consigli sopra la testa** («1 · ESTRATTO CONTO», «2 · SIMULATORE INPS», «3 · FONDO PENSIONE»), numeri in IBM Plex Mono fucsia con contorno carta; testo in IBM Plex Sans Condensed.
- **Sottotitoli** 1-2 righe sopra il 15% basso, mai su occhiali né su € (controllato con le coordinate della € misurate su ogni immagine: fondo della € ≤ y 1390 in tutte le inquadrature, sottotitoli da y ~1400).
- Solo tagli netti, una tenda (inchiostro → carta); zoom ≤ 115%.
- **Avvertenza a schermo** due volte: nella scena del fondo pensione e nella domanda finale.

## Hook: i tre canali
- **Verbale:** il numero è la prima parola («Sessantasette anni e un mese»), poi il quando e il «per quasi tutti».
- **Testo:** «67 ANNI» gigante fucsia dal fotogramma 0, «+ 1 MESE» sulla parola.
- **Visivo:** orso sorpreso e la sedia a dondolo (la pensione) che scappa via; colpo secco, punch-in.

## Loop e rewatch
- **Loop:** l'08 è lo stesso set dell'01 (inchiostro, orso a sinistra, sedia fucsia a destra): nell'01 la sedia scappa, nell'08 è ferma e l'orso saluta. Ultimi ~0,45 s: torna il fotogramma 0 con «?» al posto di «67 ANNI».
- **Rewatch / salvataggi:** tre consigli numerati, il «come» (MyINPS, SPID/CIE, «La mia pensione futura») scritto piccolo a schermo e per intero in didascalia.

## Parole chiave (SEO TikTok)
pensione 2027, età pensionabile, 67 anni e 1 mese, estratto conto INPS, simulatore pensione INPS, La mia pensione futura, fondo pensione deducibile, previdenza complementare.

## Controllo qualità (copione)
- [x] Hook in 1 s sui tre canali; numero a 0,0 s.
- [x] Fatto con fonte (INPS circ. 28/2026) in didascalia; «per quasi tutti» con le eccezioni corrette (difesa e sicurezza **non** escluse).
- [x] Consigli **generali**: strumenti pubblici gratuiti e una categoria di prodotto, nessun fondo/gestore nominato, nessun importo o rendimento promesso, «valuta» e non «apri»; avvertenza a schermo e in didascalia.
- [x] Nessuna cifra non verificata a schermo (il tetto di 5.300 € solo in didascalia, decorrenza discussa).
- [x] Domanda aperta finale, uguale in didascalia.
- [ ] **Scena 1 da registrare di nuovo** con il testo approvato.
