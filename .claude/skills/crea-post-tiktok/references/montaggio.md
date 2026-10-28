# Voce e video (opzionali, solo su richiesta)

Di default il post si consegna **senza** `voce.mp3` e `video.mp4`. Si fanno solo se l'utente lo chiede (e, per ElevenLabs, se ha confermato un piano a pagamento: vedi `voce-elevenlabs.md`).

## Riferimento: il post "risparmio quotidiano" (montaggio v2, consigliato)

`brand/tiktok/output/2026-10-risparmio-quotidiano/` è montato con la voce ElevenLabs reale e con la **versione 2** degli script, pensata per la ritenzione (un taglio ogni ~1,7 s come il riferimento principale). Leggi la sezione "Montaggio" del suo `README.md` prima di montare. Il post del caffè (`2026-10-il-prezzo-del-caffe/`) usa ancora la versione 1.

Script in `scripts/` di questa skill (copie identiche a quelle del post):

| Script | Cosa fa |
|---|---|
| `monta.sh` | catena completa, da lanciare nella cartella di lavoro: wav → `allinea.py` → `montage.py` → `effetti.py` → `norm.sh` → unione audio/video → `fotogrammi.py` |
| `allinea.py` | tempi stimati di ogni parola quando non c'è l'allineamento di ElevenLabs: frasi (`frasi.json`, inizio/fine dalle pause di `silencedetect`) + picchi di energia ≈ sillabe → `parole.json` (`[{"w","start","end"}]`). Con l'allineamento ElevenLabs basta convertire i caratteri in parole nello stesso formato |
| `montage.py` | v2: ogni inquadratura è una **vista** su un'immagine (`view: (cx, cy, zoom)`: <1 immagine intera rimpicciolita col fondo esteso, >1 primo piano, max ~1,6), zoom continuo 100→106% (`moto: "out"` sull'ultima per il loop), `ancora`, `pan`; taglio netto subito prima della parola `parola`; titoli a "run" (font/colore per pezzo, numeri in Mono) con pop solo quando cambiano, `pill: True` = titolo su targhetta nei primi piani; sottotitoli 2-4 parole con pop 90→100% e parole non ancora dette spente; fumetto `bubble`. Scrive `OUT_tempi.json` (inquadrature, titoli, sottotitoli con i tempi parola per parola, effetti). `--preview DIR [tempi]` per i fotogrammi di prova |
| `config_video_esempio.py` | configurazione del post risparmio: copiala come `config_video.py` accanto a `montage.py` e adattala |
| `effetti.py` | effetti sonori sintetizzati in numpy (colpo, moneta, monetine, pop, forbici, carta, salvadanaio), mixati sotto la voce senza toccarla; i livelli sono in `LIVELLO` (dB rispetto al picco della voce) |
| `norm.sh` | loudnorm a due passaggi: -14 LUFS, true peak -1,5 dBTP, 48 kHz |
| `fotogrammi.py` | fotogrammi di controllo (0 s, ogni taglio, metà di ogni inquadratura, ultimo) e `anteprima_video.jpg` |

## Procedura

1. **Voce**: `voce_elevenlabs.py … --conferma` (vedi `voce-elevenlabs.md`), oppure l'mp3 caricato dall'utente. **Trascrivi sempre l'audio** (in `brand/tiktok/output/2026-10-risparmio-quotidiano/script/transcribe.py`: `muse-spark-1.3` su `https://api.meta.ai/v1/chat/completions` con `input_audio`; faster-whisper non scarica il modello da qui): l'utente può aver cambiato il testo. Se cambia, aggiorna copione, `elevenlabs.txt` e `scene_elevenlabs.json` e dillo.
2. **Tempi**: `silencedetect` (es. `-35dB`, `d=0.08`) per le pause → `frasi.json` → `allinea.py` → `parole.json`.
3. **Cartella di lavoro** fuori dal repository (scratchpad): gli script di `scripts/`, `config_video_esempio.py` rinominato `config_video.py`, le immagini in `img/NN.png`, i font IBM Plex Sans Condensed (Bold, SemiBold) e IBM Plex Mono (Bold) da `google/fonts` (OFL) in `fonts/`, `voce.mp3`. Font e copie di lavoro non si committano.
4. **Inquadrature**: misura dove stanno orso, € e oggetti in ogni immagine (griglia ogni 100 px). Con 8 immagini su ~25 s fai **due inquadrature per immagine** (larga + primo piano sul dettaglio nominato dalla voce), tagli all'inizio di frase o di parola chiave. Scegli `view` in modo che: il titolo (da y=215) cada su fondo; la fascia sottotitoli (centro y≈1535, bordo basso ≤1628) cada su fondo/pavimento, **mai sulla €**; nei primi piani dove il titolo coprirebbe il disegno usa `pill` o togli il titolo.
5. **Hook e loop**: fotogramma 0 già completo (immagine, titolo grande, primo sottotitolo, nessuna dissolvenza); ultima inquadratura con `moto: "out"` che finisce alla stessa scala/posizione dell'apertura, ultimi 0,3 s senza sottotitolo.
6. `python3 montage.py voce.wav parole.json video_noaudio.mp4 --preview prev/` → guarda i fotogrammi con Read, correggi, poi `./monta.sh`.
7. **Controllo finale**: `fotogrammi.py` (almeno 12 fotogrammi + contact sheet), guarda tutto con Read; misura loudness (ebur128) e livelli degli effetti (devono stare ben sotto la voce).
8. Copia `voce.mp3`, `video.mp4`, `tempi.json`, `anteprima_video.jpg` e gli script nella cartella del post; README con sezione "Montaggio" (scelte, tempi, controlli, limiti).

Musica: niente musica scaricata dal web. Una base solo se generata in modo pulito e molto bassa (~-22 dB sotto la voce); il riferimento principale non ha musica, quindi farne a meno va bene (si può aggiungere su TikTok dalla Commercial Music Library).

## Limiti da dichiarare sempre

- Non puoi ascoltare la voce: naturalezza e calore non sono verificati da un orecchio umano.
- La sincronia dei sottotitoli dentro una frase è stimata (fino a ~0,15 s di errore) se non c'è l'allineamento parola per parola di ElevenLabs.
- Niente musica scaricata dal web.
- La catena v2 (`monta.sh`) è stata usata con la voce ElevenLabs reale del post risparmio (24 s, 14 inquadrature, render completo ~1,5 minuti). Con la voce generata da `voce_elevenlabs.py`, `tempi_voce.json` ha un segmento per immagine: per la v2 servono i tempi per parola (`parole.json`).
