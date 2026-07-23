# Workflow Pattern Comparison

This document compares the main workflow and agent patterns already identified in the research base.

Its purpose is decision support:

- when to use each pattern
- when not to use it
- what it buys you
- what it costs you
- how it usually fails

The goal is not to rank the patterns from “basic” to “advanced.”

The durable rule is:

> **Use the least agentic structure that reliably solves the task.**

---

## Quick Selection Heuristic

If the task is:

- **predictable and repeatable** -> start with **Chain**
- **one of several known task types** -> try **Route**
- **split into independent parts or multiple attempts** -> try **Parallelize**
- **open-ended with dynamic subproblems** -> consider **Orchestrator-Worker**
- **quality-limited by revision/critique** -> consider **Evaluator-Optimizer**
- **needs interleaved tool use with live observations** -> consider **ReAct**

If two patterns seem plausible, prefer the one with:

1. fewer moving parts
2. clearer stop conditions
3. easier debugging
4. less unnecessary autonomy

---

## Comparison Matrix

| Pattern | Core idea | Best fit | Main strengths | Main costs | Common failure modes | Good default? |
|---|---|---|---|---|---|---|
| **Chain** | Fixed ordered sequence of steps | Predictable tasks with known stages | Simple, inspectable, testable | Brittle when task shape varies | Early-step error propagates; unnecessary rigidity | **Yes** |
| **Route** | Classify first, then send to the right branch | Several known task types with different handling | Keeps prompts/tools specialized; avoids one giant flow | Needs reliable routing logic | Misrouting; unclear branch boundaries; classifier drift | **Yes** when branches are real |
| **Parallelize** | Run independent workers/attempts, then aggregate | Tasks that decompose cleanly or benefit from multiple attempts | Speed, breadth, diversity, compare-and-merge | Coordination and merge overhead | Duplicate work; weak aggregation; fake independence | **Sometimes** |
| **Orchestrator-Worker** | Central planner dynamically delegates subtasks | Open-ended work with uncertain step count or decomposition | Flexible, handles dynamic subproblems, specialization possible | Higher latency, more control complexity, harder debugging | Over-delegation; unclear ownership; runaway orchestration | **No** unless needed |
| **Evaluator-Optimizer** | Generate, critique, revise | Tasks where feedback meaningfully improves quality | Better polish, catches obvious defects, supports iterative refinement | Extra passes, extra cost, can loop pointlessly | Weak evaluator; endless revision; style churn instead of real improvement | **Sometimes** |
| **ReAct** | Interleave reasoning, action, and observation | Tool-using tasks where next step depends on live results | Good grounding, adapts step-by-step, handles unknowns better than fixed flows | Tool-use complexity, loop risk, harder observability needs | Bad tool choice; looping; overlong trajectories; poor stop behavior | **No** unless environment feedback matters |

---

## Pattern-by-Pattern Notes

## 1. Chain

### Shape
Step 1 -> Step 2 -> Step 3 -> done.

### Best fit
- repeatable research or document workflows
- stable transformations
- tasks with known ordering
- low ambiguity work

### Why it works
- easy to understand
- easy to verify between steps
- easy to document and reuse

### When not to use it
- when branches depend on live discoveries
- when step count is unknown
- when one failure should trigger different recovery paths

### Typical failure modes
- a bad early step poisons everything after it
- too many chain steps become ceremony
- authors keep stuffing branching logic into what should no longer be a simple chain

### Practical repository fit
Very strong default for recurring structured work.

---

## 2. Route

### Shape
Classify -> pick branch -> run specialized workflow.

### Best fit
- requests that fall into a few clearly different categories
- tasks where different branches need different tools, prompts, or policies
- situations where specialization reduces prompt bloat

### Why it works
- keeps each branch narrower and cleaner
- prevents one overloaded general-purpose workflow
- matches work type before execution cost is incurred

### When not to use it
- when branches are fuzzy or constantly changing
- when a single simple workflow already handles the cases well
- when route choice is as hard as the task itself

### Typical failure modes
- misclassification sends work into the wrong branch
- too many branches create maintenance burden
- routing labels become stale as the repository evolves

### Practical repository fit
Good when task classes are real and stable, not imagined.

---

## 3. Parallelize

### Shape
Split into independent workers or attempts -> aggregate or choose result.

### Best fit
- document sections that can be worked independently
- multiple candidate generations with later selection
- compare-and-synthesize tasks
- latency hiding when independent work can run together

### Why it works
- can improve coverage or quality through diversity
- can improve wall-clock time if work is truly independent
- gives multiple candidates for evaluation

### When not to use it
- when the work is highly sequential
- when aggregation is harder than the original task
- when workers all need the same large context and produce near-duplicates

### Typical failure modes
- “parallel” tasks are not actually independent
- aggregation step is underdesigned and weak
- duplicated context raises token cost without real gain

### Practical repository fit
Useful for independent comparisons or sectioned outputs, but easy to overuse.

---

## 4. Orchestrator-Worker

### Shape
Planner/orchestrator decides subtasks dynamically -> delegates to workers -> integrates results.

### Best fit
- open-ended tasks with unknown decomposition
- variable number of subtasks
- heterogeneous subproblems where different workers genuinely help
- cases where central ownership should remain while sub-work is delegated

### Why it works
- handles uncertainty better than fixed graphs
- can adapt as evidence arrives
- allows bounded specialization without full handoff

### When not to use it
- when a chain or route already works
- when the planner has little real basis for decomposition
- when the work is too small to justify coordination overhead

### Typical failure modes
- orchestrator creates unnecessary subtasks
- ownership becomes blurry
- context handoff to workers is poor
- the system spends more effort managing workers than solving the problem

### Practical repository fit
Useful for larger uncertain tasks, but should be justified by real complexity, not aesthetics.

---

## 5. Evaluator-Optimizer

### Shape
Generate -> critique or score -> revise -> stop when good enough.

### Best fit
- writing and synthesis tasks
- tasks where quality improves substantially after feedback
- schema-constrained or rubric-driven outputs
- cases where “first draft” is usually not enough

### Why it works
- adds a structured correction loop
- can catch defects before durable promotion
- useful when the evaluation criteria are clearer than the generation path

### When not to use it
- when evaluation criteria are vague
- when revision mostly causes churn instead of improvement
- when the first pass is already good enough and iteration adds only cost

### Typical failure modes
- evaluator is weak, inconsistent, or style-biased
- optimizer overfits to superficial feedback
- loop continues without meaningful gain

### Practical repository fit
Strong fit for reviewable drafting and durable docs, especially before final promotion.

---

## 6. ReAct

### Shape
Reason about next step -> act with a tool -> observe result -> continue.

### Best fit
- tool-rich tasks
- search, retrieval, and environment-interaction tasks
- cases where the next step depends on what the last action found
- situations where fixed planning would be too brittle

### Why it works
- grounds the workflow in external observations
- lets the system adapt incrementally
- reduces pure guesswork when tools can reveal reality

### When not to use it
- when no meaningful tools or observations are needed
- when a fixed workflow already covers the task well
- when loop behavior cannot be bounded and inspected

### Typical failure modes
- unnecessary tool calls
- tool loops or repeated retries
- poor stop conditions
- observations are misread or not integrated well

### Practical repository fit
Good for real read-search-act loops, but not as a default wrapper around every task.

---

## Tradeoff Summary by Dimension

| Dimension | Chain | Route | Parallelize | Orchestrator-Worker | Evaluator-Optimizer | ReAct |
|---|---|---|---|---|---|---|
| Predictability | High | High after routing | Medium | Low to medium | Medium | Low to medium |
| Flexibility | Low | Medium | Medium | High | Medium | High |
| Debuggability | High | Medium to high | Medium | Low to medium | Medium | Medium |
| Coordination overhead | Low | Low to medium | Medium | High | Medium | Medium |
| Best for uncertain tasks | Poor | Limited | Limited | Strong | Moderate | Strong |
| Best for tool-grounded work | Low | Medium | Medium | Medium | Low | Strong |
| Risk of runaway behavior | Low | Low | Low to medium | High | Medium | High |
| Ease of testing | High | Medium to high | Medium | Low | Medium | Low to medium |

---

## Selection Rules

### Prefer Chain when
- the steps are known
- you want boring reliability
- the task repeats often

### Prefer Route when
- there are a few stable categories
- specialization meaningfully reduces confusion

### Prefer Parallelize when
- subproblems are truly independent
- diversity or speed matters more than simplicity

### Prefer Orchestrator-Worker when
- decomposition cannot be known up front
- dynamic delegation creates real value

### Prefer Evaluator-Optimizer when
- quality improves through explicit critique
- you can define what “better” means

### Prefer ReAct when
- live tool feedback determines the next step
- reasoning without action would be guesswork

---

## Anti-Patterns

- Do **not** choose Orchestrator-Worker just because it sounds advanced.
- Do **not** add Route if the branches are cosmetic.
- Do **not** use Parallelize when the merge step is undefined.
- Do **not** use Evaluator-Optimizer when the evaluator has no stable criteria.
- Do **not** use ReAct when tools do not materially change the answer.
- Do **not** keep a Chain after it has silently turned into dynamic branching.

---

## Recommended Default Order

When exploring a new workflow, try patterns in roughly this order:

1. **Chain**
2. **Route**
3. **Parallelize** if independence is obvious
4. **Evaluator-Optimizer** if draft quality is the real bottleneck
5. **ReAct** if live observations must drive behavior
6. **Orchestrator-Worker** only when dynamic delegation is truly justified

This order is not universal, but it fits the repository’s bias toward inspectability and low unnecessary autonomy.

---

## Relationship to Other Documents

- `research/topics/agent-architectures.md`
- `research/topics/planning-systems.md`
- `research/principles-only.md`
- `research/vocabulary.md`
