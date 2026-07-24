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
- What MCP appears to add to opencode
- How MCP fits into the harness relative to references, permissions, and other control layers
- Why MCP should be adopted cautiously in this environment

## Canonical Boundary
This note is for **how opencode implements MCP today**.

For the cross-tool capability itself, see:
- `research/capabilities/mcp.md`

For the lighter-weight external context pattern that often comes first, see:
- `research/capabilities/context-attachments.md`

## Why This Matters Here
- MCP is one of the most powerful expansion points in opencode.
- It can greatly expand what the harness can see and do.
- That also makes it one of the more consequential advanced features for a local-first corporate setup.

## Current Findings
- opencode appears to support both local and remote MCP servers.
- MCP servers can be configured with:
  - command arrays
  - environment variables
  - URLs
  - headers
  - OAuth details
  - timeout settings
- MCP tools are collected from connected servers and exposed into the harness tool surface.
- MCP is therefore not just “extra context”; it is a tool-extension mechanism.

## What MCP Appears To Add
At a practical level, MCP adds external tool and service integration to the harness.

Examples include:
- local MCP servers run as processes
- remote MCP servers accessed over URLs
- tool definitions discovered from those servers and converted into usable tool entries

Practical takeaway:
- MCP changes the action surface of opencode, not just the reading surface

## Local vs Remote MCP

### Local MCP
Appears to be configured with:
- `type: "local"`
- command array
- optional cwd
- environment variables
- timeout behavior

Practical interpretation:
- local MCP is still an execution boundary
- but it is easier to inspect than a remote service

### Remote MCP
Appears to be configured with:
- `type: "remote"`
- URL
- headers
- optional OAuth/auth details
- timeout behavior

Practical interpretation:
- remote MCP introduces network, credential, and service-trust concerns

## Relationship to the Rest of the Harness

### References
References provide named external context roots.
MCP provides external tools/services.

### Permissions
Permissions bound what the harness can do.
MCP expands what there is to do.

### System prompt surface
MCP instructions appear to contribute to the assembled system prompt.

Practical takeaway:
- MCP can increase both capability and prompt surface area

## Why MCP Should Not Be the First External Layer
For this repository, references are the better first step because they are:
- simpler
- easier to inspect
- easier to reason about after a long gap

MCP should come later because it adds:
- process/runtime management
- timeout concerns
- auth concerns
- more moving parts

## Practical Adoption Order
Recommended order for this environment:

1. current repo files
2. local references
3. local-first provider clarity
4. permission discipline
5. local MCP only if a concrete need appears
6. remote MCP only with a strong justification

## Local-First / Corporate Notes
- Remote MCP is an explicit network boundary decision.
- OAuth, headers, and tokens deserve the same scrutiny as provider credentials.
- Local MCP may still depend on tools like `npx` or other runtimes that are awkward on locked-down Windows setups.
- Timeout and process-management behavior matter more than they first appear.

## Practical Guidance for This Repository

### Start with one concrete use case
Do not adopt MCP because it sounds powerful.

### Prefer local before remote
If the use case can be satisfied by a local process, that is usually easier to audit.

### Keep timeout and auth explicit
MCP is easier to maintain when the operational details are obvious.

### Remember prompt cost too
MCP is not only a capability decision; it can also enlarge the prompt surface.

## What Still Needs Practical Verification
- Which MCP servers are realistic on this machine and environment.
- Whether the operational overhead is worth the gain for this workflow.
- Which MCP uses would beat simpler references or local scripts.

## Relationship to Other Notes
- `research/capabilities/mcp.md`
- `research/capabilities/context-attachments.md`
- `research/products/opencode/references-and-external-context-basics.md`
- `research/products/opencode/permissions-and-agent-safety.md`
- `research/products/opencode/system-prompt-control.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`

## Open Questions
- Which concrete tasks here would actually justify MCP?
- Which local MCP servers would fit this environment best?
- At what point does MCP complexity exceed the benefit compared with simpler local tools?

## References
- Context7 `/anomalyco/opencode` — MCP config, source, and spec excerpts.
