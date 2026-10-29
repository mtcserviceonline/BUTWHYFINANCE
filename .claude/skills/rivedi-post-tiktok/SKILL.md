---
name: rivedi-post-tiktok
description: >-
  Rivede a più giri lo script di un video TikTok di But Why Finance fino al post definitivo: quattro agenti
  valutatori in parallelo (verifica dei fatti, ritenzione, brand, pubblico) danno punteggi e correzioni, un
  redattore le applica, e si ripete finché nessuno ha bloccanti e ogni media è ≥ 4,2 (massimo 3 giri); poi
  produzione con crea-post-tiktok (immagini, anteprima, didascalia, README "post definitivo"), voce e video
  quando l'utente carica l'mp3. Usala quando l'utente dice "rivedi il post", "valuta lo script", "migliora il
  copione", "portalo al definitivo" o lancia /rivedi-post-tiktok <cartella del post>.
---

# Rivedi un post TikTok fino al definitivo

Uso: `/rivedi-post-tiktok <cartella del post>` (es. `brand/tiktok/output/2026-11-pensione-67-anni-un-mese`).

Cartella indicata dall'utente: $ARGUMENTS

Scrivi e rispondi **in italiano**. Il post deve già avere almeno `copione.md`, `script/scene_elevenlabs.json`, `script/elevenlabs.txt`, `didascalia.md`, `ricerca.md` (come escono dalla skill `crea-post-tiktok`). Se manca qualcosa, dillo e proponi di crearlo con `crea-post-tiktok` prima di iniziare.

Criteri, soglie, metodo di conteggio parole e formato dei rapporti: [`references/rubrica.md`](references/rubrica.md).

## I ruoli

| Agente (`.claude/agents/`) | Cosa fa | Scrive |
|---|---|---|
| `bwf-verifica-fatti` | ogni numero, data, tesi attribuita con WebSearch/WebFetch; calcoli in Python | `revisione/rN-verifica-fatti.md` |
| `bwf-valuta-ritenzione` | hook, "Ma perché?", parole e durata a 170/min, cambi visivi ≤ 2 s, loop, chiusura, leggibilità, SEO | `revisione/rN-ritenzione.md` |
| `bwf-valuta-brand` | voce, neutralità, nessuna consulenza, regole visive, "Sai che…?", hashtag, etichetta IA, coerenza fra file | `revisione/rN-brand.md` |
| `bwf-valuta-pubblico` | chi parte da zero capisce, 5 parametri, commenti/condivisioni/salvataggi, fraintendimenti | `revisione/rN-pubblico.md` |
| `bwf-redattore` | applica tutti i bloccanti e i migliorativi compatibili, riscrive i file del post, changelog | file del post + `revisione/rN-redattore.md` |

I valutatori **non modificano** i file del post. Nessun agente fa commit: lo fa questa sessione, **uno solo a fine giro**.

## Come lanciare gli agenti

- **Se i tipi `.claude/agents` sono caricati** nella sessione (compaiono fra i tipi di agente disponibili): lancia ciascuno con il suo `subagent_type` (`bwf-verifica-fatti`, …) e un prompt breve: `Cartella del post: <cartella>. Giro: N.`
- **Se non sono caricati** (sessione avviata prima che i file esistessero, o ambiente che non li legge): lancia un agente **general-purpose** per ruolo con prompt = **intero contenuto del file `.claude/agents/<ruolo>.md` senza il frontmatter** + in fondo:

  ```
  ---
  Cartella del post: <cartella>
  Giro: N
  Radice del repository: /home/user/BUTWHYFINANCE
  ```

  Per il verificatore assicurati che l'agente abbia WebSearch e WebFetch (general-purpose li ha). Leggi il file con Read e incollalo così com'è: non riassumerlo.
- I quattro valutatori vanno **in background e in parallelo** (scrivono file diversi); il redattore parte **solo quando tutti e quattro hanno finito**.

## Flusso

### 0. Preparazione (una volta)
1. Leggi la cartella del post e `references/rubrica.md`. Se esiste già `revisione/`, riprendi dal primo giro incompleto (non sovrascrivere i rapporti esistenti).
2. Conta parole e durata con lo script di `rubrica.md` e dillo all'utente in una riga (es. "75 parole, ~26,5 s a 170/min").
3. Crea `revisione/` nella cartella del post.

### Giro N (N = 1, 2, 3)
1. **Valutatori in parallelo**: lancia i 4 agenti in background con cartella e `N`. Mentre lavorano non toccare i file del post.
2. **Raccogli i verdetti**: quando hanno finito, controlla che esistano i 4 file `revisione/rN-*.md` e leggi i blocchi JSON finali:

   ```bash
   python3 - <cartella> N <<'PY'
   import glob, json, re, sys
   post, n = sys.argv[1], sys.argv[2]
   ruoli = ["verifica-fatti", "ritenzione", "brand", "pubblico"]
   tutti_ok = True
   for r in ruoli:
       f = f"{post}/revisione/r{n}-{r}.md"
       try:
           blocchi = re.findall(r"```json\s*(\{.*?\})\s*```", open(f, encoding="utf-8").read(), re.S)
           v = json.loads(blocchi[-1])
       except Exception as e:
           print(f"{r}: rapporto mancante o JSON non valido ({e})"); tutti_ok = False; continue
       ok = v["bloccanti"] == 0 and v["media"] >= 4.2
       tutti_ok &= ok
       print(f"{r:15} media {v['media']:.1f} · bloccanti {v['bloccanti']} · verdetto {v['verdetto']} · soglia {'OK' if ok else 'NO'}")
   print("STOP" if tutti_ok else "CONTINUA")
   PY
   ```
   Se un JSON manca o è incoerente (es. `verdetto: ok` con bloccanti > 0), vale la soglia calcolata, non il verdetto dichiarato; se un rapporto manca, rilancia solo quel valutatore.
3. **Condizione di stop**: **nessun bloccante e media ≥ 4,2 per ognuno dei 4 valutatori** → vai a "Dopo lo stop" (non serve il redattore).
4. Altrimenti **redattore** (`bwf-redattore`, cartella + `N`): applica le correzioni e scrive `revisione/rN-redattore.md`.
5. **Controllo rapido** dopo il redattore (questa sessione, eseguendo): conteggio parole, JSON valido, testo identico fra `scene_elevenlabs.json`, `copione.md` ed `elevenlabs.txt`, nessuna cifra nel `text`. Se qualcosa non torna, correggilo o rilancia il redattore.
6. **Riepilogo del giro** in `revisione/stato.md` (una tabella che cresce giro per giro: giro, media e bloccanti per ruolo, parole, decisione) e in chat (3-6 righe + il nuovo testo della voce v3).
7. **Commit unico del giro** (vedi "Regole git") e poi giro `N+1`.
8. **Dopo il giro 3**, se la soglia non è raggiunta: il redattore del giro 3 applica le correzioni, fai il controllo rapido e **fermati**. Elenca all'utente **ciò che resta**: prima i bloccanti aperti (con ID, ruolo e cosa serve per chiuderli, es. "aprire la circolare INPS 28/2026"), poi le medie sotto 4,2 con i migliorativi principali. Chiedi se procedere comunque alla produzione o fare un altro giro.

Se l'utente è presente, mostragli il testo nuovo a ogni giro; non serve aspettare il suo ok fra un giro e l'altro, salvo che lo chieda.

## Dopo lo stop: produzione con `crea-post-tiktok`

Segui la skill `.claude/skills/crea-post-tiktok/SKILL.md` dai passi che mancano, sul testo ormai approvato dai valutatori (non riscrivere il copione):

1. **Immagini** (passo 5 della skill): `immagini/scene.json` in inglese dalle `immagini_previste` delle scene → `componi_prompt.py` → `genera_immagine.py` per ognuna → **guarda ogni immagine con Read** e lancia `controlla_immagini.py` (fondi, ingombro, fasce libere; nessuna scritta, occhiali e € visibili, niente rosso) → rigenera solo le difettose, max 3 tentativi → `anteprima.py` → `immagini/README.md`. Puoi delegare a un agente in background che scrive solo `immagini/`.
2. **Didascalia finale**: rileggi `didascalia.md` dopo le immagini (hashtag `#butwhyfinance #maperché` + 2-3 pertinenti, domanda uguale al video, etichetta IA).
3. **README "post definitivo"**: riscrivi `README.md` del post con **Stato: post definitivo (testi e immagini) · voce e video da fare**, tabella di stato, riepilogo della revisione (giri, medie finali, link a `revisione/stato.md`), il **testo da incollare in ElevenLabs** (versioni 1 e 2 di `script/elevenlabs.txt`, la 3 se serve) e la **checklist di pubblicazione**:
   - [ ] fonti "letti in sintesi" aperte sull'originale (elenco da `ricerca.md`);
   - [ ] voce registrata su ElevenLabs dal testo della versione 1, salvata come `voce.mp3` nella cartella del post;
   - [ ] video montato con `script/monta.sh` (sotto) e guardato: hook a 0,0 s, occhiali mai coperti, cambio ≤ 2 s, loop;
   - [ ] copertina caricata; didascalia e hashtag incollati alla lettera;
   - [ ] etichetta TikTok **"contenuto generato da IA"** attivata;
   - [ ] musica solo dalla libreria commerciale di TikTok, bassa (~-20 dB);
   - [ ] eventuale A/B test dell'hook (variante proposta dalla ritenzione).
4. Commit della fase di produzione; in chat: anteprima delle immagini (SendUserFile), **testo ElevenLabs incollato**, didascalia incollata, cose da verificare, cosa manca.

### Voce e video: solo quando l'utente carica l'mp3
- Non generare la voce (piano ElevenLabs gratuito: 402 sulle voci italiane). Quando l'utente carica l'mp3, copialo in `<cartella>/voce.mp3`.
- Montaggio **come nel post del risparmio** (`brand/tiktok/output/2026-10-risparmio-quotidiano/`, sezione "Montaggio v2" del README, e `crea-post-tiktok/references/montaggio.md`): copia in `<cartella>/script/` gli script di `.claude/skills/crea-post-tiktok/scripts/` (`monta.sh`, `frasi.py`, `ritmo.py`, `allinea.py`, `montage.py`, `effetti.py`, `musica.py`, `norm.sh`, `fotogrammi.py`, `trascrizione.py`), `config_video_esempio.py` come `config_video.py` e `copertina_esempio.py` come `copertina.py`, adattali (inquadrature, titoli, `SUBS`, `OCCHIALI`, `punch`, loop con "?"), trascrivi l'audio per controllare il testo, poi:

  ```bash
  bash <cartella>/script/monta.sh <cartella>/voce.mp3
  ```
  Controlli automatici a 0 errori, guarda `anteprima_video.jpg` e i fotogrammi delicati, aggiorna README (durata, parole/min, limiti: non puoi ascoltare).

## Regole git (agenti in parallelo)

- Ogni agente scrive **solo i propri file** (vedi tabella dei ruoli); nessun agente fa `git add`, commit, pull o push.
- **Un solo commit a fine giro**, fatto da questa sessione: `git add <cartella del post>` (solo quella; mai `git add -A` o `git add .`), messaggio in italiano tipo `Revisione TikTok <slug>: giro N (medie …, bloccanti …)`, con in fondo le righe di attribuzione richieste dall'ambiente, se presenti nella conversazione.
- `git pull --rebase origin <branch corrente>` poi `git push -u origin <branch corrente>`; se il push fallisce per rete, ritenta 4 volte con attese 2, 4, 8, 16 s. Mai altri branch, nessuna PR salvo richiesta.
- Prove, file scaricati e audio grezzi nello scratchpad, mai nel repository.

## Consegna finale in chat

1. Esito: giri fatti, medie finali per ruolo, bloccanti residui (0 o elenco).
2. Testo della voce definitivo (versione v3) e didascalia.
3. Cosa resta da verificare prima di pubblicare e prossima mossa (immagini / voce / montaggio).
