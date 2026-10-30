# Vero o falso?: «Il governo alza l'età pensionabile» (TikTok, v2)

Il mese in più per la pensione di vecchiaia (67 anni e 1 mese dal 2027, 67 e 3 mesi dal 2028), rifatto da zero. La domanda "Ma perché?": se l'età sale, è il governo che la alza? Verdetto: **vero a metà**. Sale per una regola automatica in vigore dal 2010, e la legge di bilancio 2026 ha rinviato al 2028 due mesi su tre.

**Stato:** bozza da approvare. Testi, scene voce, 8 immagini e copertina sono pronti; voce e video ancora da fare. **Tutte le fonti sono lette solo in sintesi.**

Rubrica: **Vero o falso?** (accento viola `#5B3FA8`) · 75 parole, ~27,5 s · post precedente sullo stesso tema, lasciato com'era per confronto: [`../2026-11-pensione-67-anni-un-mese/`](../2026-11-pensione-67-anni-un-mese/README.md)

![Anteprima delle immagini](immagini/anteprima.jpg)

## Perché questo angolo (e cosa cambia rispetto al post precedente)

1. Il post precedente (*Il numero*, blu) dava il dato «1 mese»: una notizia già letta ovunque, con «per tutti» da correggere e una tesi favorevole senza nome. Qui si parte da una **frase che circola** («il governo alza l'età della pensione», verificata anche da Pagella Politica) e si giudica coi fatti. È il formato *Vero o falso?*, con il timbro in chiusura.
2. Il verdetto «vero a metà» spiega il meccanismo senza schierarsi (regola automatica dal 2010; il governo ha rinviato 2 mesi su 3). Spiega anche **perché un mese e non tre**, cosa che il post precedente non diceva a voce.
3. Le due tesi hanno ora un nome e una data (Banca d'Italia, audizione del 6/11/2025; Cgil, Lara Ghiglione, 23/01/2026), lo stesso peso e la stessa forma. Le immagini passano da 5 a 8, con un oggetto diverso per idea.

## Contenuto della cartella

| Elemento | File | Stato |
|---|---|---|
| Ricerca e fonti | [`ricerca.md`](ricerca.md) | fatto · 12 righe, **tutte lette in sintesi** (nessun sito raggiungibile), 3 non usate |
| Copione | [`copione.md`](copione.md) | fatto · testo voce **da approvare**, production doc con tempi parola per parola |
| Scene voce | [`script/scene_elevenlabs.json`](script/scene_elevenlabs.json) | fatto (8 scene) |
| Testo da incollare | [`script/elevenlabs.txt`](script/elevenlabs.txt) | fatto (v3 tag inglesi, tag italiani, v2 per scena) |
| Immagini | [`immagini/`](immagini/README.md) | 8/8 · 16 generazioni, difetti minori di fascia bassa/destra |
| Copertina | `copertina.png` (da [`script/copertina.py`](script/copertina.py)) | fatta, 1080x1920, uguale al fotogramma 0 |
| Didascalia | [`didascalia.md`](didascalia.md) | fatta · completa, breve, commento fissato, risposte pronte |
| Voce | `voce.mp3` | **manca**: la registra l'utente su ElevenLabs con la versione 1 di `elevenlabs.txt` |
| Video | `video.mp4` | **manca**: montaggio dopo la voce (catena `monta.sh` della skill, come nel post precedente) |

## Testo da incollare in ElevenLabs (eleven_v3)

```
[surprised] Vero o falso? Il governo alza l'età pensionabile…
[curious] Ma perché?
[matter-of-fact] Dal duemilaventisette, sessantasette anni e un mese. Per quasi tutti.
[calm] È una regola: se a sessantacinque anni si vive in media di più, si va più tardi.
[calm] Stavolta toccavano tre mesi: la manovra ne ha rinviati due.
[thoughtful] Banca d'Italia: va tenuta, contiene la spesa. Cgil: va fermata, pesa su chi lavora.
[warm] Vero che sale: lo fa la regola, non il governo.
[curious] E tu, la terresti?
```

## Prima di pubblicare

1. Verificare sulle fonti originali (elenco completo in `ricerca.md`, "Da verificare"): circolare INPS 28/2026 (67a1m/67a3m ed esclusioni parola per parola), L. 199/2025 c. 180-190, decreto 19/12/2025, audizione Banca d'Italia (data e relatore), nota Cgil di Ghiglione (citazione), articoli di Pagella Politica.
2. Il giorno dell'uscita: ddl di bilancio 2027 (CdM 28/10/2026, in discussione). Controllare che non congeli lo scatto 2027 né cambi le esclusioni.
3. Approvare il testo, registrare la voce, **ascoltarla**: «Vero» iniziale pieno, «Per quasi tutti» non esclamato, «Cgil» detta come sigla, le due domande che salgono.
4. Montaggio: titoli che si sostituiscono (max 2 righe), invito «ECCEZIONI? LEGGI LA DIDASCALIA ↓» ≥ 64 px, timbro «VERO A METÀ» sull'08, sottotitoli su targhetta dove l'orso scende in fascia bassa (02, 07, 08), loop sul fotogramma 0.
5. Copertina `copertina.png`; didascalia e commento fissato da `didascalia.md`; etichetta **"contenuto generato da IA"**; musica solo dalla libreria commerciale di TikTok a ~-20 dB.

## Cosa manca

- Voce (`voce.mp3`) e video (`video.mp4`): non generati in questa sessione, su richiesta.
- Verifica delle fonti sull'originale (siti bloccati dalla rete della sessione: vanno abilitati inps.it, normattiva.it, gazzettaufficiale.it, bancaditalia.it, ansa.it, collettiva.it, pagellapolitica.it).
- Una revisione con `/rivedi-post-tiktok` prima della produzione, se si vuole lo stesso controllo a 4 valutatori del post precedente.
