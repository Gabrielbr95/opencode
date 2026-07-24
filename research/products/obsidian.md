# Obsidian

## Freshness
- Last verified: 2026-07-24
- Verified against: Obsidian docs and privacy pages
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - local data-storage model changes
  - search/URI behavior changes
  - official automation surface changes

## Scope
- Obsidian as an existing local markdown-first second-brain product
- relevance to topic-scoped retrieval for opencode

## Canonical Boundary
This note covers Obsidian as a concrete product.

For cross-product comparison, see:
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Why This Matters Here
- Obsidian is one of the cleanest local-first note tools when plain files and low lock-in matter more than built-in APIs.
- It is especially relevant if the second brain should remain transparent in the filesystem.

## Current Findings
- Obsidian stores notes as local markdown files in a vault.
- Multiple vaults provide a strong natural topic or trust boundary.
- Search appears strong for keyword/file/path-style use, but the product is more file-native than API-native.
- An `obsidian://` URI scheme exists.
- No strong official local API or MCP surface was established in this research pass.

## Product-Specific Details

### Local-first posture
- plain markdown vault on disk
- strong user control over file ownership
- low lock-in relative to database-backed note systems

### Topic scoping
Natural boundaries appear to be:
- separate vaults
- folders within a vault
- file/path conventions

This is strong for human organization and for explicit filesystem scoping.

### Retrieval surfaces
- keyword search with operators and filters
- direct file access by external tools
- URI surface for launching/navigating

### Corpus fit
Strong fit for:
- markdown notes
- research repositories
- local note gardens

Weaker fit as a ready-made retrieval layer for PDFs/manuals unless the workflow is comfortable treating those as attached files inside or beside the vault.

### Risk notes
- low phone-home concern relative to many app ecosystems
- plugin ecosystems and update flows still deserve review in a corporate environment

## Relationships to Other Notes
- `research/products/joplin.md`
- `research/products/anythingllm.md`
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Relevance to This Repository
- Obsidian currently looks strongest when local file transparency outranks official retrieval/API integration.
- It is a particularly good fit for the `research/` corpus if the goal is to keep knowledge in inspectable markdown rather than app-managed records.
- It looks weaker than Joplin for immediate opencode integration because the official automation surface is less explicit.

## Open Questions
- Would direct vault filesystem retrieval be sufficient for the intended opencode workflow?
- How much topic gating should rely on separate vaults versus in-vault structure?
- How much PDF/manual material would feel natural in an Obsidian-centered setup?

## References
- Obsidian storage docs
- Obsidian search docs
- Obsidian URI docs
- Obsidian privacy page
- Obsidian download page
