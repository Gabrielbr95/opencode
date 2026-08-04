# OMP Foundations

## Freshness
- Last verified: 2026-08-04
- Verified against: omp.sh home page/install entry, OMP GitHub repository README, OMP extensions docs, OMP porting-from-pi-mono doc, npm package page for `@oh-my-pi/pi-coding-agent`
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low-Medium
- Recheck triggers:
  - OMP README philosophy or bundled-feature claims change
  - OMP extension architecture docs change
  - OMP install/distribution surfaces change
  - OMP upstream-fork relationship changes materially

## Scope
- short product mental model for OMP
- what OMP claims to bundle directly into the product surface
- how OMP relates to baseline Pi as a forked, batteries-included variant
- what that means for local harness evaluation in this repository

## Canonical Boundary
This note is the branch mental model.

It is not the main home for:
- package-by-package ecosystem analysis
- deep security validation beyond stated product posture
- general theories of skill systems, subagents, permissions, or sessions
- full Pi-vs-OMP comparison matrices

## Why This Matters Here
- Pi research in this repository currently treats Pi as a minimal core that expects significant extension/package assembly.
- OMP appears to be a Pi-family product with a different stance: ship a much fatter default surface instead of leaving as much as possible out of core.
- That makes OMP relevant as a separate candidate harness, not just as a single Pi package.

## Current Findings
- OMP positions itself as "Pi with batteries included" and "the Pi you love, with batteries included."
- OMP is explicitly a fork of upstream Pi (`pi-mono`).
- OMP presents itself as an AI coding agent for the terminal / a coding agent with the IDE wired in.
- OMP bundles a much broader built-in capability surface than baseline Pi research currently attributes to Pi core.
- OMP remains extension-friendly, but its product philosophy is not "minimal core first" in the same way Pi's public positioning is.
- OMP is distributed as a user-facing CLI product with multiple install paths, including direct installers, Homebrew, Bun, and mise.

## Core Product Model

### 1. Pi-family fork with a different default posture
OMP is not merely a package inside the Pi ecosystem. Its official materials describe it as a fork of Pi with an intentionally more complete out-of-the-box experience.

In repository terms:
- Pi research answers: what does the minimal upstream platform provide, and what must be assembled?
- OMP research answers: what does a Pi-derived batteries-included distribution/fork provide directly?

### 2. Bundled coding-workflow surface
OMP's README presents a broad built-in surface including:
- many built-in tools
- persistent Python and JavaScript execution
- LSP integration
- debugger / DAP integration
- task or subagent support
- web search
- GitHub-oriented tooling
- memory-related tooling
- collaboration / live session sharing

This is materially different from baseline Pi's documented omission-heavy core posture.

### 3. Open extension plane
OMP still documents an extension system based on TS/JS modules.

Official docs describe extensions that can register:
- tools
- slash commands
- event handlers
- keyboard shortcuts or flags
- renderers or UI surfaces
- session/message injection behavior

So the product is not closed or monolithic; it is just more bundled by default.

### 4. Multi-surface runtime
OMP's README describes multiple ways to drive the same engine:
- interactive TUI
- one-shot CLI
- RPC mode
- ACP mode

That makes it relevant not only as an interactive terminal agent but also as a possible automation or integration surface.

### 5. Cross-ecosystem ingestion posture
OMP claims it can inherit existing rules, skills, and MCP server definitions from several other coding-agent ecosystems on disk.

If accurate in practice, this is an important product behavior because it shifts migration effort from "rebuild everything natively" toward "reuse existing local prompt/config assets where possible."

## Repository-Relevant Product Facts

### Product identity
- Website: `https://omp.sh`
- Main repository: `https://github.com/can1357/oh-my-pi`
- CLI/package identity: `@oh-my-pi/pi-coding-agent`
- User-facing command: `omp`

### Relationship to Pi
- OMP explicitly describes itself as a fork of Pi / `pi-mono`.
- OMP includes a dedicated porting/divergence document rather than presenting itself as a thin skin over unchanged upstream behavior.

### Installation and distribution
Documented install/distribution paths include:
- shell installer from `omp.sh`
- PowerShell installer from `omp.sh`
- Homebrew tap install
- global Bun install
- mise install

### Architecture signals
- OMP describes itself as "open all the way down."
- A porting doc indicates intentional divergence from upstream in areas such as tool architecture, extension architecture, auth storage, and UI architecture.
- The porting doc also describes a capability-based discovery system as part of OMP's native direction.

## Key Difference from Baseline Pi Research
The most important local conclusion from this pass is:

- **Pi** should still be treated as a minimal-core platform plus ecosystem research target.
- **OMP** should be treated as a separate product research target in the Pi family, because its default product surface and philosophy are different enough to affect migration and evaluation decisions.

In other words, "Can Pi do this with packages?" and "Does OMP already ship this?" are related but distinct questions.

## Relationships to Other Notes
- `research/products/omp/README.md`
- `research/products/pi/foundations.md`
- `research/products/pi/extension-ecosystem-and-core-gaps.md`
- `research/products/pi/providers-and-programmatic-surfaces.md`
- `research/products/pi/security-and-trust.md`
- `research/concepts/agent-architectures.md`
- `research/concepts/skill-systems.md`

## Repository Relevance
- This note establishes OMP as a separate product branch worth tracking directly.
- It prevents OMP from being collapsed into either "just Pi" or "just another Pi extension/package."
- It gives a short re-entry point for later work such as Pi-vs-OMP comparison, trust review, migration fit analysis, or bundled-feature validation.

## Open Questions
- Which OMP bundled capabilities are genuinely built-in and stable versus present but gated, optional, or immature?
- How much of OMP's marketed batteries-included surface is safe and practical on a locked-down corporate Windows laptop?
- What is OMP's trust and security posture relative to baseline Pi's documented non-sandbox model?
- Which current local workflow assets in this repository could actually be reused through OMP's claimed cross-ecosystem ingestion behavior?
- Is OMP best understood as a candidate replacement harness, a research source for good bundled defaults, or both?

## References
- [OMP website](https://omp.sh) — official homepage and install entrypoint.
- [OMP GitHub repository README](https://github.com/can1357/oh-my-pi/blob/main/README.md) — product positioning, bundled capabilities, install methods, and runtime surfaces.
- [OMP extensions documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/extensions.md) — extension registration surface and customization model.
- [Porting from pi-mono](https://github.com/can1357/oh-my-pi/blob/main/docs/porting-from-pi-mono.md) — explicit divergence from upstream Pi and native architectural direction.
- [npm package page for `@oh-my-pi/pi-coding-agent`](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent) — package identity and additional distribution/config clues.
