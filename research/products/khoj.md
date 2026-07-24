# Khoj

## Freshness
- Last verified: 2026-07-24
- Verified against: Khoj docs, feature docs, desktop docs, telemetry docs, and API references
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - Windows setup path changes
  - API/filter semantics changes
  - self-host deployment model changes

## Scope
- Khoj as an existing second-brain / knowledge-search product
- relevance to local retrieval over mixed corpora with later opencode access

## Canonical Boundary
This note covers Khoj as a concrete product.

For cross-product comparison, see:
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Why This Matters Here
- Khoj is one of the products most naturally aligned with the phrase “second brain” while still exposing real retrieval APIs.
- It is especially relevant if semantic search over a growing personal/local corpus matters strongly.

## Current Findings
- Khoj supports self-hosted/local use and can keep data private/local.
- It supports multiple source/file types including markdown, plaintext, PDFs, and office-style files.
- Search APIs support semantic search and file-type / scope filters.
- Per-conversation or per-query file scoping appears stronger than in many simple note tools.
- The main weakness for this user is Windows setup friction.

## Product-Specific Details

### Local-first posture
- strong local/private posture in principle
- explicit self-hosting story

### Topic scoping
Natural boundaries appear to include:
- file filters
- source filters
- conversation-level file pinning/scoping

This is useful, though the product looked less like a permissioned workspace platform than Open WebUI.

### Retrieval surfaces
- semantic search API
- content/file APIs
- filtering over indexed content

### Corpus fit
Strong fit for:
- mixed personal knowledge
- synced folders/files
- semantic search over notes and documents

### Risk notes
- Windows setup appears more awkward than AnythingLLM Desktop or Joplin
- WSL2/Docker or pip-style setup is a weaker fit on a locked-down corporate machine
- telemetry exists but appears configurable/disableable

## Relationships to Other Notes
- `research/products/anythingllm.md`
- `research/products/open-webui.md`
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Relevance to This Repository
- Khoj currently looks like a strong conceptual fit for a true second-brain-plus-retrieval product.
- Its main weakness here is not retrieval quality, but Windows/corporate setup friction.

## Open Questions
- Could Khoj be made practical on this machine without admin-heavy setup?
- How strong is its real topic-isolation story compared with knowledge-base/workspace products?
- Would the setup burden outweigh the product fit for day-to-day use?

## References
- Khoj setup docs
- Khoj feature overview docs
- Khoj desktop docs
- Khoj telemetry docs
- Khoj search/content API docs
