# OMP Research

This branch stores product-specific research notes about Oh My Pi (OMP).

## Branch Role

This directory is for current OMP behavior, bundled product surfaces, and fork-specific architecture choices.

Use it to answer:
- what OMP is as a product in the Pi family
- how OMP differs from baseline Pi's minimal-core stance
- which capabilities OMP bundles directly versus leaving to extensions or external tooling
- which current OMP details matter for evaluating it as a candidate local harness

For cross-tool explanations, defer to:
- `../../concepts/`
- `../../capabilities/`
- `../../syntheses/`

## Reading Order
1. `foundations.md`
2. `security-and-trust.md`
3. `architecture-and-divergence.md`

## Canonical Bridges Upward
- agent architectures -> `../../concepts/agent-architectures.md`
- skill systems -> `../../concepts/skill-systems.md`
- tool-use policy and permission systems -> `../../concepts/tool-use-policy-and-permission-systems.md`
- MCP -> `../../capabilities/mcp.md`
- tool calling -> `../../capabilities/tool-calling.md`
- sessions -> `../../capabilities/sessions.md`
- model routing -> `../../capabilities/model-routing.md`
- Pi vs OMP comparison -> `../../syntheses/pi-vs-omp-comparison.md`
- OMP reachability -> `../../syntheses/omp-reachability-matrix.md`
- vocabulary -> `../../syntheses/vocabulary.md`

## Freshness
- Last verified: 2026-08-04
- Verified against: omp.sh, OMP GitHub repository README/docs, npm package page for `@oh-my-pi/pi-coding-agent`
- Stability: Low
- Recheck triggers:
  - OMP README or docs change materially
  - bundled tool surface changes materially
  - fork relationship to upstream Pi changes materially
