# Metriche reali dei nostri video

Un file `.json` per video (nome: `AAAA-MM-tema-versione.json`), con le metriche di TikTok Studio. Servono a confrontare il punteggio della guida (`../guida-retention.md`) con i risultati reali.

## Cosa raccogliere (4 schermate per ogni post, dai "dettagli del post")
| Schermata | Cosa riporta |
|---|---|
| Panoramica (1) | Visualizzazioni, tempo di riproduzione totale, **tempo medio di visualizzazione**, **% che guarda il video completo**, nuovi follower, visualizzazioni per ora |
| Panoramica (2) | **Tasso di mantenimento** (curva di retention; leggere con il cursore i valori a 0:01, 0:02, 0:03, 0:05, 0:10, 0:20, fine) e **fonti di traffico** |
| Spettatori | Sesso, età, posizioni, tipi di spettatori |
| Coinvolgimento | Momento dei "mi piace" e parole nei commenti |

## Quando
Rilevare a **2 h**, **24 h** e **7 giorni** dalla pubblicazione (le prime ore sono un campione piccolo). Un file per rilevazione nello stesso JSON, o un nuovo file con suffisso `-24h`.

## Come
Con un clic, usando l'estensione `tools/estensione-tiktok-studio` (vedi il suo README): il file esportato va in `grezzi/` e viene trasformato nel JSON delle metriche e nel registro della guida. In alternativa: allegare gli screenshot alla conversazione.
