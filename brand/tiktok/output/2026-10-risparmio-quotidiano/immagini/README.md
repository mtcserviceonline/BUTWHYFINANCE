# Immagini: risparmio quotidiano (video TikTok)

Le 9 illustrazioni del video "consigli pratici per risparmiare nella vita di tutti i giorni" (8 della prima versione + la **09**, lo scontrino, aggiunta per la v2). Senza testi: titoli, sottotitoli, il conto sullo scontrino e il fumetto "But Why Finance?" si aggiungono in montaggio.

![Anteprima delle 9 immagini](anteprima.jpg)

| File | Contenuto |
|---|---|
| `01.png` … `09.png` | Immagini finali, PNG **1080x1920** (9:16) |
| `prompts.json` | Prompt finale (in inglese) di ogni immagine, con fondo e presenza dell'orso (09 anche con `riferimenti` e `scena`) |
| `scene_09.json` | Scena della 09 (ingresso di `componi_prompt.py`) |
| `anteprima.jpg` | Contact sheet con le 9 immagini affiancate |

La copertina (`../copertina.png`) non è un'immagine generata: è composta da `../script/copertina.py` con l'immagine 01 e i font del brand.

## Le 9 immagini

| # | Fondo | Scena | Tentativo usato |
|---|---|---|---|
| 01 | inchiostro | Orso sorpreso (bocca a "o", zampe aperte), tazzina in primo piano e striscia di scontrino bianca con sole righe grigie | 1° |
| 02 | carta | Fila infinita di tazzine bianche con bordo ambra in prospettiva, orso accanto, sorpreso, zampa sulla guancia | 1° |
| 03 | carta | Orso dietro un tavolo con una grande lente (bordo ambra) sul mucchietto di monetine ambra, curioso | 1° |
| 04 | carta | Sagoma grigia che cammina guardando altrove, dalla tasca cadono monetine ambra; orso più piccolo che indica, incredulo | 1° |
| 05 | carta | Tip 1 abbonamenti: orso con smartphone (icone tonde astratte) e indice alzato; grandi forbici ambra tagliano a metà una tessera grigia | 2° |
| 06 | carta | Tip 2 lista della spesa: orso con foglio a righe e matita ambra, carrello grigio e scaffali grigi sullo sfondo | 3° |
| 07 | carta | Tip 3 luce e gas: bilancia grigia con due fogli a righe (lampadina ambra / fiammella ambra), orso pensieroso con mano al mento | 3° |
| 08 | inchiostro | Orso con occhiolino: la lente dell'occhio che strizza è scura semitrasparente e lascia vedere l'occhio chiuso, l'altra è nera piena con riflesso; infila una moneta ambra in un salvadanaio grigio; spazio libero in alto a destra | 3° (rifatta, vedi sotto) |
| 09 | carta | **v2 (I-4/T-3).** Orso intero a sinistra, curioso, bocca a "o", che tiene in alto un lungo scontrino **vuoto e piatto** (interno bianco ~350x700 px, solo una riga grigia in alto e una in basso, bordo seghettato): in montaggio ci si stampano "1,29 € / × 365 / = 471 €" e "Fonte: Assoutenti (dati MIMIT)" in IBM Plex Mono | 2° |

Nessun rosso, nessun verde oltre alla maglietta dell'orso, unico accento ambra (`#E9A400`), nessuna scritta/lettera/numero.

## Come sono state generate

Stesso metodo del video [`../../2026-10-il-prezzo-del-caffe/`](../../2026-10-il-prezzo-del-caffe/README.md) (script `script/gen.py` e `script/make_prompts.py` di quel video, prompt adattati alle nuove scene):

- API Meta `POST https://api.meta.ai/v1/images/edits` (multipart, autenticazione fatta dal proxy, nessuna chiave), modello `muse-image-1.0`, `size=1024x1792`, `n=1`, `response_format=b64_json`.
- Riferimento sempre `brand/mascotte/mascotte-principale.jpg` come `image[0]`. Per la 08 anche `brand/mascotte/espressioni.jpg` come `image[1]`, per copiare l'occhiolino del set di espressioni.
- Risposta WebP 1152x2016 → ritaglio centrato a 1134x2016 (9:16, 9 px per lato) → ridimensionamento a 1080x1920 (Pillow, Lanczos). Nessuna deformazione.

Struttura del prompt: `Vertical 9:16 illustration…` + [ORSO] + [STILE] + `Scene:` [SCENA] + [FONDO] + [COMPOSIZIONE] + [PALETTE] + [NIENTE TESTO]. Rispetto al video del caffè:

- **ORSO**: aggiunto "euro symbol … clearly visible and not covered by props; plain short sleeves without any symbol" (contro la € coperta o sulla manica).
- **COMPOSIZIONE** (nuovo): "the top 12% and the bottom 18% of the image are completely empty background … nothing touches the bottom edge". Nel video del caffè l'orso e gli oggetti arrivavano al bordo basso.
- **PALETTE**: niente marroni caffè; "No red anywhere, no pink, no blue, no other green objects besides the bear's t-shirt".
- **SAGOMA**: inclusa da subito la frase che nel caffè aveva risolto la maglietta verde ("the whole figure including the torso is plain flat grey with no clothes, no t-shirt, no logo").
- **NIENTE TESTO**: "… any paper is blank or has only abstract grey lines".

## Cosa è stato rigenerato e perché

14 immagini generate in tutto (8 prime prove + 6 rigenerazioni), più 2 richieste fallite con `HTTP 502 upstream request failed` (errore temporaneo del server, ripetute senza modifiche). Nessun blocco del filtro contenuti.

| Img | Problema | Correzione |
|---|---|---|
| 05 | 1ª prova: la tessera era diventata 3-4 rettangoli grigi impilati e non si capiva il taglio; forbici più arancio che ambra | Chiesta "ONE single … card being cut in two", due metà che si separano, forbici con manici ambra pieni. 2ª prova buona |
| 06 | 1ª e 2ª prova: il foglio e il braccio **coprivano la € sulla maglietta**; nella 2ª anche il riflesso degli occhiali era grigio e sbiadito | 3ª prova: foglio tenuto in alto e di lato, "chest and the big yellow euro symbol … completely uncovered" |
| 07 | 1ª prova: fogli, lampadina e fiammella **nella fascia alta** (dove va il titolo). 2ª prova: composizione giusta ma sui fogli **scarabocchi** invece di righe | Scena ricomposta (bilancia a sinistra con i due fogli sui piatti, orso a destra); poi "five neat straight grey horizontal lines … no scribbles". 3ª prova buona |
| 08 | 1ª prova: per l'occhiolino **mancava una lente** (occhiali a "monocolo") e i piedi arrivavano quasi al bordo basso | Aggiunto `espressioni.jpg` come secondo riferimento e "both round black sunglasses lenses are present, one lens shows the closed eye"; orso più piccolo. 2ª prova buona |

01-04 riuscite al primo tentativo.

**09 (v2, 28/10/2026):** stesso metodo, ma con gli script della skill (`componi_prompt.py` → `genera_immagine.py`, scena in `scene_09.json`). 2 tentativi:

| Tentativo | Problema | Correzione |
|---|---|---|
| 1° | Scontrino **stretto** (interno ~220 px: "= 471 €" non ci stava leggibile), attaccato al bordo destro (fino al 96% della larghezza), orso enorme e piedi nel 15% in basso | Orso "SMALL … about 38% of the image height", scontrino "WIDE … about 40% of the image width … ending well before the right edge", "LARGE COMPLETELY EMPTY plain white area" |
| 2° (usato) | Scontrino largo e piatto, vuoto; orso ancora più grande del chiesto (testa dal 22%), scontrino fino al 97% della larghezza, piedi all'81% | Accettato: in montaggio la vista rimpicciolita (80-97%) sposta lo scontrino fuori dalla fascia destra e i piedi sopra i sottotitoli; i controlli di `montage.py` verificano che il conto stampato resti fuori dalle fasce |

**06 non rigenerata:** l'orso è intero e la lista (foglio a righe) si legge; I-6 si risolve nel montaggio (inquadratura con orso intero e titolo "2 ·" sopra la testa).

**08 rifatta (seconda revisione):** nella versione precedente l'occhiolino non si leggeva bene. Richiesta: la lente dell'occhio che strizza deve essere **nera ma trasparente** (lente scura semitrasparente) così che si veda l'occhio chiuso, mentre l'altra resta nera piena con il riflesso bianco diagonale. Al prompt è stata aggiunta, in modo esplicito e ripetuto, la descrizione "see-through dark tinted lens (black outline, translucent dark tint) so the closed, winking eye with a curved lid line is clearly visible through the lens; the other lens stays solid black with the white diagonal glare" (e tolto "eyes never visible" dalla scheda dell'orso, solo per questa immagine). Stessi riferimenti (`mascotte-principale.jpg` + `espressioni.jpg`). **1 tentativo**, riuscito al primo colpo: controllato anche ingrandito sul volto (lente fumé con l'occhio chiuso a linea curva visibile, altra lente nera piena con riflesso, occhiali tondi riconoscibili). Rigenerata anche `anteprima.jpg`.

## Controlli fatti

Ogni immagine guardata intera e, per scontrini e fogli, anche ingrandita: nessuna scritta o cifra, solo righe grigie. Fondo misurato sui bordi e ingombro verticale del contenuto (percentuale dell'altezza, dall'alto):

Ricontrollate il 28/10/2026 con `controlla_immagini.py` (tutte e 9):

| # | Dimensioni | Fondo misurato | Contenuto da… a… (altezza) | Destra fino a | Avvisi |
|---|---|---|---|---|---|
| 01 | 1080x1920 | `#0E1219` (inchiostro) | 14,9% – 84,1% | 97,8% | contenuto nel 10% a destra |
| 02 | 1080x1920 | `#F4F1E9` (carta) | 30,6% – 75,2% | 99,2% | contenuto nel 10% a destra |
| 03 | 1080x1920 | `#F4F1E9` (carta) | 18,2% – 82,4% | 98,0% | contenuto nel 10% a destra |
| 04 | 1080x1920 | `#F4F1E9` (carta) | 26,0% – 84,0% | 98,1% | contenuto nel 10% a destra |
| 05 | 1080x1920 | `#F4F1EA` (carta) | 14,4% – 87,2% | 100,0% | contenuto nel 15% in basso; nel 10% a destra |
| 06 | 1080x1920 | `#F4F1E9` (carta) | 26,9% – 76,9% | 100,0% | contenuto nel 10% a destra |
| 07 | 1080x1920 | `#F4F1E9` (carta) | 40,0% – 87,0% | 99,8% | contenuto nel 15% in basso; nel 10% a destra |
| 08 | 1080x1920 | `#0E1218` (inchiostro) | 23,6% – 80,5% | 97,1% | contenuto nel 10% a destra |
| 09 | 1080x1920 | `#F6F0EA` (carta) | 22,0% – 81,5% | 97,3% | contenuto nel 10% a destra |

Gli avvisi su fascia destra e 15% in basso riguardano le immagini intere: nel video ogni inquadratura è una vista (zoom/spostamento) e `montage.py` controlla fotogramma per fotogramma volto, occhiali e testi (vedi `../README.md`).

**Box degli occhiali e del volto** (per i controlli del montaggio, in `../script/config_video.py` → `OCCHIALI`): misurati a mano su una griglia ogni 100 px e verificati disegnandoli sulle immagini. Il rilevamento automatico (nero pieno + riflesso bianco) è stato provato e scartato: le lenti si fondono con contorni, naso e orecchie e, sul fondo inchiostro, con lo sfondo.

Fascia alta (10%) libera in tutte.

## Difetti noti

- **05 e 07: fascia bassa libera ~13%** invece del 15% (piedi dell'orso e linea del pavimento a 87%). Se il sottotitolo li copre, basta un leggero zoom/spostamento in montaggio o accettare che copra i piedi.
- **Fondo inchiostro** misurato `#0E1219`, non esattamente `#111418` (differenza minima, invisibile a occhio; se in montaggio si affianca un riquadro pieno `#111418` si può notare).
- **03**: il vetro della lente è grigio-azzurro chiaro (unica traccia di azzurro), e la lente copre in parte la spalla; la € resta visibile. Il piano del tavolo è una fascia grigia larga (70-82% dell'altezza).
- **04**: la sagoma ha il profilo del naso accennato (nessun occhio, bocca o dettaglio); le monetine escono dalla tasca davanti, non da quella posteriore.
- **06**: l'orso non sta scrivendo sul foglio: tiene il foglio in una zampa e la matita alzata nell'altra (si legge come "ho fatto la lista"). Le versioni in cui scriveva coprivano la €.
- **07**: la bilancia è un po' inclinata (non in pari); funziona comunque come "confronto tra due offerte". Lampadina e fiammella sono piccole.
- **02**: l'orso è più grande di "piccolo a lato" (circa metà altezza), e la linea del pavimento è irregolare.
- **09**: orso più grande di quanto chiesto e tratto leggermente più liscio (meno ciuffi di pelo) rispetto alle altre; il riflesso degli occhiali è una barra bianca netta. Lo scontrino è un po' storto (bordo sinistro inclinato di ~2°): il conto stampato in montaggio è dritto.
- **08**: l'orso è un po' più grande della versione precedente (testa dal 23,6% dell'altezza), ma l'angolo in alto a destra resta vuoto per il fumetto. La linea dell'occhio chiuso nella lente scura è sottile: si legge bene a schermo intero, meno nelle miniature.

**Coerenza dell'orso:** in tutte e 9 le immagini l'orso è riconoscibile e coerente con `mascotte-principale.jpg`: pelliccia ramata, muso pesca, naso nero con linea, occhiali tondi neri con riflesso bianco diagonale, maglietta verde scuro con € gialla al centro del petto e visibile, contorno nero spesso. Le proporzioni cambiano leggermente tra mezzo busto e figura intera (più tozzo nella 05).

**Su TikTok va attivata l'etichetta "contenuto generato da IA".**
