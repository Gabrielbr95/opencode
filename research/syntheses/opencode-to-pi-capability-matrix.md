# opencode to Pi Capability Matrix

This note compares the currently documented `opencode` harness surface against the currently documented Pi surface.

Its purpose is descriptive:
- identify which capabilities are built into `opencode`
- identify which capabilities are built into Pi core versus pushed into Pi extensions/packages
- identify where current research still shows a gap or an unclear match

It is not a migration plan and it is not a recommendation note.

---

## Freshness
- Last verified: 2026-07-28
- Derived from:
  - `products/opencode/*` notes verified 2026-07-24
  - `products/pi/*` notes verified 2026-07-28
- Stability: Low
- Recheck triggers:
  - opencode config/agent/permission/MCP/session surfaces change
  - Pi core adds currently omitted features
  - key Pi replacement packages change materially

---

## Scope
- current documented product surfaces only
- product-level capability matching only
- no ranking of which route is better

## Canonical Boundary
This note is a synthesis-level comparison matrix.

It does not replace the product notes that own exact mechanics.

Use the product branches for details:
- `../products/opencode/README.md`
- `../products/pi/README.md`

---

## Status Legend
- **Built-in** — documented as part of the product core
- **Extension/package** — not core; documented replacement exists through Pi's extension/package surface
- **No direct documented match** — not found as a documented direct equivalent in current notes
- **Different shape** — both products have the capability category, but the implementation surface differs materially

---

## Capability Matrix

| Capability | opencode current surface | Pi current surface | Current Pi reproduction route in notes | Notes |
|---|---|---|---|---|
| Ambient context files | Built-in `AGENTS.md` loading plus configured instruction sources | Built-in `AGENTS.md` / `CLAUDE.md` loading | Pi core | Both products have always-on context-file loading. |
| System prompt file control | Built-in; instruction/config system includes prompt control and advanced prompt-surgery surfaces | Built-in `SYSTEM.md`, `APPEND_SYSTEM.md`, and CLI prompt flags | Pi core | Same category exists in both, but file names and loader shape differ. |
| Merged settings/config system | Built-in merged config system across multiple sources | Built-in global + project settings with resource arrays and trust gating | Pi core | Both products merge configuration from more than one place, but the surfaces are different. |
| Named agents / worker identities | Built-in named agents with prompt/model/mode/permission envelope | No built-in subagent system in core; packages can add delegated child-agent behavior | `pi-subagents` | Pi core has extensions and skills, but current notes do not show a built-in equivalent to opencode's named-agent harness layer. |
| Runtime permission gating | Built-in allow / ask / deny style permission system | No built-in permission popup/gating system in core | `@gotgenes/pi-permission-system` | This is one of the clearest opencode-core versus Pi-extension differences. |
| Skills | Built-in skill discovery and on-demand loading | Built-in skill discovery and on-demand loading | Pi core | Both products support skills as distinct from ambient instructions. |
| Prompt templates / reusable prompt shortcuts | Built-in commands plus configurable prompt-like surfaces | Built-in prompt templates | Pi core | Both products support reusable prompt-like resources, though the packaging model differs. |
| References / named external context roots | Built-in references to local directories or Git repos, addressable by alias | No direct named-reference surface documented in current Pi notes | No direct documented match; current evidence shows `@file` inclusion for specific files plus local/git package-source specs, but not opencode-style named alias roots | Current Pi evidence supports direct file inclusion and path/package specs, not a documented alias layer equivalent to opencode references. |
| External-directory boundary | Built-in `external_directory` permission boundary | No built-in equivalent in core; trust is not a sandbox | `@gotgenes/pi-permission-system` for policy layer | Pi project trust controls loading, not post-start tool authorization. |
| MCP integration | Built-in local and remote MCP config surface | Explicitly omitted from Pi core | `pi-mcp-adapter` | Current research shows a documented Pi replacement package, not a core feature. |
| Session persistence | Built-in real session model | Built-in tree-structured session model | Pi core | Both products have real session persistence rather than transient chat only. |
| Resume / interrupt / continue | Built-in interrupt/resume semantics | Built-in continue/resume/new/fork/clone/session-tree semantics | Pi core | Both support resumable work, though the user-facing model differs. |
| Compaction | Built-in configurable compaction | Built-in configurable compaction | Pi core | Both have compaction as a first-class session feature. |
| Branch summarization | Not explicitly documented in current opencode notes as a named branch-summary feature | Built-in branch summarization during tree navigation | Pi core | Pi currently has a more explicit documented branch-summary mechanism in the notes. |
| Undo / redo / filesystem rollback | Built-in revert/redo tied to snapshots and file-state recovery | No equivalent documented in current Pi core notes | `pi-rewind`, `pi-chrono`, `@ayulab/pi-rewind`, plus official git-checkpoint example | Current Pi research now shows multiple documented extension/package routes for rollback or rewind, but still not a core feature. |
| Built-in file/search/shell tools | Built-in file and shell tools | Built-in `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls` | Pi core | Broadly similar capability category exists in both. |
| Provider routing / model selection | Built-in provider routing and local/custom-provider support | Built-in provider/model support plus `models.json` and custom-provider extensions | Pi core + extension hooks | Both have strong provider/model surfaces. |
| Headless / programmatic use | Built-in session/runtime objects are documented in current opencode notes | Built-in print mode, JSON mode, RPC mode, SDK/programmatic surface | Pi core | Both have non-chat-only usage surfaces, but Pi's RPC/JSON modes are more explicit in current notes. |
| Todo / progress tracking | Current opencode notes do not identify a built-in todo system as a core product layer | Explicitly omitted from Pi core | `@juicesharp/rpiv-todo` | In current notes, Pi has a documented package route; opencode does not stand out here as having a dedicated built-in todo layer. |
| Plan mode / read-only planning lane | Built-in plan-style agent and planning-oriented permission difference are documented in opencode notes | Explicitly omitted from Pi core | `@narumitw/pi-plan-mode` | The surfaces are not identical, but both notes show a planning lane exists via core in opencode versus package in Pi. |
| Background / async delegated work | Not isolated as a distinct built-in capability in current opencode notes | Explicitly omitted from Pi core; package ecosystem documents background child runs | `pi-subagents` | Current evidence for Pi is package-level and specific to subagent delegation. |
| Persistent cross-session memory / searchable memory store | Current opencode notes do not show a first-class built-in semantic memory/retrieval stack | Not core; package route exists | `pi-hermes-memory` | Current notes show Pi has a documented extension path here, while opencode appears closer to sessions + references + deterministic file navigation. |
| Extension/plugin surface | Built-in plugins, commands, MCP, and related extension hooks | Built-in TypeScript extension system and installable packages | Pi core | Both are extensible, but Pi is more explicitly minimal-core-plus-extension in current notes. |

---

## Highest-Contrast Areas Seen in Current Research

### opencode-core vs Pi-package replacement surfaces
Current notes show the largest contrast in these areas:
- permission gating
- MCP
- subagent/delegation layer
- plan mode
- todo/progress overlay
- persistent searchable memory

In the current research set, these are core or near-core harness ideas in `opencode`, but are documented as omitted-from-core and recovered through packages in Pi.

### Areas where both products look strong in core
Current notes show both products having substantial built-in support for:
- context/instruction loading
- skills
- file/search/shell tooling
- sessions and compaction
- provider/model routing
- non-interactive/programmatic operation

### Areas with no clear direct one-to-one match yet
Current notes do not show a clean Pi equivalent for:
- opencode-style named references to external directories or Git roots

The remaining named-reference gap may still be reproducible in Pi, but the current research set does not document a direct product-level alias system.

---

## Non-Capability Constraints That Still Matter

These are not capability rows, but they materially affect comparison:

- Pi core explicitly has no built-in sandbox.
- Pi project trust is a load-time boundary, not a runtime action-authorization boundary.
- Pi on Windows requires a bash shell.
- Pi package replacements vary in maturity and volatility.

Current `opencode` notes point more directly to built-in permission and external-boundary controls, while current Pi notes point more directly to extension-layer control plus OS/container boundaries.

---

## Relationship to Other Notes
- `../products/opencode/foundations.md`
- `../products/opencode/config-and-instruction-loading.md`
- `../products/opencode/agents-permissions-and-skills-basics.md`
- `../products/opencode/permissions-and-agent-safety.md`
- `../products/opencode/references-and-external-context-basics.md`
- `../products/opencode/session-control-and-recovery.md`
- `../products/opencode/mcp-and-tooling.md`
- `../products/pi/foundations.md`
- `../products/pi/config-and-instruction-loading.md`
- `../products/pi/security-and-trust.md`
- `../products/pi/sessions-and-compaction.md`
- `../products/pi/providers-and-programmatic-surfaces.md`
- `../products/pi/extension-ecosystem-and-core-gaps.md`

---

## Open Questions
- Which opencode surfaces missing from Pi core are adequately covered by current Pi packages versus still requiring custom extension work?
- Which current Pi package replacements are stable enough to treat as medium-term building blocks?
- Is a custom reference/attachment extension needed to reproduce opencode-style named external context roots in Pi?
- Among the documented rewind/rollback packages, which one most closely matches opencode's revert/redo behavior and operational assumptions?
