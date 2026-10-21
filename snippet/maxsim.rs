# SigmaTek X — estratto: rerank late-interaction (MaxSim)

> Estratto **ridotto** da un modulo reale (Rust). Mostra il punto in cui il
> progetto prova a superare, non a eguagliare, la ricerca semantica standard.

Il mean pooling produce un vettore per documento e perde le sfumature. MaxSim
tiene i vettori dei singoli token e, per ogni token della query, prende la
similarità migliore: costa di più, restituisce molto di più. È usato solo sul
top-K fuso, dove il costo è sostenibile anche su un telefono.

```rust
/// Similarità coseno, con guardia su vettori vuoti o di lunghezza diversa.
pub fn cosine(a: &[f32], b: &[f32]) -> f32 {
    if a.len() != b.len() || a.is_empty() {
        return 0.0;
    }
    let dot: f32 = a.iter().zip(b).map(|(x, y)| x * y).sum();
    let na: f32 = a.iter().map(|x| x * x).sum::<f32>().sqrt();
    let nb: f32 = b.iter().map(|x| x * x).sum::<f32>().sqrt();
    if na == 0.0 || nb == 0.0 { 0.0 } else { dot / (na * nb) }
}

/// Late-interaction tipo ColBERT: per ogni token della query,
/// il miglior token del documento. Media sui token della query.
pub fn maxsim(query: &[Vec<f32>], doc: &[Vec<f32>]) -> f32 {
    if query.is_empty() || doc.is_empty() {
        return 0.0;
    }
    let mut total = 0f32;
    for q in query {
        let mut best = f32::MIN;
        for d in doc {
            let c = cosine(q, d);
            if c > best {
                best = c;
            }
        }
        total += best;
    }
    total / query.len() as f32
}
```

Il risultato di MaxSim non sostituisce il punteggio fuso: lo **raffina**, con un
peso esplicito e conservativo. Sul mobile, un rerank aggressivo costa più di
quanto renda.
