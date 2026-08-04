# OMP Security and Trust

## Freshness
- Last verified: 2026-08-04
- Verified against: OMP GitHub repository README, OMP extensions docs, OMP porting-from-pi-mono doc, npm package page for `@oh-my-pi/pi-coding-agent`
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low
- Recheck triggers:
  - OMP security or install docs become more explicit
  - OMP extension architecture changes materially
  - OMP default-enabled tool set changes materially
  - OMP memory or collaboration features change materially

## Scope
- OMP's stated local execution and extension posture
- trust-relevant implications of its bundled feature surface
- product-facts view of what looks risky, gated, or still unverified

## Canonical Boundary
This note owns OMP's product-specific trust and local-boundary posture.

It is not the main home for:
- general permission-system theory
- full enterprise security review
- detailed Windows hardening instructions
- proof that every claimed behavior is enforced exactly as marketed

## Why This Matters Here
- A batteries-included coding agent can reduce assembly cost, but it can also widen the default local attack and side-effect surface.
- For this repository's environment, the important question is not only "what can OMP do?" but also "what does enabling that bundled surface imply on a locked-down local machine?"

## Current Findings
- OMP presents a much broader built-in local capability surface than baseline Pi research currently attributes to Pi core.
- OMP is extension-friendly and documents TS/JS extension modules, which implies arbitrary local code execution by extensions in the same broad sense as other plugin-style coding agents.
- OMP's README explicitly lists several powerful capabilities that are local-side-effect relevant, including shell/tool execution, persistent language runtimes, browser/desktop surfaces, GitHub tooling, memory tools, and collaboration features.
- Some OMP capabilities are described as off by default or setting-gated rather than always-on.
- OMP's public materials in this pass do not read like a sandbox-first product; they read like a powerful local agent surface with broad capability and customization.
- OMP claims cross-ecosystem ingestion of rules, skills, and MCP server definitions from other tool ecosystems, which is useful for migration but also expands the trust surface around imported local configuration and prompt assets.

## Trust-Relevant Product Model

### 1. Broad local agent surface
OMP's product pitch centers on shipping many capabilities directly in the product.

Trust implication:
- more built-in capability means less package assembly
- but it also means a larger default local execution and side-effect surface to evaluate

The current OMP materials point to a product that can do more immediately, not one that is primarily trying to minimize local power by default.

### 2. Extension code is part of the trust boundary
OMP documents an extension system built on TS/JS modules that can register tools, commands, handlers, renderers, and session/message behaviors.

Trust implication:
- extension code should be treated as trusted local code, not as inert configuration
- the product's openness and customizability increase power and flexibility, but they also widen the amount of logic that may influence execution

### 3. Imported ecosystem assets are convenient but high-trust
OMP claims it can inherit existing rules, skills, and MCP server definitions from several other agent-tool ecosystems already present on disk.

Trust implication:
- migration convenience is potentially strong
- but inherited prompt/config/tool definitions should be treated as executable influence, not just passive content
- this convenience feature is especially worth validating before relying on it in a corporate environment

### 4. Bundled feature breadth changes the review burden
Compared with baseline Pi's omission-heavy posture, OMP bundles more of the coding workflow directly.

Trust implication:
- evaluation shifts from "which packages do I install?" toward "which built-ins are enabled, gated, or safe enough to allow?"
- the main safety question becomes default posture, gating, and practical disablement, not only ecosystem package quality

## Concrete Risk-Relevant Product Facts

### Powerful built-in surfaces called out publicly
Official product materials describe or market capabilities including:
- many built-in tools
- persistent Python execution
- persistent JavaScript execution
- LSP integration
- debugger / DAP integration
- task or subagent support
- browser/web search surfaces
- desktop-control-related surfaces
- GitHub tooling
- memory tools
- collaboration/live session sharing

These are product facts, not a claim that every feature is equally mature or enabled by default.

### Gated or setting-dependent features
Official materials indicate that some capabilities are off by default or configuration-dependent, including examples such as:
- GitHub-related features
- security scanning
- image generation
- text-to-speech
- checkpoint / rewind features
- memory tooling depending on configured backend

This is a useful signal because it suggests OMP does have some concept of capability gating even if the current pass does not yet establish a full formal permission model.

### Fork divergence matters for trust assumptions
OMP includes a porting/divergence document and explicitly diverges from upstream Pi in areas including:
- tool architecture
- extension architecture
- auth storage
- UI architecture

Trust implication:
- baseline Pi trust findings are relevant context, but they should not be assumed to transfer unchanged
- OMP needs its own product branch and its own trust note

## What Is Still Unclear
- Whether OMP has a documented built-in runtime permission model comparable to allow/ask/deny policy systems, or whether safety primarily depends on settings, user judgment, and environment boundaries.
- Whether OMP documents a project-trust model analogous to Pi's load-time trust behavior.
- How collaboration, browser, desktop, memory, and imported-ecosystem features are enabled, restricted, or audited in practice.
- Which features work on Windows in a constrained corporate environment versus only in more permissive personal setups.
- Whether some marketed capabilities are wrappers around optional tools/services whose practical availability is narrower than the headline feature list suggests.

## Practical Repository Takeaway
- OMP currently looks more like a high-capability local coding workstation product than a minimal-core harness.
- That can be attractive for reducing assembly work.
- But for this repository's environment, it likely increases the need for careful review of:
  - default-enabled capabilities
  - Windows compatibility
  - local execution assumptions
  - imported-config trust
  - any external-service or collaboration behavior

So the right comparison is not just feature-count versus Pi.

It is:
- broader built-in surface and faster time-to-utility
versus
- broader default trust and side-effect surface to evaluate

## Relationships to Other Notes
- `research/products/omp/README.md`
- `research/products/omp/foundations.md`
- `research/products/pi/security-and-trust.md`
- `research/products/pi/foundations.md`
- `research/syntheses/pi-vs-omp-comparison.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/human-in-the-loop-control-points.md`

## Repository Relevance
- This note prevents OMP from being treated as purely a feature-bundle win without trust review.
- It also prevents baseline Pi trust conclusions from being copied over mechanically to a diverged fork.

## Open Questions
- Does OMP document a first-class permission or approval model, and if so, how strong is it?
- What are the exact enable/disable and audit surfaces for its more powerful built-ins?
- How much of OMP's claimed imported-ecosystem reuse is desirable versus risky in this repository's environment?
- Are collaboration or remote-style features easy to disable completely when not wanted?

## References
- [OMP GitHub repository README](https://github.com/can1357/oh-my-pi/blob/main/README.md) — bundled capabilities, install posture, extension openness, and gated-feature hints.
- [OMP extensions documentation](https://github.com/can1357/oh-my-pi/blob/main/docs/extensions.md) — extension registration surface and customization model.
- [Porting from pi-mono](https://github.com/can1357/oh-my-pi/blob/main/docs/porting-from-pi-mono.md) — explicit fork divergence affecting trust assumptions.
- [npm package page for `@oh-my-pi/pi-coding-agent`](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent) — package identity and configuration clues such as memory backend settings.
