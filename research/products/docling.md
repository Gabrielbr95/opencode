# Docling

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 Docling docs
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - parser API or chunking API changes
  - Windows/local installation experience differs materially from docs

## Scope
- Docling as a local document parsing and chunking tool
- relevance to retrieval pipelines over PDFs and mixed document formats

## Canonical Boundary
This note covers Docling as a concrete ingestion-layer product.

For the general retrieval subsystem model, see:
- `research/capabilities/retrieval-pipelines.md`

## Current Findings
- Docling is a document conversion/parsing tool aimed at mixed formats such as PDFs and other office-style documents.
- It exposes a `DocumentConverter` for converting source documents into structured document representations.
- It provides chunking utilities, including hierarchical chunking.
- It also exposes structured extraction features in addition to plain text extraction.

## Retrieval-Relevant Features

### Mixed-document parsing
Docling is oriented toward converting documents into machine-usable structures rather than treating them as raw opaque files.

This matters for:
- PDFs
- layout-heavy documents
- documents where sections/tables matter to later retrieval

### Chunking support
Docling provides chunking workflows that can preserve document structure.

That makes it relevant upstream of:
- lexical indexing
- semantic embeddings
- hybrid retrieval pipelines

### Structured extraction
The docs also show structured extraction capabilities.

This is relevant when documents contain tables or semi-structured information that should not be flattened blindly into plain text.

## Practical Implications for Retrieval Systems
- Docling addresses the ingestion side of retrieval rather than the search index itself.
- It is most relevant when retrieval quality depends on parsing documents better than raw text extraction would.
- It can serve as a front-end to lexical stores, vector stores, or hybrid systems.

## Limitations
- it is not itself the retrieval backend
- it adds a real ingestion dependency and processing pipeline
- later retrieval quality still depends on how outputs are chunked, stored, and indexed downstream

## Relationship to Other Notes
- `research/capabilities/retrieval-pipelines.md`
- `research/concepts/context-engineering.md`
- `research/syntheses/local-first-retrieval-tool-comparison.md`

## References
- Context7 `/docling-project/docling` — `DocumentConverter`, hierarchical chunking, and structured extraction examples.
