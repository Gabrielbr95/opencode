# LanceDB

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 LanceDB docs
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - local backend behavior changes
  - Python API for hybrid/full-text search changes materially

## Scope
- LanceDB as an embedded retrieval-oriented database
- relevance to local-first full-text, vector, and hybrid retrieval

## Canonical Boundary
This note covers LanceDB as a concrete local retrieval product.

For the general capability model, see:
- `research/capabilities/retrieval-pipelines.md`

## Current Findings
- LanceDB presents itself as an embedded retrieval-oriented database.
- The docs show support for vector search, full-text search, and hybrid search.
- Python query builders support hybrid search flows.
- Full-text indexing can be created on text columns.
- Vector search queries can combine metadata filtering with prefilter or postfilter behavior.

## Retrieval-Relevant Features

### Embedded/local posture
The product emphasizes an in-process local backend in addition to remote options.

This makes it relevant to local-first retrieval systems.

### Full-text + vector + hybrid support
LanceDB is notable because it is not only a vector store.

The docs show retrieval surfaces for:
- full-text search
- vector search
- hybrid search

### Metadata-aware querying
The query APIs support filtering around vector search.

That matters in mixed corpora where semantic retrieval often needs structured narrowing.

## Practical Implications for Retrieval Systems
- LanceDB is relevant when one wants a more integrated embedded retrieval engine.
- It overlaps some roles that other stacks split between SQL/FTS and a separate vector engine.
- It still leaves ingestion, corpus modeling, and evaluation as separate concerns.

## Limitations
- it is still a specialized retrieval dependency rather than a plain embedded SQL database
- retrieval quality still depends on ingestion, chunking, and query design upstream
- operational simplicity versus split-stack approaches depends on the surrounding architecture

## Relationships to Other Notes
- `research/capabilities/retrieval-pipelines.md`
- `research/concepts/context-engineering.md`
- `research/syntheses/local-first-retrieval-tool-comparison.md`

## References
- Context7 `/lancedb/lancedb` — embedded backend, full-text search, vector filtering, and hybrid query builder examples.
