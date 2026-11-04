# But Why Finance

But Why Finance è un progetto di divulgazione finanziaria con un profilo TikTok e un profilo Instagram (reel e caroselli).

## Mascotte

La mascotte è un orso bruno cartoon con occhiali da sole tondi neri e t-shirt verde con il simbolo € giallo.
Immagini di riferimento e scheda del personaggio in `brand/mascotte/` (vedi `brand/mascotte/README.md`).
Usala sempre quando si creano contenuti, grafiche o prompt per immagini del brand.

## TikTok

Stile e regole per i video e i caroselli TikTok in `brand/tiktok/stile-tiktok.md` (non riusare i reel di Instagram).

## Workflow video TikTok (obbligatorio)

Ogni volta che l'utente dà una notizia per TikTok (link, titolo, testo o screenshot), usa **sempre** la skill `video-tiktok` (`.claude/skills/video-tiktok/SKILL.md`):

1. **Contesto**: subagente `tiktok-ricercatore` (Opus) → `fatti.md` → **stop**: l'utente approva l'angolo; se un dato non è verificabile, chiedere.
2. **Testo per ElevenLabs**: subagente `tiktok-copywriter` (Haiku, ragionamento alto) → `voce-elevenlabs.txt` (Eleven v3, voce Valerio, 80-95 parole, 30-40 s) → **stop**: l'utente genera l'audio e lo carica.
3. **Allineamento** dell'audio con `brand/tiktok/pipeline/allinea.py`.
4. **Immagini**: subagente `tiktok-illustratore` (Opus, ragionamento medio).
5. **Montaggio** (`monta.py`), **copertina** (`copertina.py`), **didascalia** con hashtag.
6. **Commit e push** dell'episodio in `brand/tiktok/output/AAAA-MM-slug/`.

Musica: nessuna nel file, si aggiunge su TikTok. Script e formati in `brand/tiktok/pipeline/README.md`.
