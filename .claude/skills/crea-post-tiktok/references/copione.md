# Copione (`copione.md`)

Esempio completo da imitare: `brand/tiktok/copioni/2026-10-risparmio-quotidiano.md` (nei due post fatti il copione stava in `brand/tiktok/copioni/`; da ora va **dentro la cartella del post** come `copione.md`).

## Parametri

- **Durata 20-30 s, ~55-66 parole di voce.** A 140-150 parole/min, **66 parole = 26-28 s**: dillo all'utente e non superare le 66. Lezione del post del caffè: il copione stimava "~90 parole / 38 s", la colonna voce ne aveva ~150 e il video è venuto 60 s. **Conta le parole davvero** (`wc -w` sul testo della voce, tag esclusi).
- **8 immagini**, una ogni ~3 s (2-4 s), una idea per immagine.
- Se la voce reale esce più lunga: si allungano le immagini, non si accelera il parlato.

## Struttura

| Sec. | Parte | Cosa |
|---|---|---|
| 0-2 | **Hook** | il dato o la domanda "Ma perché…?" su tre canali insieme (sotto). Fondo inchiostro. |
| 2-8 | **Il fatto** | la notizia in una frase, un solo numero |
| 8-20 | **Segui i soldi** | chi paga, chi incassa, cosa cambia per famiglie e imprese; una idea per immagine |
| 20-26 | **Due tesi o consigli** | le due posizioni attribuite, senza schierarsi; oppure 2-3 consigli pratici numerati |
| 26-30 | **Domanda aperta** | domanda al pubblico (non retorica), fondo inchiostro, orso con l'occhiolino, spazio per il fumetto "But Why Finance?" |

Su 20-30 s le parti si comprimono: "segui i soldi" può essere una sola frase. Meglio un concetto in meno che una voce di corsa.

## Hook sui tre canali (primi 2 s, niente logo né intro)

- **Verbale**: la voce parte dal primo fotogramma con il dato o la domanda ("Un caffè al bar ogni giorno costa circa quattrocentosettanta euro all'anno.").
- **Testo**: il numero gigante nel colore d'accento su inchiostro ("~470 €" in IBM Plex Mono) con poche parole intorno.
- **Visivo**: l'orso con l'espressione giusta (sorpreso/pensieroso) e un oggetto concreto (tazzina e scontrino vuoto) che entra con un piccolo colpo sonoro.
- L'hook deve essere **vero**: il video deve pagare la promessa.

## Scrivere per la voce

- Frasi corte, un concetto per frase, tono da **commercialista esperto che spiega al bar**: calmo, neutro, caldo.
- **Numeri in lettere** nel testo per la sintesi vocale ("quattrocentosettanta euro", "ventiquattro per cento", "duemilaventuno", "un euro e ventinove"); a schermo e nei sottotitoli le cifre.
- Nomi difficili scritti come si pronunciano solo nel testo per la voce, se il motore sbaglia ("Asso utenti", "Illi caffè" nel post del caffè); a schermo il nome giusto.
- Stime sempre con **"circa"** nella voce e **"~"** a schermo.
- Tesi sempre attribuite: "Per Assoutenti…", "Secondo Istat…".
- Niente consigli di investimento, niente prodotti, niente marche. Consigli di buon senso solo sulla spesa quotidiana.
- Chiusura: domanda aperta in seconda persona ("E tu, quale piccola spesa taglieresti per prima?").

## Loop e rewatch

- **Loop**: l'ultimo fotogramma richiama il primo (stesso fondo inchiostro, orso nello stesso angolo, un oggetto che "risponde" a quello dell'hook: lo scontrino vuoto → la moneta nel salvadanaio). La domanda finale riporta alla frase d'apertura, così il video riparte senza strappo.
- **Rewatch trigger**: un elemento da rileggere (due numeri a confronto, tre consigli numerati 1 · 2 · 3).

## Modello di `copione.md`

```markdown
# Copione TikTok: "<titolo>"

**Rubrica:** <rubrica> (accento <colore> `#HEX`)
**Formato:** illustrato con l'orso + voce narrante; hook e chiusura su inchiostro `#111418`, il resto su carta `#F4F1EA`
**Durata:** ~<N> s, <N> parole (a 140-150 parole/min), 8 immagini da ~3 s
**Obiettivo:** <commenti / salvataggi / condivisioni, e perché>
**Suono:** voce narrante + base strumentale leggera a -20 dB con licenza commerciale; effetti: <…>
**Etichetta IA:** attivare "contenuto generato da IA". Testi solo in montaggio, mai nelle immagini.
**Fatti e fonti:** [`ricerca.md`](ricerca.md) · **Scene per la voce:** [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json)

## Testo della voce (da approvare)

    [sorpreso] …
    [curioso] …
    [calmo] …
    [pensieroso] …
    [caldo] E tu, …?

## Production doc

| # | Tempo | Immagine | Testo a schermo | Voce (tono) | Suono |
|---|---|---|---|---|---|
| 1 | 0:00-0:03 | **Hook.** Fondo inchiostro; orso sorpreso con <oggetto> | **<NUMERO>** (gigante, accento) | *(sorpreso)* "…" | colpo |
| 2 | 0:03-0:06 | Fondo carta; … | … | *(sorpreso)* "…" | base entra |
| … | | | | | |
| 8 | 0:25-0:28 | **Chiusura.** Fondo inchiostro; orso con l'occhiolino, <oggetto che richiama l'hook>, spazio per il fumetto "But Why Finance?" | **<DOMANDA>** | *(caldo)* "…?" | base sfuma |

Note di montaggio: <durate delle immagini, zoom lento 100%→104% se una scena resta lunga, "~" davanti alle stime, sottotitoli 3-5 parole nelle zone sicure>.

## Hook: i tre canali
- **Verbale:** …
- **Testo:** …
- **Visivo:** …

## Loop e rewatch
- …

## SEO TikTok
- **Parole chiave** (da dire, scrivere a schermo e mettere in didascalia): …
- **Hashtag:** 3-5 parola chiave + nicchia (vedi `didascalia.md`).

## Controllo qualità
- Hook in 1 s su tre canali: …
- Passo: 8 immagini in ~<N> s …
- Tono neutro, tesi attribuite / consigli dichiarati come buon senso: …
- Nessun consiglio di investimento: …
- Numeri: tutti con fonte o marcati come stima: …
- Colori: un solo accento <colore>, carta/inchiostro al posto giusto, niente rosso accanto a verde: …
- Testi solo in montaggio: …
- Domanda finale aperta, ripetuta in didascalia: …
- Da fare: …
```
