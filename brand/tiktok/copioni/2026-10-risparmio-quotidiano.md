# Copione TikTok: "Il prezzo di… un caffè al giorno" (risparmio quotidiano)

**Rubrica:** Il prezzo di… (accento ambra `#E9A400`, numeri e scontrino in IBM Plex Mono). Il video parte dal prezzo di un'abitudine e chiude con tre consigli pratici.
**Formato:** illustrato con l'orso + voce narrante; hook e chiusura su inchiostro `#111418`, spiegazioni e consigli su carta `#F4F1EA`
**Durata:** ~25 s, ~66 parole, 8 immagini da ~3 s (2-4 s)
**Obiettivo:** commenti (domanda aperta sulla spesa da tagliare) e salvataggi (tre consigli da ricordare)
**Suono:** audio originale (voce narrante) + base strumentale leggera a -20 dB, con licenza commerciale
**Etichetta IA:** attivare "contenuto generato da IA" se le immagini sono generate o la voce è sintetica. Il testo si aggiunge sempre in montaggio, mai dentro le immagini.
**Scene per la voce:** [`../output/2026-10-risparmio-quotidiano/script/scene_elevenlabs.json`](../output/2026-10-risparmio-quotidiano/script/scene_elevenlabs.json) (tono, tag v3, stability/style e immagini per ogni scena)

## Testo della voce (approvato)

> **Aggiornato il 28/10/2026 con il testo effettivamente registrato** (voce ElevenLabs "Valerio – Warm Italian Storyteller", [`voce.mp3`](../output/2026-10-risparmio-quotidiano/voce.mp3), 24,0 s, verificato trascrivendo l'audio): l'ultima frase è **"Non serve cambiare vita, basta iniziare a guardare le piccole spese."** al posto della domanda "E tu, quale piccola spesa taglieresti per prima?". La domanda per i commenti resta nella didascalia. Il video montato è in [`../output/2026-10-risparmio-quotidiano/`](../output/2026-10-risparmio-quotidiano/README.md).

```
[sorpreso] Un caffè al bar ogni giorno costa circa quattrocentosettanta euro all'anno. Ma perché non ce ne accorgiamo?
[curioso] Perché sono piccole spese, e le piccole spese non le guardiamo mai.
[calmo] Primo: controlla gli abbonamenti che non usi.
[calmo] Secondo: fai la lista prima di andare al supermercato.
[pensieroso] Terzo: confronta le offerte di luce e gas una volta all'anno.
[caldo] Non serve cambiare vita, basta iniziare a guardare le piccole spese.
```

## Fatti da verificare prima di pubblicare

| Dato o affermazione | Fonte | Nota |
|---|---|---|
| Un caffè al giorno ≈ 470 € all'anno | **Calcolo nostro:** 1,29 € × 365 giorni = 470,85 €. Il prezzo medio dell'espresso al bar (1,29 €) è di Assoutenti su dati del Ministero delle Imprese, [Teleborsa, 18 ago 2026](https://www.teleborsa.it/News/2026/08/18/prezzi_caffe_al_bar_%2b_24_2percento_in_cinque_anni-115.html) | **stima, da verificare** sulla fonte originale (Assoutenti/MIMIT): l'ho letta solo in sintesi. Ipotesi: un caffè tutti i giorni dell'anno, weekend e ferie compresi. Con i prezzi città per città (1,20-1,40 €, [Altroconsumo](https://www.altroconsumo.it/alimentazione/fare-la-spesa/news/aumento-costo-caffe), giugno 2026) si va da ~438 a ~511 €; con un caffè solo nei giorni lavorativi (~250) si scende a ~323 €. Per questo la voce dice "circa" e il testo a schermo usa "~". |
| "Le piccole spese non le guardiamo mai" | nessuna | osservazione generica, non un dato: va detta come constatazione, senza attribuirla a studi. Non citare il "latte factor" o simili, che sono discussi. |
| Controllare gli abbonamenti che non si usano | nessuna | consiglio generico di buon senso, **non sostenuto da dati** nel video. Nessun servizio citato per nome. |
| Fare la lista prima di andare al supermercato | nessuna | consiglio generico di buon senso, **non sostenuto da dati** nel video. |
| Confrontare le offerte di luce e gas una volta all'anno | strumento esistente: il [Portale Offerte](https://www.ilportaleofferte.it) di ARERA, sito pubblico e gratuito per confrontare le offerte luce e gas (attivo dal 2018, [comunicato ARERA](https://www.arera.it/comunicati-stampa/dettaglio/it/com-stampa/18/180918)) | **la frequenza "una volta all'anno" non è sostenuta da una fonte**: nelle ricerche non ho trovato una raccomandazione ufficiale su ogni quanto confrontare. Va presentata come abitudine consigliata, non come regola. Una notizia secondaria ([Segugio](https://tariffe.segugio.it/news-tariffe/luce-e-gas-come-cambiano-portale-offerte-e-portale-consumi-00047753.aspx)) parla di un rinnovo del Portale (delibera 268/2026/R/com): verificarlo su arera.it prima di citarlo. Non ho potuto aprire arera.it da qui. |

Da fare: aprire la fonte originale Assoutenti/MIMIT e confermare 1,29 € prima di registrare la voce; se il prezzo medio è cambiato, rifare il conto (prezzo × 365) e aggiornare voce, testo a schermo e didascalia.

## Production doc

| # | Tempo | Immagine | Testo a schermo | Voce (tono) | Suono |
|---|---|---|---|---|---|
| 1 | 0:00-0:03 | **Hook.** Fondo inchiostro; orso sorpreso (espressione "sorpreso") con una tazzina e uno scontrino vuoto | **CAFFÈ AL GIORNO: ~470 € ALL'ANNO** ("~470 €" gigante, ambra, IBM Plex Mono) | *(sorpreso)* "Un caffè al bar ogni giorno costa circa 470 euro all'anno." | colpo di scontrino |
| 2 | 0:03-0:06 | Fondo carta; lunga fila di tazzine uguali che si perde in lontananza, orso che la guarda sorpreso | resta **CAFFÈ AL GIORNO: ~470 € ALL'ANNO** (facoltativo: "MA PERCHÉ?" sotto, piccolo) | *(sorpreso)* "Ma perché non ce ne accorgiamo?" | base musicale entra |
| 3 | 0:06-0:08 | Fondo carta; orso con lente d'ingrandimento su un mucchietto di monetine | **PICCOLE SPESE** | *(curioso)* "Perché sono piccole spese," | |
| 4 | 0:08-0:10 | Fondo carta; sagoma grigia senza volto che guarda altrove mentre cadono monetine | resta **PICCOLE SPESE** | *(curioso)* "e le piccole spese non le guardiamo mai." | tintinnio leggero di monete |
| 5 | 0:10-0:13 | **Consiglio 1.** Fondo carta; forbici ambra che tagliano una tessera/abbonamento, orso accanto con lo smartphone | **1 · ABBONAMENTI** | *(calmo)* "Primo: controlla gli abbonamenti che non usi." | taglio di forbici |
| 6 | 0:13-0:17 | **Consiglio 2.** Fondo carta; orso con la lista della spesa (foglio e matita) davanti a un carrello, sagome di scaffali | **2 · LISTA DELLA SPESA** | *(calmo)* "Secondo: fai la lista prima di andare al supermercato." | fruscio di carta |
| 7 | 0:17-0:21 | **Consiglio 3.** Fondo carta; orso pensieroso con due fogli di offerta affiancati, una lampadina e una fiammella del gas | **3 · LUCE E GAS** | *(pensieroso)* "Terzo: confronta le offerte di luce e gas una volta all'anno." | |
| 8 | 0:21-0:25 | **Chiusura.** Fondo inchiostro; orso con l'occhiolino, salvadanaio con una moneta, spazio libero per il fumetto "But Why Finance?" (aggiunto in montaggio) | **BASTA GUARDARE LE PICCOLE SPESE** (prima: "E TU? QUALE TAGLIERESTI?") | *(caldo)* "Non serve cambiare vita, basta iniziare a guardare le piccole spese." (registrato; prima: "E tu, quale piccola spesa taglieresti per prima?") | moneta nel salvadanaio |

Note di montaggio:
- Il numero 470 è sempre preceduto da "~" a schermo e da "circa" nella voce.
- Le immagini 3 e 4 durano ~2 s, le 6, 7 e 8 ~4 s: se la voce reale allunga le scene finali, aggiungere un leggero zoom (100% → 104%) invece di nuove immagini. Se la voce supera i 25 s, allungare le immagini, non accelerare il parlato.
- Sottotitoli sincronizzati con la voce (3-5 parole alla volta) oltre ai titoli della colonna "Testo a schermo"; rispettare le zone sicure di TikTok.

## Hook: i tre canali

- **Verbale:** "Un caffè al bar ogni giorno costa circa 470 euro all'anno." (la voce parte dal primo fotogramma)
- **Testo:** "~470 €" gigante in ambra su inchiostro, con "CAFFÈ AL GIORNO … ALL'ANNO" più piccolo in carta.
- **Visivo:** orso sorpreso con tazzina e scontrino vuoto, lo scontrino entra con un colpo. Niente logo né intro.

## Loop e rewatch

- L'ultimo fotogramma (inchiostro, orso con l'occhiolino, salvadanaio con una moneta) richiama il primo (inchiostro, orso sorpreso, tazzina e scontrino vuoto): stesso fondo, orso nello stesso angolo, la moneta nel salvadanaio "risponde" allo scontrino vuoto. La frase finale ("…basta iniziare a guardare le piccole spese") porta naturalmente alla frase d'apertura sul caffè, così il video riparte senza strappo.
- Il rewatch trigger sono i tre consigli numerati (1 · 2 · 3): brevi, da salvare o rileggere.

## SEO TikTok

- **Parole chiave** (parlato + testo + didascalia): come risparmiare, consigli per risparmiare, risparmio quotidiano, piccole spese, abbonamenti, lista della spesa, bollette luce e gas.
- **Hashtag:** #risparmio #finanzapersonale #bollette #consiglipratici #imparacontiktok (parole chiave + nicchia, non solo hashtag generici).

## Didascalia (bozza)

> Un caffè al bar ogni giorno costa circa 470 € all'anno (stima: 1,29 € a tazzina, prezzo medio secondo Assoutenti, per 365 giorni). Non è il caffè il problema: sono le piccole spese che non guardiamo. Tre abitudini semplici: controllare gli abbonamenti che non usi, fare la lista prima della spesa, confrontare le offerte di luce e gas (c'è il Portale Offerte pubblico di ARERA). E tu, quale piccola spesa taglieresti per prima? 👇
> #risparmio #finanzapersonale #bollette #imparacontiktok

## Controllo qualità

- Hook in 1 s su tre canali: sì (voce, "~470 €" in ambra, orso sorpreso).
- Passo: 8 immagini in ~25 s, un'immagine nuova ogni ~3 s, nessuna pausa lunga.
- Tono: neutro e calmo, nessun giudizio su chi beve il caffè al bar; il 470 è dichiarato come stima ("circa").
- Nessun consiglio di investimento né prodotto finanziario: solo abitudini di spesa quotidiana; nessun fornitore, servizio o marca citati per nome (il Portale Offerte ARERA solo in didascalia, come strumento pubblico).
- Colori: ambra come unico accento (titoli, forbici, "~470 €"); carta per le spiegazioni, inchiostro per hook e chiusura; niente rosso accanto a verde (la fiammella del gas va in blu, non rossa/arancio accanto alla maglietta verde dell'orso; il verde marchio compare solo sulla maglietta e sul fumetto del logo).
- Testi solo in montaggio: le immagini non devono contenere scritte (scontrino vuoto, fogli di offerta senza cifre leggibili).
- Domanda aperta per i commenti: nella voce registrata non c'è più (la chiusura è "Non serve cambiare vita, basta iniziare a guardare le piccole spese."), resta **solo in didascalia**.
- Da fare: verifica della fonte Assoutenti/MIMIT. Voce registrata (ElevenLabs, 28/10/2026) e video montato: vedi [`../output/2026-10-risparmio-quotidiano/README.md`](../output/2026-10-risparmio-quotidiano/README.md).
