# Immagini del post

Esempio da imitare: `brand/tiktok/output/2026-10-risparmio-quotidiano/immagini/` (README, prompts.json, anteprima.jpg). Metodo e problemi anche in `brand/tiktok/output/2026-10-il-prezzo-del-caffe/README.md`.

## Principi

- **~8 immagini 9:16** (una ogni ~3 s), numerate `01.png`… nell'ordine del production doc.
- **Una idea = una immagine = un oggetto concreto** (un concetto astratto diventa una cosa: catena, bilancia, forbici, salvadanaio, fila di tazzine). Stile Video 2 di @cashfoxclub0: illustrazione piatta, fondo uniforme quasi vuoto, personaggio sempre uguale.
- 01 (hook) e l'ultima (chiusura) su **inchiostro**, le altre su **carta**. L'ultima richiama la prima (loop).
- Orso in quasi tutte le immagini, con l'espressione della scena; altre persone = sagome grigie senza volto.
- Regole vincolanti: vedi `brand.md` → "Regole vincolanti per le immagini".

## 1. Scrivere le scene (`immagini/scene.json`)

Una voce per immagine, in **inglese**, partendo dalla colonna "Immagine" del production doc:

```json
{
  "accento": "ambra",
  "immagini": [
    {"id": "01", "orso": true, "fondo": "inchiostro",
     "scena": "Medium-full shot of the bear, centered, looking SURPRISED: mouth open in a small round 'o' shape, eyebrows raised above the sunglasses, both paws open and raised slightly in astonishment. In the foreground, in front of him at chest height on a small floating saucer, a small white espresso cup, and next to it a long strip of BLANK white paper receipt curling down, with only a few short abstract grey lines and no print."},
    {"id": "04", "orso": true, "fondo": "carta",
     "scena": "On the left, a full-body {SAGOMA} walking toward the left and looking away; from a small hole in the back pocket a trail of plain {ACCENTO} coins, plain discs without symbols, falls to the ground. On the right, the bear, smaller, full body, INCREDULOUS, one paw pointing at the falling coins."}
  ]
}
```

Segnaposto: `{SAGOMA}` / `{SAGOME}` = persona/e grigia/e senza volto e senza vestiti; `{ACCENTO}` = nome + esadecimale del colore della rubrica (scrivi "plain {ACCENTO} coins", non "golden {ACCENTO}").

Consigli per la scena (da quello che ha funzionato):
- Emozione in MAIUSCOLO con la formula collaudata (tabella in `brand.md`).
- Dì **dove** sta l'orso e **quanto è grande** ("on the right, full body, smaller, about half the image height"). Preferisci **figura intera piccola** o **mezzo busto dietro un tavolo/bancone**: il mezzo busto "nel vuoto" esce enorme, col torso tagliato netto e le braccia che toccano i bordi (prova di questa skill).
- Gli oggetti in mano vanno **tenuti di lato o in alto**, "so the euro symbol on his t-shirt stays uncovered".
- Un oggetto forte per immagine; se ce ne sono due da confrontare, mettili su una bilancia o affiancati.
- Fogli, scontrini, schermi: "BLANK", "only neat straight grey horizontal lines", "abstract round grey icons, no text".
- Per l'occhiolino basta scrivere "WINKING like the winking face in the second reference image" nella scena: se la scena contiene "wink", `componi_prompt.py` aggiunge `espressioni.jpg` come secondo riferimento, la frase della **lente fumé** (occhio chiuso visibile attraverso una lente scura semitrasparente, l'altra nera piena con riflesso) e toglie "eyes never visible" dalla scheda dell'orso.

## 2. Comporre i prompt (`immagini/prompts.json`)

```bash
K=.claude/skills/crea-post-tiktok/scripts
P=brand/tiktok/output/AAAA-MM-slug
python3 $K/componi_prompt.py $P/immagini/scene.json $P/immagini/prompts.json
```

Struttura di ogni prompt (blocchi fissi nello script, gli stessi del post risparmio più la fascia destra e la precisazione sull'ambra):
`Vertical 9:16 illustration…` + [ORSO] + [STILE] + `Scene:` [SCENA] + [FONDO inchiostro/carta] + [COMPOSIZIONE: 12% in alto e 18% in basso vuoti, niente al bordo basso, fascia destra libera] + [PALETTE: accento della rubrica, niente rosso/rosa/blu/altri verdi] + [NIENTE TESTO: "Absolutely no text, no letters, no numbers, no words, no labels, no logo, no watermark…"].

`prompts.json` (stesso formato della risparmio, con in più `riferimenti` e `scena`): `{"01": {"bear": true, "background": "inchiostro #111418", "riferimenti": ["brand/mascotte/mascotte-principale.jpg"], "scena": "…", "prompt": "…"}}`. Se rigeneri con un prompt corretto a mano, aggiorna anche `prompts.json`: deve contenere il prompt **finale** di ogni immagine.

## 3. Generare

```bash
for i in 01 02 03 04 05 06 07 08; do
  python3 $K/genera_immagine.py --prompts $P/immagini/prompts.json --id $i --out $P/immagini/$i.png
done
```

Cosa fa `genera_immagine.py`:
- `POST https://api.meta.ai/v1/images/edits`, multipart, `model=muse-image-1.0`, `size=1024x1792`, `n=1`, `response_format=b64_json`, riferimenti come `image[0]`, `image[1]`… (indici consecutivi da 0; `image[]` è rifiutato). Default `image[0]` = `brand/mascotte/mascotte-principale.jpg`.
- Senza orso e senza riferimenti (`"bear": false` o `--senza-riferimento`) usa `POST /v1/images/generations` (JSON). Parametri accettati: `model`, `prompt`, `size`, `n`, `response_format`, `output_format`, `user`; **non** accetta `quality`, `style`, `seed`, `negative_prompt`, `aspect_ratio`, `mask`.
- **Nessuna chiave**: autentica il proxy.
- Risposta WebP **1152x2016** → ritaglio centrale **1134x2016** → **1080x1920** (Lanczos), senza deformare (`ritaglia_916.py`, usabile anche da solo).
- 10-30 s per immagine. Ritenta da solo su 5xx ed errori di rete (5 s, 10 s, 20 s); su 4xx esce con codice 2 senza ritentare (filtro contenuti: riformula).
- `--originale file.webp` salva anche la risposta grezza (non committarla).

Si possono lanciare più generazioni in parallelo (2-4 alla volta) se il tempo conta.

## 4. Guardare e correggere

1. **Guarda ogni immagine con Read**, intera; ingrandisci (ritaglio con Pillow) scontrini, fogli e schermi per cercare scritte.
2. Controlli misurati: `python3 $K/controlla_immagini.py $P/immagini --prompts $P/immagini/prompts.json` → tabella (fondo misurato, ingombro verticale, fascia destra, avvisi) da incollare nel README delle immagini. Non sostituisce lo sguardo.
3. Rigenera **solo le immagini difettose**, correggendo il prompt sul difetto preciso (tabella sotto). **Massimo 3 tentativi per immagine**; se al terzo resta un difetto minore, tieni la migliore e scrivilo in "Difetti noti".
4. Anteprima: `python3 $K/anteprima.py $P/immagini` → `immagini/anteprima.jpg` (4 colonne, 1130x990 con 8 immagini). Guardala con Read: coerenza dell'orso e alternanza dei fondi si vedono meglio affiancate.

## Problemi noti e come evitarli

| Problema | Dove è successo | Rimedio |
|---|---|---|
| **€ sulla manica** e braccio deformato nei primi piani della zampa | caffè 05 | niente primi piani della zampa; "plain short sleeves without any symbol" (già nel blocco ORSO) |
| **€ coperta** da fogli, braccia, lente | risparmio 06 (2 prove), caffè 13-14 | oggetti tenuti "high and to the side", "chest and the big yellow euro symbol completely uncovered and clearly visible" |
| **Scritte, cifre, scarabocchi** su fogli/scontrini/calendari | riferimenti IA; risparmio 07 (scarabocchi) | "BLANK", "five neat straight grey horizontal lines… no scribbles, no words"; testi sempre in montaggio |
| **Forbici (o oggetti ambra) arancio invece che ambra** | risparmio 05 | "solid amber (#E9A400) handles", la palette dice "amber objects are golden yellow, not orange" |
| **Oggetto moltiplicato** (tessera diventata 3-4 rettangoli) | risparmio 05 | "ONE single …", descrivere l'azione (due metà che si separano) |
| **Sagoma con vestiti colorati o logo** (maglietta verde con un orso) | caffè 12 | blocco `{SAGOMA}`: "the whole figure including the torso is plain flat grey with no clothes, no t-shirt, no logo" |
| **Sagoma con profilo del viso** accennato | risparmio 04 | accettabile se non ha occhi/bocca; altrimenti "smooth head like a mannequin, no nose" |
| **Contenuto nelle fasce alta/bassa** (oggetti dove va il titolo, piedi al bordo basso) | caffè (tutte, orso fino al bordo); risparmio 07, 05 (13% libero in basso) | blocco COMPOSIZIONE (12% / 18%); scena "the whole scene is in the middle of the image, nothing in the top part"; orso più piccolo |
| **Fascia destra occupata** (oggetti fino al bordo destro) | tutte le immagini dei due post (misurato: contenuto fino al 97-100% della larghezza) | frase sulla fascia destra nel blocco COMPOSIZIONE (nuova: verificata su una sola prova); orso "on the left/center"; se resta, tenere l'elemento importante lontano dall'angolo in basso a destra dove stanno i pulsanti |
| **Mezzo busto tagliato nel vuoto**, braccia ai bordi | prova di questa skill | figura intera piccola o mezzo busto dietro un tavolo/bancone |
| **Occhiolino senza una lente** (monocolo) | risparmio 08, 1ª prova | `espressioni.jpg` come `image[1]` + "both lenses present, same round size, joined by the black bridge" |
| **Occhiolino che non si legge** (lente nera piena, occhio chiuso invisibile) | risparmio 08, 2ª versione | lente fumé: "see-through dark tinted lens … the closed, winking eye with a curved lid line is clearly visible through the lens; the other lens stays opaque solid black with the white diagonal glare", e senza "eyes never visible" nella scheda (lo fa `componi_prompt.py`). Riuscita al primo colpo; la linea dell'occhio è sottile e si legge meno nelle miniature |
| **Riflesso degli occhiali grigio/sbiadito** | risparmio 06 | rigenerare; il blocco ORSO chiede "one white diagonal glare stripe on each lens" |
| **Filtro dei contenuti** (richiesta bloccata, HTTP 4xx) | caffè 11 ("carrying on his shoulders, bending under the weight") | riformulare senza fatica/peso fisico/pericolo: "holds the sack in both arms, the sack looks heavy" |
| **HTTP 502 `upstream request failed`** | risparmio (2 volte) | temporaneo: ritentare uguale (lo script lo fa da solo) |
| **Inquadratura diversa da quella chiesta** (chiesto "waist up", uscito figura intera) | caffè 01 | se il risultato funziona, tienilo e annotalo; altrimenti dire la misura ("about 40% of the image height") |
| **Fondo inchiostro misurato `#0E1219`** invece di `#111418` | risparmio 01, 08 | invisibile a occhio; in montaggio campionare il colore reale del fondo (come fa `montage.py`) invece di affiancare un riquadro `#111418` |
| **Oggetti piccoli o poco leggibili** (lampadina, fiammella) | risparmio 07 | "big", "large", "the main prop"; un solo oggetto forte |

## Modello di `immagini/README.md`

```markdown
# Immagini: <titolo> (video TikTok)

Le <N> illustrazioni del video. Senza testi: titoli, sottotitoli e il fumetto "But Why Finance?" si aggiungono in montaggio.

![Anteprima delle <N> immagini](anteprima.jpg)

| File | Contenuto |
|---|---|
| `01.png` … `0N.png` | Immagini finali, PNG 1080x1920 (9:16) |
| `scene.json` | Scene in inglese (ingresso di `componi_prompt.py`) |
| `prompts.json` | Prompt finale di ogni immagine, con fondo e riferimenti |
| `anteprima.jpg` | Contact sheet |

## Le <N> immagini

| # | Fondo | Scena | Tentativo usato |
|---|---|---|---|
| 01 | inchiostro | … | 1° |

Unico accento <colore> (`#HEX`), nessun rosso, nessuna scritta/lettera/numero.

## Come sono state generate
API Meta `POST /v1/images/edits`, `muse-image-1.0`, `size=1024x1792`, riferimento `brand/mascotte/mascotte-principale.jpg` (`image[0]`) [+ `espressioni.jpg` per …]; WebP 1152x2016 → 1134x2016 → 1080x1920. Script: `.claude/skills/crea-post-tiktok/scripts/`.

## Cosa è stato rigenerato e perché
<N> immagini generate in tutto (<N> prime prove + <N> rigenerazioni), <N> richieste fallite (502 / filtro).

| Img | Problema | Correzione |
|---|---|---|

## Controlli fatti
<tabella di controlla_immagini.py>

## Difetti noti
- …

**Coerenza dell'orso:** …

**Su TikTok va attivata l'etichetta "contenuto generato da IA".**
```
