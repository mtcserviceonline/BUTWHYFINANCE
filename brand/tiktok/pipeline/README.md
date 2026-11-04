# Pipeline dei video TikTok

Script usati dal workflow `video-tiktok` (vedi `.claude/skills/video-tiktok/SKILL.md`). Si lanciano dalla radice del repo.

| Script | Fase | Cosa fa |
|---|---|---|
| `setup.sh` | 0 | Installa le dipendenze Python e scarica i font IBM Plex (licenza OFL) in `fonts/` |
| `testo_elevenlabs.py EP` | 2 | Controlla `scene.json` (lunghezza, numeri in lettere, sottotitoli che coprono la voce) e scrive `voce-elevenlabs.txt` |
| `allinea.py EP AUDIO [--locale]` | 3 | Copia l'audio in `voce/`, lo converte e trova dove inizia e finisce ogni scena → `voce/tempi.json` |
| `genera_immagini.py EP [ID…]` | 4 | Compone i prompt (blocchi fissi del brand + scena) e genera le immagini con l'API Meta `muse-image-1.0` |
| `provino.py EP` | 4 | Griglia di tutte le immagini in `_lavoro/provino-immagini.jpg` |
| `monta.py EP [--anteprima]` | 5 | Video 1080x1920 con zoom lento, titoli, sottotitoli, fumetto, colpo sonoro sull'hook, -14 LUFS |
| `copertina.py EP` | 5 | `copertina.png` 9:16 |

`EP` = cartella dell'episodio, es. `brand/tiktok/output/2026-11-mutui-tassi-bce`.

## Cartella di un episodio

```
fatti.md                 fase 1: fatti, fonti, contesto, tesi, angolo
scene.json               fase 2: le scene (voce, sottotitoli, titoli, sfondo) – formato in esempio-scene.json
voce-elevenlabs.txt      fase 2: testo da incollare in ElevenLabs (una riga per scena, tag v3)
didascalia.md            fase 2: didascalia + hashtag
voce/voce-originale.mp3  fase 3: l'audio caricato dall'utente
voce/tempi.json          fase 3: inizio/fine di ogni scena (e delle parole, se c'è la trascrizione)
immagini/prompts.json    fase 4: scene da illustrare;  immagini/prompt/ID.txt prompt completi
immagini/ID.png          fase 4: illustrazioni senza testo
video.mp4, copertina.png, tempi-video.json, README.md   fase 5
_lavoro/                 file temporanei (non committati)
```

## Formato di `scene.json`

Vedi `esempio-scene.json`. Per ogni scena:

- `id`, `immagine` (id del PNG; può ripetersi, es. l'ultima scena riusa `01` per il loop)
- `sfondo`: `inchiostro` | `carta`
- `tag`: tag di Eleven v3 (`[curious]`, `[thoughtful]`…) o vuoto
- `voce`: la frase parlata, con i numeri in lettere
- `sottotitoli`: `[[mostrato, parlato|null], …]`, 3-5 parole, `*parola*` = colore d'accento
- `titolo`: lista di righe; una riga di sole cifre/€/% viene resa in IBM Plex Mono; per forzare: `{"testo": "1,04 €", "font": "mono", "dim": 170}`
- `fumetto`: `true` per il fumetto "But Why Finance?"
- `scala` (facoltativo): rimpicciolisce l'immagine (es. 0.84)

A livello di episodio: `titolo`, `rubrica` (dà il colore d'accento, vedi `comune.py`), `accento` facoltativo (`#RRGGBB`), `copertina` `{"immagine", "titolo", "fumetto"}`.

## Allineamento dell'audio

1. **ElevenLabs Speech-to-Text** (`scribe_v1`): tempi di ogni parola; i sottotitoli cambiano esattamente sulla parola. Costa circa 1 credito al secondo di audio.
2. **Locale (pause)**, usato da solo se mancano i crediti o con `--locale`: cerca le pause nell'audio e sceglie, con la programmazione dinamica, quelle più vicine ai tagli attesi in base alle sillabe di ogni scena. Sul video del caffè (21 scene, voce Kokoro) ritrova tutti i tagli con meno di 0,1 s di errore. Serve una pausa udibile tra le scene: per questo `voce-elevenlabs.txt` ha una riga per scena.

Whisper e altri modelli locali non sono utilizzabili nelle sessioni cloud (Hugging Face è bloccato dal proxy).

## Immagini

API compatibile con OpenAI, autenticata dal proxy: `POST https://api.meta.ai/v1/images/edits` (con `brand/mascotte/mascotte-principale.jpg` come `image[0]`) per le scene con l'orso, `/v1/images/generations` per le altre; `size=1024x1792` → 1152x2016. Dettagli e problemi noti in `../output/2026-10-il-prezzo-del-caffe/README.md`.
