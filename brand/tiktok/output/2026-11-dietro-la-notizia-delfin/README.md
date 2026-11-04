# Dietro la notizia: Delfin, video TikTok (prima versione)

Realizza il copione [`../../copioni/2026-11-dietro-la-notizia-delfin.md`](../../copioni/2026-11-dietro-la-notizia-delfin.md) con la stessa pipeline del video sul caffè (vedi [`../2026-10-il-prezzo-del-caffe/README.md`](../2026-10-il-prezzo-del-caffe/README.md) per i dettagli tecnici delle API).

## Da fare prima di pubblicare

1. **Verificare le cifre sulle fonti originali** (elenco nel copione). Le ho prese dagli estratti delle ricerche, non dagli articoli completi.
2. **Attivare l'etichetta "contenuto generato da IA"** su TikTok: immagini IA e voce sintetica.
3. **La voce è provvisoria** (Kokoro `im_nicola`). ElevenLabs ha ancora **4 crediti** (ne servono circa 900) e le voci italiane della libreria richiedono il piano a pagamento. Il README del caffè spiega come rifarla con ElevenLabs.
4. **La notizia si muove in fretta:** l'incontro proposto ai soci è entro il 7 novembre 2026. Se cambia qualcosa prima della pubblicazione, aggiornare le inquadrature 11-13.
5. Aggiungere la musica dalla Commercial Music Library di TikTok, circa 20 dB sotto la voce. Nel video non ce n'è.

## File

| File | Contenuto |
|---|---|
| `video.mp4` | 1080x1920, 30 fps, H.264 + AAC 48 kHz, **52,8 s**, 9,2 MB, -14,4 LUFS (picco -1,4 dBFS) |
| `voce.mp3` | Solo la voce, normalizzata a -14 LUFS |
| `immagini/01.png` … `14.png` | Le 14 illustrazioni senza testo (1152x2016) |
| `tempi.json` | Inizio e fine di ogni inquadratura e di ogni sottotitolo |
| `script/` | `make_prompts.py` (prompt) → `gen.py` (API Meta `muse-image-1.0`) → `kok_all.py` (voce) → `audio.py` (colpo sonoro) → `montage.py` + `config_video.py` (montaggio) → `norm.sh` (loudness) |

## Scelte fatte (da confermare)

- **Accento verde** della rubrica: `#006B3C` nei titoli su carta. Su fondo inchiostro e nei sottotitoli (bianchi con contorno scuro) uso il verde chiaro `#6FCF97` dell'adesivo "Ma perché?", perché lì il verde scuro non si legge. `montage.py` è quello del caffè, con l'ambra sostituita da questi due verdi.
- **Persone reali come sagome grigie** senza volto (Leonardo Maria, Strnad, i soci). Nessun ritratto né somiglianza.
- **"Mps" letto "emme pi esse"** e "EssilorLuxottica" scritto "Essilor Luxottica" per la pronuncia. "Ceco" è diventato "della Repubblica Ceca", perché la trascrizione di prova lo capiva come "cieco".

## Immagini

Generate 18 in tutto: 14 alla prima prova, più 4 rifatte.
- 04 e 07: era comparso un orsetto di peluche fuori modello che non era stato richiesto. Rifatte aggiungendo "no animals, no teddy bears, no characters".
- 02: le otto sagome non si contavano. Rifatta con due file da quattro ben separate.
- 03: il fondo era color pesca invece che carta. Rifatta.

Ho controllato tutte le immagini: nessuna scritta, nessun rosso, sagome senza volto, orso coerente (occhiali tondi con riflesso, maglietta verde con € giallo).

## Limiti noti

- **Durata 52,8 s**, oltre i 30-45 s della guida. Per accorciarlo si possono togliere le inquadrature 6 (Mps e Generali) e 9 (prestito Citi): si scende a circa 45 s.
- Voce **non ascoltata da un orecchio umano**. Il testo l'ho controllato con la trascrizione automatica (`muse-spark-1.3`): corrisponde al copione.
- Le inquadrature 4 e 8 durano più di 4 s (frasi lunghe). Si possono dividere in due immagini ciascuna.
- Dentro una stessa frase, i tempi dei sottotitoli sono stimati (errore fino a circa 0,2 s).
