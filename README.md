# SigmaTek X — laboratorio AI su un telefono

Costruisco sistemi AI **nativi su Android/Termux**, senza emulazione e senza cloud.
Tre progetti reali, un metodo solo: *niente è "fatto" finché un comando non lo dimostra*.

Nessun finanziamento, nessun team, un dispositivo. Il collo di bottiglia non è l'idea:
è la verifica — e quella è la parte che ho costruito.

---

## Cosa c'è dentro

### 1. P.E.I. — memoria persistente per agenti AI (Rust)
Memoria che non si inventa ricordi: ogni riga ha un'impronta SHA-256, ogni richiamo
è tracciato, ogni modifica lascia una prova. Include ancoraggio su un transparency
log pubblico (Sigstore/Rekor): chiunque può verificare che un artefatto esistesse a
una certa data **senza vedere il contenuto**.

- ricerca ibrida (full-text + vettoriale) fusa, con rerank *late-interaction* (MaxSim)
- bi-temporalità: "cosa sapevo il 12 marzo" è una domanda legittima
- manomissione diretta del database: rilevata dall'audit
- embedder semantico reale (all-MiniLM-L6-v2) in esecuzione su ARM64 Android

### 2. NexQX — linguaggio di programmazione con frontend completo
Lexer, parser, type system, IR e MIR propri, con backend nativo. La suite copre
precedenza degli operatori, tipi ricorsivi, sicurezza dei puntatori, array a runtime
e la pipeline completa da sorgente a esecuzione. Il self-hosting è la fase in corso.

### 3. IQ Vibe Code — piattaforma di sviluppo con agenti AI (Rust)
Piattaforma che orchestra agenti, con una regola non negoziabile: **un task non è
"fatto" perché l'agente lo dice**, ma perché il criterio di accettazione è stato
eseguito e superato. Il motore di stato registra ogni transizione, con prova.

---

## Numeri

| Cosa | Valore | Come si verifica |
|---|---|---|
| Test automatici (piattaforma Forge) | **465 test in 89 suite** | conteggio nel repo privato, mostrabile a schermo |
| Task chiusi con verifica eseguita (IQ Vibe Code) | **196 su 235** | runner di stato, mostrabile in demo |
| Crate Rust nel workspace | **9** | `Cargo.toml` in demo |
| Ancoraggio pubblico | **Rekor, 16/10/2026** | link verificabile qui sotto |

Tutti i numeri sono ricavati da esecuzioni reali, non da stime.

## Prova pubblica, senza codice

```
https://rekor.sigstore.dev/api/v1/log/entries/108e9186e8c5677a3cc6f009457e946a450d22672d3d36ecded5b4dead3327ba12460f52e9aaac6a
```

Risponde `HTTP 200`. Contiene un hash SHA-512, una firma Ed25519 e la data.
Non contiene una riga di codice: è una prova di esistenza e integrità, non una fuga
di proprietà intellettuale.

## Cosa NON pubblico

Il codice sorgente dei tre progetti resta privato. In questo repository ci sono solo:

- due estratti scelti (Merkle proof, MaxSim) per far vedere *come* scrivo;
- output reali catturati dall'esecuzione;
- la descrizione delle capacità, non dell'implementazione.

Se serve una verifica più profonda: demo dal vivo, condivisione schermo, o revisione
sotto NDA. Mai file sorgente inviati.

## Video

[`video-presentazione.mp4`](video-presentazione.mp4) — 60 secondi, generato dagli
output reali: nessuna ripresa dello schermo, nessun sorgente leggibile, codice
parzialmente sfocato nel fotogramma.

## Contatti

- GitHub: [@ANGEL-HoG](https://github.com/ANGEL-HoG)
- Demo dal vivo: su richiesta, con condivisione schermo

---

*Repository di presentazione. Il contenuto è proprietario: vedi [LICENSE](LICENSE).*
