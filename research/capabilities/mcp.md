# MCP

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - authorization patterns
  - transport/runtime ergonomics

## Summary
- MCP is a capability for exposing external tools, resources, and prompts from servers to AI clients through a standard protocol.
- The durable idea is capability extension through a structured boundary, not any one product's config syntax.
- MCP is more than extra context: it can expand both what the harness can read and what it can do.

## Motivation
- Product notes often need the same explanation of what MCP is before discussing product-specific config and safety.
- This note gives MCP a reusable home so product branches can stay focused on current implementation details.

## Problem Statement
- Systems need a standard way to connect AI clients to external tools and data without hard-coding every integration.
- That power also expands trust, auth, runtime, and observability concerns.

## Core Function
- Attach external servers that expose tools, resources, or prompts to a client.
- Expand capability surface without embedding every integration directly in the harness.

## Common Patterns
- local subprocess server
- remote service server
- read-heavy resource access
- tool/action exposure with auth and timeout controls
- progressive adoption from local to remote

## Typical Components
- MCP client
- MCP server
- transport/runtime boundary
- capability discovery
- auth and timeout handling
- tool/resource/prompt exposure

## Portability
- Portable across tools:
  - MCP is a cross-tool protocol capability
  - auth, timeout, and trust boundaries matter regardless of product
  - MCP is best treated as capability expansion, not as a casual convenience
- Product-shaped:
  - config syntax
  - discovery UX
  - how MCP instructions affect prompt surface
  - how permissions interact with MCP-derived tools

## Advantages
- reusable integration model across tools
- avoids one-off bespoke integrations
- can expose both data and actions through one protocol family

## Risks / Failure Modes
- enlarged attack and trust surface
- unclear auth handling
- runtime/process fragility
- prompt-surface growth from extra tool instructions
- treating remote MCP as if it were equivalent to local files

## Tradeoffs
- MCP is more extensible than plain references, but more operationally complex.
- Local MCP is easier to audit than remote MCP, but still adds process/runtime burden.
- Standardization improves interoperability, but not safety by itself.

## Relationships to Other Notes
- `../concepts/context-engineering.md`
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../products/opencode/mcp-and-tooling.md`
- `../products/opencode/references-and-external-context-basics.md`

## Practical Applications for This Repository
- Prefer references or simpler local mechanisms before adopting MCP.
- If MCP is justified, start with one concrete local use case.
- Treat auth, timeout, and prompt-surface cost as first-class design concerns.

## Open Questions
- Which actual tasks in this workflow justify MCP over references or local scripts?
- What is the smallest auditable MCP footprint that still provides value here?

## References
- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro) — MCP documentation, intro to the protocol and its purpose.
- [Architecture overview (MCP)](https://modelcontextprotocol.io/docs/learn/architecture) — MCP documentation, client/server/tool/resource framing.
- `../products/opencode/mcp-and-tooling.md` — concrete product implementation and adoption cautions for this repository.
