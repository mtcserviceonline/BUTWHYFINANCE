# Rubrica di revisione dei post TikTok

Criteri, punteggi e soglie usati dai quattro valutatori (`.claude/agents/bwf-*.md`) e dalla skill `rivedi-post-tiktok`. Ogni agente ha i propri criteri anche nel suo file, per essere autosufficiente: **se un file di ruolo e questa rubrica divergono, vale questa rubrica** (e va corretto il file di ruolo).

Da dove vengono le regole: `CLAUDE.md`, `brand/tiktok/stile-tiktok.md`, `brand/tiktok/analisi-riferimenti.md`, la skill `crea-post-tiktok` (`references/brand.md`, `copione.md`, `voce-elevenlabs.md`, `didascalia.md`, `controllo-qualita.md`, `montaggio.md`), la skill editoriale `but-why-finance-post` e le lezioni del post finito `brand/tiktok/output/2026-10-risparmio-quotidiano/` (v2b).

## Scala dei punteggi (uguale per tutti)

| Voto | Significato |
|---|---|
| 5 | pronto da pubblicare, niente da toccare |
| 4 | buono, solo ritocchi migliorativi |
| 3 | funziona ma con un difetto evidente da correggere |
| 2 | difetto serio: il criterio non è rispettato |
| 1 | assente o sbagliato |

Ogni voto ha una motivazione di **una riga**. Un problema **bloccante** porta il criterio a **≤ 2**. La **media** di un valutatore è la media aritmetica dei suoi criteri numerati (una cifra decimale), salvo dove indicato.

## Soglie e condizione di stop

- Un valutatore dà **`"verdetto": "ok"`** solo se ha **0 bloccanti e media ≥ 4,2**; altrimenti `"da_rivedere"`.
- Il ciclo si ferma quando **tutti e quattro** i valutatori dello stesso giro danno `ok`.
- **Massimo 3 giri.** Dopo il terzo giro, se qualcosa resta aperto, si consegna all'utente l'elenco di ciò che resta (bloccanti per primi).
- Un bloccante non si "compensa" con voti alti: anche con media 4,8 un solo bloccante dà `da_rivedere`.

## Conteggio parole e durata (uguale per tutti)

Si contano le parole del campo `text` di `script/scene_elevenlabs.json`, tag `[...]` esclusi, "…" escluso (stesso metodo che dà 75 parole al post della pensione). Durata stimata a **170 parole/min** (ritmo misurato nel post risparmio v2b: 165-175 parole/min dopo l'accorciamento delle pause).

```bash
python3 - <cartella-del-post>/script/scene_elevenlabs.json <<'PY'
import json, re, sys
scene = json.load(open(sys.argv[1], encoding="utf-8"))
tot = 0
for s in scene:
    t = re.sub(r"\[[^\]]*\]", " ", s["text"])
    n = len([w for w in t.split() if re.search(r"\w", w)])
    tot += n
    print(f"scena {s['id']}: {n} parole, ~{n / 170 * 60:.1f} s")
print(f"TOTALE {tot} parole · a 170/min {tot / 170 * 60:.1f} s · a 165-175/min {tot / 175 * 60:.1f}-{tot / 165 * 60:.1f} s")
PY
```

| Parole | Giudizio |
|---|---|
| 60-75 (≈ 21-27 s) | ideale |
| 76-80 | migliorativo: tagliare, salvo motivazione scritta nel changelog |
| > 80 (> ~28 s) | **bloccante**, salvo motivazione esplicita accettata dal valutatore della ritenzione |
| < 50 | migliorativo: probabilmente manca un passaggio (fatto, tesi o domanda) |

Nota: `stile-tiktok.md` e `copione.md` parlano ancora di 140-150 parole/min e ≤ 66 parole; le lezioni del post risparmio (v2b, 170 parole/min) hanno superato quel valore. Qui vale **170 parole/min, ~75 parole max**.

## 1. Verifica dei fatti (`bwf-verifica-fatti`)

| # | Criterio | Bloccante quando |
|---|---|---|
| F1 | **Esattezza dei numeri** (valore, unità, anno, perimetro) | un numero è sbagliato, non trovato, o diverso da quello della fonte |
| F2 | **Qualità delle fonti** (primarie prima: Istat, Eurostat, Banca d'Italia, BCE, MEF, INPS, ARERA, ministeri, Gazzetta Ufficiale) | una cifra poggia su una sola fonte secondaria non confermata, o su fonti discordanti senza dirlo |
| F3 | **Attualità** (data della fonte, notizia superata, dato provvisorio/definitivo) | il dato è stato rivisto/superato, o una misura non approvata è presentata come decisa |
| F4 | **Attribuzione delle tesi** (chi la sostiene, con nome e citazione reale, data, link) | una tesi è attribuita a un soggetto (es. "i sindacati") senza una dichiarazione reale trovata |
| F5 | **Fatto / stima / ipotesi distinti** ("circa" a voce e "~" a schermo per le stime; parti interessate dichiarate) | una stima è detta come fatto; un dato di parte (associazione, azienda) non è dichiarato come tale |
| F6 | **Calcoli** rifatti con Python | un conto non torna (oltre l'arrotondamento dichiarato) |

Stato di ogni cifra: **verificato su fonte originale** · **letto in sintesi** (concordante su ≥ 2 testate indipendenti, va nella lista "da verificare prima di pubblicare") · **non verificabile** (→ **bloccante finché resta nel testo**: o si toglie, o si sostituisce con un dato verificato).

## 2. Ritenzione (`bwf-valuta-ritenzione`)

| # | Criterio | Bloccante quando |
|---|---|---|
| R1 | **Hook nel primo secondo sui tre canali**: voce (prima parola forte: il numero o la parola chiave), testo a schermo **a 0,0 s**, visivo (orso con espressione + oggetto concreto, colpo sonoro) | la prima parola è debole ("Se", "Allora", "Oggi", "Ciao", "Sai", "Ma"), oppure il testo a schermo non è previsto a 0,0 s |
| R2 | **Struttura "Ma perché?"**: domanda detta entro ~6 s, preceduta dalla pausa "…", poi risposta | manca "Ma perché?" o arriva dopo la metà del video |
| R3 | **Ritmo e durata** (tabella parole sopra; frasi corte, un concetto per frase) | > 80 parole senza motivazione |
| R4 | **Cambio visivo ogni ≤ 2 s** possibile con le scene previste (inquadrature, righe di titolo, scritte che entrano) | una scena dura > 4 s con una sola immagine e nessun elemento previsto che entri |
| R5 | **Open loop e payoff**: l'hook promette qualcosa che il video paga | l'hook promette una risposta che il video non dà |
| R6 | **Loop finale**: l'ultima immagine richiama la prima (stesso fondo, oggetto dell'hook, "?") | — (solo migliorativo) |
| R7 | **Chiusura**: frase forte + domanda aperta in seconda persona | il video non finisce con una domanda |
| R8 | **Leggibilità dei testi a schermo**: ≤ 2 righe, 3-5 parole, cifre (non lettere), parola chiave nell'accento, fuori dalle zone sicure | — (migliorativo, salvo testi che coprono gli occhiali: lo segnala il brand) |
| R9 | **SEO TikTok**: 2-4 parole chiave dette a voce **e** scritte a schermo **e** in didascalia (prima riga) | — (migliorativo) |

## 3. Brand (`bwf-valuta-brand`)

| # | Criterio | Bloccante quando |
|---|---|---|
| B1 | **Voce "commercialista al bar"**: calma, diretta, calda; mai allarmista, cattedratica, infantile o da meme | allarmismo o tono da meme |
| B2 | **Neutralità e tesi contrapposte con pari dignità** (stesso spazio, stessa forza delle parole, entrambe attribuite) | il testo si schiera, o una tesi è caricaturale |
| B3 | **Nessuna consulenza** (niente investimenti, prodotti, marche consigliate; consigli di buon senso solo sulla spesa quotidiana, come abitudini) | un consiglio finanziario o un prodotto/marca consigliato |
| B4 | **Fatto / stima / ipotesi e misure "in discussione"** nel linguaggio (lato forma; i numeri li controlla il verificatore) | una misura non approvata detta come decisa |
| B5 | **Regole visive**: accento della rubrica, un solo accento; mai rosso, mai rosso accanto a verde; inchiostro `#111418` solo hook e chiusura, carta `#F4F1EA` le altre; **nessuna scritta nelle immagini**; sagome grigie senza volto; € della maglietta visibile; **occhiali dell'orso mai coperti** da testi o oggetti | una scena chiede scritte nell'immagine, rosso, o un testo/oggetto sopra gli occhiali |
| B6 | **Momento "Sai che…?"** (pillola di economia in verde marchio `#006B3C`, separata dal resto) | — (migliorativo: in 25 s può stare in didascalia o in una riga a schermo) |
| B7 | **Hashtag obbligatori `#butwhyfinance` e `#maperché`** + 2-3 parola chiave/nicchia (totale 3-6) | manca uno dei due obbligatori |
| B8 | **Etichetta IA** ("contenuto generato da IA") nelle note di pubblicazione | manca |
| B9 | **Coerenza** fra `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt` (tre versioni) e `didascalia.md`: stesso testo, stessi numeri, stessa domanda finale, stessi tag | due file dicono testi o numeri diversi |

## 4. Pubblico (`bwf-valuta-pubblico`)

| # | Criterio | Bloccante quando |
|---|---|---|
| P1 | **Chi parte da zero capisce**: ogni termine tecnico è spiegato in parole semplici o sostituito | un termine indispensabile resta oscuro (es. "speranza di vita a 65 anni" senza dire cosa significa) |
| P2 | **Potenziale di commenti** (domanda a cui si risponde in una riga, che divide senza insultare) | domanda chiusa (sì/no retorico) o che invita all'insulto |
| P3 | **Potenziale di condivisione** ("lo mando a…": riguarda la vita di chi guarda) | — |
| P4 | **Potenziale di salvataggio** (un dato o un conto da ritrovare) | — |
| P5 | **Rischio di fraintendimento o polemica sterile** (5 = rischio basso) | una frase, tolta dal contesto, dice una cosa falsa o fa sembrare il canale schierato |
| P6 | **Resta aperto alla discussione** (non chiude con una sentenza) | chiude con una sentenza |

**I 5 parametri della skill editoriale** (voga, discussione, dati reali, scalpore e sua causa, divisione tra correnti di pensiero), 1-5 ciascuno, si riportano a parte: misurano il **tema**, non il testo, quindi **non entrano nella media** e non bloccano. Servono a dire se l'angolo scelto sfrutta il tema (es. tema molto divisivo ma testo che non lo fa emergere → migliorativo su P2/P6).

## 5. Redattore (`bwf-redattore`)

Non dà voti. Applica **tutti i bloccanti** e i migliorativi compatibili con i vincoli:

- ≤ ~75 parole (oltre solo con motivazione nel changelog, mai oltre 80);
- numeri in lettere nel testo per la voce, cifre a schermo; stime con "circa" / "~";
- prima parola forte, "…" prima di "Ma perché?", chiusura frase forte + domanda aperta;
- tag `eleven_v3` in inglese (`[surprised]`, `[curious]`, `[calm]`, `[thoughtful]`, `[warm]`, `[matter-of-fact]`…), tag italiani nella versione 2;
- nessun numero nuovo che non sia "verificato" o "letto in sintesi" nel rapporto `rN-verifica-fatti.md` del giro.

Scrive `revisione/rN-redattore.md` (changelog: cosa ha cambiato e perché, citando il valutatore; cosa ha rifiutato e perché).

## Formato dei rapporti (`revisione/rN-<ruolo>.md`)

```markdown
# Giro N · <ruolo> · <titolo del post>

Data: AAAA-MM-GG · File letti: …

## Punteggi
| # | Criterio | Voto | Motivazione (una riga) |
|---|---|---|---|

## Problemi bloccanti
1. **[fatti-r1-1] (F1)** <problema> — dove (file, scena, riga) — perché blocca.

## Problemi migliorativi
1. **[brand-r1-2] (B6)** …

## Proposte di riscrittura (testo pronto)
- **[fatti-r1-1] Scena 3, voce:** prima «…» → dopo «…» (parole: x → y)
- **[rit-r1-4] didascalia, prima riga:** «…»

## Note per il redattore
<vincoli, cose da non toccare, dubbi>

```json
{"ruolo": "<verifica-fatti|ritenzione|brand|pubblico>", "giro": N, "media": 4.3, "bloccanti": 0, "verdetto": "ok"}
```
```

ID dei problemi: `<ruolo>-r<giro>-<n>` con ruolo `fatti`, `rit`, `brand`, `pub` (es. `fatti-r1-2` = verifica fatti, giro 1, problema 2), così il redattore li cita nel changelog e non si confondono con i codici dei criteri (F1, R3…). Il blocco JSON è **l'ultima cosa del file**, su una riga, valido (punto decimale, non virgola).
