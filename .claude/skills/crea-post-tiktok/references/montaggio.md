# Voce e video (opzionali, solo su richiesta)

Di default il post si consegna **senza** `voce.mp3` e `video.mp4`. Si fanno solo se l'utente lo chiede (e, per ElevenLabs, se ha confermato un piano a pagamento: vedi `voce-elevenlabs.md`; con il piano gratuito l'API è bloccata e la voce la registra l'utente dal sito).

## Riferimento: il post "risparmio quotidiano" v2 (consigliato)

`brand/tiktok/output/2026-10-risparmio-quotidiano/` è montato con la catena **v3 degli script** (video v2 del post, 28/10/2026), nata dalle correzioni puntuali dell'utente sulla v1. Leggi il suo `README.md` (sezioni "Montaggio v2", "Controlli automatici", "Limiti") prima di montare. La v1 del post (24 s) e il post del caffè usano versioni precedenti.

Regole che l'utente ha chiesto esplicitamente e che la catena applica e controlla:

- **Occhiali dell'orso sempre visibili e liberi da testi** in ogni inquadratura; volto mai tagliato dal bordo; zoom mai oltre ~120% (115% sul volto).
- **Titoli sopra la testa** dell'orso, mai sul viso; numeri dei consigli "1 ·", "2 ·", "3 ·" in Mono ambra.
- **Sottotitoli** su 1-2 righe sempre sopra il 15% in basso (bordo basso del testo ≤ y=1632), niente nel 10% in alto e nella fascia destra di 120 px.
- **Un cambio visivo ogni ≤ 2 s** (tagli, righe di titolo, scritte o fumetto che entrano); un'immagine che resta più di ~2 s si divide in due inquadrature.
- **Solo tagli netti**; al più una transizione ("tenda", 0,2 s) nel passaggio inchiostro → carta.
- **Numeri a schermo che entrano sulla parola** (riga del titolo con `parola`), con un effetto leggero; effetti sonori **solo sui numeri**.
- **Loop**: l'ultimo ~0,5 s ripete la composizione del primo fotogramma (stessa immagine e vista, ferma) con "?" al posto del numero; il video finisce entro 0,5 s dall'ultima parola.
- **Numeri per esteso** nel testo per la voce; a schermo in cifre.
- **Fonte nominata** a voce, a schermo (es. "Fonte: …" sullo scontrino) e in didascalia; cifre accanto ai consigli solo se verificate.
- **Musica** solo con licenza commerciale, a -20 dB sotto la voce; altrimenti niente (si aggiunge in app dalla Libreria musicale commerciale).

## Script (`scripts/`, copie identiche a quelle del post)

| Script | Cosa fa |
|---|---|
| `monta.sh VOCE.mp3 [CARTELLA_POST]` | **un comando** dalla voce al video: copia script, `immagini/NN.png` e font (scaricati da `google/fonts` in `~/.cache/butwhy-fonts`) in una cartella temporanea, poi `frasi.py` → `ritmo.py` → `allinea.py` → `montage.py` → `effetti.py` → [`musica.py`] → `norm.sh` → unione → `fotogrammi.py` → `copertina.py` → `trascrizione.py`; riscrive nel post `video.mp4`, `tempi.json`, `trascrizione.md`, `sottotitoli.srt`, `anteprima_video.jpg`, `copertina.png`, `script/frasi.json`, `script/parole.json`. Va copiato in `script/` del post insieme agli altri script, a `config_video.py` e a `scene_elevenlabs.json`. Variabili: `MUSICA=`, `RITMO=0`, `PAUSA_PRIMA=`, `LAVORO=`, `FONTS=`, `FORZA=1` |
| `frasi.py` | divide il **testo noto** (campo `text` di `scene_elevenlabs.json`) in frasi allineate alle pause (silencedetect -35 dB / 0,08 s). Pause e spazi tra parole si confrontano "in sillabe" (picchi di energia ≈ sillabe), con programmazione dinamica; preferisce punteggiatura e congiunzioni, scarta le micro-pause dentro le parole (occlusive). Verificato sulla voce v1 del post risparmio (13 frasi identiche a quelle fatte a mano) e sulla v2 (controllata con energia e fricative). Se lo scarto medio supera 3 sillabe, il testo letto è probabilmente diverso: trascrivi |
| `ritmo.py` | pause tra frasi oltre 0,4 s → 0,3 s (taglio dal centro del silenzio, dissolvenze 10 ms), pausa scelta prima di una frase (`--pausa-prima "Ma perché?=0.36"`), attacco 0,05 s; accelera (rubberband di ffmpeg, formanti preservate; altrimenti atempo) **solo** se si resta sotto 165 parole/min, fino a ~170 e mai oltre 1,12x. Riscrive i tempi delle frasi e salva il resoconto (`frasi_ritmo.json`) |
| `allinea.py` | tempi stimati di ogni parola dentro le frasi → `parole.json` (`[{"w","start","end"}]`). Con l'allineamento ElevenLabs basta convertire i caratteri in parole nello stesso formato |
| `config_video_esempio.py` | configurazione del post risparmio v2: copiala come `config_video.py` e adattala. Parole indicate **per testo** (`"quattrocentosettanta"`, `"mai#2"`), titoli **riga per riga** con ingresso su una parola, `SCRITTE` stampate sulla sorgente (il conto sullo scontrino), `SUBS` con `{n}` (un numero a schermo che copre n parole parlate) e `_` (spazio che non separa), `OCCHIALI` (box di occhiali e volto per immagine), `EFFETTI` (effetto, parola) |
| `montage.py` | **controlli automatici** (volto in campo, occhiali fuori dalla fascia destra e non coperti da titoli/sottotitoli/fumetto/scritte, zoom massimo, zone sicure dei testi, cambio visivo ≤ 2 s, loop) e rendering: viste con zoom 100→104% che cresce attorno agli occhiali, tagli prima della parola o dopo la fine di una parola (`dopo`), tenda, titoli a righe con pop, scritte, sottotitoli ancorati in basso con parole spente/accese, fumetto (`bubble_parola`). Fine video = ultima parola + 0,45 s. `--preview DIR`, `--solo-controlli`, `--forza` |
| `effetti.py` | effetti sintetizzati in numpy: `scontrino`, `tick`, `pop` (più i vecchi colpo, moneta, monetine, forbici, carta, salvadanaio); livelli in `LIVELLO` (dB sul picco della voce) |
| `musica.py` | base con licenza: -20 dB sotto la voce (misura LUFS), loop/taglio, dissolvenze, ducking sidechain 3:1 |
| `norm.sh` | loudnorm a due passaggi: -14 LUFS, true peak -2 dBTP (dopo l'AAC il picco risale di ~0,4 dB) |
| `fotogrammi.py` | fotogrammi di controllo (0 s, ogni taglio, 60% di ogni inquadratura, ultimo) e `anteprima_video.jpg` |
| `copertina_esempio.py` | copertina 1080x1920 del post risparmio (immagine 01 + "470 €"): da copiare come `copertina.py` e cambiare testi e vista |
| `trascrizione.py` | `trascrizione.md` e `sottotitoli.srt` da `parole.json` (battute alla punteggiatura, ≤ 42 caratteri) |

## Procedura

1. **Voce**: `voce_elevenlabs.py … --conferma` (vedi `voce-elevenlabs.md`) oppure l'mp3 caricato dall'utente in `voce.mp3`. **Trascrivi sempre l'audio** (`script/transcribe.py` del post risparmio: `muse-spark-1.3`, intero e a spezzoni da almeno 3-5 s; gli spezzoni troppo corti tornano "non vedo audio"): controlla che il testo sia quello delle scene, che i tag (`[surprised]`…) non siano stati letti e che non ci siano parole aggiunte. Se il testo cambia, aggiorna `scene_elevenlabs.json` (`text`), `SUBS` e le parole di `config_video.py` prima di montare.
2. **Ritmo**: misura le parole al minuto (le stampa `ritmo.py`). Obiettivo dell'utente 165-175 parole/min, pause solo a fine frase. Attenzione: la durata dipende dalle parole (93 parole a 170/min = 33 s), non si "comprime" un testo lungo in 27 s senza superare 175 parole/min.
3. **Immagini e box**: per ogni immagine misura su una griglia ogni 100 px il box degli occhiali (lenti + ponte) e del volto (orecchie comprese) e scrivili in `OCCHIALI`; verificali disegnandoli. (Il rilevamento automatico del nero pieno è stato provato e non è affidabile: le lenti si fondono con contorni e fondo inchiostro.)
4. **Inquadrature**: due-tre per immagine, tagli all'inizio di frase o di parola chiave, una ogni ≤ 2 s. Larghe 70-95% (orso intero, testa sotto il titolo), strette fino a 112-115% sul soggetto nominato con il volto intero. Scegli `view` in modo che i sottotitoli (1400-1600) cadano su pavimento/fondo o sul corpo, mai sugli occhiali.
5. `python3 montage.py voce.wav parole.json x.mp4 --solo-controlli` finché non ci sono errori, poi `--preview prev/` e guarda i fotogrammi con Read (fai un contact sheet con le fasce sicure). Poi `monta.sh`.
6. **Controllo finale**: `anteprima_video.jpg` + fotogrammi a ogni taglio, a piena risoluzione i punti delicati (ingresso dei numeri, transizione, scritte); loudness (-14 LUFS, true peak ≤ -1 dBFS) e livello degli effetti (ben sotto la voce).
7. README del post: stato, checklist di pubblicazione, voce e ritmo (durate e parole/min prima/dopo), tabella inquadrature, controlli, limiti, comando per rifarlo.

Senza voce (per provare impaginazione e inquadrature) si può fare un render con un audio muto e `parole.json` costruito dai tempi del piano (sillabe distribuite nei secondi di ogni scena): `montage.py` non ha bisogno d'altro.

## Limiti da dichiarare sempre

- Non puoi ascoltare la voce: naturalezza, intonazione (domande che salgono, enfasi) e tagli delle pause non sono verificati da un orecchio umano.
- La sincronia delle parole dentro una frase è stimata (fino a ~0,15 s) se non c'è l'allineamento parola per parola di ElevenLabs.
- Niente musica scaricata dal web.
