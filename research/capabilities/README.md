# Capabilities Research

This directory stores notes about medium-volatility capabilities: protocols, functional building blocks, and reusable engineering patterns.

## What Belongs Here
- MCP
- RAG
- tool calling
- model routing
- retrieval pipelines
- eval harnesses

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
- `rag.md`
- `tool-calling.md`
- `model-routing.md`
