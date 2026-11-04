---
name: video-tiktok
description: Workflow obbligatorio per ogni video TikTok di But Why Finance. Usalo SEMPRE quando l'utente dà una notizia (link, titolo, testo incollato o screenshot) da trasformare in video TikTok, quando carica l'audio di ElevenLabs di un episodio, o quando chiede di riprendere un episodio in corso. Contesto (Opus) → testo ElevenLabs (Haiku alto) → audio dell'utente → immagini (Opus medio) → montaggio, copertina, didascalia → commit e push.
---

# Workflow video TikTok — But Why Finance

Tu (sessione principale) **coordini**: le fasi creative le fanno i subagenti con il modello fissato nel loro file. Non scrivere tu il testo né i prompt delle immagini.

| Fase | Chi | Modello |
|---|---|---|
| 1. Contesto | subagente `tiktok-ricercatore` | Opus, ragionamento alto |
| 2. Testo ElevenLabs | subagente `tiktok-copywriter` | Haiku, ragionamento alto |
| 3. Allineamento audio | script | — |
| 4. Immagini | subagente `tiktok-illustratore` | Opus, ragionamento medio |
| 5. Montaggio, copertina | script + tuo controllo | — |
| 6. Commit e push | tu | — |

Riferimenti: `brand/tiktok/stile-tiktok.md`, `brand/mascotte/README.md`, `brand/tiktok/pipeline/README.md`.

## 0. Preparazione (ogni sessione)

```bash
bash brand/tiktok/pipeline/setup.sh
```

Cartella dell'episodio: `brand/tiktok/output/AAAA-MM-slug/` (data di oggi, slug breve in minuscolo con trattini, es. `2026-11-mutui-tassi-bce`). Se l'utente riprende un episodio esistente, guarda quali file ci sono già e riparti dalla fase giusta.

## 1. Contesto → STOP

Lancia `tiktok-ricercatore` passandogli la notizia così come l'hai ricevuta (link, testo, o il percorso dello screenshot) e la cartella dell'episodio. Produce `fatti.md`.

Poi **fermati** e mostra all'utente, in breve: notizia in una frase, il numero chiave, le due tesi, rubrica e gancio proposti, la domanda finale.
- Se ci sono **dati non verificati**: elencali e chiedi come procedere (toglierli, cercare ancora, o una fonte dall'utente). Non andare avanti finché non lo dice.
- Chiedi di approvare o correggere l'angolo. Per le domande usa AskUserQuestion quando le opzioni sono chiare.

## 2. Testo per ElevenLabs → STOP

Dopo l'approvazione, lancia `tiktok-copywriter` con la cartella e le eventuali correzioni dell'utente. Produce `scene.json`, `voce-elevenlabs.txt`, `didascalia.md`. Controlla tu che `python3 brand/tiktok/pipeline/testo_elevenlabs.py <cartella>` esca senza ERRORE (altrimenti rimandalo al copywriter con l'errore).

Poi **fermati** e consegna all'utente il contenuto di `voce-elevenlabs.txt` in un blocco di codice, pronto da incollare, con le istruzioni:
- ElevenLabs → Text to Speech, modello **Eleven v3**, voce **Valerio**, lingua italiano.
- Incollare il testo così com'è (una riga per scena: gli a capo creano le pause su cui cadono i tagli).
- Scaricare l'mp3 e **caricarlo in chat**.

## 3. Audio → allineamento

Quando l'utente carica l'audio, trova il file (percorso indicato nel messaggio o tra gli allegati) e lancia:

```bash
python3 brand/tiktok/pipeline/allinea.py <cartella> <file audio>
```

Prova prima lo Speech-to-Text di ElevenLabs (tempi parola per parola, pochi crediti); se non ci sono crediti usa da solo il metodo locale basato sulle pause. Controlla la tabella stampata: ogni scena deve avere una durata sensata (circa 1-5 s). Se l'audio dura più di 42 s o una scena è palesemente sbagliata, dillo all'utente prima di andare avanti.

## 4. Immagini

Lancia `tiktok-illustratore` con la cartella. Produce `immagini/prompts.json` e `immagini/ID.png`, controllate e rigenerate (al massimo 2 volte ciascuna). Può partire anche mentre aspetti l'audio, subito dopo l'approvazione del testo, per risparmiare tempo.

## 5. Montaggio e controllo

```bash
python3 brand/tiktok/pipeline/monta.py <cartella> --anteprima   # un fotogramma per scena
```

Guarda `_lavoro/anteprima/provino.jpg`: titoli leggibili e non sovrapposti all'orso, sottotitoli dentro le zone sicure, nessuna scritta nelle immagini. Poi:

```bash
python3 brand/tiktok/pipeline/monta.py <cartella>      # video.mp4 (circa 2-3 minuti)
python3 brand/tiktok/pipeline/copertina.py <cartella>  # copertina.png
```

Scrivi `README.md` dell'episodio: tabella delle scene (tempo, immagine, titolo, voce), fonti, cosa è stato rigenerato, limiti noti.

## 6. Consegna, commit e push

- Commit con `fatti.md`, `scene.json`, `voce-elevenlabs.txt`, `didascalia.md`, `immagini/` (PNG + `prompts.json` + `prompt/`), `voce/voce-originale.*`, `voce/tempi.json`, `video.mp4`, `copertina.png`, `tempi-video.json`, `README.md`. **Non** committare `_lavoro/` (è in `.gitignore`).
- Push sul branch di lavoro della sessione.
- Messaggio finale all'utente: durata del video, la didascalia pronta da copiare e i promemoria: **attivare l'etichetta "contenuto generato da IA"** su TikTok, **aggiungere la base musicale dalla Commercial Music Library di TikTok** a circa -20 dB, caricare `copertina.png` come copertina.
