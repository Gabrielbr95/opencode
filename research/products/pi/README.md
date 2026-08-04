# Pi Research

This branch stores product-specific research notes about Pi.

## Branch Role

This directory is for current Pi behavior, package surfaces, and extension seams.

Use it to answer:
- how Pi structures its minimal core
- which built-in versus extension-based surfaces exist today
- which current product and package details matter for reproducing harness behavior

For cross-tool explanations, defer to:
- `../../concepts/`
- `../../capabilities/`
- `../../syntheses/`

## Reading Order
1. `foundations.md`
2. `config-and-instruction-loading.md`
3. `security-and-trust.md`
4. `sessions-and-compaction.md`
5. `providers-and-programmatic-surfaces.md`
6. `extension-ecosystem-and-core-gaps.md`

## Canonical Bridges Upward
- instruction theory -> `../../concepts/instruction-layering.md`
- prompt-repo structure -> `../../concepts/prompt-modularity-repository-architecture.md`
- sessions -> `../../capabilities/sessions.md`
- policy and permission systems -> `../../concepts/tool-use-policy-and-permission-systems.md`
- MCP -> `../../capabilities/mcp.md`
- tool calling -> `../../capabilities/tool-calling.md`
- model routing -> `../../capabilities/model-routing.md`
- vocabulary -> `../../syntheses/vocabulary.md`

## Freshness
- Last verified: 2026-07-28
- Verified against: pi.dev docs/pages, Pi package catalog, Pi GitHub repository README/docs, selected raw GitHub docs, selected package READMEs, selected GitHub example listings
- Stability: Low
- Recheck triggers:
  - core docs or package docs change materially
  - extension API or trust model changes
  - package ecosystem shifts for core replacement surfaces
