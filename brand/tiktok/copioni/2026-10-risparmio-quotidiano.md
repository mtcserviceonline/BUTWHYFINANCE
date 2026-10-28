# Copione TikTok: "Il prezzo di… un caffè al giorno" (risparmio quotidiano) — v2b

**Rubrica:** Il prezzo di… (accento ambra `#E9A400`, numeri e scontrino in IBM Plex Mono). Il video parte dal prezzo di un'abitudine, lo dimostra con la fonte e chiude con tre consigli pratici e una domanda.
**Formato:** illustrato con l'orso + voce narrante; hook e chiusura su inchiostro `#111418`, spiegazioni e consigli su carta `#F4F1EA`
**Durata:** piano A1 ~27 s; v2b registrata 35,7 s, montata **34,1 s** (95 parole, 170 parole/min dopo aver accorciato le pause), 9 immagini, 23 inquadrature
**Obiettivo:** commenti (domanda finale "qual è quella che non guardi mai?") e salvataggi (tre consigli)
**Suono:** voce + effetti leggeri solo sui numeri; base musicale a -20 dB **solo con licenza commerciale** (in app dalla Libreria musicale commerciale, oppure file dell'utente con `MUSICA=`)
**Etichetta IA:** attivare "contenuto generato da IA" (immagini generate, voce sintetica). Il testo si aggiunge sempre in montaggio, mai dentro le immagini.
**Scene per la voce:** [`../output/2026-10-risparmio-quotidiano/script/scene_elevenlabs.json`](../output/2026-10-risparmio-quotidiano/script/scene_elevenlabs.json) (7 scene: tono, tag v3/italiani, stability/style, secondi del piano, immagini) e [`elevenlabs.txt`](../output/2026-10-risparmio-quotidiano/script/elevenlabs.txt)
**Video:** [`../output/2026-10-risparmio-quotidiano/`](../output/2026-10-risparmio-quotidiano/README.md) (v2b `video.mp4`; v2a `video_v2a.mp4` con l'apertura "Se ti bevi…"; v1 da 24 s `video_v1_24s.mp4` per l'A/B test)

## Testo della voce (v2b, 28/10/2026, registrato)

Numeri per esteso (A5), pause solo a fine frase (A3), 0,3-0,4 s prima di "Ma perché?" con la voce che sale ed enfasi su "non te ne accorgi" (A2).

```
[surprised] Quattrocentosettanta euro all'anno. È più o meno quanto spendi con un caffè al bar ogni giorno… e NON TE NE ACCORGI. … [curious] Ma perché?
[matter-of-fact] Per Assoutenti un espresso costa in media uno e ventinove. Moltiplicato per trecentosessantacinque giorni: quattrocentosettantuno euro.
[curious] Sono piccole spese. E le piccole spese non le guardiamo mai.
[calm] Primo: controlla gli abbonamenti che non usi.
[calm] Secondo: fai la lista prima di andare al supermercato.
[thoughtful] Terzo: confronta le offerte di luce e gas una volta all'anno.
[warm] Non serve cambiare vita. Basta guardare le piccole spese. [curious] E tu: qual è quella che non guardi mai?
```

Apertura v2b registrata a parte (`voce_hook_v2b.mp3`) e unita al resto della v2a da "Per Assoutenti…". Apertura v2a: "Se ti bevi un caffè al bar ogni giorno, spendi circa quattrocentosettanta euro all'anno e non te ne accorgi. Ma perché?". La v2b dice "più o meno" invece di "circa": la didascalia ("circa 470 euro") resta coerente nel senso.

Nota sulla durata: 93-95 parole a 165-175 parole/min (A3) durano 32-34 s; ~27 s vorrebbe dire ~205 parole/min. La registrazione (158 parole/min) è stata portata a 168 parole/min solo accorciando le pause (nessuna accelerazione). Per stare vicino a 27 s bisogna togliere ~15 parole (per esempio "Moltiplicato per trecentosessantacinque giorni:" → "Per un anno:" e "Non serve cambiare vita." in meno).

Testo v1 (registrato il 28/10 mattina, video da 24 s): "Un caffè al bar ogni giorno costa circa quattrocentosettanta euro all'anno. Ma perché non ce ne accorgiamo? Perché sono piccole spese, e le piccole spese non le guardiamo mai. Primo… Secondo… Terzo… Non serve cambiare vita, basta iniziare a guardare le piccole spese."

## Fatti da verificare prima di pubblicare

| Dato o affermazione | Fonte | Stato |
|---|---|---|
| Un espresso al bar costa in media **1,29 €** | Studio del **Centro di formazione e ricerca sui consumi (CRC) con Assoutenti**, 18 agosto 2026, su dati MIMIT. Riportato da [Teleborsa, 18/08/2026](https://www.teleborsa.it/News/2026/08/18/prezzi_caffe_al_bar_%2b_24_2percento_in_cinque_anni-115.html) e da ANSA ([il NordEst](https://www.ilnordest.it/italia-ed-esteri/e-caro-tazzina-espresso-in-media-a-1-29-euro-24-5-sul-2025-e7o8qk6d)) | **concordante su più testate; comunicato originale da aprire a cura dell'utente** (assoutenti.it non raggiungibile da questa sessione: 403 del proxy). La percentuale d'aumento **non si usa**: +24,2% sul 2021 per Teleborsa, "+24,5% sul 2025" nel titolo dell'altra testata (incoerente) |
| 1,29 € × 365 = **470,85 €** → "circa 470" / "471" | calcolo nostro | regge. Ipotesi: un caffè tutti i giorni dell'anno, weekend e ferie compresi. Con i prezzi città per città (1,20-1,40 €, [Altroconsumo](https://www.altroconsumo.it/alimentazione/fare-la-spesa/news/aumento-costo-caffe), giugno 2026) si va da ~438 a ~511 €; solo nei giorni lavorativi (~250) ~323 € |
| "Le piccole spese non le guardiamo mai" | nessuna | constatazione, non un dato; nessuno studio citato (niente "latte factor") |
| Consiglio 1: abbonamenti che non usi | nessuna | **senza cifra (T-5):** nessun dato verificato su quanto si spende in abbonamenti inutilizzati |
| Consiglio 2: lista della spesa | nessuna | **senza cifra (T-5):** nessun dato verificato sul risparmio con la lista |
| Consiglio 3: confrontare luce e gas una volta all'anno | strumento pubblico: [Portale Offerte ARERA](https://www.ilportaleofferte.it) | **senza cifra (T-5);** la frequenza "una volta all'anno" è un'abitudine consigliata, non una regola con fonte |
| Frase di colpo di scena prima dei consigli (M-6) | — | **non aggiunta:** era richiesta solo con una fonte, e non ne ho una verificata |

Da fare: aprire il comunicato originale Assoutenti/CRC e confermare 1,29 €. Se il valore è diverso, rifare il conto, il testo, la voce e rilanciare `monta.sh`.

## Production doc (v2, tempi del video montato)

| # | Tempo | Immagine / inquadratura | Testo a schermo | Voce (tono) | Suono |
|---|---|---|---|---|---|
| 1 | 0:00-0:06,9 | **Hook**, inchiostro. 01 orso intero sorpreso (70%) con **punch-in rapido a 112% in 0,7 s** verso scontrino e tazzina → 90% su "È" → 100% su "caffè" → volto 115% su "e non te ne accorgi" | in alto **"470 €"** (ambra, Mono, gigante) **dal fotogramma 0**, **"ALL'ANNO"** su "all'anno"; spariscono su "e non te ne accorgi"; in basso solo la riga parlata | *(il numero subito, poi sorpreso)* "Quattrocentosettanta euro all'anno. È più o meno quanto spendi con un caffè al bar ogni giorno… e non te ne accorgi." | colpo di scontrino a 0,0 s |
| 2 | 0:06,9-0:07,7 | 02 fila di tazzine, carta; unica transizione: tenda da inchiostro a carta (0,2 s) | nessun titolo; sottotitolo "MA **PERCHÉ?**" | *(curioso, voce che sale)* "Ma perché?" | — |
| 3 | 0:07,7-0:15,2 | **Numero e fonte.** 09 orso con scontrino lungo, quattro inquadrature alternate larga / scontrino + orso | sullo scontrino (Mono): "1,29 €" su "uno e ventinove", "× 365" su "trecentosessantacinque", "= 471 €" su "quattrocentosettantuno"; "Fonte: Assoutenti (dati MIMIT)" dall'inizio della scena | *(chiaro)* "Per Assoutenti un espresso costa in media uno e ventinove. Moltiplicato per trecentosessantacinque giorni: quattrocentosettantuno euro." | tre tick leggeri sui numeri |
| 4 | 0:15,2-0:18,6 | 03 lente sulle monetine → 04 sagoma che perde monete (92% → 108%) | **PICCOLE SPESE** | *(curioso)* "Sono piccole spese. E le piccole spese non le guardiamo mai." | — |
| 5 | 0:18,6-0:21,2 | 05 smartphone e forbici (75% → 100%) | **1 · ABBONAMENTI** sopra la testa | *(calmo)* "Primo: controlla gli abbonamenti che non usi." | pop leggero |
| 6 | 0:21,2-0:24,4 | 06 orso intero con la lista (100% → 112%) | **2 · LISTA DELLA SPESA** sopra la testa | *(calmo)* "Secondo: fai la lista prima di andare al supermercato." | pop leggero |
| 7 | 0:24,4-0:28,3 | 07 bilancia con le due offerte (95% → 112% → 100%) | **3 · LUCE E GAS** sopra la testa | *(pensieroso)* "Terzo: confronta le offerte di luce e gas una volta all'anno." | pop leggero |
| 8 | 0:28,3-0:33,6 | **Chiusura**, inchiostro. 08 volto + salvadanaio (112%) → larga con titolo → fumetto "But Why Finance?" | **BASTA GUARDARE LE / PICCOLE SPESE** (la seconda riga entra su "piccole"); poi solo il sottotitolo "E TU: QUAL È QUELLA CHE NON GUARDI **MAI?**" | *(caldo, poi curioso)* "Non serve cambiare vita. Basta guardare le piccole spese. E tu: qual è quella che non guardi mai?" | — |
| 9 | 0:33,6-0:34,1 | **Loop.** 01 con la stessa vista del fotogramma 0 (prima del punch-in) | **"?"** al posto di "470 €"; resta la domanda nel sottotitolo | — (fine 0,45 s dopo l'ultima parola) | — |

Regole di montaggio applicate (dettagli e controlli nel README del post): occhiali sempre visibili e mai coperti da testi (controllo automatico per ogni inquadratura), zoom ≤ 120% (115% sul volto), un cambio visivo ogni ≤ 2 s, tagli netti salvo la tenda a 0:06,9, sottotitoli sempre sopra il 15% in basso.

## Hook: i tre canali

- **Verbale:** "Quattrocentosettanta euro all'anno." come prima parola (voce da 0,05 s).
- **Testo:** "470 €" gigante in ambra già nel fotogramma 0, con il colpo di scontrino; "ALL'ANNO" sulla parola.
- **Visivo:** orso intero sorpreso con tazzina e scontrino, punch-in rapido (112% in 0,7 s) verso lo scontrino; poi avvicinamenti fino al volto su "non te ne accorgi".

## Loop e rewatch

- L'ultimo mezzo secondo ripete la composizione del primo fotogramma (01, stessa vista, prima del punch-in) con "?" al posto di "470 €": il video riparte senza strappo e la domanda "qual è quella che non guardi mai?" porta alla risposta del primo fotogramma.
- Rewatch: il conto sullo scontrino (1,29 × 365) e i tre consigli numerati.

## SEO TikTok

- **Parole chiave** (parlato + testo + didascalia): caffè al bar, prezzo del caffè, Assoutenti, risparmio, piccole spese, abbonamenti, lista della spesa, luce e gas.
- **Hashtag (P-4):** #caffè #prezzi #risparmio #finanzapersonale

## Didascalia (P-3, testo esatto)

> Se ti bevi un caffè al bar ogni giorno, spendi circa 470 euro all'anno. Per Assoutenti l'espresso costa in media 1,29 euro. Qual è la piccola spesa che non guardi mai? 👇
> #caffè #prezzi #risparmio #finanzapersonale

Versione breve e note in [`../output/2026-10-risparmio-quotidiano/didascalia.md`](../output/2026-10-risparmio-quotidiano/didascalia.md).

## A/B test (P-6)

1. v1 (24 s, `video_v1_24s.mp4`) contro v2b (34,1 s, `video.mp4`); eventualmente v2a (`video_v2a.mp4`, apertura "Se ti bevi…") contro v2b.
2. Finale con la domanda (v2) contro taglio netto su "Basta guardare le piccole spese." (come rimontarla: README del post).

## Controllo qualità

- Hook in 1 s su tre canali: numero detto subito, "470 €" a schermo e colpo di scontrino dal fotogramma 0, orso sorpreso con punch-in.
- Fonte nominata a voce, a schermo e in didascalia (P-5); il 1,29 € da confermare sul comunicato originale.
- Tono: neutro e calmo, nessun giudizio su chi beve il caffè al bar; "più o meno" in apertura (stima).
- Nessun consiglio d'investimento, nessun fornitore o marca citati.
- Colori: ambra unico accento ("470 €", "?", numeri dei consigli, parole chiave); verde solo su maglietta e fumetto del logo.
- Testi solo in montaggio: le immagini non hanno scritte (scontrino della 09 vuoto, il conto si stampa in montaggio).
- Domanda aperta per i commenti: nel video (sottotitolo finale) e in didascalia.
