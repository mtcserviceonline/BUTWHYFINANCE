# Estensione "BWF · Salva analitiche TikTok Studio"

Estensione per **Chrome, Edge e Brave** (Manifest V3). Con un clic salva in un file `.json` le analitiche del post aperto in TikTok Studio: le tre schede (Panoramica, Spettatori, Coinvolgimento) e le risposte che la pagina ha già scaricato, dove si trovano anche i dati della curva di retention.

**Stato: versione 0.1, collaudata solo su una pagina finta** che imita TikTok Studio (`test/`). Il primo salvataggio sul vero TikTok Studio serve a vedere come sono fatti i dati reali; poi si sistema il lettore.

## Installazione (una volta)
1. Apri `chrome://extensions` (o `edge://extensions`).
2. Attiva **Modalità sviluppatore** (in alto a destra).
3. **Carica estensione non pacchettizzata** e scegli questa cartella (`tools/estensione-tiktok-studio`).
4. Fissa l'icona verde con "€" nella barra del browser.

## Uso (per ogni post)
1. Apri in TikTok Studio i **dettagli del post** (la pagina con Panoramica, Spettatori, Coinvolgimento).
2. **Ricarica la pagina (F5)** una volta: serve a registrare le risposte della pagina dall'inizio.
3. Clic sull'icona → **Salva dati di questo post**. Per qualche secondo l'estensione apre da sola le tre schede, come faresti tu; non cambiare pagina.
4. Il file arriva in `Download/BWF-metriche/tiktok-studio_<id>_<data>.json`. Il popup mostra un riepilogo (metriche lette, risposte salvate, curve numeriche trovate).
5. Metti il file in `brand/tiktok/metriche/grezzi/` oppure allegalo in chat: lo trasformo nel JSON delle metriche e aggiorno il registro della guida.

Quando farlo: a **2 ore**, **24 ore** e **7 giorni** dalla pubblicazione.

## Cosa salva
- **Testo di ogni scheda** (completo, "testo_grezzo") e i valori letti: titolo, data, contatori (visualizzazioni, mi piace, commenti, condivisioni, salvataggi), tempo totale e medio di visione, % che guarda tutto il video, nuovi follower, picco di abbandono, fonti di traffico, sesso, età, posizioni, momento dei mi piace.
- **Risposte JSON** che TikTok Studio ha caricato (fino a 300; ognuna sotto 1,5 MB), con l'indirizzo ripulito dai parametri sensibili (token, firme, id di dispositivo, ecc., sostituiti da `REDATTO`).
- **Indizi:** gli elenchi di numeri trovati nelle risposte (probabili curve di retention, visualizzazioni per ora, momenti dei mi piace).

## Privacy e sicurezza
- L'estensione **non fa richieste di rete**, non invia nulla fuori dal browser e non legge pagine diverse da `tiktok.com`. Il file resta sul tuo computer.
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
`node test/prova.js` (serve Playwright) carica l'estensione in Chromium, apre una pagina finta con le stesse etichette degli screenshot di TikTok Studio e verifica 21 punti: lettura delle metriche, delle fonti di traffico, di età, sesso e posizioni, registrazione di `fetch` e `XMLHttpRequest`, rimozione dei token e ritrovamento delle curve. Il salvataggio su disco è verificato solo fino alla richiesta di download al browser (non il percorso finale in headless).
