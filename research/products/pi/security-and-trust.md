# Pi Security and Trust

## Freshness
- Last verified: 2026-07-28
- Verified against: Pi security docs, settings docs, usage docs, Pi GitHub repository README, Pi containerization doc
- Product version: current docs snapshot
- Stability: Medium for stated security model; Low for extension/package ecosystem specifics
- Recheck triggers:
  - project trust or sandbox docs change
  - package install behavior changes
  - permission-related extension examples change materially

## Scope
- Pi's stated local security model
- project trust boundaries
- what Pi does and does not treat as a security boundary

## Canonical Boundary
This note owns Pi's documented trust and local-boundary behavior.

It is not the main home for:
- third-party permission-extension policies
- general policy-engine concepts
- containerization details beyond their relation to Pi's stated model

## Why This Matters Here
- Local corporate use depends on whether behavior is built into core, delegated to extensions, or expected to come from OS/container boundaries.

## Current Findings
- Pi states that it runs with the permissions of the local user account.
- Pi states that project trust is not a sandbox.
- Pi states that built-in tools and extensions run with local user permissions.
- Pi expects real isolation to come from the operating system, VM, container, or sandbox boundary rather than an in-process permission boundary.
- Pi's repository README and containerization docs describe multiple containment patterns rather than presenting in-process permissions as the main security boundary.

## Project Trust Facts

Project trust controls loading of project-local:
- settings
- resources under `.pi`
- project packages
- project-local extensions

It does not restrict what the model can ask tools to do once the session is running in a directory.

Saved trust decisions are stored in `~/.pi/agent/trust.json`.

Global fallback behavior is controlled by `defaultProjectTrust` in global settings, with documented values:
- `ask`
- `always`
- `never`

## No Built-in Sandbox

Pi documents that it has no built-in sandbox.

Documented implications:
- built-in tools can read files, write files, edit files, and run shell commands with process permissions
- extensions run with the same permissions
- package installs, shell commands, language servers, and other developer tools behave as ordinary local processes

## Documented Risk Model

Pi docs explicitly treat these as expected local-agent risks rather than prevented classes:
- prompt injection from repository files, comments, docs, or output
- behavior of user-installed extensions or skills
- lack of a built-in sandbox

## Non-Interactive Trust Behavior

For `-p`, `--mode json`, and `--mode rpc`:
- no trust prompt is shown
- without a saved decision, `defaultProjectTrust` controls fallback behavior
- `--approve` and `--no-approve` can override trust for one run

## Documented Isolation Guidance

Pi docs point users to:
- containers
- VMs or micro-VMs
- remote sandboxes
- reduced mounts and reduced credentials
- restricted network access when not needed

Repository docs describe three concrete isolation patterns:
- Gondolin extension — keep Pi and provider auth on the host while routing built-in tools and `!` shell commands into a local Linux micro-VM
- Plain Docker — run the whole Pi process inside a local container
- OpenShell — run the whole Pi process inside a policy-controlled sandbox backed by a local or remote gateway

The containerization doc also states:
- extensions run wherever the Pi process runs
- if Pi runs on the host and tool execution is routed elsewhere, other extension tools still run on the host unless they also delegate their operations

## Extension and Package Security Facts

Pi docs state that:
- extensions can execute arbitrary code
- packages can execute code and influence agent behavior
- skills can instruct the model to perform actions and may include executable code the model invokes

Extension docs also state that:
- auto-discovered project-local extensions load only after project trust is established
- extensions supplied from global locations or CLI `-e` participate in the `project_trust` decision phase before project-local resources load

## Relationships to Other Notes
- `research/products/pi/foundations.md`
- `research/products/pi/extension-ecosystem-and-core-gaps.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/human-in-the-loop-control-points.md`

## Repository Relevance
- This note clarifies which trust and safety properties exist in Pi core versus which remain extension- or environment-level concerns.

## Open Questions
- Which extension-layer permission systems are needed to recreate current workflow gates inside Pi while staying consistent with Pi's documented trust model?

## References
- [Security](https://pi.dev/docs/latest/security) — Pi's documented local security model and non-sandbox stance.
- [Settings](https://pi.dev/docs/latest/settings) — `defaultProjectTrust` and trust-related settings.
- [Using Pi](https://pi.dev/docs/latest/usage) — project trust behavior during interactive and non-interactive use.
- [Pi GitHub repository README](https://github.com/earendil-works/pi/blob/main/README.md) — top-level security and containerization summary.
- [Containerization](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md) — documented host-versus-sandbox deployment patterns.
- [Extensions docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) — extension trust-loading behavior and arbitrary-code warning.
