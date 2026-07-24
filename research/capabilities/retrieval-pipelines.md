# Retrieval Pipelines

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - vendor-specific indexing APIs and store abstractions
  - default chunking/ranking heuristics
  - built-in citation and filtering features

## Summary
- Many systems need more than explicit file attachment; they need retrieval over a larger corpus.
- The durable capability is the pipeline that turns source documents into retrievable units, keeps them fresh enough, and returns grounded results with acceptable quality and traceability.
- The reusable problem is not just “semantic search.” It is the full chain from source ingestion through index maintenance to retrieval-time evidence.
- Retrieval may be lexical, semantic, hybrid, or structured; the stable capability is the pipeline and evidence contract, not one ranking method.
- In local-first environments, retrieval often needs to bridge several source types at once: plain text, markdown, PDFs, and structured records.

## Motivation
- A simple file or root attachment works well for bounded context, but it does not scale to large or changing corpora.
- Once a system depends on indexed stores, chunked documents, or retrieval-time ranking, the engineering problem changes.
- This note captures that capability boundary separately from context attachments and separately from long-term memory architecture.

## Problem Statement
- Systems need relevant context from large collections without pasting entire corpora into prompts.
- The design problem is how to:
  - ingest documents reliably
  - preserve identity and provenance
  - keep the index fresh enough
  - retrieve relevant evidence with acceptable recall and precision
  - make failures visible when retrieval goes stale or weak

For mixed corpora, the problem is harder because the system must reconcile:
- free text documents
- semi-structured documents with headings/tables/layout
- structured rows and metadata records
- multiple retrieval modes with different strengths

## Core Function
- Convert source material into retrievable representations.
- Maintain enough document identity, provenance, and freshness information to trust the results.
- Return relevant evidence rather than forcing the model to search blindly through raw corpora.

## Local-First Retrieval Goals
- Keep the corpus and indexes local by default.
- Work without cloud-only managed services.
- Support inspectable evidence and reproducible queries.
- Stay maintainable on ordinary developer machines.
- Respect practical constraints like corporate environments, Windows laptops, and intermittent workflow continuity.

## Typical Retrieval Modes

### Lexical retrieval
- keyword match
- exact term search
- path/name filters
- structured field filters

Strength:
- precise when the user knows exact terms or identifiers

Weakness:
- weak at paraphrase and concept-level similarity

### Semantic retrieval
- embedding similarity
- approximate nearest-neighbor search
- concept-level matching across wording variation

Strength:
- better recall across paraphrase and fuzzy language

Weakness:
- harder to debug, can look plausible while missing exact constraints

### Hybrid retrieval
- combine lexical filtering with semantic ranking or reranking

Strength:
- often the most practical compromise

Weakness:
- more moving parts, more drift surfaces, harder evaluation

### Structured retrieval
- IDs
- metadata constraints
- graph/record lookups
- explicit document links

Strength:
- high precision and inspectability when the corpus has good structure

Weakness:
- requires better source modeling up front

## Mixed-Corpus Retrieval Pattern

### Source families
Common local-first source families include:
- markdown / text notes
- PDFs and office-style documents
- code and config files
- structured tables or SQLite rows
- manually curated metadata records

### Stable architecture pattern
The most reusable architecture is often:
1. **ingest/normalize** each source family into a common record model
2. **preserve source identity and metadata**
3. **index multiple retrieval surfaces**:
   - lexical/full-text
   - semantic/vector
   - structured fields
4. **query with mode selection or hybrid fusion**
5. **return compact evidence with provenance**

### Why this matters
A mixed corpus is usually not well served by a single retrieval mechanism.

- PDFs often need parsing and chunking first.
- structured records often want exact filters first.
- notes and prose often benefit from lexical or semantic search.
- the best answer may require combining several result types.

## What This Note Is About
- Ingestion
- document identity
- chunking boundaries
- indexing
- freshness/update rules
- retrieval-time filtering, ranking, and evidence return

## What This Note Is Not About
- Not broad memory architecture
- Not simple one-off file attachment
- Not the full philosophy of context engineering
- Not vendor-specific SDK details except as examples

## Minimal Durable Model

### 1. Source identity
What source document or artifact does this indexed content come from?

Minimum useful fields:
- source ID
- source location or URI
- content type
- version or modified-at marker

### 2. Ingestion transform
How is the source turned into retrievable units?

Typical steps:
- parsing
- normalization
- segmentation/chunking
- metadata enrichment
- embedding and/or keyword indexing

For mixed corpora, also ask:
- was layout preserved?
- were tables or structured fields extracted?
- does the transform create one common record model or many source-specific ones?

### 3. Index record
What retrievable object gets stored?

Typical fields:
- chunk or document ID
- source ID
- chunk text or representation
- metadata
- embedding and/or lexical index terms

Helpful extra fields for mixed corpora:
- source family (`pdf`, `markdown`, `table_row`, `code_file`, etc.)
- section/title path
- page number or row key
- extraction confidence if OCR or parsing was involved

### 4. Freshness policy
When is re-ingestion required?

Typical options:
- never/immutable snapshot
- manual refresh
- scheduled refresh
- event-triggered refresh

### 5. Retrieval result
What evidence comes back at query time?

Typical fields:
- matched chunk/document
- score or rank
- source citation
- metadata filters used
- retrieval timestamp or run context

High-value extras:
- retrieval mode used (`lexical`, `semantic`, `hybrid`, `structured`)
- source family
- stable source locator (path, page, row key, URI)

## Common Patterns
- upload documents into a hosted knowledge store
- maintain a vector store keyed by source documents
- combine semantic and keyword retrieval
- attach metadata filters to narrow the search space
- return citations or source references with retrieved text
- re-index on source changes or scheduled refresh
- preserve stable document identity across re-ingestion
- keep structured IDs alongside embeddings instead of treating embeddings as the only retrieval path
- evaluate retrieval quality with explicit benchmark queries and failure tags
- use SQLite or other embedded stores for structured metadata and lexical retrieval
- use a dedicated parser/chunker for PDFs rather than pretending raw byte/text extraction is enough
- prefilter by metadata or source family before semantic ranking when the corpus is heterogeneous

## Typical Components
- document loader/parser
- chunker/segmenter
- metadata extractor
- embedding/index writer
- store or search backend
- freshness tracker
- retrieval/ranking layer
- optional reranker
- citation/provenance formatter
- evaluation harness for retrieval quality

Common local-first concrete building blocks:
- embedded SQL/FTS store for records and lexical search
- vector engine for semantic retrieval
- document parsing layer for PDFs and office documents
- thin tool/API surface the agent can query

## Durable Distinctions

### Retrieval vs attachment
Attachment says what outside corpus, store, or resource is available.

Retrieval says how relevant pieces are selected from that larger available corpus.

### Retrieval vs memory
Retrieval can serve memory systems, but retrieval alone is not memory.

Memory also needs persistence policy, write policy, promotion rules, correction, and retirement.

### Retrieval vs file/navigation tools
Many products expose `read`, `grep`, `glob`, filters, or path aliases.

Those can support retrieval-like workflows, but they are not automatically full retrieval pipelines.

If there is no ingestion, indexing, chunk identity, freshness policy, or retrieval evidence contract beyond raw file reads and matches, the product may still be doing bounded document navigation rather than true RAG-like retrieval infrastructure.

### Retrieval vs database querying
Structured database queries are retrieval too, but not all retrieval should be forced into vector search.

For inventories, logs, tabular records, and keyed artifacts, exact filters and SQL-style queries may be the primary retrieval surface, with semantic retrieval only as a secondary aid.

### Document identity vs chunk identity
The source document and the retrievable chunk are related but different.

Stable source identity matters for provenance, deduplication, and freshness.

### Freshness vs relevance
A relevant result can still be stale.

A fresh result can still be irrelevant.

Both must be considered separately.

## Portability
- Portable across tools:
  - large corpora need indexing or structured search rather than raw prompt stuffing
  - provenance and source identity matter
  - freshness policy matters as much as ranking quality
  - retrieval should return inspectable evidence, not only invisible host magic
  - metadata filters are often necessary, not optional sugar
  - lexical, semantic, and hybrid retrieval all exist; the right choice depends on corpus shape and error tolerance
  - mixed corpora usually require multiple retrieval surfaces, not one universal index alone
- Product-shaped:
  - exact upload/store API shape
  - chunking defaults
  - embedding and ranking implementation
  - hosted versus self-managed indexes
  - citation and filter syntax

## Advantages
- scales beyond direct file attachment
- reduces prompt size for large corpora
- enables reusable knowledge stores
- can improve grounding and citation quality
- supports selective retrieval over changing corpora
- can unify documents and structured records behind one consultation interface

## Risks / Failure Modes
- stale index after source changes
- chunking that breaks important context
- poor metadata causing wrong filtering or no filtering
- weak provenance that makes results hard to audit
- hidden retrieval logic that is hard to debug
- over-retrieval that floods the model with noise
- under-retrieval that misses crucial evidence
- retrieval quality drifting silently over time
- assuming semantic retrieval is always better than exact or structured lookup
- using retrieval where direct file attachment or direct navigation would have been simpler and more trustworthy
- poor PDF extraction leading to confident but wrong retrieval results
- trying to force structured records into document-style chunking when exact keys/filters would work better

## Tradeoffs
- **Big chunks vs small chunks**: more context continuity versus better pinpoint retrieval.
- **Semantic vs lexical retrieval**: conceptual recall versus exact-term precision.
- **Hybrid ranking vs simple search**: often better results versus more complexity and more hidden failure modes.
- **One unified store vs split stores**: simpler mental model versus using the best tool for each retrieval mode.
- **Raw text extraction vs layout-aware parsing**: simpler ingestion versus better quality for PDFs and tables.
- **Hosted store vs local/self-managed index**: convenience versus transparency and control.
- **Frequent refresh vs cheaper refresh**: freshness versus cost and operational complexity.
- **Aggressive recall vs tight precision**: completeness versus context noise.

## Practical Local-First Architectures

### A. Embedded lexical + structured base
Typical shape:
- SQLite + FTS for full-text
- normal relational tables for metadata and structured records

Common fit:
- exact lookup matters
- the corpus is mostly text + records
- simplicity and inspectability matter more than semantic fuzziness

### B. Split ingestion + vector retrieval
Typical shape:
- document parser/chunker for PDFs and mixed files
- vector store for semantic retrieval
- metadata filters around vector search

Common fit:
- paraphrase-heavy queries matter
- the corpus is too fuzzy for lexical search alone

### C. Hybrid local stack
Typical shape:
- embedded SQL/FTS for exact and metadata retrieval
- vector engine for semantic retrieval
- one thin query tool that fuses results

Common fit:
- the corpus mixes notes, PDFs, and structured records
- both auditability and semantic reach matter

This is usually the strongest long-term pattern for mixed local corpora.

## Common Selection Heuristics
- **Direct attachment** is common when the needed context is small and already known.
- **Direct navigation/search tools** fit local corpora that remain inspectable and deterministic.
- **Retrieval pipelines** become more common when the corpus is large, dynamic, or semantically fuzzy enough that direct navigation stops being reliable.
- **Memory architecture** becomes the main concern when the problem shifts from corpus search to persistence, promotion, correction, and retirement across time.

## Relationships to Other Notes
- `../concepts/context-engineering.md`
- `../concepts/memory-systems.md`
- `../concepts/observability-traceability.md`
- `../concepts/evaluation-prompt-testing.md`
- `../capabilities/context-attachments.md`
- `../capabilities/eval-harnesses.md`
- `../syntheses/memory-policy.md`
- `../syntheses/observability-schema.md`
- `../products/opencode/memory-and-retrieval.md`

## Relevance to This Repository
- This repository already distinguishes between direct file/context access and broader retrieval infrastructure.
- If a local knowledge store is introduced later, source identity and modified-at metadata would be especially important for auditability and refresh behavior.
- Repo-local `read`/`grep`/`glob` workflows remain simpler than a maintained retrieval pipeline and solve a different class of problem.
- Mixed-corpus retrieval patterns are relevant here because the target corpus may include notes, PDFs, and structured records together.
- PDF ingestion quality and exact-key lookup for structured records both remain important even in systems that also add semantic retrieval.

## Open Questions
- If this repository ever uses a knowledge store, what source metadata is the minimum useful set?
- Which refresh policy would be maintainable in a long-gap, local-first workflow?
- When is exact search enough, and when is semantic retrieval justified?
- What retrieval evidence should be surfaced by default for audit and debugging?
- Should a future local consultation tool expose one unified query interface with mode selection, or separate tools for exact search, semantic search, and structured lookup?

## References
- OpenAI file search / retrieval docs — representative hosted example of store-backed retrieval, metadata filters, and citations.
- RAG paper (`Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks`) — foundational framing of retrievable external knowledge.
- `../concepts/memory-systems.md` — clarifies why retrieval is only one part of memory architecture.
- `../capabilities/context-attachments.md` — clarifies the boundary between making a corpus available and searching within it.
- SQLite FTS5 docs — strong representative example of boring local lexical retrieval with embedded structured storage.
- Qdrant local mode docs — representative example of local semantic/hybrid retrieval with metadata payload filters.
- Docling docs — representative example of local mixed-document parsing and chunking for PDF-heavy corpora.
