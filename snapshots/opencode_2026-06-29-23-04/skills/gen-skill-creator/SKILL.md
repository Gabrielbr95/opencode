---
name: gen-skill-creator
description: >-
  Author, revise, or audit agent skills (SKILL.md files) for OpenCode and the
  cross-platform Agent Skills standard. Use this whenever the user wants to
  create, write, build, scaffold, or rewrite a skill; says "turn this into a
  skill" / "make this a skill" / "skill for X"; describes a repeating workflow
  they keep re-explaining to the agent; or asks to improve, tighten, or audit
  an existing skill. Also self-trigger when the agent notices the user
  re-explaining the same workflow across multiple turns and a reusable skill
  would help — in that case, emit a short notification before proceeding. Also
  use when the user asks how skills work, what the SKILL.md format is, or
  where to place skills. Do NOT use for one-off tasks that won't be repeated.
---

# Skill Creator

Author agent skills — self-contained `SKILL.md` files that teach the agent a repeatable procedure. A good skill passes two bars: triggers at the right moment (description) and changes agent behavior once loaded (body). Most skills fail one bar. This skill catches both.

## Self-trigger protocol

When agent-initiated (not user-asked), emit before doing anything:

```
ℹ️ Skill proposal: <name> — <1-line summary>.
   I noticed <observation>. Drafting now — say "stop" to cancel.
```

Skip the interview (Step 1 Branch A); extract the pattern from context and proceed to Step 2.

## Naming scheme

Format: `[auto-]<category>-<name>` — all kebab-case, regex `^[a-z0-9]+(-[a-z0-9]+)*$`, 1–64 chars, must match directory name.

- `auto-` = agent-generated. Omit for user-directed authoring.
- `plan-` = produces plans/specs, no execution
- `exec-` = runs code, modifies files
- `gen-` = reference, workflow, meta

Examples: `plan-pdf-extraction`, `auto-exec-deploy-script`, `gen-skill-creator`

## Output structure

```
<name>/
├── SKILL.md              # required
├── references/           # optional — long docs, loaded just-in-time
├── scripts/              # optional — deterministic logic only
└── assets/               # optional — templates, examples
```

Locations: `.opencode/skills/<name>/` (project) or `~/.config/opencode/skills/<name>/` (global).

After writing, **remind user to restart opencode** — sessions don't hot-reload.

## SKILL.md format

**Frontmatter** (YAML):
- `name` (required): matches directory, follows naming scheme
- `description` (required, 1–1024 chars): the routing signal — only thing the agent sees before loading. Must cover *what* + *when*. Front-load trigger keywords. Use "Use when…" / "Use ONLY when…".
- Optional: `license`, `compatibility`, `metadata`

**Body** (<500 lines / ~5000 tokens): loads after trigger. Imperative voice. Offload bulk to helpers.

Token budget by stage: description ~100 tokens (advertise) → body <5000 (load) → helpers as needed (read/run).

## Workflow

### Step 1 — DISCOVER

**User-initiated (interview)**. Ask in one batch:
1. What repeatable task does this encode?
2. When should it trigger? What should NOT trigger it?
3. What does the agent do wrong without this skill? (the failure mode)
4. What does "done" look like?
5. Any helpers needed — scripts, references, templates?

If source material provided, read first, ask only gaps. Don't draft until you can state the specific failure this prevents.

**Agent-initiated**: extract answers from conversation context. You already emitted the notification. Proceed to Step 2.

### Step 2 — PLAN

Decide: name (follow scheme), scope (one skill = one task), rigid vs flexible body, helpers needed (default: none), location (confirm with user).

### Step 3 — GENERATE

Frontmatter: `name` follows scheme, `description` covers what+when, front-loads trigger keywords, slightly "pushy" > modest.

Body structure:
```markdown
# Title
[1–2 sentences: the specific failure this prevents.]

## When to use
[Concrete triggers — restates description to confirm correct load.]

## Procedure
1. [Imperative step. Exact command or decision branch.]
2. [If conditional: "If X do Y. Otherwise skip to step N."]

## Output format
[Exact shape if it matters. Use assets/ for templates.]

## Examples
[1–2 realistic input/output pairs. No placeholders.]

## Edge cases
- [What breaks naive execution.]
```

Body rules: imperative voice; numbered steps for fragile workflows, guidelines for flexible ones; give defaults not menus; reference helpers explicitly (`[references/api.md](references/api.md)`); keep flat (one level deep); use standard folder names.

### Step 4 — VALIDATE

Checklist:
- [ ] Name follows `[auto-]<category>-<name>`, matches directory, satisfies regex
- [ ] Description 1–1024 chars, covers what+when, front-loads keywords, distinct from siblings
- [ ] Body: imperative voice, procedural, starts with trigger conditions
- [ ] Edge cases documented, realistic examples included
- [ ] Under 500 lines; bulk in helpers; helpers one level deep and explicitly referenced

**Two-bar self-test:**
1. **Trigger test**: read only `description` — would agent load it on a realistic matching request? Would it wrongly load on an adjacent non-matching request? If either fails, rewrite.
2. **Would-have-anyway test**: for each body line — would a competent agent already do this? If yes, cut or sharpen into something non-obvious.

Do not ship until both pass.

### Step 5 — INSTALL

Create directory, write `SKILL.md` (all caps, case-sensitive), write helpers, verify files exist.

### Step 6 — HANDOFF

```
SKILL CREATED
Name:         <name>
Path:         <full path>
What:         <one sentence>
Triggers on:  <paraphrase description>
Helpers:      <list or "none">
Lines:        <n>/500
Trigger test: PASS
Body test:    PASS

Next: restart opencode, then test on a real request.
```

## Modes

**Create** (default): interview/extract → plan → generate → validate → install → handoff.

**Rewrite**: read existing skill, run both self-tests on every line. Report: lines failing would-have-anyway, description failing trigger test, missing specifics, naming issues. Then rewrite. If renaming, move directory and update `opencode.json` permission refs.

**Audit**: score only, no rewrite. Mark each line: **keeps** (specific, passes both tests), **weak** (would-have-anyway), **trigger-risk** (description too narrow/vague), **naming** (flag, don't fix). Summarize with concrete fixes.

## Anti-patterns

- Documentation prose instead of procedure — rewrite as commands
- Vague description ("helps with code") or overly broad ("does everything")
- Trigger info only in body (invisible at routing time) — put keywords in `description`
- Missing `auto-` on agent-generated skills
- Deeply nested helpers — one level only
- Bundling importable libraries in `scripts/`
- Placeholder examples — use real specifics
- Skipping interview (user-initiated) or notification (agent-initiated)

## Troubleshooting

1. `SKILL.md` must be **all caps** — case-sensitive
2. Frontmatter needs both `name` and `description`
3. Skill names must be unique across all locations
4. `name` must match parent directory exactly
5. Check `opencode.json` permissions — `deny` hides skills
6. Wrap YAML strings with special chars in quotes
7. Restart opencode after changes
