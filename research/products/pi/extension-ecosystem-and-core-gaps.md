# Pi Extension Ecosystem and Core Gaps

## Freshness
- Last verified: 2026-07-28
- Verified against: Pi extensions docs, Pi package docs, Pi package catalog, selected package pages, Pi GitHub repository/docs, selected package READMEs, selected extension-example listings
- Product version: current docs snapshot; package versions captured as of verification date
- Stability: Low
- Recheck triggers:
  - package catalog changes materially
  - extension API changes
  - major package version or ownership changes in key replacement surfaces

## Scope
- what Pi core leaves out and exposes through extensions/packages
- which documented extension seams exist in core
- selected package examples relevant to replacing common harness features

## Canonical Boundary
This note owns the product-specific extension/package landscape around Pi core gaps.

It is not the main home for:
- general MCP, permission, or subagent theory
- repository decisions about which packages to adopt

## Why This Matters Here
- The candidate migration target is not Pi core alone; it is Pi core plus add-ons that reproduce needed harness behavior.

## Current Findings
- Pi's docs and home page present the missing-core features as extension/package targets rather than planned built-ins.
- Pi's extension API covers tools, commands, lifecycle events, context mutation, provider overrides, UI, and session hooks.
- The public package catalog is large and fast-moving; the catalog page showed 5,418 packages at verification time.
- Pi's official examples directory listed extension examples for permission gates, subagent behavior, plan mode, sandboxing, MCP-adjacent patterns, custom compaction, and to-do tooling.
- The extension docs explicitly state that auto-discovered extensions in standard locations can be hot-reloaded with `/reload`.
- The extension docs show that extension state meant to survive branching should be reconstructed from session entries or tool-result details rather than only in-memory state.

## Documented Extension Capabilities

Pi docs state that extensions can:
- register custom tools
- intercept tool calls and results
- block or modify behavior at runtime
- register commands and shortcuts
- inject or filter context
- customize compaction and session behavior
- register custom providers
- add custom UI and rendering
- persist state via session entries

## Core-Omission to Ecosystem Mapping

Documented core omissions on the Pi home/usage pages include:
- MCP
- sub-agents
- permission popups
- plan mode
- built-in to-dos
- background bash

The docs and package catalog show corresponding extension/package examples for several of these categories.

## Selected Package Examples Relevant to Core-Gap Replacement

### MCP adapter
- Package: `pi-mcp-adapter`
- Package page version at verification: `2.15.0`
- Package page type: extension
- Stated purpose: MCP adapter extension for Pi
- Documented behavior includes lazy server connection, config layering, proxy-tool access, optional direct-tool registration, auth flows, and UI integration.

### Subagents
- Package: `pi-subagents`
- Package page version at verification: `0.37.2`
- Package page types: extension, skill, prompt
- Stated purpose: delegating tasks to subagents with chains, parallel execution, and clarification support.
- GitHub README describes bundled builtin roles including `scout`, `researcher`, `planner`, `worker`, `reviewer`, `context-builder`, `oracle`, and `delegate`.
- GitHub README documents both natural-language triggering and direct slash-command workflows such as `/run`, `/chain`, `/parallel`, and saved chains.
- GitHub README documents background runs, async status inspection, lifecycle artifacts, nested-run visibility, and an in-process RPC/event-bus surface for other extensions.
- GitHub README documents a recursion/depth guard and child-safety behavior that withholds subagent capability from children unless explicitly allowed.
- GitHub README documents native supervisor coordination tools for child-to-parent questions without requiring a separate intercom package.

### Permission system
- Package: `@gotgenes/pi-permission-system`
- Package page version at verification: `24.0.0`
- Package page type: extension
- Stated purpose: centralized permission enforcement over tools, bash, MCP, skills, and special operations.
- GitHub README states it hides disallowed tools before agent start, enforces `allow` / `ask` / `deny` at runtime, and applies cross-cutting path rules plus an `external_directory` boundary.
- GitHub README states it fails closed on internal gate errors and on unparseable bash commands.
- GitHub README states project-scoped permission config loads only after project trust, so an untrusted repository cannot loosen global policy through project config.
- GitHub README documents native integration with subagent extensions by forwarding `ask` prompts from child processes to the parent session UI.

### Todo tracking
- Package: `@juicesharp/rpiv-todo`
- Package page version at verification: `2.1.0`
- Package page type: extension
- Stated purpose: todo list tool plus live overlay that survives reload and compaction.
- Current README location is in the `juicesharp/rpiv-mono` monorepo; the older standalone repo is archived/read-only.
- Monorepo README states the extension adds a `todo` tool, `/todos` command, and a live panel above the editor.
- Monorepo README states the list is rebuilt from conversation state, survives `/reload` and compaction, supports `blockedBy` dependency validation, and keeps task state separated by session.
- Monorepo README documents optional config at `~/.config/rpiv-todo/config.json` for overlay size, collapse keybinding, and guidance text.

### Plan mode
- Package: `@narumitw/pi-plan-mode`
- Package page version at verification: `0.35.0`
- Package page type: extension
- Stated purpose: Codex-like read-only `/plan` mode with structured completion flow.
- Package page README states the package also adds `--plan` for starting a session in plan mode.
- Package page README states plan mode enables built-in read-only tools by default, disables extension/custom tools by default, and adds a `/plan tools` selector for explicit opt-in.
- Package page README states it blocks mutating built-in tools, `update_plan`, and unsafe `bash` forms including writes, substitutions, background jobs, dependency installs, and mutating Git commands.
- Package page README states plan completion is carried through required `plan_mode_question` and `plan_mode_complete` tools, persists in the Pi session, and can later transition into implementation with restored full tool access.
- Package page README states the package requires Pi `0.80.6` or newer.

### Persistent memory
- Package: `pi-hermes-memory`
- Package page version at verification: `0.9.1`
- Package page type: extension
- Stated purpose: persistent memory, session search, secret scanning, and procedural skill capture.
- Package page README states the extension uses SQLite FTS5 for session/history search and mirrors successful Markdown memory writes into SQLite-backed search.
- Package page README states default behavior is token-aware policy-only memory rather than always injecting full memory into the prompt.
- Package page README states it stores global memory under `~/.pi/agent/pi-hermes-memory/` and project-scoped memory under `~/.pi/agent/projects-memory/<project>/`.
- Package page README states it manages Pi-native skills under `skills/<slug>/SKILL.md`, includes migration logic for older skill layouts, and exposes memory/session-search/skill-management commands.
- Package page README states `better-sqlite3` is a native addon and documents rebuild steps for Node ABI mismatches.

### Rollback / rewind
- Package: `pi-rewind`
- Package page version at verification: `0.5.0`
- Package page type: extension
- Stated purpose: checkpoint/rewind extension with per-tool snapshots, `/rewind`, diff preview, safe restore, and redo stack.
- Package page README states it uses automatic git-based snapshots of the working tree, supports files-plus-conversation restore modes, and includes redo behavior.

- Package: `pi-chrono`
- Package page version at verification: `0.3.2`
- Package page type: extension
- Stated purpose: session rollback extension that restores workspace and session context.
- Package page README states it captures file states before each AI turn, tracks file operations in journals, supports `/chrono`, rollback preview, session forking, and workspace restoration.

- Package: `@ayulab/pi-rewind`
- Package page version at verification: `0.4.6`
- Package page type: extension
- Stated purpose: `/rewind` checkpoint navigation.
- Package page README states it supports interactive checkpoint lists, restore-code / restore-conversation / restore-both modes, tree-navigation file-state sync options, and fork/clone-aware checkpoint restore behavior.

## Package-System Facts

Pi packages can be installed from:
- npm
- git
- local paths

Packages can bundle:
- extensions
- skills
- prompt templates
- themes

The package catalog page exposes metadata such as:
- package type
- version
- publish date
- download counts
- repo/home links when available

Extension docs additionally state:
- packages can declare extension entry points through a `pi` manifest in `package.json`
- distributed package installs use production dependencies by default (`npm install --omit=dev`), so runtime dependencies must live in `dependencies`

## Official Example Coverage

The Pi examples listing included example files/directories for:
- `permission-gate.ts`
- `protected-paths.ts`
- `plan-mode/`
- `subagent/`
- `todo.ts`
- `custom-compaction.ts`
- `sandbox/`
- `gondolin/`
- `custom-provider-*`

The extension docs also include example patterns for:
- git-checkpoint-based code restoration across forks
- state reconstruction from tool-result details during session branching
- custom project-trust decisions from global/CLI extensions before project-local resources load

## Relationships to Other Notes
- `research/products/pi/foundations.md`
- `research/products/pi/security-and-trust.md`
- `research/products/pi/providers-and-programmatic-surfaces.md`
- `research/capabilities/mcp.md`
- `research/capabilities/policy-engines.md`

## Repository Relevance
- This note records which missing-core surfaces currently have documented extension or package implementations in the Pi ecosystem.

## Open Questions
- Which current package surfaces are sufficient to recreate the present harness behavior without custom extension work?
- Which current package categories remain too volatile to treat as durable research inputs without local source review?
- Which package READMEs and repository docs stay aligned with their package-catalog snapshots over time, and which ones need direct source re-verification before any migration work?
- Is there any clearly documented Pi package that reproduces opencode-style named external-context aliases rather than only file inclusion, filesystem paths, or package-source specs?

## References
- [Extensions](https://pi.dev/docs/latest/extensions) — extension API and lifecycle surface.
- [Pi Packages](https://pi.dev/docs/latest/packages) — package installation and manifests.
- [Package catalog](https://pi.dev/packages) — current ecosystem listing.
- [pi-mcp-adapter package page](https://pi.dev/packages/pi-mcp-adapter) — MCP adapter package metadata and README snapshot.
- [pi-subagents package page](https://pi.dev/packages/pi-subagents) — subagent package metadata and README snapshot.
- [@gotgenes/pi-permission-system package page](https://pi.dev/packages/@gotgenes/pi-permission-system) — permission package metadata and README snapshot.
- [@juicesharp/rpiv-todo package page](https://pi.dev/packages/@juicesharp/rpiv-todo) — todo package metadata and README snapshot.
- [@narumitw/pi-plan-mode package page](https://pi.dev/packages/@narumitw/pi-plan-mode) — plan-mode package metadata and README snapshot.
- [pi-hermes-memory package page](https://pi.dev/packages/pi-hermes-memory) — memory package metadata and README snapshot.
- [pi-rewind package page](https://pi.dev/packages/pi-rewind) — rewind/redo package metadata and README snapshot.
- [pi-chrono package page](https://pi.dev/packages/pi-chrono) — rollback package metadata and README snapshot.
- [@ayulab/pi-rewind package page](https://pi.dev/packages/@ayulab/pi-rewind) — checkpoint-navigation package metadata and README snapshot.
- [Pi extension examples listing](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions) — official examples directory listing.
- [Pi extensions docs in repository](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md) — deeper extension semantics, events, and example patterns.
- [Pi GitHub repository README](https://github.com/earendil-works/pi/blob/main/README.md) — top-level ecosystem framing and containment patterns.
- [pi-subagents README](https://github.com/nicobailon/pi-subagents/blob/main/README.md) — package-specific roles, workflows, and status surfaces.
- [@gotgenes/pi-permission-system README](https://github.com/gotgenes/pi-packages/tree/main/packages/pi-permission-system) — package-specific policy surface and trust-loading behavior.
- [@juicesharp/rpiv-todo README](https://github.com/juicesharp/rpiv-mono/tree/main/packages/rpiv-todo) — current monorepo README for todo overlay behavior.
