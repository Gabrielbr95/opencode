# Product Research

This directory stores fast-moving notes about specific tools and implementations.

## What Belongs Here
- Product feature maps
- configuration behavior
- advanced features
- local workflow fit
- version- or release-sensitive findings

## Typical Products
- opencode
- Claude Code
- LM Studio
- Obsidian
- SQLite / SQLite FTS5
- Docling
- Qdrant
- LanceDB
- Chroma

## What Does Not Belong Here
- Vendor-neutral concepts or general design rules. Put those in `../concepts/`.
- Capability-level notes that apply across many tools. Put those in `../capabilities/`.
- Cross-product comparisons or repository-level conclusions. Put those in `../syntheses/`.

## Freshness Guidance
Every product note should carry a small freshness block near the top.

Suggested fields:
- Last verified
- Verified against
- Product/version if known
- Stability
- Recheck triggers

Treat these notes as dated field notes, not permanent truth.

## Suggested Shape
- One subdirectory per product once the product grows beyond a single note.
- Start with a `README.md` or `overview.md` for each product.
- Split only when the branch becomes crowded.
