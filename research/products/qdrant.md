# Qdrant

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 Qdrant client docs
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - local mode behavior changes
  - hybrid/fusion API changes
  - metadata filter behavior changes materially

## Scope
- Qdrant as a local semantic/vector retrieval product
- relevance to local-first agent retrieval with metadata filtering and hybrid patterns

## Canonical Boundary
This note covers Qdrant as a concrete product implementing semantic/vector retrieval.

For the general capability model, see:
- `research/capabilities/retrieval-pipelines.md`

## Current Findings
- Qdrant's Python client supports a local mode.
- Local mode can run in memory or persist to a filesystem path.
- Qdrant stores vectors with payload metadata.
- Query APIs support metadata filtering through payload conditions.
- The docs also show hybrid-style workflows that fuse dense and sparse results client-side.

## Retrieval-Relevant Features

### Local mode
The same client can run without a separate remote service by using:
- in-memory mode
- persistent local path mode

That makes Qdrant relevant for local-first experimentation and embedded workflows.

### Vector retrieval
Qdrant is built for dense-vector search.

This makes it relevant to:
- semantic search
- paraphrase-tolerant retrieval
- embedding-based nearest-neighbor lookup

### Payload metadata filters
Qdrant supports payload metadata on stored points and filtering during queries.

This matters for mixed corpora because semantic search often needs:
- source-family filtering
- project filtering
- document-type filtering
- exact narrowing before or alongside vector ranking

### Hybrid fusion patterns
The client docs show reciprocal-rank-fusion style workflows across dense and sparse retrieval outputs.

This makes Qdrant relevant beyond pure dense-vector retrieval.

## Practical Implications for Retrieval Systems
- Qdrant provides a concrete local semantic retrieval layer.
- It is especially relevant when lexical retrieval alone misses paraphrase-heavy or fuzzy queries.
- It still depends on an embedding pipeline and retrieval evaluation discipline.

## Limitations
- it is not the document parser or chunker
- semantic retrieval quality depends on embedding choices and corpus preparation
- hybrid retrieval still requires orchestration beyond bare storage/query primitives

## Relationships to Other Notes
- `research/capabilities/retrieval-pipelines.md`
- `research/concepts/context-engineering.md`
- `research/syntheses/local-first-retrieval-tool-comparison.md`

## References
- Context7 `/qdrant/qdrant-client` — local mode, payload filtering, and hybrid fusion examples.
