# AI Workflow Research

This directory stores structured research notes for improving the AI workflow over time.

## Goals
- Keep findings local and durable.
- Separate slower-changing ideas from faster-changing ecosystem and product details.
- Make it easy to extend topic-by-topic across interrupted sessions.
- Preserve source traceability through citations.

## Partitioning Rule: Organize by Stability Horizon

This repository uses three primary research layers plus a synthesis layer.

### 1. `concepts/` — Concepts
Slow-moving ideas that should remain useful across vendor or framework churn.

Examples:
- agent architectures
- planning systems
- memory systems
- evaluation
- agent harnesses

These notes answer:
- What is it?
- Why does it matter?
- What are the main tradeoffs and boundaries?

### 2. `capabilities/` — General Tools and Functionalities
Medium-moving capabilities, protocols, and building blocks that outlive any one product but can evolve with the ecosystem.

Examples:
- MCP
- RAG
- tool calling
- model routing
- retrieval pipelines

These notes answer:
- What capability does this provide?
- What are the common implementation patterns?
- What is portable versus tool-specific?

### 3. `products/` — Tool-Specific Implementations
Fast-moving notes about how a specific product works right now.

Examples:
- opencode
- Claude Code
- LM Studio
- Obsidian

These notes answer:
- What does this tool support today?
- How is it configured?
- What matters for this local workflow?
- What might go stale soon?

### 4. `syntheses/` — Repository-Level Knowledge
Cross-cutting conclusions distilled from multiple concepts, capabilities, and product notes.

Examples:
- vocabulary
- control boundaries
- memory policy
- comparison matrices

These notes answer:
- What have we concluded for this repository?
- Which distinctions should stay stable across future research?
- What decision aids reduce re-learning after long gaps?

## Structure
- `index.md` — research map, grouped by layer.
- `backlog.md` — future concepts, capabilities, open questions, and follow-up ideas.
- `concepts/` — concept notes.
- `capabilities/` — medium-volatility capability notes.
- `products/` — fast-moving product notes.
- `syntheses/` — cross-cutting distilled notes, vocabularies, and comparison docs.
- `templates/` — reusable note templates for consistent capture.

## Freshness Expectations
- **Concepts**: prioritize durable definitions, boundaries, and tradeoffs.
- **Capabilities**: include likely drift areas and portability notes.
- **Products**: include explicit freshness metadata such as last verified date, source checked, and recheck triggers.

## Working Rules
- Prefer small, focused notes over giant summary documents.
- Record tradeoffs, not just summaries.
- Cite sources in every research note.
- Cross-link related notes when useful.
- Update the index when a new note is added.
- Put vendor-neutral understanding in `concepts/` or `capabilities/`, not in `products/`.
- Use `syntheses/` for repository conclusions and decision aids, not for raw product findings.
- Treat product notes as dated snapshots, not timeless truth.
