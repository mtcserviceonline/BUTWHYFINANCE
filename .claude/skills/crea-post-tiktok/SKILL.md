---
name: crea-post-tiktok
description: >-
  Crea un intero post TikTok di But Why Finance (video illustrato con l'orso e voce narrante),
  dalla ricerca dell'argomento alla consegna: proposta di 3 temi con angolo "Ma perché?" e rubrica,
  fatti verificati con fonti, copione da 20-30 secondi, scene e testo da incollare in ElevenLabs,
  8 immagini 9:16 generate con la mascotte, didascalia, cartella del post in brand/tiktok/output/,
  commit e messaggio finale con testi e anteprima. Usala quando l'utente dice "crea un post TikTok",
  "nuovo video", "prepara il prossimo post", "idea per un video di finanza", "facciamo un TikTok su…"
  o lancia /crea-post-tiktok [argomento].
---

# Crea un post TikTok di But Why Finance

Produce un post completo nella cartella `brand/tiktok/output/AAAA-MM-slug/`: `ricerca.md`, `copione.md`, `didascalia.md`, `script/` (scene ElevenLabs + testo da incollare), `immagini/` (8 PNG 1080x1920 + prompt + README + anteprima), `README.md`. Voce e video solo su richiesta.

Argomento indicato dall'utente (può essere vuoto): $ARGUMENTS

Il metodo viene dai due post già fatti; quando hai un dubbio, imita `brand/tiktok/output/2026-10-risparmio-quotidiano/` (forma standard) e leggi il README di `brand/tiktok/output/2026-10-il-prezzo-del-caffe/` (API, errori); per il montaggio del video la sezione "Montaggio" del README di `2026-10-risparmio-quotidiano/`.

## Prima di iniziare

1. Leggi `CLAUDE.md`, `brand/tiktok/stile-tiktok.md`, `brand/tiktok/analisi-riferimenti.md`, `brand/mascotte/README.md`: se contraddicono questa skill, valgono loro.
2. Leggi [`references/brand.md`](references/brand.md): rubriche e accenti, colori, regole vincolanti delle immagini, espressioni dell'orso, tono.
3. Controlla `brand/tiktok/output/` per non rifare un tema già trattato.

## Preferenze dell'utente (sempre)

- Scrivi e rispondi **in italiano**.
- Testi e prompt **direttamente in chat**, non solo nei file. Il **testo ElevenLabs va sempre incollato nel messaggio**.
- Delega volentieri il lavoro lungo ad **agenti in background** (immagini e testi in parallelo, su file diversi, ognuno con `git add` dei soli propri percorsi e `git pull --rebase` prima del push): vedi [`references/cartella-e-consegna.md`](references/cartella-e-consegna.md).
- Il tema resta **aperto alla discussione**: si chiude con una domanda, mai con una sentenza. **Nessun consiglio di investimento** né prodotto finanziario.

## Flusso

### 1. Argomento
- Con un tema dato: trova l'angolo "Ma perché?" e la rubrica, poi vai al passo 2.
- Senza tema: WebSearch su notizie economiche italiane recenti e temi evergreen di vita quotidiana; proponi **3 argomenti** (domanda "Ma perché…?", rubrica con accento, il fatto con fonte, perché può funzionare) e **chiedi quale scegliere, poi aspetta**. Se l'utente ha detto "scegli tu", scegli il migliore e dillo in una riga.
- Dettagli e formato della proposta: [`references/ricerca.md`](references/ricerca.md).

### 2. Fatti verificati → `ricerca.md`
- Dati con WebSearch/WebFetch, **fonti primarie** prima (Istat, Eurostat, Banca d'Italia, ARERA, ministeri; associazioni citate per nome). Annota valore, fonte, data, link.
- Tabella fatto/fonte/data/stato: **verificato su fonte originale** o **letto solo in sintesi**. Tesi contrapposte attribuite a chi le sostiene. Ogni numero calcolato da noi = **stima con il calcolo**. **Mai inventare numeri.**

### 3. Copione → `copione.md`
- Rubrica, formato, durata **20-30 s (~55-66 parole)**: conta le parole e avvisa che a 140-150 parole/min 66 parole = 26-28 s. Obiettivo, hook sui **tre canali** (verbale, testo, visivo) nei primi 2 s.
- Struttura: hook → fatto → segui i soldi → due tesi o consigli → domanda aperta. Loop: l'ultimo fotogramma richiama il primo.
- Production doc (tempo, immagine, testo a schermo, voce con tono, suono), parole chiave SEO, controllo qualità.
- Voce: commercialista esperto che spiega al bar, neutro, frasi corte, **numeri in lettere**.
- Mostra in chat il testo della voce; se l'utente è presente chiedi l'ok prima delle immagini, altrimenti prosegui e segnalalo come "da approvare".
- Modello completo: [`references/copione.md`](references/copione.md).

### 4. Voce → `script/scene_elevenlabs.json` + `script/elevenlabs.txt`
- Scene con lo schema della risparmio (id, secondi, espressione_orso, tono, tag_v3, stability, style, text, immagini): [`references/voce-elevenlabs.md`](references/voce-elevenlabs.md).
- `python3 .claude/skills/crea-post-tiktok/scripts/elevenlabs_txt.py <post>/script/scene_elevenlabs.json <post>/script/elevenlabs.txt --titolo "…"` → tag italiani (`[sorpreso]`, `[curioso]`, `[calmo]`, `[pensieroso]`, `[caldo]`), tag inglesi per `eleven_v3`, impostazioni per scena per `eleven_multilingual_v2`. **Incollalo in chat.**
- **Non generare la voce**: account ElevenLabs gratuito (voci italiane → 402 `paid_plan_required`, pochi crediti). Solo se l'utente lo chiede o conferma un piano a pagamento: `scripts/voce_elevenlabs.py … --conferma`.

### 5. Immagini → `immagini/`
- ~8 immagini 9:16, una idea = una immagine = un oggetto concreto; inchiostro `#111418` solo su hook e chiusura, carta `#F4F1EA` sulle altre; un solo accento; niente rosso; **nessuna scritta**; fasce alta ~10%, bassa ~15% e destra libere; **€ sempre visibile**; sagome grigie senza volto.
- Procedura (dettagli, problemi noti e rimedi in [`references/immagini.md`](references/immagini.md)):
  1. scene in inglese in `immagini/scene.json`;
  2. `scripts/componi_prompt.py immagini/scene.json immagini/prompts.json` (blocchi fissi di brand);
  3. `scripts/genera_immagine.py --prompts immagini/prompts.json --id 01 --out immagini/01.png` per ogni immagine (riferimento `brand/mascotte/mascotte-principale.jpg`, ritenta da solo sui 5xx);
  4. **guarda ogni immagine con Read**; `scripts/controlla_immagini.py immagini --prompts immagini/prompts.json`;
  5. rigenera solo le difettose, **max 3 tentativi** per immagine;
  6. `scripts/anteprima.py immagini` → `immagini/anteprima.jpg`; scrivi `immagini/README.md` (tentativi, controlli, difetti noti).

### 6. Didascalia → `didascalia.md`
Fatto con fonte nominata, tesi attribuite, domanda aperta, 3-5 hashtag parola chiave + nicchia, versione breve, promemoria etichetta **"contenuto generato da IA"**. Modello: [`references/didascalia.md`](references/didascalia.md).

### 7. Cartella del post → `README.md`
Indice, stato di ogni elemento, cose da verificare prima di pubblicare, cosa manca (voce, montaggio). Struttura e modello: [`references/cartella-e-consegna.md`](references/cartella-e-consegna.md). `voce.mp3` e `video.mp4` solo su richiesta: [`references/montaggio.md`](references/montaggio.md).

### 8. Controllo qualità
Checklist in [`references/controllo-qualita.md`](references/controllo-qualita.md): hook in 1 s su tre canali, un'immagine ogni 2-3 s, tesi attribuite e neutrali, nessun consiglio di investimento, numeri con fonte o marcati come stima, domanda aperta, colori e regole di brand, orso coerente, fasce libere, nessuna scritta nelle immagini.

### 9. Consegna
- `git add` **solo** della cartella del post; commit in italiano con le righe di attribuzione richieste dall'ambiente (se presenti nella conversazione); `git pull --rebase origin <branch corrente>`; `git push -u origin <branch corrente>` con retry 2/4/8/16 s solo per errori di rete. Mai altri branch, nessuna PR.
- In chat: anteprima delle immagini (SendUserFile), **testo ElevenLabs e didascalia incollati**, cose da verificare, cosa manca.

## Script (`.claude/skills/crea-post-tiktok/scripts/`)

| Script | A cosa serve |
|---|---|
| `componi_prompt.py` | scene.json → prompts.json con i blocchi fissi (orso, stile, fondo, composizione, palette della rubrica, niente testo) |
| `genera_immagine.py` | prompt + riferimento → PNG 1080x1920 via `api.meta.ai` (`muse-image-1.0`), retry sui 5xx |
| `ritaglia_916.py` | ritaglio centrale 9:16 + resize senza deformare (usato da `genera_immagine.py`) |
| `controlla_immagini.py` | fondo misurato, ingombro, fasce libere: tabella per il README |
| `anteprima.py` | contact sheet `anteprima.jpg` |
| `elevenlabs_txt.py` | scene_elevenlabs.json → elevenlabs.txt |
| `voce_elevenlabs.py` | voce scena per scena + tempi per immagine (solo con `--conferma`; `--simula` per prove) |

Richiedono Python 3 con `requests`, `Pillow`, `numpy`, e `ffmpeg` per la voce. Prove e file grezzi vanno nello scratchpad, non nel repository.
