# Capabilities Research

This directory stores notes about medium-volatility capabilities: protocols, functional building blocks, and reusable engineering patterns.

## What Belongs Here
- MCP
- RAG
- tool calling
- model routing
- retrieval pipelines
- eval harnesses
- policy engines
- sessions
- context attachments

## What Does Not Belong Here
- Broad conceptual notes that should survive ecosystem churn unchanged. Put those in `../concepts/`.
- Product-specific behavior, config keys, or feature inventories. Put those in `../products/`.

## Recommended Questions
- What capability does this provide?
- What problem does it solve?
- What are common implementation patterns?
- What is portable across products?
- Which parts are evolving fastest?

## Freshness Guidance
- Stability: Medium
- Recheck when a major protocol, ecosystem, or best-practice shift appears.
- Call out which parts are durable versus likely to drift.

## Suggested Starter Notes
- `mcp.md`
- `context-attachments.md`
- `retrieval-pipelines.md`
- `model-routing.md`
- `sessions.md`
- `tool-calling.md`
- `eval-harnesses.md`
- `policy-engines.md`

## Working Rule
Capability notes should describe **cross-tool subsystems or facilities**, not broad architecture ideas.

- concepts explain the durable idea
- capabilities explain the reusable subsystem or mechanism
- products explain how one tool implements it today

If a filename sounds like a thesis statement or architecture essay, it probably belongs in `../concepts/` instead.
