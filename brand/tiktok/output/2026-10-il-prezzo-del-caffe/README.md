# Il prezzo di… un caffè — video TikTok (prima versione)

Realizzazione del copione [`../../copioni/2026-10-il-prezzo-del-caffe.md`](../../copioni/2026-10-il-prezzo-del-caffe.md).

## Prima di pubblicare (obbligatorio)

1. **I numeri del copione vanno ancora verificati sulle fonti originali** (Assoutenti/MIMIT per 1,04 € → 1,29 € e +24%; intervista a Cristina Scocchia di illycaffè per arabica +80% e "sotto la media 2025"). Sono stati usati così come sono nel copione, senza verifica.
2. **Su TikTok va attivata l'etichetta "contenuto generato da IA"**: tutte le immagini sono generate con IA e la voce è sintetica.
3. **La voce è provvisoria** (vedi sotto): ElevenLabs non era utilizzabile. Si consiglia di rigenerarla con ElevenLabs prima di pubblicare.

## File

| File | Contenuto |
|---|---|
| `video.mp4` | Video finale: 1080x1920, 30 fps, H.264 + AAC 48 kHz, **60,6 s**, 14 MB, audio a -14,3 LUFS (picco -1,4 dBFS) |
| `voce.mp3` | Solo voce narrante, normalizzata a -14 LUFS |
| `immagini/01.png` … `20.png` | Le 20 illustrazioni finali, senza testi (1152x2016) |
| `tempi.json` | Inizio/fine di ogni inquadratura e tempi di ogni sottotitolo |
| `script/` | Script usati, per rifare o modificare il video (vedi "Come rifarlo") |

## Struttura del video

21 inquadrature da 20 immagini (l'ultima riusa l'immagine 01 per il loop). Un'immagine nuova ogni **2,9 s** in media. Tagli netti, zoom lento 100%→104% su ogni immagine, titolo con dissolvenza di 4 fotogrammi (sull'hook un piccolo "colpo" di scala insieme all'effetto sonoro).

| # | Tempo (s) | Immagine | Titolo a schermo | Voce |
|---|---|---|---|---|
| 1 | 0,0-4,4 | 01 | CAFFÈ **+24%** | Il caffè al bar costa il 24% in più di cinque anni fa. |
| 2 | 4,4-5,5 | 02 | MA **PERCHÉ?** | Ma perché? |
| 3 | 5,5-9,6 | 03 | NEL 2021 / **1,04 €** | Nel 2021 una tazzina costava 1,04 euro. |
| 4 | 9,6-11,9 | 04 | 1,04 € → **1,29 €** (+ numeri sugli scontrini) | Oggi, in media, 1,29. |
| 5 | 11,9-14,4 | 05 | **+25** CENTESIMI | Sono 25 centesimi in più. |
| 6 | 14,4-16,5 | 06 | QUALCUNO INCASSA **DI PIÙ?** | Chi incassa questa differenza? |
| 7 | 16,5-18,5 | 07 | **DUE** SPIEGAZIONI | Ci sono due spiegazioni. |
| 8 | 18,5-20,9 | 08 | **PRIMA TESI** / IL CAFFÈ CRUDO | Prima tesi: costa di più la materia prima. |
| 9 | 20,9-23,7 | 09 | ARABICA **+80%** | L'arabica è salita dell'80%. |
| 10 | 23,7-27,0 | 10 | ARABICA **+80%** / TAZZINA **+24%** | Ma la tazzina è salita solo del 24%. |
| 11 | 27,0-30,4 | 11 | **SECONDO ILLYCAFFÈ** / I BAR HANNO ASSORBITO UNA PARTE | Per illycaffè, parte dell'aumento l'hanno assorbita i bar. |
| 12 | 30,4-33,0 | 12 | **SECONDA TESI** / GESTIRE IL BAR | Seconda tesi: costa di più gestire un bar. |
| 13 | 33,0-37,2 | 13 | **SECONDO ASSOUTENTI** / ENERGIA E COSTI DI GESTIONE | Per Assoutenti pesano energia e costi di gestione, non il caffè. |
| 14 | 37,2-39,7 | 14 | CHI HA **RAGIONE?** | Le due cose possono essere vere insieme. |
| 15 | 39,7-43,0 | 15 | QUANTO PESA **OGNI VOCE?** | Dipende da quanto pesa ogni voce sul conto del bar. |
| 16 | 43,0-47,0 | 16 | CAFFÈ VERDE: SOTTO LA MEDIA **2025** | E oggi il caffè crudo vale meno della media del 2025. |
| 17 | 47,0-50,5 | 17 | E LA **TAZZINA?** | Ma il prezzo alla tazzina potrebbe non seguirlo subito. |
| 18 | 50,5-52,2 | 18 | CHI **PAGA?** | Alla fine, qualcuno paga: |
| 19 | 52,2-54,7 | 19 | CHI **PAGA?** + etichette CLIENTE · BAR · TORREFATTORE | il cliente, il bar o il torrefattore. |
| 20 | 54,7-57,5 | 20 | QUANTO DOVREBBE COSTARE UN **CAFFÈ?** + fumetto "But Why Finance?" | E per te? Quanto dovrebbe costare un caffè al bar? |
| 21 | 57,5-60,6 | 01 | E CHI ASSORBE **L'AUMENTO?** | E chi dovrebbe assorbire l'aumento? |

In grassetto le parti in ambra `#E9A400`. Fondo inchiostro `#111418` su hook (1) e chiusura (20-21), carta `#F4F1EA` su tutto il resto. Il verde marchio `#006B3C` compare solo nel fumetto. Nessun rosso.

**Loop:** l'ultima inquadratura è la stessa immagine della prima (orso sorpreso, tazzina, scontrino bianco senza totale) con un'altra domanda: il video riparte senza strappo.

**Sottotitoli:** IBM Plex Sans Condensed Bold 86 px, bianchi con contorno inchiostro di 9 px, 3-5 parole (al massimo 2 righe), centrati a y≈1440 (fuori dal 15% in basso), una parola chiave in ambra. **Titoli:** IBM Plex Sans Condensed Bold (ridotti in automatico per stare nella larghezza utile); numeri di prezzo e scontrini in IBM Plex Mono Bold. Testo sempre tra x=60 e x=950 (la fascia destra dei pulsanti resta libera) e sotto y=215 (sotto il 10% in alto).

**Font:** IBM Plex Sans Condensed (Bold, SemiBold) e IBM Plex Mono (Bold) scaricati dal repository `google/fonts` (licenza OFL). Non sono inclusi qui.

## Immagini: API Meta (`muse-image-1.0`)

L'endpoint è compatibile con OpenAI. Nessuna chiave: l'autenticazione la fa il proxy.

- `POST https://api.meta.ai/v1/images/generations` (JSON): parametri accettati `model`, `prompt`, `size` ("WxH"), `n`, `response_format` (`url` | `b64_json`), `output_format`, `user`. **Non** accetta `quality`, `style`, `seed`, `negative_prompt`, `aspect_ratio`.
- `POST https://api.meta.ai/v1/images/edits` (multipart): stessi parametri più **immagini di riferimento** come `image[0]`, `image[1]`… (indici consecutivi da 0; `image[]` viene rifiutato). In JSON si usa invece `images: [{"image_url": …} | {"file_id": …}]`. Niente `mask`.
- Con `size=1024x1792` restituisce un WebP **1152x2016** (circa 9:16). 10-30 s per immagine.

Esempio (immagine con l'orso, riferimento `mascotte-principale.jpg`):

```bash
curl -s https://api.meta.ai/v1/images/edits \
  -F model=muse-image-1.0 -F size=1024x1792 -F n=1 -F response_format=b64_json \
  -F "prompt=$(cat prompt.txt)" \
  -F "image[0]=@brand/mascotte/mascotte-principale.jpg" \
  | python3 -c "import sys,json,base64;open('out.webp','wb').write(base64.b64decode(json.load(sys.stdin)['data'][0]['b64_json']))"
```

Le immagini con l'orso sono state fatte con `/edits` passando `brand/mascotte/mascotte-principale.jpg` come riferimento: l'orso è rimasto riconoscibile in tutte (occhiali tondi con riflesso, maglietta verde con € giallo, contorno nero spesso). Le immagini senza orso (04, 10, 12, 19) con `/generations`. Script: `script/gen.py`.

### Prompt

Ogni prompt è composto così (testo completo di ognuno in `script/prompts.json`, generato da `script/make_prompts.py`):

`Vertical 9:16 illustration for a short educational video.` + [ORSO, solo se c'è] + [STILE] + `Scene: ` [SCENA] + [FONDO] + [SPAZIO IN ALTO] + [PALETTE] + [NIENTE TESTO]

- **ORSO:** The character is EXACTLY the bear mascot shown in the reference image: a cartoon brown bear with copper-orange fur (#C2622A) with small fur tufts on cheeks and shoulders, round chubby body, light peach muzzle (#F6C78E), round ears with black inner ears, black rounded-triangle nose with a short vertical line to the mouth, ROUND BLACK SUNGLASSES with one white diagonal glare stripe on each lens (always worn, eyes never visible), dark green t-shirt (#0F5E3F) with a big yellow euro symbol (#F6C21C) in the center of the chest. Keep the exact same character design, proportions and colors as the reference.
- **STILE:** Flat 2D vector cartoon illustration, thick uniform black outlines, solid flat colors, no gradients, no shading, no photographic texture, simple and very readable, one strong prop, lots of empty space.
- **FONDO inchiostro (01, 20):** Background: perfectly uniform flat solid very dark charcoal color (#111418), empty, no pattern, no floor, no gradient.
- **FONDO carta (tutte le altre):** Background: perfectly uniform flat solid warm off-white paper color (#F4F1EA), empty, no pattern, no gradient, no wall decorations, at most a very thin simple floor line.
- **SPAZIO IN ALTO:** Keep the top quarter of the image completely empty background (space for a title added later).
- **PALETTE:** Color palette limited to: the bear's own colors, warm amber/golden yellow (#E9A400) accents, greys, white, black outlines and coffee browns. No red anywhere, no other green objects besides the bear's t-shirt.
- **NIENTE TESTO:** Absolutely no text, no letters, no numbers, no words, no labels, no logo, no watermark anywhere in the image.
- **SAGOMA** (dove c'è una persona): faceless plain flat medium-grey silhouette person (#9A9A9A, no face, no eyes, no mouth, no hair details, smooth mannequin-like shape, thick black outline)

| Img | Orso | Fondo | Scena |
|---|---|---|---|
| 01 | sì | inchiostro | Bear centered in the lower part, SURPRISED: mouth in a small round "o", eyebrows raised above the sunglasses, both paws raised in astonishment. In front of him a small white espresso cup on a saucer and a long BLANK white paper receipt curling down (completely empty paper, no print). *(prompt della prova iniziale: chiedeva "waist up", è uscito a figura intera; tenuto perché riuscito)* |
| 02 | sì | carta | Waist-up, centered, THOUGHTFUL and puzzled: one paw on his chin, mouth twisted to one side, one eyebrow raised, head slightly tilted. No props. |
| 03 | sì | carta | Waist-up, centered, holding up a small white espresso cup on a saucer and looking at it with curiosity, gentle closed-mouth smile, slightly nostalgic mood. |
| 04 | no | carta | Still life: two BLANK white receipts standing straight side by side, facing the viewer, zigzag torn bottom edges, completely empty; the left a bit shorter than the right. In front, centered, a small white espresso cup on a saucer. |
| 05 | sì | carta | Waist-up behind a flat wooden bar counter, front view, euro symbol on the chest (plain short sleeves without any symbol). With one paw he places a small stack of plain golden amber coins on the counter, next to an espresso cup; looks down at the coins, slightly surprised. |
| 06 | sì | carta | Coffee bar counter from the front; behind it a barista = SAGOMA, next to a simple grey espresso machine. In front, on the right, the bear waist-up in three-quarter view, THOUGHTFUL, paw on chin, looking at the barista. |
| 07 | sì | carta | Waist-up, centered, index finger raised ("I have an idea"), open smiling mouth. A small burlap sack of coffee beans on the left and a small grey espresso machine on the right, floating at shoulder height like two options. |
| 08 | sì | carta | Bear full body on the right, pointing at a big open burlap sack full of pale beige raw coffee beans on the left. Curious, small smile. |
| 09 | sì | carta | Big open burlap sack of coffee beans in the center; behind it a very large bold solid amber arrow pointing straight up. Bear on the right, waist-up, looking up at the arrow SURPRISED. |
| 10 | no | carta | Still life: old-fashioned brass balance scale, left pan with a heavy coffee sack hanging much LOWER, right pan with a tiny espresso cup much HIGHER; beam clearly tilted; brass in warm amber tones. |
| 11 | sì | carta | On the left, behind a bar counter, a barista = SAGOMA with a plain grey apron, holding a big heavy burlap sack of coffee beans in both arms. On the right the bear, waist-up, sympathetic expression (eyebrows tilted, small frown). |
| 12 | no | carta | Small coffee bar from the front: counter with grey cash register and espresso machine; behind it a barista = SAGOMA, "the whole figure including the torso is plain flat grey with no clothes, no t-shirt, no logo". A bare light bulb hangs from the top, glowing amber. A long BLANK white bill hangs over the counter edge. |
| 13 | sì | carta | Waist-up, centered, WORRIED: light-blue sweat drop, eyebrows tilted, mouth turned down, holding a very long BLANK white bill that unrolls to the floor. Beside him a simple amber lightning bolt and a grey electric plug with cable. |
| 14 | sì | carta | Waist-up, leaning forward, examining with a big magnifying glass a long BLANK white receipt held in the other paw. Concentrated, curious. |
| 15 | sì | carta | On a flat wooden bar counter three stacks of plain golden amber coins of very different heights. Bear on the right, waist-up behind the counter, THOUGHTFUL, paw on chin. |
| 16 | sì | carta | Big blank presentation board on an easel with only a thick amber line chart that first rises high and then clearly drops at the end; no labels, no numbers. Bear on the right pointing at the falling part, curious. |
| 17 | sì | carta | Metaphor: on the left a burlap coffee sack sliding down a grey slope; on the right an espresso cup sitting firmly on top of a tall grey pedestal. Bear, small, full body, between them, looking up at the cup, THOUGHTFUL. |
| 18 | sì | carta | Bar counter: on the left a customer = SAGOMA holding an espresso cup; on the right the bear waist-up with a curious questioning face; on the counter between them a long BLANK white receipt. |
| 19 | no | carta | Three SAGOME in a row, same size, full body: left holds an espresso cup (customer), middle wears a plain grey apron and holds a cloth (barista), right carries a burlap coffee sack on the shoulder (roaster). |
| 20 | sì | inchiostro | Waist-up, in the LOWER LEFT of the frame, WINKING (one eye closed visible through the lens), friendly closed-mouth smile, holding an espresso cup on a saucer. Upper right empty. |

### Cosa è stato rigenerato e perché

In tutto 22 immagini generate (1 prova + 18 + 3 rigenerazioni), più una richiesta bloccata dal filtro.

| Img | Problema nella prima versione | Correzione |
|---|---|---|
| 05 | Primo piano della zampa: il simbolo € era finito **sulla manica** (fuori modello) e il braccio era deformato | Rifatta con l'orso a mezzo busto dietro il bancone, "plain short sleeves without any symbol" |
| 11 | Prima richiesta **bloccata dal filtro dei contenuti** (probabilmente "carrying… on his shoulders, bending under the weight") | Riformulata: la sagoma tiene il sacco in braccio, "the sack looks heavy" |
| 12 | La sagoma del barista aveva una **maglietta verde con un logo a forma di orso** (non grigia, e un altro verde in scena) | Aggiunto "the whole figure including the torso is plain flat grey with no clothes, no t-shirt, no logo" |

Controllate tutte: nessuna scritta, nessun rosso, sagome grigie senza volto, orso coerente.

## Voce

### ElevenLabs: non utilizzabile

- `GET https://api.elevenlabs.io/v1/voices` (header `xi-api-key` con valore fittizio) funziona: ci sono voci italiane della libreria (Antonio Farina `uScy1bXtKz8vPzfdFsFw`, Valerio `f8NAZK1ciwrVujah7clz`, Alessandro `JfznbVXrGXYh0gZo9Lcp`) e voci premade che supportano l'italiano (River `SAz9YHcvj6GT2YYXdXww`, Alice `Xb7hH8MSUJpSbSDYk0k2`, Matilda `XrExE9yKIg1WjnnlVkGX`, George `JBFqnCBsd6RMkjVDRZzb`).
- Le voci della libreria rispondono `402 paid_plan_required` ("Free users cannot use library voices via the API"): l'account è sul piano gratuito.
- Le voci premade rispondono `401 quota_exceeded`: **restano 21 crediti su 10.000** e la voce completa ne richiede circa 850. Il formato `mp3_44100_192` richiede il piano Creator (`mp3_44100_128` va bene).
- Per lo stesso motivo non è stato possibile generare musica né effetti con ElevenLabs.

### Voce provvisoria usata: Kokoro (open source)

- Modello **Kokoro-82M v1.0** (licenza Apache 2.0), via il pacchetto Python `kokoro-onnx` 0.6.1, con i file del modello scaricati dalla release GitHub `thewh1teagle/kokoro-onnx` `model-files-v1.0`. Gira in locale, senza servizi esterni.
- Voce **`im_nicola`** (maschile, italiano), `lang="it"`, `speed=1.1`.
- Sintetizzata **un'inquadratura alla volta** (21 frasi, testi in `script/shots_voice.json`), poi unita con pause controllate (0,12 s dentro la stessa riga del copione, 0,30 s tra una riga e l'altra). Così ogni taglio d'immagine cade esattamente all'inizio della frase. Dentro una frase, i sottotitoli sono distribuiti in proporzione alle sillabe e agganciati alle pause rilevate nell'audio (non c'è un allineamento parola per parola come con ElevenLabs).
- Testo: identico alla colonna "Voce" del copione. Per la pronuncia, numeri scritti in lettere ("ventiquattro per cento", "duemilaventuno", "un euro e quattro centesimi", "un euro e ventinove"), "illycaffè" scritto "Illi caffè" e "Assoutenti" scritto "Asso utenti". Sottotitoli e titoli mostrano le cifre.
- Controllo: trascrizione dell'audio con `muse-spark-1.3` (vedi sotto). Il testo trascritto corrisponde al copione. "Assoutenti" viene trascritto "assutenti" (può essere la pronuncia o la trascrizione).
- **Non ho potuto ascoltare la voce:** naturalezza e calore non sono verificati da un orecchio umano. Kokoro in italiano è comprensibile ma meno naturale di ElevenLabs; può avere un'intonazione un po' straniera.

### Trascrizione (`muse-voice-transcribe-1.0`)

Gli endpoint `/v1/audio/transcriptions` e simili rispondono 404, e `muse-voice-transcribe-1.0` su `/v1/chat/completions` dà `model_not_found`. Funziona invece `muse-spark-1.3` su `/v1/chat/completions` con un messaggio che contiene `{"type": "input_audio", "input_audio": {"data": <wav base64>, "format": "wav"}}` più la richiesta di trascrivere (`script/transcribe.py`). Va bene per controllare il testo, non per giudicare la qualità della voce.

### Musica ed effetti

- **Musica: nessuna.** Senza crediti ElevenLabs non c'era modo di generarla con licenza, e non ho usato brani presi dal web. Su TikTok si può aggiungere una base dalla Commercial Music Library a circa -20 dB sotto la voce.
- **Effetto "colpo di scontrino"** sull'hook (0,0 s): sintetizzato in Python (tonfo grave da 150 a 55 Hz più un breve fruscio), senza campioni esterni, quindi senza problemi di licenza. Non ascoltato.
- Mix normalizzato in due passaggi con `loudnorm` di ffmpeg (I=-14, TP=-1,5): misurato -14,3 LUFS.

## Come rifarlo

Gli script in `script/` si aspettano, nella stessa cartella: `fonts/` (i 3 TTF IBM Plex), `img/final/NN.png` (le immagini), `kokoro/` (modello), un venv con `kokoro-onnx` e `soundfile`.

1. `make_prompts.py` → `prompts/NN.txt`; `gen.py OUT.webp PROMPT.txt 1024x1792 [riferimento.jpg]` per ogni immagine.
2. Voce: `kok_all.py <cartella> im_nicola 1.1 voce/final` → `final.wav` + `final.json` (tempi delle frasi).
3. `audio.py final.wav mix.wav sfx.wav` (aggiunge l'effetto); `montage.py final.wav final.json video_noaudio.mp4` (`--preview DIR` per un fotogramma per inquadratura); `norm.sh` per la normalizzazione; poi ffmpeg per unire video e audio.

**Per passare alla voce ElevenLabs** quando ci sono crediti (o con il piano a pagamento, che sblocca le voci italiane della libreria come Antonio Farina o Valerio):

```bash
# testo = i testi di shots_voice.json uniti con uno spazio (si possono riscrivere le cifre: ElevenLabs le legge bene)
python3 tts.py <voice_id> testo.txt voce/eleven eleven_multilingual_v2 0.95   # stability 0.65, similarity 0.8, style 0.1
python3 eleven_to_segments.py voce/eleven.json shots_voice.json voce/eleven_tempi.json
ffmpeg -i voce/eleven.mp3 -ar 24000 -ac 1 voce/eleven.wav
python3 montage.py voce/eleven.wav voce/eleven_tempi.json video_noaudio.mp4
```

`tts.py` usa `POST /v1/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128` con `language_code: "it"` e restituisce l'allineamento dei caratteri; il montaggio si rifà da solo sui nuovi tempi.

## Limiti noti

- **Durata 60,6 s, non 35-40 s.** Il copione stima "~90 parole", ma la colonna "Voce" ne contiene circa 150. A un ritmo calmo (circa 150 parole/min, come chiede la guida di stile) servono circa 60 s. Per arrivare a 40 s va accorciato il testo, per esempio togliendo le righe 8 e 9 oppure condensando le due tesi. Non l'ho fatto perché la consegna chiedeva il testo esatto.
- **Voce provvisoria** Kokoro, non ElevenLabs (vedi sopra). Non ascoltata da un umano.
- **Niente musica di sottofondo.**
- L'hook (inquadratura 1) dura 4,4 s, più dei 2-3 s ideali, perché la prima frase è lunga. Si può dividere in due immagini.
- La sincronia dei sottotitoli è precisa all'inizio di ogni frase. Dentro la frase è stimata (errore atteso fino a circa 0,2 s).
- Immagine 17: la metafora "il sacco scende, la tazzina resta in alto" si legge, ma il sacco sembra più "rovesciato" che "in discesa".
- Immagini 13 e 14: la carta/la lente copre in parte la € sulla maglietta (la maglietta resta riconoscibile).
- Il fumetto "But Why Finance?" è disegnato in montaggio (verde `#006B3C`, contorno carta, testo bianco), non con un logo ufficiale.
