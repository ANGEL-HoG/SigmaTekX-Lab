# Estratti

Due file, non di più. Servono a rispondere a una domanda sola: *come scrive,
questa persona?*

| File | Cosa mostra | Perché proprio questo |
|---|---|---|
| `merkle.rs` | albero di Merkle con dominio separato, length-prefix, `None` sul vuoto | è il punto in cui la correttezza si vede: i dettagli sbagliati qui producono prove false |
| `maxsim.rs` | rerank late-interaction su top-K | è il punto in cui il progetto sceglie di superare lo standard (mean pooling) invece di copiarlo |

Sono **estratti ridotti**, non moduli completi: manca tutto il contorno
(persistenza, gestione errori, test, integrazione). Il sorgente completo resta
privato — la demo dal vivo è il modo corretto per valutarlo.
