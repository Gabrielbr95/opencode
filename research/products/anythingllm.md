# AnythingLLM

## Freshness
- Last verified: 2026-07-24
- Verified against: AnythingLLM docs and README
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - Desktop workspace-access model changes
  - API or MCP surface changes
  - telemetry/network behavior changes

## Scope
- AnythingLLM as an existing retrieval-first knowledge workspace product
- relevance to a second-brain system over mixed corpora with later opencode retrieval

## Canonical Boundary
This note covers AnythingLLM as a concrete product.

For cross-product comparison, see:
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Why This Matters Here
- AnythingLLM is one of the strongest existing products when the main goal is asking a local knowledge workspace questions rather than maintaining a classical note app.
- It is especially relevant for mixed corpora including manuals and PDFs.

## Current Findings
- AnythingLLM Desktop is explicitly positioned as a local-on-device option.
- Local storage includes SQLite plus local vector-store material such as LanceDB.
- The product supports common document types such as PDFs and office-style files.
- A developer API exists, and MCP compatibility is documented.
- Workspaces are the natural corpus boundary.
- Stronger workspace access management appears to belong to Docker/server deployment rather than Desktop.

## Product-Specific Details

### Local-first posture
- Desktop mode is suitable when data should stay on the device
- local storage paths and database/index components are documented

### Topic scoping
Natural topic boundary:
- workspace

This is useful, but topic gating by permissions appears stronger in server/Docker mode than in plain Desktop use.

### Retrieval surfaces
- retrieval-oriented workspace UX
- API surface
- MCP compatibility
- local vector-backed search infrastructure

### Corpus fit
Strong fit for:
- mixed documents
- manuals
- PDFs
- procedures
- growing retrieval-oriented corpora

Less naturally a human-authored “note garden” than Joplin or Obsidian.

### Risk notes
- telemetry and some outbound convenience/network behavior need review and likely hardening
- Desktop is the easiest local fit, but the strongest scoped-access controls may require heavier deployment shape

## Relationships to Other Notes
- `research/products/open-webui.md`
- `research/products/khoj.md`
- `research/products/joplin.md`
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Relevance to This Repository
- AnythingLLM currently looks like the strongest retrieval-first existing product for a local second-brain-like corpus on a corporate Windows laptop.
- It is a strong candidate for the manuals/procedures corpus even if a separate note-centric product handles curated research knowledge.

## Open Questions
- Is Desktop-scoped workspace separation sufficient, or would the desired topic gating require server/Docker mode?
- How cleanly can opencode query only selected workspaces through the documented API/MCP surfaces?
- How much network behavior can be disabled in practice in this environment?

## References
- AnythingLLM installation overview docs
- AnythingLLM desktop storage docs
- AnythingLLM README
- AnythingLLM API/MCP feature docs
