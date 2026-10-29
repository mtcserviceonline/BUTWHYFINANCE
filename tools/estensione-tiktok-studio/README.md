# Estensione "BWF · Salva analitiche TikTok Studio"

Estensione per **Chrome, Edge e Brave** (Manifest V3). Con un clic salva in un file `.json` le analitiche del post aperto in TikTok Studio: le tre schede (Panoramica, Spettatori, Coinvolgimento) e le risposte che la pagina ha già scaricato, dove si trovano anche i dati della curva di retention.

**Stato: versione 0.2, collaudata solo su una pagina finta** che imita TikTok Studio (`test/`). Il primo salvataggio sul vero TikTok Studio serve a vedere come sono fatti i dati reali; poi si sistema il lettore.

## Installazione (una volta)
1. Apri `chrome://extensions` (o `edge://extensions`).
2. Attiva **Modalità sviluppatore** (in alto a destra).
3. **Carica estensione non pacchettizzata** e scegli questa cartella (`tools/estensione-tiktok-studio`).
4. Fissa l'icona verde con "€" nella barra del browser.

## Dove salva: scegli tu
Clicca sull'icona e, sotto il pulsante, **"scegli una cartella fissa"** (o "cambia cartella"): si apre una pagina con due modalità.
- **Cartella fissa:** scegli una volta una cartella, anche dentro il repo (consigliata: `brand/tiktok/metriche/grezzi`). Da quel momento ogni salvataggio scrive lì, senza finestre. Il browser non permette di scegliere direttamente Documenti, Download o Scrivania: scegli una cartella dentro. Il browser può chiederti di riconfermare il permesso all'inizio di una nuova sessione; il pulsante "Verifica il permesso" lo fa subito.
- **Chiedi ogni volta:** dopo la lettura si apre una scheda con il pulsante "Scegli dove salvare…" (finestra "Salva con nome", con il nome già proposto).
Se non hai ancora scelto nessuna cartella, l'estensione usa "Chiedi ogni volta". Se la cartella fissa non è più scrivibile (spostata, cancellata, permesso negato), passa da sola a "Chiedi ogni volta" e te lo dice.

## Uso (per ogni post)
1. Apri in TikTok Studio i **dettagli del post** (la pagina con Panoramica, Spettatori, Coinvolgimento).
2. **Ricarica la pagina (F5)** una volta: serve a registrare le risposte della pagina dall'inizio.
3. Clic sull'icona → **Salva dati di questo post**. Per qualche secondo l'estensione apre da sola le tre schede, come faresti tu; non cambiare pagina.
4. Il file `tiktok-studio_<id>_<data>.json` finisce nella cartella scelta (o dove lo salvi tu). Il popup mostra un riepilogo (metriche lette, risposte salvate, curve numeriche trovate).
5. Se non lo hai già salvato in `brand/tiktok/metriche/grezzi/`, mettilo lì o allegalo in chat: lo trasformo nel JSON delle metriche e aggiorno il registro della guida.

Quando farlo: a **2 ore**, **24 ore** e **7 giorni** dalla pubblicazione.

Dopo un aggiornamento dell'estensione: `chrome://extensions` → pulsante "Ricarica" sulla scheda dell'estensione, poi F5 sulla pagina di TikTok Studio.

## Cosa salva
- **Testo di ogni scheda** (completo, "testo_grezzo") e i valori letti: titolo, data, contatori (visualizzazioni, mi piace, commenti, condivisioni, salvataggi), tempo totale e medio di visione, % che guarda tutto il video, nuovi follower, picco di abbandono, fonti di traffico, sesso, età, posizioni, momento dei mi piace.
- **Risposte JSON** che TikTok Studio ha caricato (fino a 300; ognuna sotto 1,5 MB), con l'indirizzo ripulito dai parametri sensibili (token, firme, id di dispositivo, ecc., sostituiti da `REDATTO`).
- **Indizi:** gli elenchi di numeri trovati nelle risposte (probabili curve di retention, visualizzazioni per ora, momenti dei mi piace).

## Privacy e sicurezza
- L'estensione **non fa richieste di rete**, non invia nulla fuori dal browser e non legge pagine diverse da `tiktok.com`. Il file resta sul tuo computer, nella cartella che scegli. Non ha il permesso "downloads": scrive solo dove glielo permetti tu con il selettore del browser.
- Non usa e non salva password né cookie. I corpi delle risposte però possono contenere identificativi del tuo account: **controlla il file prima di condividerlo**.
- Si attiva **solo quando clicchi** sull'icona. L'unica azione automatica sulla pagina è il clic sulle tre schede.
- Per registrare le risposte modifica `fetch` e `XMLHttpRequest` della pagina (in sola lettura). È un intervento sulla pagina che TikTok potrebbe non gradire: rischio basso, ma non nullo. È molto più prudente di uno script che apre i post da solo.

## Se qualcosa non funziona
| Sintomo | Cosa fare |
|---|---|
| "La pagina non risponde" | Ricarica la pagina (F5) e riprova; l'estensione agisce solo su pagine aperte dopo l'installazione |
| "Nessuna risposta di rete registrata" | Ricarica (F5) e riclicca; se resta vuoto, TikTok carica i dati in modo diverso: manda il file e lo adatto |
| Metriche lette = 0 | Le etichette in pagina sono cambiate o la lingua non è l'italiano: manda il file (c'è il testo grezzo) e adatto il lettore |
| La scheda non cambia | TikTok ha cambiato l'interfaccia: manda il file con il testo grezzo |

## Collaudo
`node test/prova.js` (serve Playwright) carica l'estensione in Chromium, apre una pagina finta con le stesse etichette degli screenshot di TikTok Studio e verifica 27 punti: lettura delle metriche, delle fonti di traffico, di età, sesso e posizioni, registrazione di `fetch` e `XMLHttpRequest`, rimozione dei token, ritrovamento delle curve e i tre percorsi di salvataggio (cartella fissa, "chiedi ogni volta", pagina delle opzioni). **Limite:** i veri selettori di cartella e di file del browser non si possono automatizzare; nel collaudo li sostituisco con una cartella interna dell'estensione, che usa le stesse funzioni di scrittura. La scelta con il selettore vero va provata a mano la prima volta.
