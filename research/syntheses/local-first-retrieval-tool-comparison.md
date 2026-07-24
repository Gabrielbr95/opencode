# Local-First Retrieval Tool Comparison

This note compares concrete local-first tools that can participate in agent retrieval over mixed corpora.

Its goal is descriptive:
- what role each tool appears to play
- what retrieval surfaces it exposes
- where it fits in a mixed local corpus stack

It is not an adoption plan by itself.

---

## Scope

Tools covered here:
- SQLite FTS5
- Docling
- Qdrant
- LanceDB
- Chroma

These tools do not all solve the same problem.
Some are ingestion tools, some are lexical/structured retrieval tools, and some are semantic retrieval engines.

---

## Comparison Matrix

| Tool | Primary role | Local-first shape | Retrieval surfaces shown in docs | Mixed-corpus relevance | Main boundary |
|---|---|---|---|---|---|
| SQLite FTS5 | Embedded lexical + structured retrieval | Embedded DB file | full-text search + SQL tables/filters | Strong for text chunks + structured rows | No built-in semantic retrieval |
| Docling | Document ingestion / parsing / chunking | Local parsing library | upstream parsing and chunking rather than search | Strong for PDFs and office-style docs | Not a search/index backend |
| Qdrant | Semantic/vector retrieval | Local mode in memory or on disk | vector search + payload filters + hybrid-style fusion patterns | Strong when paraphrase/fuzzy retrieval matters | Needs embeddings and upstream chunking |
| LanceDB | Embedded retrieval database | Embedded/local backend | vector + full-text + hybrid search | Strong candidate for integrated local retrieval | Still a specialized retrieval engine |
| Chroma | Local vector retrieval | Persistent local client | vector search + metadata/document filters | Useful for semantic retrieval layers | Primarily vector-focused, not relational |

---

## Observed Tool Roles

### SQLite FTS5
Observed role:
- lexical search
- structured record storage
- metadata filtering and exact lookup in the same local store

### Docling
Observed role:
- parse documents into more usable structures
- chunk documents before indexing
- preserve more structure than plain text extraction alone

### Qdrant
Observed role:
- semantic/vector retrieval with metadata payloads
- local semantic search without requiring a remote hosted database

### LanceDB
Observed role:
- one embedded engine that spans full-text, vector, and hybrid retrieval

### Chroma
Observed role:
- local persistent semantic/vector retrieval with filtering support

---

## Mixed-Corpus View

For mixed corpora, the tools line up into distinct layers:

### Ingestion layer
- Docling

### Lexical / structured retrieval layer
- SQLite FTS5

### Semantic retrieval layer
- Qdrant
- Chroma

### Integrated retrieval-engine alternative
- LanceDB

This layered view matches the capability note more closely than treating all of these tools as interchangeable "RAG databases".

---

## Common Boundaries Seen Across Tools

- document parsing is not the same as retrieval
- lexical/structured retrieval is not the same as semantic retrieval
- vector stores do not remove the need for metadata and provenance
- local persistence does not automatically solve freshness, evaluation, or evidence formatting

---

## Relationship to Other Notes

- `../capabilities/retrieval-pipelines.md`
- `../concepts/context-engineering.md`
- `../products/sqlite-fts5.md`
- `../products/docling.md`
- `../products/qdrant.md`
- `../products/lancedb.md`
- `../products/chroma.md`
