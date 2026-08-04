# Pi Foundations

## Freshness
- Last verified: 2026-07-28
- Verified against: pi.dev home page, docs overview, usage docs, Pi GitHub repository README
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low-Medium
- Recheck triggers:
  - core design-principles docs change
  - built-in tool surface changes
  - documentation changes around omitted built-ins

## Scope
- short product mental model for Pi
- what Pi includes directly in core versus what it expects from extensions or packages
- the main product surfaces that shape day-to-day use

## Canonical Boundary
This note is the branch mental model.

It is not the main home for:
- extension API details
- session format internals
- package-by-package ecosystem details
- general theories of skill systems, permissions, or sessions

## Why This Matters Here
- Pi is the candidate replacement harness being researched in this repository.
- A short mental model reduces re-learning before deeper branch notes.

## Current Findings
- Pi describes itself as a minimal terminal coding harness.
- Pi core includes interactive TUI usage, built-in file/shell tools, session persistence, compaction, provider/model selection, skills, prompt templates, themes, packages, and programmatic modes.
- Pi core explicitly does not include built-in MCP, sub-agents, permission popups, built-in plan mode, built-in to-dos, or built-in background bash.
- Pi expects users to shape behavior through TypeScript extensions, skills, prompt templates, themes, and Pi packages.
- The public Pi repository presents Pi as a multi-package agent toolkit rather than only a single CLI.

## Core Product Model

### 1. Minimal core runtime
Pi provides a terminal agent runtime with built-in tools, provider/model routing, slash commands, and session storage.

The top-level repository README describes the main repository packages as:
- `@earendil-works/pi-coding-agent` — interactive coding agent CLI
- `@earendil-works/pi-agent-core` — agent runtime with tool calling and state management
- `@earendil-works/pi-ai` — unified multi-provider LLM API
- `@earendil-works/pi-tui` — terminal UI library with differential rendering

### 2. Context loading
Pi loads context files and optional system prompt files from global and project locations.

### 3. Extension plane
Extensions can register tools, commands, providers, UI, event handlers, and context modifications.

### 4. Skill plane
Skills are on-demand capability packages discovered from standard locations and exposed to the model progressively.

### 5. Package plane
Pi packages bundle extensions, skills, prompt templates, and themes for installation from npm, git, or local paths.

### 6. Session plane
Sessions are tree-structured JSONL files with resume, branch navigation, compaction, and branch-summary behavior.

## Built-in Core Surfaces
- built-in tools: `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`
- built-in context-file loading from `AGENTS.md` and `CLAUDE.md`
- system-prompt replacement/append files
- model/provider selection and thinking-level control
- session save/resume/fork/clone/tree navigation
- compaction and branch summarization
- prompt templates, skills, themes, and packages
- RPC, JSON event-stream, and SDK/programmatic usage modes

## Explicitly Omitted Core Features
- built-in MCP
- built-in sub-agents
- built-in permission popups
- built-in plan mode
- built-in to-do tracking
- built-in background bash execution

## Windows-Specific Product Fact
- On Windows, Pi requires a bash shell.
- The documented lookup order is: custom `shellPath`, Git Bash at `C:\Program Files\Git\bin\bash.exe`, then `bash.exe` on PATH.

## Repository and Distribution Facts
- The public repository README points to RFCs at `https://rfc.earendil.com/keyword/pi/` for longer-term plans.
- The repository README documents standalone-binary builds from release source archives using pre-generated provider model data.
- The repository README documents supply-chain hardening measures including exact-version direct dependencies, `--ignore-scripts` install paths where supported, shrinkwrap generation for the published CLI package, and CI audit/signature checks.

## Relationships to Other Notes
- `research/products/pi/README.md`
- `research/products/pi/config-and-instruction-loading.md`
- `research/products/pi/extension-ecosystem-and-core-gaps.md`
- `research/products/pi/sessions-and-compaction.md`
- `research/products/pi/providers-and-programmatic-surfaces.md`
- `research/products/omp/foundations.md`
- `research/concepts/agent-architectures.md`
- `research/concepts/skill-systems.md`

## Repository Relevance
- This note is the shortest product-level re-entry point for the Pi branch.
- Notes that need to explain Pi-specific behavior can point here for the basic mental model, then narrow to their own topic.

## Adjacent Pi-Family Branch
- `research/products/omp/` tracks Oh My Pi (OMP) separately.
- Keep that branch separate from this one: OMP is relevant precisely because it appears to be a batteries-included Pi-family fork/product rather than baseline Pi core.
- Use this Pi note for the upstream minimal-core mental model.
- Use the OMP branch when the real question is whether a Pi-derived product already bundles capabilities that baseline Pi would otherwise recover through extensions or packages.

## Open Questions
- Which extension combinations are needed to reproduce the current local workflow surface being used in this repository?
- Which Pi package surfaces are stable enough to treat as durable building blocks versus fast-moving community add-ons?

## References
- [Pi home page](https://pi.dev/) — product overview and stated core omissions.
- [Pi documentation index](https://pi.dev/docs/latest) — current docs entry point.
- [Using Pi](https://pi.dev/docs/latest/usage) — built-in commands, tools, and usage surface.
- [Windows setup](https://pi.dev/docs/latest/windows) — Windows bash requirement.
- [Pi GitHub repository README](https://github.com/earendil-works/pi/blob/main/README.md) — repository package structure, containerization summary, and development/distribution facts.
