# Ricerca: argomento e fatti verificati

## 1. Scegliere l'argomento

### Se l'utente ha dato un tema
Parti da quello. Non rimetterlo in discussione: cerca l'angolo "Ma perché?" e la rubrica adatta, poi verifica i fatti. Se i dati non reggono, dillo subito.

### Se non l'ha dato
Cerca con WebSearch (data di oggi nella query, risultati delle ultime 2-4 settimane) due tipi di temi:

- **Notizie economiche italiane recenti**: dati Istat (inflazione, prezzi al consumo, occupazione), bollette e tariffe (ARERA), carburanti (MIMIT, Osservaprezzi), mutui e tassi (Banca d'Italia, BCE), manovra e misure fiscali (MEF, Parlamento), affitti, pensioni, stipendi, prezzi di prodotti simbolo (caffè, pane, pasta, olio).
- **Temi evergreen di vita quotidiana**: piccole spese, abbonamenti, spesa al supermercato, bollette, contante o carta, mance, saldi, costo di un'abitudine, perché una cosa costa quello che costa.

Esempi di query: `Istat inflazione ottobre 2026`, `ARERA bollette gas novembre 2026`, `prezzo medio carburanti MIMIT settimana`, `Banca d'Italia tassi mutui 2026`, `manovra 2027 misure famiglie`, `Assoutenti prezzi`, `Altroconsumo indagine prezzi 2026`.

Criteri per un buon argomento TikTok:
- un **numero concreto** e verificabile da mettere nell'hook;
- tocca la **vita quotidiana** di chi guarda (portafoglio, spesa, casa);
- la domanda **"Ma perché…?"** viene naturale;
- ci sono **due spiegazioni o due tesi** da attribuire, oppure 2-3 consigli pratici di buon senso;
- si racconta in **20-30 s** con 8 immagini concrete (se servono più di 3 concetti, è troppo grande: restringi l'angolo).

Valuta ogni candidato 1-5 su: voga, discussione, dati reali, scalpore (e sua causa), divisione tra correnti di pensiero (stessi parametri della skill Instagram `but-why-finance-post`). Serve a scegliere l'angolo, non a bocciare.

Evita: temi già fatti (guarda `brand/tiktok/output/` e `brand/tiktok/copioni/`), dati vecchi presentati come nuovi, misure non approvate presentate come decise, consigli di investimento o prodotti finanziari.

### Come proporre (in chat)

Proponi **3 argomenti** e chiedi quale scegliere. Formato:

```
1. **Ma perché il gas costa di più a novembre?** · rubrica *Il prezzo di…* (ambra)
   Il fatto: … (fonte, data)
   Angolo: chi incassa la differenza tra prezzo all'ingrosso e bolletta
   Perché può funzionare: tocca tutti, numero chiaro nell'hook, due tesi (fornitori / oneri di sistema)
   Punteggio: voga 4 · discussione 4 · dati 5 · scalpore 3 · divisione 3

2. …
3. …

Quale scegli? Posso anche cambiare angolo o rubrica.
```

Fermati e aspetta la risposta. Se l'utente ha detto "scegli tu", scegli il migliore, scrivi in una riga quale e perché, e prosegui. In ogni caso il tema resta **aperto alla discussione**: la chiusura è una domanda, non una sentenza.

## 2. Fatti verificati

### Fonti, in ordine di preferenza
1. **Fonti primarie**: Istat, Eurostat, Banca d'Italia, BCE, ARERA, MEF, MIMIT (Osservaprezzi), INPS, Agenzia delle Entrate, Gazzetta Ufficiale, Parlamento, Commissione europea, OCSE.
2. **Associazioni e aziende citate per nome** (Assoutenti, Codacons, Altroconsumo, Confcommercio, FIPE, un'azienda del settore): sono parti interessate. Il loro dato si attribuisce sempre ("secondo Assoutenti…").
3. **Giornali e agenzie** (ANSA, Il Sole 24 Ore, Teleborsa, LaPresse…): vanno bene per trovare il dato, ma risali alla fonte originale citata nell'articolo.

### Regole
- Per ogni dato annota: valore, fonte, **data di pubblicazione**, link, se è provvisorio o definitivo.
- Prova ad aprire la fonte originale (WebFetch). Se non ci riesci, il dato resta **"letto solo in sintesi"** e va nella lista da verificare prima di pubblicare (nei due post fatti finora è successo con Assoutenti/MIMIT, illycaffè e arera.it).
- **Mai inventare numeri.** Se un dato non si trova, il copione si adatta (o diventa una domanda), non si stima a occhio.
- Ogni numero **calcolato da noi** è una **stima**: scrivi il calcolo e le ipotesi (es. "1,29 € × 365 giorni = 470,85 €, ipotesi: un caffè tutti i giorni, weekend compresi") e una forbice se le ipotesi cambiano molto. Nel parlato diventa "circa", a schermo "~".
- Se due fonti danno cifre diverse, riportale entrambe e scegli quella attribuibile per nome; non mediare a caso.
- **Tesi contrapposte**: attribuite a chi le sostiene, sullo stesso piano, senza giudizio.
- Consigli pratici senza dati (es. "fai la lista della spesa") sono **osservazioni di buon senso**: dichiaralo e non attribuirli a studi. Niente "latte factor" o teorie discusse spacciate per fatti.
- Controlla la data degli articoli: una fonte vecchia non è una notizia.
- Nessun consiglio di investimento, nessun prodotto finanziario, nessuna marca o servizio consigliati (uno strumento pubblico e gratuito come il Portale Offerte ARERA si può citare in didascalia).

### Modello di `ricerca.md`

```markdown
# Ricerca: <titolo del post>

**Data della ricerca:** AAAA-MM-GG
**Argomento scelto:** <tema> · **Rubrica:** <rubrica> (<accento>) · **Angolo "Ma perché?":** <domanda>
**Alternative proposte:** 1) … 2) … (scartate perché …)

## Fatti

| # | Fatto (come lo usiamo) | Valore | Fonte | Data | Link | Stato |
|---|---|---|---|---|---|---|
| 1 | Prezzo medio dell'espresso al bar | 1,29 € | Assoutenti su dati MIMIT (via Teleborsa) | 18/08/2026 | <url> | letto solo in sintesi |
| 2 | … | … | Istat | … | <url> | verificato su fonte originale |

Stato: **verificato su fonte originale** / **letto solo in sintesi** / **stima nostra** / **non verificabile (non usato)**.

## Stime nostre

| Stima | Calcolo | Ipotesi | Forbice |
|---|---|---|---|
| Un caffè al giorno ≈ 470 €/anno | 1,29 × 365 = 470,85 | un caffè tutti i giorni dell'anno | 323-511 € (250 giorni lavorativi; prezzi 1,20-1,40 €) |

## Tesi a confronto

| Tesi | Chi la sostiene | Fonte |
|---|---|---|
| … | … | … |

## Affermazioni senza dati
- "<frase del copione>": osservazione di buon senso, non sostenuta da dati; detta come constatazione.

## Da verificare prima di pubblicare
- [ ] Aprire la fonte originale di … e confermare …
```
