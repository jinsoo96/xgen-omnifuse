# Changelog

## 0.4.0

- Replaced `Memory` (remember/recall) with **`Vault`** — an omnifuse-native memory:
  - `fuse(text=, facts=)` write / `surface(query)` read (on-brand verbs, not generic remember/recall).
  - **fuse-on-write**: facts deduped & entities coreferenced by label (knowledge merges, not piles).
  - **salience**: each fuse/surface bumps node salience; `surface()` re-ranks results by it (no PPR/Hebbian).
  - `save()/load()` JSONL incl. salience; incremental label set (no per-write re-derivation).
- **Breaking**: `Memory`/`remember`/`recall` removed (the lib is pre-1.0; no released users relied on it).

## 0.3.0

- `Memory` — a growing store built on OmniFuse search. `remember()` facts/notes over time,
  `recall()` via the same one-shot graph+vector fusion. Notes auto-link to known entities by
  label; `save()/load()` JSONL persistence. (synaptic-memory–style memory on omnifuse's engine.)

## 0.2.0

- Convenience loaders so you can give loose data and search immediately (synaptic `from_data` style):
  - `from_triples(triples, chunks=...)` — accepts `(s, p, o)` tuples / dicts / `Triple`; **infers nodes**
    (object of an is-a edge → class) when none are given.
  - `from_jsonl(triples=, nodes=, chunks=)` and `from_csv(triples=, chunks=)` — stdlib json/csv, zero deps.
  - `from_fuseki(query_url, graph_uri, user=, password=)` — one call over any SPARQL endpoint.
- `build_inmemory` now coerces loose tuples/dicts too.

## 0.1.0

Initial extraction of the one-shot GraphRAG fusion algorithm as a backend-agnostic library.

- `OmniFuse.search` — one-shot fusion: vector/lexical + graph label-linking + class
  enumeration + HippoRAG 1-hop, fused with MMR diversity and adaptive top-k, single synthesis.
- `GraphStore` / `VectorStore` / `LLM` protocols (structural typing).
- Zero-infra backends: `InMemoryGraph` (BM25 label search with CJK n-grams, class
  enumeration, 1-hop traversal) and `InMemoryVector` (cosine or BM25 lexical).
- `EchoLLM` so the pipeline runs with no API key; `build_inmemory(...)` one-call setup.
- `FusekiGraph` — stdlib-only SPARQL adapter (any SPARQL 1.1 endpoint); same algorithm runs
  on a real Apache Jena Fuseki store. Self-contained (in-memory) and Jena modes both supported.
- Language-neutral default system prompt (overridable via `system_prompt=`).
- `dependencies = []` core; pytest smoke tests; quickstart + fuseki examples.
