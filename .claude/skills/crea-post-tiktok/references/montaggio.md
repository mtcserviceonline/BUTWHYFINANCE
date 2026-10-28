# Voce e video (opzionali, solo su richiesta)

Di default il post si consegna **senza** `voce.mp3` e `video.mp4`. Si fanno solo se l'utente lo chiede (e, per ElevenLabs, se ha confermato un piano a pagamento: vedi `voce-elevenlabs.md`).

## Riferimento: il post del caffè

`brand/tiktok/output/2026-10-il-prezzo-del-caffe/` è l'unico video montato finora. Leggi il suo `README.md` (sezioni "Struttura del video", "Sottotitoli", "Come rifarlo", "Limiti noti") prima di montare.

Script in `brand/tiktok/output/2026-10-il-prezzo-del-caffe/script/`:

| Script | Cosa fa |
|---|---|
| `montage.py` | rende ogni fotogramma con Pillow (immagine con zoom lento 100%→104%, titolo, sottotitoli 3-5 parole) e lo passa a ffmpeg (1080x1920, 30 fps, H.264). `--preview DIR` salva un fotogramma per inquadratura |
| `config_video.py` | le inquadrature: `img`, `bg` (`ink`/`paper`), `title` (righe con `*parola*` nel colore d'accento), `subs` (testo mostrato, testo parlato) e opzioni `pop`, `bubble`, `scale`, `dy` |
| `tts.py` + `eleven_to_segments.py` | voce ElevenLabs intera con allineamento → tempi per inquadratura |
| `audio.py` | effetto "colpo di scontrino" sintetizzato in numpy (nessun campione esterno) |
| `norm.sh` | loudnorm a due passaggi: -14 LUFS, true peak -1,5 dBTP, 48 kHz |

## Procedura

1. **Voce**: `voce_elevenlabs.py … --conferma` (vedi `voce-elevenlabs.md`) → `voce/voce.wav` e `voce/tempi_voce.json` con **un segmento per immagine** (formato `{"segments": [{"start", "end", …}], "total"}` letto da `montage.py`).
2. **Preparare la cartella di lavoro** fuori dal repository (scratchpad): copia `montage.py` e `config_video.py` del caffè; metti le immagini in `img/final/NN.png`; scarica i font IBM Plex Sans Condensed (Bold, SemiBold) e IBM Plex Mono (Bold) dal repository `google/fonts` (licenza OFL) in `fonts/`. Font e copie di lavoro non si committano.
3. **Adattare `config_video.py`**: una voce di `SHOTS` per ogni segmento di `tempi_voce.json` (stesso numero, stesso ordine), titoli dal production doc, sottotitoli 3-5 parole con la parola chiave tra `*…*`, `"pop": True` sull'hook, `"bubble": True` sulla chiusura (fumetto "But Why Finance?" verde `#006B3C`).
4. **Adattare `montage.py`**: il colore d'accento è fisso (`AMBER = (233, 164, 0)`): cambialo con quello della rubrica; togli i livelli specifici del caffè (`receipts`, `labels`) se non servono. I sottotitoli sono centrati a `SUB_CY = 1440` (75% dell'altezza): con le immagini nuove, che hanno il soggetto fino all'~80-85%, **coprono spesso la € dell'orso** (visto nella prova). Valuta `SUB_CY` intorno a 1560 (resta sopra il 15% in basso) e controlla nei fotogrammi di anteprima.
5. `python3 montage.py voce/voce.wav voce/tempi_voce.json video_noaudio.mp4 --preview anteprima_video/` → guarda i fotogrammi con Read (titoli fuori dalle zone sicure? sottotitoli leggibili?), poi senza `--preview`.
6. Audio: eventuale effetto con `audio.py`, base musicale **solo con licenza commerciale** a circa -20 dB (oppure niente musica: si aggiunge su TikTok dalla Commercial Music Library), `norm.sh` per la normalizzazione, poi ffmpeg per unire video e audio (`-c:v copy -c:a aac`).
7. Copia `voce.mp3` e `video.mp4` nella radice della cartella del post; aggiorna il README (durata, loudness misurata, limiti).

## Limiti da dichiarare sempre

- Non puoi ascoltare la voce: naturalezza e calore non sono verificati da un orecchio umano.
- La sincronia dei sottotitoli dentro una frase è stimata (fino a ~0,2 s di errore) se non c'è l'allineamento parola per parola.
- Niente musica scaricata dal web.
- Questa catena (voce per scena → `tempi_voce.json` → `montage.py`) è stata provata con un audio finto e tempi simulati sulle 8 immagini della risparmio (anteprima e render completo 1080x1920, 30 fps, ~28,5 s, circa 1 minuto di calcolo), non ancora con una voce ElevenLabs reale.
