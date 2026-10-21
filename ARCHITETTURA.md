# Architettura, a parole

Nessun diagramma con nomi di file, nessuno schema di database. Solo le decisioni
che spiegano il resto.

## Il principio: la verifica non è una formalità

In un sistema con agenti AI il rischio non è che il codice sia sbagliato: è che
sia *dichiarato* giusto. Un agente che dice "fatto" senza prova è indistinguibile
da uno che ha fatto. Per questo ogni passaggio ha un criterio eseguibile, e lo
stato "fatto" esiste solo dopo che quel criterio è passato.

Conseguenza pratica: il sistema può dire "non lo so" e "non verificato". È una
funzionalità, non un'ammissione di debolezza.

## Tre strati

**Memoria (P.E.I.).** Ciò che l'agente sa, con la sua storia. Ogni riga è
identificata da un'impronta; ogni modifica è un evento; il richiamo è ibrido
(testo + vettori) e rifinito da un rerank che lavora sui token, non solo sul
vettore medio. La bi-temporalità permette di chiedere non solo *cosa so*, ma
*cosa sapevo allora*.

**Linguaggio (NexQX).** Dal testo al'esecuzione passando per analisi: lessico,
sintassi, tipi, rappresentazione intermedia. Ogni strato ha la sua suite, e la
pipeline completa è testata da sorgente a risultato — non solo i pezzi in
isolamento.

**Piattaforma (IQ Vibe Code).** Orchestrazione di agenti con un motore di stato
che registra transizioni, dipendenze e criteri. Un task non può essere chiuso
senza che il suo criterio sia stato eseguito: il motore non accetta
autocertificazioni.

## Perché su un telefono

Non è una scelta romantica: è un vincolo che elimina le scorciatoie. Niente
cluster, niente "scala dopo". Se una scelta è troppo costosa in memoria o in
tempo, va rifatta. Il risultato è un sistema che gira dove nessuno si aspetta
che giri.

## Cosa non c'è, e lo dico

- Nessun benchmark comparativo contro Mem0/Zep: non ancora misurato sullo stesso
  protocollo.
- Il self-hosting del linguaggio è in corso, non concluso.
- L'ancoraggio pubblico è reale per l'artefatto registrato; il ciclo automatico
  di ri-ancoraggio non è completo.

Un'architettura presentata senza i suoi buchi non è un'architettura: è marketing.
