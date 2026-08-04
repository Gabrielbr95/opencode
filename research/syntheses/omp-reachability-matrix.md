# OMP Reachability Matrix

This note maps selected OMP capabilities against the current evidence for reaching them through baseline Pi plus documented extensions/packages.

Its purpose is practical:
- separate "Pi can already do this" from "Pi might do this with custom work"
- identify where OMP still looks like a distinct integrated product
- reduce hand-wavy claims about parity

It is not a final recommendation.

---

## Freshness
- Last verified: 2026-08-04
- Derived from:
  - `research/products/omp/*` notes verified 2026-08-04
  - `research/products/pi/*` notes verified 2026-07-28
  - selected official Pi package pages reviewed 2026-08-04
- Stability: Low
- Recheck triggers:
  - OMP built-in capability claims change materially
  - Pi package ecosystem gains first-class equivalents for current gap areas
  - reviewed package READMEs or package pages change materially

---

## Scope
- selected OMP capabilities that matter for this repository
- off-the-shelf Pi parity versus custom-extension possibility versus likely OMP-specific integration
- product-level reachability only

## Canonical Boundary
This note is a synthesis matrix.

Use product notes for exact mechanics:
- `../products/omp/README.md`
- `../products/omp/foundations.md`
- `../products/omp/architecture-and-divergence.md`
- `../products/pi/README.md`

---

## Status Legend
- **Pi core parity** — baseline Pi already has the capability category in core
- **Pi package parity** — official current evidence shows a documented package/extension route
- **Custom extension maybe** — Pi likely could approach it with custom engineering, but current official package evidence is not enough to call it off-the-shelf parity
- **Currently OMP-specific/integrated** — current reviewed sources do not show a clean documented Pi path, and the feature appears tightly integrated into OMP's own product/runtime

---

## Reachability Matrix

| OMP capability | Current reachability from Pi | Current Pi route / evidence | Notes |
|---|---|---|---|
| Subagents / task delegation / parallel worker patterns | **Pi package parity** | `pi-subagents` | Strongest clear parity area. |
| Plan mode / read-only planning lane | **Pi package parity** | `@narumitw/pi-plan-mode` | Clear package-level parity in category, though exact UX may differ. |
| Web search / URL fetch / PDF extraction / GitHub fetch-style workflows | **Pi package parity** | `pi-web-access` | Strong parity at workflow level. |
| Browser automation / authenticated browser sessions / Electron-style automation | **Pi package parity** | `pi-agent-browser-native` | Strong category parity, though full OMP integration surface may still differ. |
| Persistent memory / session search / learned memory behavior | **Pi package parity** | `pi-hermes-memory` | Broad parity at category level. |
| Todo tracking | **Pi package parity** | `@juicesharp/rpiv-todo` | Broad parity at workflow level. |
| Runtime permission/approval layer | **Pi package parity** | `@gotgenes/pi-permission-system` | Important parity area, though exact defaults/UX differ from OMP's unclear model. |
| Basic LSP diagnostics / fixes | **Pi package parity** | `@narumitw/pi-lsp` | Current package evidence supports diagnostics/fixes, not full LSP parity. |
| Session persistence / resume / compaction | **Pi core parity** | Pi core | Baseline parity exists, though exact session model differs. |
| Provider/model routing / RPC/programmatic use | **Pi core parity** | Pi core | Broad parity category exists in both products. |
| Richer LSP integration wired into every write | **Custom extension maybe** | `@narumitw/pi-lsp` is partial | Current Pi package evidence is not enough for full parity. |
| Advisor model watching turns and intervening inline | **Custom extension maybe** | no reviewed official package match | Feels extension-plausible, not verified off-the-shelf. |
| Rich built-in review semantics with structured verdict/ranking | **Custom extension maybe** | `pi-subagents` gives review workflows, not exact parity | Similar workflows exist, exact built-in contract not verified. |
| Commit splitting / validated atomic commit workflow | **Custom extension maybe** | no reviewed official package match | Likely buildable, not verified as current package parity. |
| ACP/editor-driven experience beyond Pi RPC/SDK | **Custom extension maybe** | Pi RPC/SDK exists | Foundation exists, exact parity not verified. |
| Built-in persistent Python + Bun eval bridge with tool-calling callback model | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Looks like integrated runtime/product work. |
| Built-in DAP/debugger integration | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Possible in theory, not evidenced in current package set reviewed. |
| Virtual path schemes like `pr://`, `issue://`, `ssh://`, `skill://`, `agent://` | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Looks deeply integrated into OMP's tool surface. |
| AST preview/accept conflict-resolution flow | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Looks product-specific. |
| Desktop/computer tool for window/input/accessibility control | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Browser/Electron parity exists nearby; full desktop parity not verified. |
| Live collaboration relay / join links / watch mode | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Pi sharing exists, but not this same live-collab surface in current notes. |
| Cross-ecosystem inheritance of rules/skills/MCP definitions from many other coding-agent tools | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | Important migration-related OMP differentiator. |
| Native Rust-backed tool/runtime engine | **Currently OMP-specific/integrated** | no reviewed official Pi parity source | This is architectural, not just feature-level. |

---

## Main Pattern
The matrix suggests three layers:

### Layer 1: Workflow parity is often reachable
Many user-visible workflow features are already reachable through Pi packages.

### Layer 2: Richer behaviors may need custom engineering
Some features look plausible in Pi because the extension surface is broad, but current official package evidence does not show easy parity.

### Layer 3: OMP still owns an integrated product layer
The deepest gaps are not random features. They cluster around:
- runtime integration
- native tooling
- debugger/eval surfaces
- desktop/collab integration
- virtual path abstractions
- cross-ecosystem import behavior

That pattern is consistent with OMP being a real product fork rather than merely a curated package distribution.

---

## Practical Reading of the Matrix
- If your goal is **workflow approximation**, Pi plus packages looks viable for a large subset of OMP.
- If your goal is **full product parity**, the current evidence does not support "just install enough packages" as a complete answer.
- If your goal is **lowest maintenance**, the matrix alone is not enough; you must also consider package sprawl, trust review, and Windows fit.

---

## Relationships to Other Notes
- `../products/omp/foundations.md`
- `../products/omp/architecture-and-divergence.md`
- `../products/omp/security-and-trust.md`
- `../products/pi/extension-ecosystem-and-core-gaps.md`
- `../products/pi/providers-and-programmatic-surfaces.md`
- `../syntheses/pi-to-omp-reachability.md`
- `../syntheses/pi-vs-omp-comparison.md`

---

## Open Questions
- Which current gap areas already have packages that were simply not reviewed in this pass?
- Which OMP-integrated features actually matter in day-to-day use versus just sounding impressive?
- Which parity gaps would still matter after filtering for your actual workflow and environment constraints?
