# Regole di brand per i post TikTok

Sintesi operativa di `brand/tiktok/stile-tiktok.md`, `brand/tiktok/analisi-riferimenti.md` e `brand/mascotte/README.md`. Se questi file cambiano, valgono loro: rileggili a ogni post.

## Formato

- **Video narrato con l'orso** (formato principale): illustrazioni 9:16 + voce narrante + sottotitoli + titoli aggiunti in montaggio. Questa skill punta a **20-30 s** (il brief generale dice 20-40 s, ma i due post fatti hanno mostrato che i testi lunghi esplodono: il caffè è arrivato a 60 s).
- Carosello TikTok (photo mode, 6-8 slide) è il formato secondario: non è coperto da questa skill.
- Mai riusare i reel di Instagram: ogni pezzo nasce per TikTok.
- Modello di ritmo: Video 2 di @cashfoxclub0. **Una idea = una immagine = un oggetto concreto**, un'immagine nuova ogni 2-3 s (8 immagini per 25 s), voce calma: il passo lo dà il montaggio, non la fretta del parlato.

## Rubriche e colore d'accento

Un solo accento per post, quello della rubrica. Si usa su oggetti-chiave delle immagini (monete, forbici, frecce), sulla parola evidenziata dei sottotitoli e sui numeri dei titoli.

| Rubrica | Quando sceglierla | Accento | `accento` in `componi_prompt.py` |
|---|---|---|---|
| **Il prezzo di…** | il costo di una cosa quotidiana (caffè, spesa, bollette, abitudini) e cosa c'è dentro | ambra `#E9A400` | `ambra` |
| **Chi paga?** | una misura, un rincaro o una tassa: chi ci perde e chi ci guadagna | arancio `#B8420F` | `arancio` |
| **Vero o falso?** | una frase che circola (luogo comune, slogan politico) da verificare coi dati; timbro VERO/FALSO in montaggio | viola `#5B3FA8` / giallo `#FFD60A` | `viola` (o `giallo`: scegline **uno** per le immagini; nel dubbio chiedi) |
| **Il numero** | un solo dato sorprendente che regge tutto il pezzo | blu `#1F4FA3` | `blu` |
| **In 60 secondi** | spiegare un meccanismo (spread, inflazione, mutuo variabile) in modo compatto; barra che scorre | fucsia `#B0186E` | `fucsia` |
| **Dietro la notizia** | una notizia di attualità e il perché economico che c'è sotto; ritaglio di giornale in montaggio | verde `#006B3C` | `verde` |

Attenzione per i colori (consigli pratici, non regole del brief):
- `arancio` è vicino alla pelliccia dell'orso (`#C2622A`) e tende al rosso: tienilo su oggetti staccati dall'orso e lontani dalla maglietta verde.
- `verde` è anche il colore del marchio e della maglietta: usalo su pochi oggetti, mai accanto a qualcosa di rosso o arancio.
- `blu`/`fucsia`: lo script toglie da solo "no blue"/"no pink" dal prompt quando sono l'accento.

## Colori base

| Nome | Esadecimale | Uso |
|---|---|---|
| Inchiostro | `#111418` | fondo di **hook (prima immagine) e chiusura (ultima)**, e nient'altro |
| Carta | `#F4F1EA` | fondo di **tutte le altre immagini** |
| Verde marchio | `#006B3C` | logo, fumetto "But Why Finance?" (in montaggio), "Sai che…?" |

Font (solo in montaggio): IBM Plex Sans Condensed (titoli, sottotitoli), IBM Plex Mono (numeri, scontrini).

## Regole vincolanti per le immagini

1. Fondo inchiostro solo per hook e chiusura; carta per le altre. Fondo uniforme, quasi vuoto.
2. Un solo accento (quello della rubrica). **Mai rosso accanto a verde** (richiama vero/falso): niente rosso in nessuna immagine.
3. **Nessuna scritta, lettera o numero** nelle immagini: titoli, cifre, etichette e fumetto si aggiungono in montaggio. Fogli e scontrini sono bianchi o con righe grigie astratte.
4. **Zone sicure TikTok libere**: ~10% in alto (titolo), ~15% in basso (sottotitoli e didascalia dell'app), fascia destra (pulsanti). Nei prompt si chiede il 12% in alto e il 18% in basso, più margine.
5. **€ della maglietta sempre visibile**, al centro del petto, mai coperto da oggetti o braccia, mai sulla manica.
6. Le altre persone (lo Stato, la banca, il cliente, il barista) sono **sagome grigie senza volto**, senza vestiti colorati né loghi.
7. Orso coerente con `brand/mascotte/mascotte-principale.jpg` in tutte le immagini; resta in un angolo o a lato quando la scena è un oggetto, non riempie sempre lo schermo.
8. Stile: illustrazione piatta 2D, contorno nero spesso, colori pieni, niente sfumature, un oggetto forte per immagine, tanto spazio vuoto.
9. Se le immagini (o la voce) sono generate con IA, su TikTok va attivata l'etichetta **"contenuto generato da IA"**.

## La mascotte

- Orso bruno cartoon, pelliccia ramata `#C2622A`, muso pesca `#F6C78E`, naso nero a goccia con linea verso la bocca, **occhiali da sole tondi neri con riflesso bianco diagonale** (gli occhi non si vedono mai, salvo l'occhiolino visibile nella lente), **t-shirt verde scuro `#0F5E3F` con € giallo `#F6C21C`** al centro del petto, retro senza grafica, contorno nero spesso.
- Riferimento da allegare **sempre**: `brand/mascotte/mascotte-principale.jpg` (`image[0]`). Per espressioni particolari (soprattutto l'occhiolino) anche `brand/mascotte/espressioni.jpg` (`image[1]`). `brand/mascotte/turnaround.jpg` per profilo, tre quarti o retro.
- Il nome dell'orso **non è ancora deciso**: non inventarlo.
- Ruolo: l'orso domanda, reagisce, guarda; **la risposta la dà la voce narrante**. Presente in apertura e chiusura, più reazioni nel mezzo.

Espressioni (dal set `espressioni.jpg`) e formula inglese collaudata nei prompt:

| Espressione | Uso tipico | Formula nel prompt |
|---|---|---|
| Sorpreso | hook, un prezzo che non torna | `SURPRISED: mouth open in a small round 'o' shape, eyebrows raised above the sunglasses, both paws open and raised slightly in astonishment` |
| Pensieroso | dilemma, due tesi | `THOUGHTFUL: one paw on his chin, mouth twisted to one side, one eyebrow raised` |
| Preoccupato | un costo che pesa | `WORRIED: a light-blue sweat drop on his temple, eyebrows tilted, mouth turned down` |
| Ho un'idea / spiega | spiegazione, consigli | `explaining: one index finger raised up ('I have an idea' pose), open smiling mouth` |
| Felice | consiglio pratico, soluzione | `pleased smile` / `satisfied smile` |
| Occhiolino | chiusura, domanda finale | `WINKING like the winking face in the second reference image` + la frase sulla **lente fumé**: la lente dell'occhio che strizza è scura ma semitrasparente e lascia vedere l'occhio chiuso (linea curva), l'altra resta nera piena con il riflesso bianco; entrambe le lenti presenti. `componi_prompt.py` aggiunge da solo la frase, `espressioni.jpg` come `image[1]` e toglie "eyes never visible" dalla scheda dell'orso |

## Voce e tono

- **Commercialista esperto che spiega al bar**: calmo, diretto, caldo; mai allarmista, mai infantile, niente ritmo da meme.
- Neutro: presenta i fatti e le tesi attribuite a chi le sostiene, non si schiera. Il tema resta **aperto alla discussione**.
- **Nessun consiglio di investimento, nessun prodotto finanziario**, nessuna marca o servizio citato come consiglio. Consigli di buon senso sulla spesa quotidiana sono ammessi, presentati come abitudini e non come regole sostenute da dati che non abbiamo.
- Velocità 140-150 parole/min, frasi corte, un concetto per frase.
- Chiusura sempre con una **domanda aperta** (non retorica), ripetuta nella didascalia.

## Sottotitoli e titoli (in montaggio)

- Sempre presenti, grandi, 3-5 parole alla volta, al massimo 2 righe, sincronizzati con la voce; la frase prosegue da un'immagine alla successiva.
- IBM Plex Sans Condensed Bold, testo carta su inchiostro semi-opaco (o bianco con contorno inchiostro), una parola chiave per riga nel colore d'accento.
- Testo fuori dalle zone sicure: niente nel 10% in alto, nel 15% in basso, nella colonna destra.
- Transizioni: taglio netto o dissolvenza breve (0,2 s), sempre la stessa; niente zoom aggressivi né glitch (va bene uno zoom lento 100%→104%).
- Musica: base strumentale leggera a circa -20 dB sotto la voce, **solo con licenza commerciale** (libreria commerciale di TikTok); pochi effetti (timbro, carta, scontrino).

## Hashtag

3-5, **parola chiave + nicchia**, non solo generici (es. `#risparmio #finanzapersonale #bollette #imparacontiktok`). Nei due post TikTok fatti finora non c'è `#butwhyfinance` (che la skill Instagram mette sempre): chiedi all'utente se vuole aggiungerlo, non deciderlo in silenzio.
