# SigmaTek X — estratto: Merkle + firma Ed25519

> Estratto **ridotto** da un modulo reale (Rust). Le parti di contorno non sono
> incluse. Pubblicato per mostrare il metodo, non l'implementazione.

Tre scelte che spiegano il resto del progetto:

1. **Dominio separato** tra foglia e nodo interno: senza, un nodo interno può
   coincidere con una foglia e la prova diventa ambigua.
2. **Length-prefix** nella foglia: evita le collisioni da concatenazione banale.
3. **`None` su insieme vuoto**: nessuna radice inventata. Se non c'è niente, non
   esiste una prova — mai fingere una certezza.

```rust
use sha2::{Digest, Sha256};

/// Foglia: hash con dominio separato e lunghezza esplicita.
pub fn hash_leaf(item: &[u8]) -> [u8; 32] {
    let mut h = Sha256::new();
    h.update(b"iqvibe.pei.anchor.leaf.v1");
    h.update((item.len() as u64).to_le_bytes());
    h.update(item);
    h.finalize().into()
}

/// Nodo interno: dominio diverso dalla foglia.
fn hash_node(left: &[u8; 32], right: &[u8; 32]) -> [u8; 32] {
    let mut h = Sha256::new();
    h.update(b"iqvibe.pei.anchor.node.v1");
    h.update(left);
    h.update(right);
    h.finalize().into()
}

/// Radice del batch. `None` su batch vuoto: nessuna certezza su nulla.
pub fn merkle_root(leaves: &[[u8; 32]]) -> Option<[u8; 32]> {
    if leaves.is_empty() {
        return None;
    }
    let mut level: Vec<[u8; 32]> = leaves.to_vec();
    while level.len() > 1 {
        let mut next: Vec<[u8; 32]> = Vec::with_capacity(level.len().div_ceil(2));
        let mut i = 0;
        while i < level.len() {
            let left = level[i];
            // Nodi dispari: l'ultimo si duplica (convenzione RFC 6962).
            let right = if i + 1 < level.len() { level[i + 1] } else { level[i] };
            next.push(hash_node(&left, &right));
            i += 2;
        }
        level = next;
    }
    Some(level[0])
}
```

Una sola firma Ed25519 per l'intero batch, non una per elemento: la stessa
economia dei transparency log. Chiunque verifica l'inclusione di un elemento con
la sua prova, senza avere gli altri.
