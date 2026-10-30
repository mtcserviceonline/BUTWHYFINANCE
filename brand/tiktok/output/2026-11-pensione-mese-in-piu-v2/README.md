# In 60 secondi · Pensione a 67 anni e un mese: cosa puoi fare (TikTok, v2)

**Stato: in attesa della nuova scena 1 per il montaggio.** Testo approvato dall'utente e registrato (30/10/2026); ricerca, copione, scene voce, didascalia, 8 immagini, copertina e configurazione del montaggio sono pronti. La registrazione attuale (`voce.mp3`) ha la **scena 1 sbagliata** e **non è stata montata**: quando arriva la scena 1 rifatta bastano due comandi (sotto). Fonti tutte **lette solo in sintesi**.

Rubrica: **In 60 secondi** (accento fucsia `#B0186E`, unico accento) · 80 parole, ~28 s previsti a ~170 parole/min · post precedente sullo stesso tema, lasciato com'era: [`../2026-11-pensione-67-anni-un-mese/`](../2026-11-pensione-67-anni-un-mese/README.md)

![Anteprima delle immagini](immagini/anteprima.jpg)

## Cosa è cambiato (30/10/2026)

L'utente non ha gradito lo speech "Vero o falso? Il governo alza l'età pensionabile" e l'ha cambiato del tutto: dire che l'età pensionabile si alza, dare **consigli finanziari semplici** su cosa fare per tutelarsi e chiedere cosa ne pensano. Quindi:

1. **Rubrica** da *Vero o falso?* (viola) a ***In 60 secondi*** (fucsia): spiega un meccanismo in modo compatto (perché l'età sale) e poi tre passi pratici. *Il numero* (blu) è già del post precedente.
2. **Immagini tutte nuove** in fucsia (le 8 viola avevano oggetti viola pensati per il verdetto: timbro, ingranaggi, cubi, bilancia).
3. **Regola di brand nuova** (decisione dell'utente): consigli finanziari semplici e generali sì, mai prodotti/fondi/titoli specifici né importi o rendimenti promessi, sempre l'avvertenza "informazione, non consulenza". Aggiornati `references/brand.md`, `SKILL.md`, `controllo-qualita.md`, `copione.md`, `didascalia.md`, `ricerca.md` di `crea-post-tiktok`, la rubrica di `rivedi-post-tiktok` e i valutatori `bwf-valuta-brand`, `bwf-valuta-pubblico`, `bwf-redattore`.

## Contenuto della cartella

| Elemento | File | Stato |
|---|---|---|
| Ricerca e fonti | [`ricerca.md`](ricerca.md) | fatto · 9 righe, **tutte lette in sintesi** (inps.it e gli altri siti non raggiungibili), 3 non usate |
| Copione + production doc | [`copione.md`](copione.md) | approvato dall'utente (testo); 16 inquadrature |
| Scene ElevenLabs | [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json), [`script/elevenlabs.txt`](script/elevenlabs.txt) | pronte, col testo approvato (tre versioni) |
| Immagini | [`immagini/`](immagini/README.md): 8 PNG 1080x1920, `scene.json`, `prompts.json`, `anteprima.jpg` | pronte · 11 generazioni, 3 rifatte |
| Copertina | [`copertina.png`](copertina.png) (`script/copertina.py`) | pronta: orso sorpreso + sedia che scappa, «PENSIONE / 67 ANNI / + 1 MESE» |
| Didascalia | [`didascalia.md`](didascalia.md) | pronta: completa, breve, commento fissato, risposte pronte |
| Voce | `voce.mp3` (ElevenLabs, "Valerio – Warm Italian Storyteller", 30,04 s) | **scena 1 da rifare** (sotto); il resto è giusto |
| Montaggio | `script/` (`monta.sh`, `config_video.py`, `montage.py`, `sostituisci_scena1.py` e gli altri script) | **pronto, non lanciato** sulla voce del post (provato solo nello scratchpad) |
| Video, `trascrizione.md`, `sottotitoli.srt`, `tempi.json`, `anteprima_video.jpg` | — | da fare con la nuova scena 1 |

## Voce: perché la scena 1 va rifatta

Trascrizione della registrazione (`muse-spark-1.3`, `script/transcribe.py`, file intero e 8 spezzoni) confrontata con il testo approvato:

- **Scena 1 diversa (5 trascrizioni su 5):** l'audio dice «Dal duemilaventisette, **per raggiungere la pensione di vecchiaia, si dovrà lavorare un mese in più**» invece di «Dal duemilaventisette, **per quasi tutti, la pensione di vecchiaia si sposta più in là**». Lo confermano le micro-pause (3,37-3,48 s dopo «duemilaventisette», 3,69-3,81 s dopo un solo «per»). Manca «per quasi tutti», la correzione chiave del post precedente.
- **Il resto è giusto:** «Ma perché? Si vive più a lungo. L'età sale con la speranza di vita. Cosa puoi fare? Primo, controlla i contributi versati, nel tuo estratto conto INPS. Secondo, stima la tua pensione con il simulatore gratuito dell'INPS. Terzo, valuta un fondo pensione. Quello che versi si può dedurre dalle tasse. Prima inizi, meglio è. E tu, ci stai già pensando?» Nessun tag letto. (Il file intero aggiunge «Ma tu quando andrai in pensione?», che negli spezzoni non c'è: invenzione del trascrittore.)

**Testo da registrare di nuovo** (solo questo, eleven_v3, stessa voce e impostazioni):

```
[surprised] Sessantasette anni e un mese. Dal duemilaventisette, per quasi tutti, la pensione di vecchiaia si sposta più in là.
```

(Si può anche rigenerare il testo intero di `script/elevenlabs.txt`, versione 1: lo script sotto prende solo la scena 1.)

## Montaggio: come finirlo quando arriva la scena 1

Dalla radice del repository:

```bash
P=brand/tiktok/output/2026-11-pensione-mese-in-piu-v2
python3 $P/script/sostituisci_scena1.py NUOVA_SCENA1.mp3 --out $P/voce.mp3   # controlla la trascrizione che stampa
bash $P/script/monta.sh $P/voce.mp3                                          # ~3 minuti
```

- `sostituisci_scena1.py` tiene la voce attuale da 7,70 s (nel silenzio 7,34-7,77 s, subito prima di «Ma perché?») e ci mette davanti la nuova scena 1, tolti i silenzi. Se il file nuovo contiene tutto il testo, cerca da solo la fine della scena 1 (il silenzio più lungo fra 4,5 e 10 s, stampa i candidati; altrimenti `--fine SECONDI`). Pareggia il volume solo oltre 3 dB di differenza, 0,40 s di pausa alla giunzione, dissolvenze di 10 ms, e **trascrive la nuova scena 1** per controllare il testo. Provato sulla voce attuale: giunzione pulita, «Ma perché?» a ~7,9 s.
- `monta.sh` (catena della skill, copiata dal post `2026-11-pensione-67-anni-un-mese` con montage.py in fucsia): frasi → ritmo (pause > 0,4 s → 0,3 s, 0,36 s prima di «Ma perché?», **accelerazione al massimo 1,05x**, variabile `VMAX`) → parole → controlli automatici + video → effetti → -14 LUFS → fotogrammi, copertina, trascrizione. Scrive nel post `video.mp4`, `tempi.json`, `trascrizione.md`, `sottotitoli.srt`, `anteprima_video.jpg`, `copertina.png`.
- **Prova della catena** (nello scratchpad, con la voce attuale e una copia del post: non è il video del post): 79 parole, 30,04 → 27,96 s, 158 → 162 parole/min dopo le pause → **170 parole/min a 1,047x**; video **28,3 s**; **controlli automatici 0 errori, 0 avvisi**; cambio visivo più lungo 1,87 s; -14,9 LUFS, true peak -1,9 dBFS. Con la scena 1 nuova i numeri cambieranno di poco; se un controllo fallisce (di solito un cambio > 2 s), spostare la parola d'inizio dell'inquadratura in `config_video.py`.
- **Inquadrature** (16, dettagli nel production doc di `copione.md`): hook su 01 con «PENSIONE / 67 ANNI» dal fotogramma 0, colpo e punch-in 112%, «+ 1 MESE» sulla parola · 02 calendario (tenda) «DAL 2027» → «PER QUASI TUTTI» → «ECCEZIONI? LEGGI LA DIDASCALIA ↓», poi «PENSIONE DI VECCHIAIA / PIÙ IN LÀ →» · 01 stretta «MA PERCHÉ?» + fumetto, nessun titolo di rubrica · 03 sentiero «SI VIVE PIÙ A LUNGO / → L'ETÀ SALE» · 04 «COSA PUOI FARE?» → «1 · ESTRATTO CONTO» · 05 «2 · SIMULATORE INPS» · 06 «3 · FONDO PENSIONE» + «Informazione, non consulenza finanziaria» · 07 clessidra «PRIMA INIZI, / MEGLIO È» · 08 occhiolino «CI STAI GIÀ PENSANDO?» + avvertenza · loop sul fotogramma 0 con «?» al posto di «67 ANNI». Titoli dei consigli sopra la testa; sottotitoli mai su occhiali (controllo automatico) né su € (controllato con le coordinate della € di ogni immagine: fondo della € ≤ y 1390, sottotitoli da ~1400).

## Didascalia

Pronta in [`didascalia.md`](didascalia.md): fatto con fonte (INPS circ. 28/2026), perché, i tre consigli con il «come» (MyINPS → Estratto conto contributivo; MyINPS → La mia pensione futura; fondo pensione con versamenti deducibili fino a 5.300 €/anno dal 2026), eccezioni corrette (difesa e sicurezza **non** escluse), avvertenza, domanda «E tu, ci stai già pensando?», hashtag `#butwhyfinance #maperché #pensioni #fondopensione #educazionefinanziaria`.

## Checklist di pubblicazione

- [ ] **Scena 1 registrata di nuovo** col testo approvato; `sostituisci_scena1.py` → trascrizione giusta; `monta.sh` → controlli a 0 errori.
- [ ] Guardare `anteprima_video.jpg` e i fotogrammi a ogni cambio; **ascoltare** il video intero sul telefono (giunzione prima di «Ma perché?», «per quasi tutti» detto piano, domande che salgono).
- [ ] Fonti "lette in sintesi" aperte sull'originale:
  - [ ] INPS, circolare n. 28 del 16/03/2026: 67a1m nel 2027; lista delle esclusioni parola per parola; difesa e sicurezza **non** esclusi.
  - [ ] L. 199/2025, art. 1 c. 180-190 (esclusioni) e **c. 201** (deducibilità 5.300 €, decorrenza): Normattiva o Gazzetta Ufficiale; D.Lgs. 252/2005 art. 8.
  - [ ] inps.it: servizi "Estratto conto contributivo" e "La mia pensione futura" attivi, accesso con SPID/CIE/CNS, nomi del menu.
  - [ ] Il giorno dell'uscita: ddl di bilancio 2027 (CdM 28/10/2026), che non cambi lo scatto 2027, le esclusioni o la deducibilità.
- [ ] Copertina `copertina.png` caricata; didascalia e hashtag incollati alla lettera da `didascalia.md`; commento fissato pubblicato subito.
- [ ] Etichetta TikTok **"contenuto generato da IA"** attivata (immagini e voce).
- [ ] Musica solo dalla libreria commerciale di TikTok, bassa (~-20 dB sotto la voce).

## Limiti

- Non posso ascoltare: giunzione, intonazione e pause non sono verificate da un orecchio. La sincronia delle parole dentro le frasi è stimata (errore atteso < 0,15 s).
- Nessuna fonte aperta sull'originale (siti non raggiungibili da questa sessione): domini da abilitare `www.inps.it`, `www.normattiva.it`, `www.gazzettaufficiale.it`, `www.agenziaentrate.gov.it`, `www.covip.it`.
