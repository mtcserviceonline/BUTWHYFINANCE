# Cartella del post e consegna

## Struttura

`brand/tiktok/output/AAAA-MM-slug/` (anno e mese di oggi, slug corto in minuscolo con trattini, es. `2026-11-bollette-gas`):

```
AAAA-MM-slug/
├── README.md              indice, stato di ogni elemento, cose da verificare, cosa manca
├── ricerca.md             fatti con fonte/data/link/stato, stime, tesi, da verificare
├── copione.md             rubrica, durata, testo voce, production doc, hook, loop, SEO, controllo qualità
├── didascalia.md          versione completa e breve, hashtag, note di pubblicazione
├── script/
│   ├── scene_elevenlabs.json
│   └── elevenlabs.txt     testo unico da incollare (tag IT, tag EN v3, impostazioni v2)
├── immagini/
│   ├── 01.png … 08.png    1080x1920
│   ├── scene.json         scene in inglese (ingresso di componi_prompt.py)
│   ├── prompts.json       prompt finali
│   ├── README.md          tentativi, rigenerazioni, controlli, difetti noti
│   └── anteprima.jpg      contact sheet
├── voce.mp3               solo su richiesta (voce generata)
└── video.mp4              solo su richiesta (montaggio)
```

Non committare: risposte grezze `.webp`, immagini scartate, prove (tienile nello scratchpad), font, modelli.

## Modello di `README.md` del post

```markdown
# <Rubrica>: <titolo> (TikTok)

<Una riga: di cosa parla e qual è la domanda "Ma perché?".>

**Stato:** <bozza da approvare / pronto da montare / pubblicabile>

## Contenuto della cartella

| Elemento | File | Stato |
|---|---|---|
| Ricerca e fonti | [`ricerca.md`](ricerca.md) | fatto · <N> dati da verificare sulla fonte originale |
| Copione | [`copione.md`](copione.md) | fatto · testo voce da approvare |
| Scene voce | [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json) | fatto |
| Testo da incollare | [`script/elevenlabs.txt`](script/elevenlabs.txt) | fatto |
| Immagini | [`immagini/`](immagini/README.md) | 8/8 · difetti minori in README |
| Didascalia | [`didascalia.md`](didascalia.md) | fatto |
| Voce | `voce.mp3` | **manca**: piano ElevenLabs gratuito (402 sulle voci italiane) |
| Video | `video.mp4` | **manca**: montaggio da fare dopo la voce |

![Anteprima](immagini/anteprima.jpg)

## Prima di pubblicare
1. Verificare sulle fonti originali: <…>.
2. Approvare il testo della voce, poi registrarlo/generarlo.
3. Montaggio: titoli e sottotitoli (IBM Plex), zone sicure, base musicale con licenza a -20 dB.
4. Attivare su TikTok l'etichetta **"contenuto generato da IA"**.

## Cosa manca
- <voce, montaggio, musica, …>
```

## Lavoro in parallelo (agenti in background)

L'utente delega volentieri il lavoro lungo ad agenti in background. Dopo il copione (passo 3), si possono dividere:

- **Agente immagini**: solo `immagini/` (scene, prompt, generazione, controlli, anteprima, README delle immagini).
- **Agente testi**: `script/`, `didascalia.md`, `README.md`.

Regole per ogni agente: lavora solo sui **propri file**; `git add` **solo dei propri percorsi** (mai `git add -A` né `git add .`); `git pull --rebase origin <branch>` prima del push; non toccare cartelle di altri post su cui sta lavorando qualcun altro. Nel prompt dell'agente passa: percorso della cartella, copione, rubrica e accento, regole di brand (`references/brand.md`) e cosa deve restituire.

## Commit e push

- Solo sul **branch di sviluppo corrente** (`git branch --show-current`); mai su altri branch, **nessuna PR** salvo richiesta.
- `git add brand/tiktok/output/AAAA-MM-slug` (solo i percorsi del post).
- Messaggio di commit **in italiano**, breve e descrittivo (es. `TikTok bollette del gas: ricerca, copione, scene voce, 8 immagini e didascalia`).
- In fondo al messaggio le **righe di attribuzione richieste dall'ambiente**, se presenti nella conversazione (per esempio `Co-Authored-By: …` e `Claude-Session: …`): copiale esattamente come date, non inventarle.
- `git pull --rebase origin <branch>` poi `git push -u origin <branch>`. Se il push fallisce **per errore di rete**, ritenta fino a 4 volte con attese 2 s, 4 s, 8 s, 16 s. Per altri errori (rifiuto, conflitti) fermati e spiega.

## Messaggio finale in chat

L'utente vuole i testi **direttamente nel messaggio**, non solo nei file. In questo ordine:

1. Una riga: argomento, rubrica, durata stimata, link alla cartella.
2. **Anteprima delle immagini**: invia `immagini/anteprima.jpg` con SendUserFile (o lo strumento disponibile per inviare file).
3. **Testo ElevenLabs incollato** (contenuto di `script/elevenlabs.txt`: almeno tag italiani e tag inglesi v3, più le impostazioni per scena).
4. **Didascalia incollata** (completa + breve).
5. **Da verificare prima di pubblicare** (dati letti solo in sintesi, stime, difetti delle immagini).
6. **Cosa manca** (voce, montaggio, musica) e la prossima mossa utile.
