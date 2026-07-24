# SQLite FTS5

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 SQLite docs and sqlite-utils docs
- Product version: current docs snapshot; exact local SQLite build not verified
- Stability: High
- Recheck triggers:
  - local SQLite build lacks expected FTS5 support
  - tokenizer or extension requirements change materially

## Scope
- SQLite as an embedded local database
- FTS5 as its built-in full-text search mechanism
- relevance to local-first agent retrieval over text and structured records

## Canonical Boundary
This note covers SQLite FTS5 as a concrete local lexical/structured retrieval implementation.

For the cross-tool capability model, see:
- `research/capabilities/retrieval-pipelines.md`

## Current Findings
- SQLite provides an embedded, serverless SQL database that stores data locally in ordinary database files.
- FTS5 provides full-text search via virtual tables.
- FTS5 can be used directly or tied to a normal content table.
- Content-table patterns use triggers to keep the full-text index synchronized with inserts, updates, and deletes.
- SQLite's ordinary relational tables remain available for exact lookup, metadata filters, joins, and structured records beside the FTS index.

## Retrieval-Relevant Features

### Embedded local storage
- no separate service process is required
- persistence is file-based
- useful for local-first environments

### Full-text search tables
FTS5 virtual tables can index text columns for full-text search.

This makes SQLite more than a metadata store; it becomes a searchable corpus store as well.

### Content-table synchronization
SQLite supports an external-content style pattern where:
- the main table stores authoritative rows
- the FTS table stores the searchable projection
- triggers keep them aligned

This is useful when retrieval must coexist with structured metadata and exact SQL queries.

### Structured + lexical retrieval in one place
Because SQLite is still a relational database, the same local database can hold:
- documents or chunks
- metadata
- extraction status
- structured records
- exact filters and joins

## Practical Implications for Retrieval Systems
- SQLite FTS5 fits lexical retrieval well.
- It naturally supports structured lookup and metadata filtering.
- It does not provide semantic/vector retrieval by itself.
- Quality for PDFs or office-style documents depends on upstream extraction and chunking.

## Related Ecosystem Note
The `sqlite-utils` project provides a practical Python/CLI layer for enabling FTS, creating triggers, and querying SQLite more ergonomically.

That is an ecosystem convenience, not the core FTS implementation itself.

## Limitations
- no built-in semantic retrieval layer
- retrieval quality depends on tokenizer choice and upstream text extraction
- hybrid fusion must be built around SQLite rather than assumed to exist automatically

## Relationship to Other Notes
- `research/capabilities/retrieval-pipelines.md`
- `research/concepts/context-engineering.md`
- `research/syntheses/local-first-retrieval-tool-comparison.md`

## References
- Context7 `/websites/sqlite_docs` — FTS5 virtual table creation and content-table trigger examples.
- Context7 `/simonw/sqlite-utils` — FTS enable/search/populate APIs used as practical SQLite ergonomics examples.
