# Affittare a 800 € rende più che a 1.000 €? — fotogrammi iniziali

Primo fotogramma di ognuna delle 6 scene del reel (canone concordato under 35, tassa all'1%).

| File | Scena | Cosa mostra |
|---|---|---|
| `fotogrammi/01.png` | 1 · Il paradosso | Orso con la chiave di carta davanti a due casette identiche, espressione curiosa |
| `fotogrammi/02.png` | 2 · La proposta | Orso con i due cartellini del prezzo, si gira verso il grande foglio attaccato al muro col nastro; sotto, tavolino con tre timbri di misura decrescente |
| `fotogrammi/03.png` | 3 · I conti del proprietario | Orso in piedi accanto alla scrivania di carta, sopra due scontrini arrotolati e la lente |
| `fotogrammi/04.png` | 4 · Chi ci guadagna | Orso seduto alla scrivania con gli scontrini srotolati; monete di carta sparse, pronte da impilare |
| `fotogrammi/05.png` | 5 · Chi paga | Orso accanto alle due pile di monete (alta e bassa), serio, si gira verso l'edificio pubblico con le colonne; portafoglio chiuso a terra |
| `fotogrammi/06.png` | 6 · La domanda | Orso davanti a un tavolino con due cartoncini bianchi, guarda in camera |

Ogni primo fotogramma riprende la fine della scena precedente, così le scene si legano.

## Come sono fatti

- API Meta `muse-image-1.0`, `POST /v1/images/edits`, riferimento `brand/mascotte/mascotte-principale.jpg`, `size=1024x1792` → 1152x2016 (9:16).
- Prompt = lo STILE del copione + descrizione dell'orso + scena + "no text". Testi completi in `script/prompts.json` (generati da `script/make_prompts.py`); `script/gen.py` genera un'immagine.
- Rigenerate una volta: 01 (le casette non erano identiche), 03 e 04 (l'orso era tagliato in basso).

## Note

- **Simbolo €:** lo STILE del copione dice "white euro sign", ma la mascotte ufficiale ha la € **gialla**. Ho seguito la mascotte. Se nel video vuoi la € bianca, va cambiato anche negli ultimi fotogrammi, sennò l'orso cambia maglietta da una scena all'altra.
- Scena 4: le monete sparse sono finite davanti alla scrivania (sul pavimento) invece che sopra. Il movimento "impila le monete" funziona lo stesso.
- Scena 1: la chiave è nella zampa all'altezza della pancia, non alzata.
- Su TikTok/Instagram va attivata l'etichetta "contenuto generato con IA".
