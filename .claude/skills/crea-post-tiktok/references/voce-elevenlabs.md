# Voce: scene ElevenLabs e testo da incollare

## `script/scene_elevenlabs.json`

Stesso schema del post risparmio (`brand/tiktok/output/2026-10-risparmio-quotidiano/script/scene_elevenlabs.json`). Una scena = un tono = 1-2 immagini; 5-6 scene per 25-30 s.

```json
[
  {
    "id": 1,
    "secondi": "0-6",
    "espressione_orso": "sorpreso, bocca a \"o\"",
    "tono": "incredulo e curioso, come davanti a un conto che non ti aspettavi; \"circa\" detto chiaro, senza enfasi allarmista",
    "tag_v3": "[surprised]",
    "stability": 0.35,
    "style": 0.45,
    "text": "Un caffè al bar ogni giorno costa circa quattrocentosettanta euro all'anno. Ma perché non ce ne accorgiamo?",
    "immagini": [1, 2]
  }
]
```

| Campo | Contenuto |
|---|---|
| `id` | numero della scena, da 1 |
| `secondi` | intervallo previsto, es. `"0-6"` (dal production doc) |
| `espressione_orso` | espressione dell'orso nelle immagini della scena (dal set `espressioni.jpg`) |
| `tono` | indicazione di recitazione in italiano, una riga |
| `tag_v3` | tag inglese per `eleven_v3` (tabella sotto) |
| `stability`, `style` | impostazioni per `eleven_multilingual_v2` (tabella sotto) |
| `text` | testo parlato, **numeri in lettere**, senza tag |
| `immagini` | numeri delle immagini coperte dalla scena; se sono 2, il testo si divide sulla punteggiatura (prima `. ? !`, poi `: ;`, poi la virgola) o con il campo facoltativo `"frasi_immagini": ["…", "…"]` |

Facoltativo: `"tag_it"` se il tag italiano non è uno dei cinque standard.

### Toni, tag e impostazioni (valori usati nei due post)

| Tono (tag italiano, come lo scrive l'utente) | Tag `eleven_v3` | stability | style | Dove |
|---|---|---|---|---|
| `[sorpreso]` | `[surprised]` | 0.35 | 0.45 | hook, un prezzo che non torna |
| `[curioso]` | `[curious]` | 0.5 | 0.3 | il fatto, la risposta al "perché" |
| `[calmo]` | `[calm]` | 0.7 | 0.1 | tesi, consigli, dati |
| `[pensieroso]` | `[thoughtful]` | 0.7 | 0.1 | seconda tesi, dilemma |
| `[caldo]` | `[warm]` | 0.5 | 0.3 | domanda finale |

Sempre: `similarity_boost` 0.8, speaker boost attivo, lingua italiana, velocità 0,95-1,0.

## `script/elevenlabs.txt` (testo unico da incollare)

Si genera dal JSON, non si scrive a mano:

```bash
python3 .claude/skills/crea-post-tiktok/scripts/elevenlabs_txt.py \
  brand/tiktok/output/AAAA-MM-slug/script/scene_elevenlabs.json \
  brand/tiktok/output/AAAA-MM-slug/script/elevenlabs.txt --titolo "<titolo>"
```

Contiene tre blocchi: (1) testo con i tag in italiano `[sorpreso] …`; (2) testo con i tag in inglese per `eleven_v3`; (3) per `eleven_multilingual_v2`, che non interpreta i tag, il testo di ogni scena senza tag con stability/style da impostare. Stampa anche il conteggio parole e la durata stimata.

**L'utente vuole sempre questo testo anche incollato nel messaggio in chat**, non solo nel file: copia almeno i blocchi 1 e 2 (e il 3 se usa `eleven_multilingual_v2`).

## Stato dell'account ElevenLabs (ottobre 2026)

- Piano **gratuito**. Le voci italiane della libreria rispondono **402 `paid_plan_required`** ("Free users cannot use library voices via the API"):
  - Valerio – Warm Italian Storyteller `f8NAZK1ciwrVujah7clz`
  - Valerio – Deep `wQAoCaUYKpd8fFWwtvnq`
  - Achille Valerio `94VTtZwvNmsppde6nAW0`
- Restano **pochi crediti** (le voci premade danno `401 quota_exceeded`; nel post del caffè restavano 21 crediti su 10.000, ne servono ~850 per una voce completa).
- Quindi: **non tentare la generazione** a meno che l'utente lo chieda esplicitamente o confermi di essere passato a un piano a pagamento. Di default si consegnano solo `scene_elevenlabs.json` e `elevenlabs.txt`, e nel README la voce risulta "da registrare".

## Generare la voce (solo su richiesta / piano a pagamento)

```bash
python3 .claude/skills/crea-post-tiktok/scripts/voce_elevenlabs.py \
  brand/tiktok/output/AAAA-MM-slug/script/scene_elevenlabs.json \
  --out-dir brand/tiktok/output/AAAA-MM-slug/voce --conferma [--voice-id f8NAZK1ciwrVujah7clz]
```

- Chiama `POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128` **una scena alla volta**, con `model_id: eleven_multilingual_v2`, `language_code: "it"`, stability/style della scena, similarity 0.8; header `xi-api-key` con un **valore fittizio** (l'autenticazione su `api.elevenlabs.io` la fa il proxy). `mp3_44100_192` richiede il piano Creator: resta su `mp3_44100_128`.
- Scrive `voce/scene/NN.mp3`, `voce/voce.wav`, `voce/voce.mp3` e `voce/tempi_voce.json` con un segmento per immagine (formato di `montage.py`).
- Su 401/402 si ferma subito: avvisa l'utente, non ritentare.
- Senza `--conferma` non parte; `--simula` produce solo tempi finti (utile per provare il montaggio senza consumare crediti).
- Poi: ascolto (non puoi farlo tu: dichiaralo), trascrizione di controllo se serve, montaggio (vedi `montaggio.md`). Copia `voce.mp3` nella radice della cartella del post.

In alternativa, per la sola voce intera con allineamento: `brand/tiktok/output/2026-10-il-prezzo-del-caffe/script/tts.py` + `eleven_to_segments.py` (impostazioni uniche per tutto il testo).

Voce provvisoria open source (solo se l'utente la chiede): Kokoro-82M (`kokoro-onnx`, voce `im_nicola`, speed 1.1), usata nel post del caffè (`script/kok_all.py`). È comprensibile ma meno naturale; nessuno l'ha ascoltata prima della consegna.
