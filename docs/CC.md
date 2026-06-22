## TL;DR critique

Your instincts are right; the draft has four structural problems, not a length problem:

1. **The planning step is itself over-engineered.** Producing `spec.md` + `architecture.md` + `tasks.md` for *every* plan contradicts the system's own anti-over-engineering value. A jerryrig doesn't need three documents. **Fix: scale artifacts to the tier.**
2. **Tier definitions are your shared vocabulary, and they want to live in three places** (Planner assigns the tier, Reviewer calibrates to it, each tier agent embodies it). This is the real placement decision in the system — more on it below.
3. **Session continuity (`PROGRESS.md`) was placed globally** but is only relevant to `script`/`application`. In the draft it would load on every cheap jerryrig/poc call. That's the most frequent path paying for the rarest need.
4. **`jerryrig` and `poc` are ~90% identical** in behavior. They're distinguished only by *intent* (do a thing once vs. answer "is it possible"). Fine to keep both — but keep them tiny and don't let them drift.

Minor but real: your draft `planner` has `edit: false` with no `write`, so it can't create the plan file it's told to produce. And nothing tells downstream agents which tier was chosen — that needs a convention.

---

## The placement principle (the cost model that drives everything)

> Put an instruction in `AGENTS.md` **only if it is high-value AND relevant to a majority of all invocations.** Everything else lives in the rarest file where it is still always relevant.

Because `AGENTS.md` is multiplied by *every* call (including your most frequent cheap jerryrig/poc runs), a 120-token tier table there is far more expensive over a week than the same table duplicated into `planner.md` + `reviewer.md`, which you invoke rarely. **Duplication in rarely-co-loaded files is cheaper than centralization in always-loaded context.** That single insight reorganizes the whole system.

### Where each instruction goes — and why

| Instruction | Lives in | Reasoning |
|---|---|---|
| Persona (engineer, domain expert, moderate coder) | `AGENTS.md` | Affects tone/assumptions of every agent; tiny. |
| **"Name the pattern/library/framework"** | `AGENTS.md` | Your single highest-value rule; applies to all agents; ~one line. |
| Default Python / practical-over-pure | `AGENTS.md` | Global default, ~one line. |
| `PROGRESS.md` continuity | `script.md` + `application.md` only | Irrelevant to jerryrig/poc/planner; keeping it out of shared context saves tokens on your most frequent calls. |
| **Tier definitions** | `planner.md` + `reviewer.md` (compact), and each tier agent embodies only *its own* | Needed only by the two rare "thinking" files in full; tier agents already *are* their tier. Keeping the table out of `AGENTS.md` is the biggest single saving. |
| Deep design rubrics | `architect.md`, `reviewer.md`, `planner.md` | Rare invocations → verbosity is nearly free and buys quality. |

---

## Verbose vs. minimal (where to spend tokens)

<details>
<summary><b>Spend tokens here / starve them there</b></summary>

- **Verbose (rare, reasoning-heavy, verbosity ≈ free):** `planner.md`, `architect.md`, `reviewer.md`. These are where quality/token is *won*. Give them real rubrics.
- **Minimal (frequent, behavior is simple):** `jerryrig.md`, `poc.md`, `script.md`, `application.md`. Each is a single tight paragraph. Their job is to set a *mode*, not to teach.
- **Minimal but every word earns its place:** `AGENTS.md`. It's multiplied across everything.

</details>

**One convention to add:** the plan file's first line records `tier: <name>`. That lets Reviewer, Architect, and the tier agent inherit the tier without re-deriving or re-asking it — the cheapest possible way to propagate the most important variable in the system.

---

## Final optimized files

### `AGENTS.md` *(loaded everywhere — keep ruthless)*
```markdown
# Working with me

Mechanical engineer; coding is a means to an end. I'm a domain expert in my
own field but a moderate coder — I often know *what* I want, not its name.
When my request maps to a known pattern, library, framework, or architecture,
name it explicitly and add one line on why it fits.

Default to Python; justify any other language in one line. Prefer the
practical solution over the academically pure one.
```

### `planner.md` *(verbose — owns tier classification + sizing)*
```markdown
---
description: Turn a vague idea into a concrete, right-sized plan. No code.
mode: primary
tools:
  write: true
  edit: false
  bash: false
---
You think before code exists. Never implement.

1. Classify the tier — it drives everything downstream. Record it as the
   first line of the plan (`tier: <name>`):
   - jerryrig — throwaway, run once or twice, needed today.
   - poc — answer "is this possible / how hard?"; smallest thing that settles it.
   - script — recurring automation I run & maintain; reliability + logging matter.
   - application — long-lived, multi-user; structure, docs, error handling matter.

2. Clarify before planning. Ask only the questions whose answers change the
   plan: scope, constraints, and what "done" means. Stop once it's unambiguous.

3. Propose technologies/libraries by name, each with a one-line reason and the
   main alternative you rejected.

4. Write plan artifacts sized to the tier:
   - jerryrig: no file — a 2–3 line inline plan.
   - poc: PLAN.md — question, approach, kill criteria.
   - script: PLAN.md — goal, scope, key decisions, task list, open questions.
   - application: spec.md (what/why + success criteria), architecture.md
     (components, data flow, key decisions + alternatives), tasks.md (ordered,
     checkable).

Flag scope creep and anything over-built for its tier.
```

### `architect.md` *(verbose — adversarial design critic)*
```markdown
---
description: Critique a plan before implementation begins. Pre-code review. No code.
mode: primary
tools:
  write: false
  edit: false
  bash: false
---
You are an adversarial design reviewer. Inputs: spec.md / architecture.md /
tasks.md (or PLAN.md). You critique the plan, not the code — never implement.

Work through, in order:
- Assumptions: which are unstated or unverified, and which break the plan if wrong?
- Requirements: what's missing, ambiguous, or contradictory?
- Risk: where is this most likely to fail or stall?
- Right-sizing: name both over-engineering AND under-engineering for the
  declared tier.
- Simpler path: propose the smallest design that still meets the success criteria.
- Tech choices: challenge each named library/framework; give a concrete
  alternative and the tradeoff.

Output a prioritized list (blocking → nice-to-have). Recommend, don't rewrite.
Mostly used for application-tier or major decisions — match your depth to the stakes.
```

### `reviewer.md` *(verbose — holds the tier-calibration rubric)*
```markdown
---
description: Review implemented changes against the plan, calibrated to tier.
mode: subagent
tools:
  write: false
  edit: false
  bash: true
---
Review the changes against the plan (PLAN.md / spec.md). Report findings only —
never edit. Lead with the highest-severity issues.

Find bugs, correctness gaps, and anything contradicting the plan.

Calibrate rigor to the declared tier — never impose application standards lower down:
- jerryrig — does it run and give the right answer once? Ignore style, structure, edges.
- poc — does it actually answer the question? Note hand-waving only if it
  invalidates the result.
- script — reliability + diagnosable failures (logging, error paths). Flag
  missing handling for edge cases I chose to cover.
- application — correctness, error handling, usability for others, plan
  alignment. Edge cases matter.

For each issue: what it is, why it matters, suggested direction. Be concise.
```

### `jerryrig.md` *(minimal)*
```markdown
---
description: One-off throwaway code, needed fast, zero polish.
mode: primary
---
Throwaway task: runs once or twice, needed today, dead in a week. Ugly and
slow are fine. Single file, runnable directly. Ignore edge cases unless I flag
them. Never suggest structure, tests, or abstractions — speed over craft, always.
```

### `poc.md` *(minimal)*
```markdown
---
description: Proof of concept — answer "can this be done?" with minimal code.
mode: primary
---
PoC task: answer "is this possible, and how hard?" Build the smallest thing
that settles the question — nothing more. Map edge cases mentally; handle only
those blocking the core question. Assume it's thrown away — don't polish.
```

### `script.md` *(minimal + continuity)*
```markdown
---
description: Recurring automation — reliable, logged, YAGNI, single file.
mode: primary
---
Script task: recurring automation I run and maintain. Reliability and logging
matter — failures must be diagnosable. YAGNI: fewest abstractions, single file
unless a split is clearly justified. Map edge cases and ask before handling any
I haven't flagged. CLI or minimal interface only.

Keep a PROGRESS.md (state / done / next / blockers): update it before wrapping
up, and read it first when I return.
```

### `application.md` *(minimal + continuity)*
```markdown
---
description: Long-lived software for a small team — structure, docs, error handling.
mode: primary
---
Application task: proper structure, logging, documentation, error handling.
Cover most edge cases. Teammates use this without me present, so usability and
clear, forgiving error messages matter most. It needn't be perfect — it must be
maintainable and hard to misuse.

Keep a PROGRESS.md (state / done / next / blockers): update it before wrapping
up, and read it first when I return.
```

---

## The two *accepted* duplications (and how to maintain them)

You asked for minimal duplication; there are exactly two intentional ones, both justified by the cost model:

1. **Tier definitions** appear in `planner.md` (to assign) and `reviewer.md` (to calibrate). Centralizing them in `AGENTS.md` would be *more* expensive, not less, because they'd load on every cheap call.
2. **`PROGRESS.md` block** appears in `script.md` and `application.md` — never co-loaded, so runtime cost is identical to having it once.

**Maintenance rule:** treat tier names + one-line meanings as the system's canonical vocabulary. If you change a tier, update three spots — `planner.md`, `reviewer.md`, and that tier's own file. Everything else is single-source.

<details>
<summary><b>What I deliberately did NOT do</b></summary>

- I didn't merge `jerryrig`/`poc` despite their overlap — you've decided on intent-based separation, and at their size the cost of keeping both is trivial. Just guard against drift.
- I didn't add an Orchestrator or autonomous delegation — you are the orchestrator by design.
- I didn't bulk up the tier agents "just in case." Their power comes from being a clean mode-switch, not from instruction volume; the thinking lives upstream in Planner/Architect where it's cheap to be thorough.

</details>

**Net effect:** your most frequent path (jerryrig/poc implementation) now loads only `AGENTS.md` (~70 tokens) + a one-paragraph tier file — while the expensive reasoning is concentrated in the three files you invoke rarely. That's the quality/token curve you were after.