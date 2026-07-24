# Chroma

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 Chroma docs
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - local persistent client behavior changes
  - search/query API changes materially

## Scope
- Chroma as a local persistent vector/embedding retrieval product
- relevance to local-first semantic retrieval

## Canonical Boundary
This note covers Chroma as a concrete local semantic retrieval product.

For the general capability model, see:
- `research/capabilities/retrieval-pipelines.md`

## Current Findings
- Chroma provides a persistent local client.
- Collections can be created and loaded from a local path.
- Query APIs support nearest-neighbor retrieval over embeddings.
- Query surfaces also support metadata filters and document-content filters.
- The docs show query-by-text, query-by-embedding, and document filter patterns.

## Retrieval-Relevant Features

### Local persistence
Chroma can store collections locally through a persistent client.

This makes it relevant for local-first semantic retrieval systems.

### Vector retrieval
The core query API is nearest-neighbor retrieval over embeddings.

This makes it relevant to semantic search and similar-query lookup.

### Metadata and document filters
The docs show both:
- metadata filtering
- document-content filtering

This matters because pure vector similarity often needs additional narrowing.

## Practical Implications for Retrieval Systems
- Chroma is a concrete local vector retrieval option.
- It fits semantic retrieval use cases where embeddings are already part of the pipeline.
- Structured retrieval and rich relational querying remain separate concerns.

## Limitations
- it is primarily a vector/embedding store rather than a relational metadata system
- ingestion, chunking, and extraction quality remain upstream responsibilities
- mixed-corpus systems may still need separate structured or lexical retrieval surfaces beside it

## Relationship to Other Notes
- `research/capabilities/retrieval-pipelines.md`
- `research/concepts/context-engineering.md`
- `research/syntheses/local-first-retrieval-tool-comparison.md`

## References
- Context7 `/chroma-core/chroma` — persistent local client, query, and filtering examples.
