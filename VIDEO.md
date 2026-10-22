# Video — 60 secondi

Formato: verticale 1080×1920, 30 fps, muto (o voce registrata sopra).
Regola unica: **si vedono solo output, mai sorgente leggibile.**

## Storyboard

| Tempo | Scena | Cosa si vede | Cosa NON si vede |
|---|---|---|---|
| 0-5s | Titolo | SigmaTek X — "Sistemi AI costruiti su un telefono" | — |
| 5-15s | P.E.I. | `peimem stato` → embedder semantico, integrità OK | percorsi interni completi |
| 15-24s | Prova pubblica | link Rekor troncato, HTTP 200, "solo un hash" | il contenuto dell'artefatto |
| 24-36s | Codice oscurato | estratto reale, **3 righe leggibili**, resto sfocato | logica completa |
| 36-46s | Numeri | 465 test · 89 suite · 196/235 · 9 crate | nomi dei file |
| 46-54s | NexQX | "TUTTI I CONTROLLI CORRETTI" | sorgente del linguaggio |
| 54-60s | Chiusura | "Demo su richiesta. Nessun sorgente inviato." | — |

## Regole di ripresa (se lo giri tu)

1. **Mai l'editor aperto.** Solo terminale con l'output già prodotto, o app in uso.
2. **Mai il file tree**, mai `ls -R`, mai percorsi assoluti con nomi di progetto.
3. **Mai schede del browser interne** con documenti di progetto.
4. **Mai notifiche**: modalità aereo o non disturbare, o comparirà un messaggio
   privato in un video destinato a un'azienda.
5. Se devi mostrare codice: **blur vero** sulle righe da nascondere, non un
   rettangolo nero (sembra un errore di montaggio e attira l'occhio).
6. Il video si chiude con una frase secca. Niente giri di parole finali.

## Versione generata

`video/presentazione.mp4` è prodotta da un renderer che legge gli output reali
in `anteprime/` e applica la sfocatura in fase di fotogramma. Zero footage di
schermo: nessun rischio di far entrare codice o notifiche.
