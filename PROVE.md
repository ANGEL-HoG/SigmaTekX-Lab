# Prova, non promesse

Ogni riga di questa tabella è stata prodotta da un comando eseguito, non da una stima.

| Dichiarazione | Come si verifica | Cosa rivela |
|---|---|---|
| Memoria con integrità verificata | `peimem stato` → `integrità: OK` | niente |
| Embedder semantico reale su ARM64 | stesso comando → `semantico (all-MiniLM-L6-v2)` | niente |
| Ancoraggio pubblico esistente | link Rekor → `HTTP 200` | solo un hash |
| 465 test in 89 suite | conteggio nel repo privato, a schermo | niente |
| 196 task chiusi su 235 | runner di stato, a schermo | niente |
| Linguaggio con pipeline completa | esecuzione della suite: `TUTTI I CONTROLLI CORRETTI` | niente |
| 9 crate Rust | `Cargo.toml`, a schermo | niente |

## Perché l'ancoraggio pubblico conta

Un hash senza data non prova nulla: chiunque può produrlo oggi e dire che è di
ieri. La voce su Rekor ha una data controfirmata da un log pubblico che nessuno
può riscrivere. È la differenza tra "fidati" e "verifica".

Contiene: hash SHA-512 dell'artefatto, firma Ed25519, indice e data.
**Non contiene**: codice, nomi di file, struttura del progetto.

## Quello che non dichiaro

Non ho numeri di benchmark contro Mem0 o Zep: non li ho ancora misurati sullo
stesso protocollo. Finché non li misuro, non li cito. Un numero inventato
sopravvive un colloquio e muore il giorno dopo.
