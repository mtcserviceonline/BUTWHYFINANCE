# Copione TikTok: "In 60 secondi · Pensione a 67 anni e un mese: cosa puoi fare"

**Rubrica:** In 60 secondi (accento fucsia `#B0186E` su oggetti, numeri dei titoli e parole chiave dei sottotitoli; unico accento)
**Formato:** illustrato con l'orso + voce narrante; hook (01) e chiusura (08) su inchiostro `#111418`, le altre 6 immagini su carta `#F4F1EA`
**Durata:** **80 parole parlate** (81 per `elevenlabs_txt.py`, che conta anche «…»). Voce del 30/10: 30,04 s → pause > 0,4 s portate a 0,3 s, **nessuna accelerazione** → parlato 29,26 s, **164 parole/min**; video **29,7 s**; 8 scene voce, 8 immagini, 16 inquadrature, cambio visivo più lungo 1,74 s
**Obiettivo:** salvataggi (tre cose da fare, con il «come» in didascalia) e commenti (domanda personale «ci stai già pensando?")
**Suono:** voce narrante; base strumentale leggera a -20 dB solo dalla libreria commerciale di TikTok; effetti: colpo secco a 0,0 s, «tick» su «mese» e sui numeri dei consigli
**Etichetta IA:** attivare "contenuto generato da IA" (immagini e voce). Testi solo in montaggio, mai nelle immagini.
**Stato:** testo approvato dall'utente (30/10/2026), registrato e **montato** (`video.mp4`). La scena 1 registrata è diversa dal testo approvato e l'utente ha deciso di tenerla: il testo qui sotto è **allineato alla registrazione**.
**Fatti e fonti:** [`ricerca.md`](ricerca.md) · **Scene per la voce:** [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json) · **Testo da incollare:** [`script/elevenlabs.txt`](script/elevenlabs.txt) · **Montaggio:** [`script/config_video.py`](script/config_video.py)

## Testo della voce (allineato alla registrazione del 30/10, eleven_v3, tag inglesi)

```
[surprised] Sessantasette anni e un mese. Dal duemilaventisette, per raggiungere la pensione di vecchiaia, si dovrà lavorare un mese in più. … [curious] Ma perché?
[matter-of-fact] Si vive più a lungo: l'età sale con la speranza di vita.
[calm] Cosa puoi fare? Primo: controlla i contributi versati, nel tuo estratto conto Inps.
[calm] Secondo: stima la tua pensione con il simulatore gratuito dell'Inps.
[thoughtful] Terzo: valuta un fondo pensione. Quello che versi si può dedurre dalle tasse.
[warm] Prima inizi, meglio è. [curious] E tu, ci stai già pensando?
```

Il testo approvato diceva nella scena 1 «Dal duemilaventisette, **per quasi tutti, la pensione di vecchiaia si sposta più in là**». La registrazione dice «per raggiungere la pensione di vecchiaia, si dovrà lavorare un mese in più» e l'utente ha deciso di tenerla (ha ricaricato lo stesso file). Quindi:
- a voce **manca «per quasi tutti»**: la precisazione è affidata allo **schermo** («PER QUASI TUTTI» grande + «ECCEZIONI? / LEGGI LA DIDASCALIA ↓» sulla frase «si dovrà lavorare un mese in più») e alla **didascalia** (eccezioni complete);
- «si dovrà lavorare un mese in più» è una **semplificazione**: il requisito è l'età (67 anni e 1 mese), non un mese di lavoro in più per chi ha già smesso.

## Production doc

Tempi del video montato (`tempi.json`, voce del 30/10 dopo `ritmo.py`). Le inquadrature sono in `script/config_video.py`.

| # | Tempo | Immagine / inquadratura | Testo a schermo (entra sulla parola) | Voce (tono) | Suono |
|---|---|---|---|---|---|
| 1 | 0,0-2,3 | **01 · Hook.** Inchiostro; orso intero sorpreso, zampe aperte; sedia a dondolo fucsia che **si allontana** (linee di movimento). Vista larga + punch-in 112% in 0,7 s | **a 0,0 s**, come la copertina: «PENSIONE» piccolo + **«67 ANNI»** gigante fucsia (cifre Mono) · su «mese» (1,6): **«+ 1 MESE»** | *(sorpreso)* "Sessantasette anni e un mese." | **colpo** a 0,0 s, tick su «mese» |
| 2 | 2,3-5,4 | **02.** Carta; calendario a strappo grigio, pagine bianche, **una pagina fucsia nuova** in cima; orso che spiega, indice alzato. Larga (85%), **tenda** inchiostro → carta | **«DAL 2027»** · su «raggiungere» (3,9): «PENSIONE DI VECCHIAIA» | *(chiaro)* "Dal duemilaventisette, per raggiungere la pensione di vecchiaia," | — |
| 3 | 5,4-7,6 | 02, media (90%), titoli su targhetta carta (passano sopra il calendario) | **a 5,4 s, sulla frase «si dovrà lavorare…»: «PER QUASI TUTTI»** grande (100 px, QUASI fucsia) · su «mese» (6,5): **«ECCEZIONI?»** (76 px) + **«LEGGI LA DIDASCALIA ↓»** (62 px) | "si dovrà lavorare un mese in più. …" | — |
| 4 | 7,6-8,5 | 01, stretta (110%) su orso sorpreso + sedia | **«MA PERCHÉ?»** gigante · fumetto «But Why Finance?» su «perché», sopra la sedia | *(curioso)* "Ma perché?" | — |
| 5 | 8,5-9,9 | **03.** Carta; sentiero in salita, sagoma grigia con bastone, **sedia fucsia spostata più in là** (sagoma tratteggiata + freccia fucsia); orso pensieroso, mano al mento. Larga (92%) | **«SI VIVE PIÙ A LUNGO»** | *(chiaro)* "Si vive più a lungo:" | — |
| 6 | 9,9-12,0 | 03, stretta (109%) | su «sale»: **«→ L'ETÀ SALE»** · su «speranza»: «adeguamento alla speranza di vita (Istat)» | "l'età sale con la speranza di vita." | — |
| 7 | 12,0-13,0 | **04.** Carta; orso che tiene in alto un **foglio bianco a righe grigie astratte** (l'estratto conto) e una **lente fucsia**. Larga | **«COSA PUOI FARE?»** | *(calmo)* "Cosa puoi fare?" | — |
| 8 | 13,0-14,3 | 04, larga (stessa vista, cambia il titolo) | **«1 · ESTRATTO CONTO»** (1 in Mono fucsia) sopra la testa | "Primo:" | tick su «Primo» |
| 9 | 14,3-17,1 | 04, media (103%) | su «estratto»: «MyINPS, gratis con SPID o CIE» | "controlla i contributi versati, nel tuo estratto conto Inps." | — |
| 10 | 17,1-18,6 | **05.** Carta; orso contento con uno **smartphone** alzato: grafico astratto fucsia che sale, barre grigie, **nessun numero**. Larga | **«2 · SIMULATORE INPS»** | *(calmo)* "Secondo: stima la tua" | tick su «Secondo» |
| 11 | 18,6-21,2 | 05, media (108%) | su «simulatore»: ««La mia pensione futura»» | "pensione con il simulatore gratuito dell'Inps." | — |
| 12 | 21,2-23,5 | **06.** Carta; **salvadanaio** grigio, moneta fucsia che entra, **tre pile di monete fucsia che crescono**; orso che spiega. Larga | **«3 · FONDO PENSIONE»** · su «fondo»: **«Informazione, non consulenza finanziaria»** (piccola, resta fino al taglio) | *(pensieroso)* "Terzo: valuta un fondo pensione." | tick su «Terzo» |
| 13 | 23,5-26,0 | 06, media (108%) | + su «dedurre»: «versamenti deducibili, con un tetto annuo» (nessuna cifra a schermo) | "Quello che versi si può dedurre dalle tasse." | — |
| 14 | 26,0-27,6 | **07.** Carta; **clessidra** con sabbia fucsia appena iniziata a scendere; orso con l'indice alzato verso la clessidra | **«PRIMA INIZI,»** · su «meglio»: **«MEGLIO È»** fucsia | *(caldo)* "Prima inizi, meglio è." | — |
| 15 | 27,6-29,3 | **08 · Chiusura.** Inchiostro; orso con l'**occhiolino** che saluta, **la stessa sedia fucsia, ferma** accanto a lui | **«CI STAI GIÀ PENSANDO?»** + sotto, piccola, «Informazione, non consulenza finanziaria» · fumetto «But Why Finance?» su «già» | *(curioso)* "E tu, ci stai già pensando?" | — |
| 16 | 29,3-29,7 | **loop:** 01, la vista del fotogramma 0 (prima del punch-in), ferma | «PENSIONE» + **«?»** fucsia al posto di «67 ANNI», stessa posizione | — | — |

Note di montaggio:
- **Fotogramma 0 = copertina**: stesse righe di `copertina.png` (`script/copertina.py`), numero a schermo e colpo a 0,0 s.
- «Ma perché?» senza titolo di rubrica: solo la domanda e il fumetto.
- **Titoli dei consigli sopra la testa** («1 · ESTRATTO CONTO», «2 · SIMULATORE INPS», «3 · FONDO PENSIONE»), numeri in IBM Plex Mono fucsia con contorno carta; testo in IBM Plex Sans Condensed.
- **Sottotitoli** 1-2 righe sopra il 15% basso, mai su occhiali né su € (controllato con le coordinate della € misurate su ogni immagine: fondo della € ≤ y 1390 in tutte le inquadrature, sottotitoli da y ~1400).
- Solo tagli netti, una tenda (inchiostro → carta); zoom ≤ 115%.
- **Avvertenza a schermo** due volte: nella scena del fondo pensione e nella domanda finale.

## Hook: i tre canali
- **Verbale:** il numero è la prima parola («Sessantasette anni e un mese»), poi il quando; «per quasi tutti» non è detto a voce (registrazione del 30/10) ed è a schermo.
- **Testo:** «67 ANNI» gigante fucsia dal fotogramma 0, «+ 1 MESE» sulla parola.
- **Visivo:** orso sorpreso e la sedia a dondolo (la pensione) che scappa via; colpo secco, punch-in.

## Loop e rewatch
- **Loop:** l'08 è lo stesso set dell'01 (inchiostro, orso a sinistra, sedia fucsia a destra): nell'01 la sedia scappa, nell'08 è ferma e l'orso saluta. Ultimi ~0,45 s: torna il fotogramma 0 con «?» al posto di «67 ANNI».
- **Rewatch / salvataggi:** tre consigli numerati, il «come» (MyINPS, SPID/CIE, «La mia pensione futura») scritto piccolo a schermo e per intero in didascalia.

## Parole chiave (SEO TikTok)
pensione 2027, età pensionabile, 67 anni e 1 mese, estratto conto INPS, simulatore pensione INPS, La mia pensione futura, fondo pensione deducibile, previdenza complementare.

## Controllo qualità (copione)
- [x] Hook in 1 s sui tre canali; numero a 0,0 s.
- [x] Fatto con fonte (INPS circ. 28/2026) in didascalia; «per quasi tutti» a schermo e in didascalia con le eccezioni corrette (difesa e sicurezza **non** escluse); a voce semplificato («si dovrà lavorare un mese in più»).
- [x] Consigli **generali**: strumenti pubblici gratuiti e una categoria di prodotto, nessun fondo/gestore nominato, nessun importo o rendimento promesso, «valuta» e non «apri»; avvertenza a schermo e in didascalia.
- [x] Nessuna cifra non verificata a schermo (il tetto di 5.300 € solo in didascalia, decorrenza discussa).
- [x] Domanda aperta finale, uguale in didascalia.
- [x] Scena 1: registrazione tenuta per scelta dell'utente; «per quasi tutti» a schermo (5,4-7,6 s) e in didascalia.
