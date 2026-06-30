# Session 6 — Harness Design: Current State

## Context

Greenfield repo. Goal: build a coding harness for agentic tools (OpenCode primary, others possible later).
Not just a tool setup — a *harness*: the scaffolding that makes agents work reliably and consistently for your situation.

Working directory: `opencode_v5/` (clean slate, separate from existing `~/.config/opencode/`).

---

## Non-Negotiables

- No phone-home MCP servers (per-case exceptions allowed)
- Corporate data stays local or through approved Claude API only
- Works on corporate Windows without admin (npm/pip user-level OK)
- Platform-agnostic — harness must survive a tool switch
- Portable — git-synced home, manual-copy work (GitHub restricted at work)

---

## Architecture Decision: Tool-Agnostic Core

The harness is designed to survive a tool switch. OpenCode is a consumer of it, not the foundation.

Structure: tool-agnostic core (AGENTS.md + MCP config + rules) with a thin OpenCode adapter layer on top. If you move to Cursor/Cline/other in future, 80% survives unchanged.

---

## Harness Layers

### 1. Identity Layer (tool-agnostic)

- **`AGENTS.md`** (global) — compact. Who you are, universal rules, tier system, core behavior. Short and stable. *Not* a knowledge dump.
- **`my-context.md`** — kept separate, invoked manually when needed. Not auto-loaded.
- **Project-level `AGENTS.md`** — exception, not the rule. Use only when a project has genuinely different rules.

Rule: if removing something from AGENTS.md wouldn't cause a mistake on a typical session, cut it.

### 2. MCP Stack (local only, no phone-home)

Baseline three:
- `@modelcontextprotocol/server-filesystem` — file read/write (Node, local)
- `@modelcontextprotocol/server-git` — git operations
- `mcp-server-fetch` — web fetch (no telemetry)

Corporate-specific (SAP, PDF workflows): custom Python MCP, built when a concrete target exists. Not V1.

Configured once in a shared `mcp.json`; each tool adapter points at it.

### 3. Rules Layer

Scoped markdown files:
- `rules/global.md` — universal coding standards
- `rules/work.md` — compliance, data-locality reminders
- `rules/python.md` — Python conventions

### 4. Skills Layer

Reusable workflows loaded on demand. Current skills are disposable — ideas are worth keeping, files are not. Will be redesigned.
Key distinction: skills are recipes (protocols the generalist follows), not actors.

### 5. Hooks (safety rails)

Minimal:
- Block destructive commands (`rm -rf` variants)
- Require confirmation before git push to remote
- Audit log for work sessions (all tool calls)

### 6. Sync

- Home: git repo, push/pull freely
- Work: flattened export folder (`harness-work/`) — AGENTS.md, mcp.json, rules/ — updated manually when needed

---

## Tier System

Stated by you at session start. If not stated, agent infers and confirms before acting.

| Tier | Purpose | Plan format | Autonomy |
|---|---|---|---|
| **Jerryrig** | One-off, throwaway | None | Direct action |
| **POC** | Feasibility only, disposable code | In-chat, quick approval | After approval |
| **Script** | Recurring personal automation, YAGNI | Written plan file | After approval |
| **Application** | Small-team, long-lived | Spec + tasks file, you edit | After approval, pause on uncertainty |

Tier drives: plan rigor, working mode, definition of done.

---

## Working Modes

Three modes on a spectrum, fluid and switchable mid-session:

1. **Direct edit** — no ceremony, agent acts immediately (jerryrig default)
2. **Human-in-the-loop** (default for script/application) — explore → plan → you approve → execute with checkpoints
3. **Autonomous** — after plan approval, runs to completion; pauses only on genuine uncertainty

Hard limits always apply in autonomous mode: restricted scope, no remote git push, no silent deletes.

---

## Memory & Planning Artifacts

### Memory layers

| Layer | File | Owner | Purpose |
|---|---|---|---|
| Global identity | `AGENTS.md` (global) | You | Who you are, how you work — always loaded |
| Project context | `AGENTS.md` (project root) | Agent maintains, you review | Build commands, architecture, gotchas |
| Session continuity | `activeContext.md` | Agent writes at session end | Current focus, last state, next steps — solves the offshore gap problem |

Auto-memory (tool-specific) is noisy — don't rely on it.

**Key behavior rule (goes in AGENTS.md):** agent updates `activeContext.md` at the end of every script/application-tier session. Not on request — automatic.

### Planning artifacts (flat file pattern)

```
project/
└── plan/
    ├── spec.md       # What, why, constraints, out-of-scope
    ├── tasks.md      # Numbered checklist, agent marks [x] as it works
    └── decisions.md  # Key choices, alternatives rejected, why
```

Calibrated by tier:

| Tier | Artifacts |
|---|---|
| Jerryrig | None |
| POC | None (or one-liner comment in file) |
| Script | `plan/tasks.md` |
| Application | `plan/spec.md` + `plan/tasks.md` + `plan/decisions.md` + `activeContext.md` |

The plan file is the human-to-autonomous handoff artifact. You approve it → agent executes against it. Survives session breaks.

---

## Agent Architecture: Generalist + Specialist Subagents

**Not a multi-agent architecture. Single generalist with on-demand specialist subagents.**

The generalist: knows you, your standards, your tier system, your workflow. Handles everything from jerryrig edits to application planning. Always codes and plans in main context.

Specialist subagents: narrow, stateless, disposable. Dispatched when a task is bounded, one-way, and either:
- Too large to run in main context without significant bloat, or
- Requires independence/fresh context (review)

### When to dispatch a subagent (practical heuristic)

```
Is the task interactive or requires your input mid-execution?
→ Main agent.

Is it a one-way bounded task that returns a result?
→ Subagent candidate.

Is it a subagent candidate AND large enough that its token cost
  in main context exceeds subagent overhead?
→ Subagent. Otherwise: main agent.
```

### Specialist types

| Specialist | When dispatched | Tools needed |
|---|---|---|
| **Explorer** | Before planning, when codebase read would significantly bloat main context | Filesystem, grep, read. No network. |
| **Researcher** | External information needed (docs, web, library references) | Fetch/web. Minimal filesystem. Output flagged with confidence + sources. |
| **Reviewer** | Script/application tier, after implementation | Fresh context, adversarial. No bias from having written the code. |

Explorer vs Researcher: explorer looks inward (your files), researcher looks outward (external sources).

### Phase × Tier dispatch table

| Phase | Jerryrig | POC | Script | Application |
|---|---|---|---|---|
| Explore | Main | Main | Subagent if large | Subagent |
| Research | Skip | Main or subagent | Subagent | Subagent |
| Plan | Main | Main | Main | Main |
| Code | Main | Main | Main | Main |
| Review | Skip | Skip | Subagent | Subagent |

Planning always stays in main context — it requires dialogue with you.

### Skill vs subagent distinction

| Skill | Subagent |
|---|---|
| Recipe — instructions the generalist follows | Actor — has own context, tools, judgment |
| Loaded into existing context | Runs independently, returns output |
| Workflow/protocol | Worker |
| Value = consistency | Value = independence or context isolation |

---

## What's NOT in V1

- Task Master (claude-task-master) — V2. Useful for structured autonomous work but overkill until harness is working.
- Serena MCP (code intelligence) — worth evaluating for personal coding, not V1.
- Custom corporate MCP (SAP/PDF) — build when concrete target exists.
- Scheduled/autonomous unattended runs — too much infrastructure for now.
- Parallel multi-agent orchestration — revisit if application-tier work routinely hits context limits.

---

## Next Step

Design the folder structure and file breakdown for `opencode_v5/`.
