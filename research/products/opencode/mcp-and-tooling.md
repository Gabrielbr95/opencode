# opencode: MCP and Tooling

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, source excerpts, v2 spec excerpts
- Product version: current docs/source snapshot plus spec direction; exact installed local version not verified
- Stability: Low-Medium
- Recheck triggers:
  - MCP config changes
  - auth or timeout behavior changes
  - local behavior differs from docs

## Scope
- what MCP appears to add to opencode
- what MCP config surfaces appear present
- how MCP-derived tools enter the harness today

## Canonical Boundary
This note is for **how opencode implements MCP today**.

For the cross-tool capability itself, see:
- `research/capabilities/mcp.md`

For the lighter-weight external context pattern, see:
- `research/capabilities/context-attachments.md`

## Why This Matters Here
- MCP is one of opencode's strongest extension points.
- In this branch, the main value of the note is to record what product surfaces actually exist, not to restate general MCP theory.

## Current Findings
- opencode appears to support both local and remote MCP servers.
- MCP servers can be configured with command arrays, environment variables, URLs, headers, OAuth details, and timeout settings.
- MCP tools are collected from connected servers and exposed into the harness tool surface.
- MCP-related prompt material appears to contribute to the assembled system prompt.

## Observed MCP Shapes

### Local MCP
Appears to support:
- `type: "local"`
- command array
- optional cwd
- environment variables
- timeout behavior

### Remote MCP
Appears to support:
- `type: "remote"`
- URL
- headers
- optional OAuth/auth details
- timeout behavior

## Product Boundary Seen Here
- references expand bounded context roots
- MCP expands tool and service integration surfaces
- permissions still decide what actually executes
- MCP-related instructions can increase prompt surface as well as action surface

## Local-First / Corporate Relevance
- remote MCP is an explicit network and credential boundary
- local MCP still introduces process/runtime overhead even when data stays local
- auth, headers, and timeouts are part of the product surface that matter in this environment

## Relationships to Other Notes
- `research/capabilities/mcp.md`
- `research/capabilities/context-attachments.md`
- `research/products/opencode/references-and-external-context-basics.md`
- `research/products/opencode/permissions-and-agent-safety.md`
- `research/products/opencode/system-prompt-control.md`

## Relevance to This Repository
- This note is the product-level home for current MCP surface facts in opencode.
- Broader adoption posture, trust hierarchy, or local-vs-remote recommendations should defer to higher-level notes.

## Open Questions
- Which MCP servers are realistic in this environment?
- Which current tasks would justify MCP rather than simpler local mechanisms?
- How much operational overhead does the product surface imply in daily use?

## References
- Context7 `/anomalyco/opencode` — MCP config, source, and spec excerpts.
