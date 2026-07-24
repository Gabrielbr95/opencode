# Eval Harnesses

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - vendor SDKs for trace capture, experiment runs, and judge orchestration
  - dataset interchange formats and built-in scorer registries
  - CI and approval-gate integrations bundled into hosted platforms

## Summary
- Evaluation harnesses are the reusable infrastructure layer that turns evaluation ideas into repeatable engineering practice.
- The durable idea is not a vendor dashboard or a prompt-testing UI. It is the combination of:
  - versioned evaluation cases
  - run capture and replay hooks
  - scorer execution
  - score recording
  - threshold comparison
  - release or approval decisions
- Good eval infrastructure makes workflow changes testable before release, inspectable after failure, and gateable at consequential boundaries.

## Motivation
- The concept note `../concepts/evaluation-prompt-testing.md` already covers why prompts and workflows need tests.
- What was missing was the capability-layer note describing the engineering machinery that makes those tests durable, automatable, and comparable across runs.

## Problem Statement
- AI workflow systems change constantly: prompts, tools, models, retrieval logic, orchestration, and approval rules all move.
- Without an evaluation harness, teams end up with:
  - manual spot checks that do not reproduce
  - scattered ad hoc examples with no versioning
  - traces that cannot be scored consistently
  - no stable regression thresholds
  - no clear rule for whether a change should ship, pause for review, or be rejected

## Core Function
- Run a candidate workflow or component against a defined set of cases.
- Capture the evidence needed to judge the run.
- Apply one or more evaluators.
- Store scores in a stable schema.
- Compare results against baselines or thresholds.
- Feed the outcome into CI, approval, or release decisions.

## Minimal Durable Model

### 1. Evaluation case
Defines what should be tested.

Minimum useful fields:
- stable case ID
- input or starting state
- task or scenario label
- expected outcome, rubric, or grading instructions

Often also useful:
- risk level
- workflow type
- tags such as happy-path, edge-case, safety, latency-sensitive
- source of the case: handcrafted, production failure, synthetic, human review sample

### 2. Evaluation run
Defines one execution of a system version against one case or case set.

Typical fields:
- run ID
- system version identifiers: prompt, workflow, model, tool, repo revision
- case IDs executed
- timestamps
- environment or config snapshot

### 3. Trajectory or evidence record
Defines what happened during the run.

Typical fields:
- final output
- intermediate tool calls or workflow steps
- retrieved context IDs
- approvals, handoffs, retries, stops, and failures
- latency, token, and cost metadata

### 4. Score record
Defines the judgment applied to a run.

Typical fields:
- evaluator ID and method
- metric name
- score value
- pass/fail or ordinal outcome
- explanation or evidence pointer
- judge version when the evaluator is itself a model or rubric set

### 5. Gate decision
Defines what the scores mean operationally.

Typical fields:
- baseline or threshold reference
- gate type: advisory, warning, blocking, human-review-required
- decision outcome
- rationale

## Evaluation Lifecycle
The portable evaluation loop looks roughly like this:

1. define or update cases
2. version the dataset and evaluator configuration
3. run the candidate workflow offline, online, or both
4. capture final outputs plus workflow trajectory evidence
5. score the run with one or more evaluators
6. compare against baseline, thresholds, or pairwise alternative
7. produce a gate decision for CI, review, or release
8. feed new failures back into the dataset

Hosted platforms may collapse several steps into one feature, but the loop still exists.

## Common Patterns
- golden dataset plus targeted edge-case suite
- replay of captured trajectories against a changed prompt or workflow
- offline pre-release benchmark plus online production sampling
- exact checks for objective failures before semantic judging
- workflow-level grading over traces, not only final answer strings
- pairwise comparison against a current baseline
- case tagging for selective regression suites
- sampled human review for ambiguous or consequential cases
- blocked merges or manual approval when thresholds fail

## Typical Components
- case store or dataset registry
- run orchestrator
- trace or trajectory capture hooks
- evaluator registry
- score schema and result store
- baseline store
- threshold and policy engine
- CI adapter or approval workflow integration
- review UI or human annotation queue

## Durable Distinctions

### Offline evaluation vs online evaluation
Offline evaluation uses controlled cases and repeatable inputs.
Online evaluation uses real or near-real traffic, sampled production behavior, or shadow runs.

Offline is better for repeatability and pre-merge comparison.
Online is better for realism, drift detection, and finding failures the benchmark missed.

### Dataset vs trajectory
A dataset defines what should be run.
A trajectory records what actually happened in a specific run.

Trajectories often become future dataset cases, but they are not the same artifact.

### Observability data vs evaluation result
Observability records execution.
Evaluation converts selected execution evidence into a judgment.

### Final-answer grading vs workflow-level grading
Some tasks can be scored from the final answer alone.
Agent workflows often require judging retrieval quality, tool choice, handoff correctness, stopping decisions, approval behavior, and side effects.

### Metric value vs gate decision
A score is an observation.
A gate is a policy decision about whether that score is acceptable for a given boundary.

### Benchmark threshold vs baseline comparison
Absolute thresholds answer "is this good enough?"
Baselines answer "is this better or worse than what we have now?"

Both are useful, and they answer different release questions.

## Dataset Design Heuristics

### Keep case identity stable
Case IDs should survive prompt and model changes so regressions stay attributable.

### Preserve source provenance
It should remain visible whether a case came from:
- a handcrafted benchmark
- a real failure
- a support or review sample
- a synthetic generator

### Tag by failure mode, not only domain
Tags like `tool-selection`, `retrieval-miss`, `unsafe-write`, `handoff-loop`, or `slow-path` help targeted reruns and root-cause analysis.

### Separate reusable fixtures from volatile runtime exhaust
Keep durable cases small and inspectable.
Store large raw traces or screenshots by reference when possible.

### Prefer representative slices over benchmark vanity size
A smaller, curated, trusted suite is often more useful than a huge mixed-quality set.

## Trajectory Capture Heuristics

### Capture the boundaries that affect judgment
At minimum, retain enough evidence to explain:
- what input was given
- what major steps occurred
- what tools or retrieval actions fired
- what final output or side effect resulted

### Keep stable IDs even if raw payloads are redacted
This preserves comparability while respecting privacy or local data constraints.

### Record workflow metadata with the run
Prompt version, model, tool registry version, repo revision, and evaluator version all matter for later comparison.

### Do not require full-fidelity replay for every use case
Some eval loops need exact replay.
Others only need enough trace evidence to score behavior consistently.

## Score Schema Design Heuristics

### Separate metric definition from metric result
The definition should say what the metric means.
The result should say what happened on this run.

### Allow mixed evaluator types in one run
One case may legitimately produce:
- exact match for structured fields
- heuristic pass/fail for workflow safety
- LLM-judge quality score
- human override or adjudication

### Keep scores interpretable
Scores should include enough metadata to answer:
- who or what graded this
- under which rubric or prompt
- on which evidence
- with what threshold or comparison rule

### Store per-case results, not only aggregates
Aggregate pass rates are useful for dashboards.
Per-case records are what make debugging and targeted regression repair possible.

## Regression Thresholds and Gate Design

### Common gate shapes
- minimum absolute threshold on one metric
- no regression allowed on a protected case subset
- relative improvement over baseline on a comparison suite
- maximum allowed latency or cost increase
- composite rule requiring several metrics to pass together
- mandatory human review when evaluator disagreement exceeds a threshold

### Protected subsets matter
It is common to maintain a small set of must-not-break cases for safety, approvals, tool correctness, or business-critical workflows.

### Gates should match consequence
Low-risk prompt iteration may use advisory thresholds.
Durable workflow changes, side-effecting agents, or approval logic often justify blocking gates or required review.

### Avoid one-number release gates when the workflow is multi-objective
Quality, cost, latency, safety, and workflow correctness often move differently.
Single aggregate scores can hide dangerous tradeoffs.

## Workflow-Level Evaluation
- Workflow-level eval infrastructure must treat the run as more than an answer string.
- Common workflow-level score dimensions include:
  - correct tool selected
  - arguments valid and sufficiently specific
  - retrieval results relevant and grounded
  - handoff occurred when needed and not otherwise
  - stop condition chosen correctly
  - approval gate respected
  - side effects avoided or executed correctly
  - latency and cost remained inside budget
- This is where trace capture, event schemas, and score schemas have to line up cleanly.

## Human, Heuristic, and LLM-Judge Mixes
- The most durable pattern is a layered evaluator stack, not a single universal grader.
- Common layering order:
  - deterministic checks for cheap objective failures
  - heuristics or rule-based workflow checks for policy and structure
  - LLM judge for nuanced semantic judgment at scale
  - human review for ambiguity, consequence, or arbitration
- Good eval harnesses treat these as composable evaluators with explicit provenance, not as hidden dashboard magic.

## CI, Approval, and Operational Uses
- pre-merge regression suite for prompts, workflow definitions, and tool-routing changes
- nightly benchmark runs to catch drift from models, dependencies, or retrieval changes
- approval gates before enabling a new workflow in production
- canary or shadow evaluation before widening traffic
- audit support for explaining why a release was blocked or approved
- failure harvesting from production or review into future regression suites

## Portability
- Portable across tools:
  - case versioning matters more than dataset file syntax
  - trajectory capture is necessary for workflow evals
  - mixed evaluator stacks are more trustworthy than one evaluator alone
  - thresholds and approval rules are separate from scoring logic
  - protected regression subsets are usually worth maintaining
- Vendor-shaped:
  - experiment tracking UI and run browsing
  - built-in judge templates and scorer libraries
  - native online eval traffic hooks
  - exact dataset import/export format
  - where gate decisions are enforced in CI or deployment flows

## Advantages
- makes workflow changes comparable and repeatable
- turns observed failures into durable regression cases
- supports workflow-level scoring instead of shallow answer-only testing
- enables proportionate CI and approval gates
- improves auditability around release decisions

## Risks / Failure Modes
- overfitting to a narrow benchmark
- datasets with weak provenance or stale assumptions
- trajectories captured without enough detail to score meaningfully
- too much raw data capture, creating privacy or storage problems
- hidden evaluator drift, especially with LLM judges
- thresholds chosen for convenience rather than operational consequence
- one aggregate score masking regressions in critical subsets
- conflating observability tooling with actual grading logic
- using human review as a checkbox instead of true arbitration

## Tradeoffs
- **Offline vs online**: repeatability and speed versus realism and drift detection.
- **Rich trajectory capture vs light capture**: better workflow judgment versus lower storage and privacy burden.
- **Absolute thresholds vs pairwise baselines**: shipping bar versus change detection.
- **Single suite vs tagged suites**: simplicity versus targeted diagnosis.
- **More automation vs more human review**: scale and speed versus nuance and accountability.

## Relationships to Other Notes
- `../concepts/evaluation-prompt-testing.md`
- `../concepts/observability-traceability.md`
- `../concepts/human-in-the-loop-control-points.md`
- `../capabilities/tool-calling.md`
- `../syntheses/evaluation-method-comparison.md`
- `../syntheses/observability-schema.md`
- `../syntheses/control-boundaries.md`

## Relevance to This Repository
- Treat eval infrastructure as a first-class workflow component rather than an afterthought.
- Keep small versioned case sets for research quality, workflow correctness, approval behavior, and safety-sensitive changes.
- Capture enough run metadata to compare prompt, workflow, and tool changes without guessing what changed.
- Define a minimal score schema before adopting any platform-specific eval tooling.
- Use protected subsets and proportionate gates for consequential workflow changes.
- Feed review failures and production misses back into durable regression cases.

## Open Questions
- What is the minimum trajectory schema that still supports trustworthy workflow-level grading in this repository?
- Which changes deserve blocking eval gates versus advisory evidence only?
- How much online evaluation is worth doing in a local-first, corporate environment?
- Which evaluator outputs should be stored long-term versus summarized?

## References
- [Define success criteria and build evaluations](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success) — Anthropic docs. Useful for task definition, evaluator layering, and dataset curation.
- [Evaluate agent workflows](https://platform.openai.com/docs/guides/agent-evals) — OpenAI docs. Useful evidence for workflow-level evaluation and trace-based assessment.
- [Working with evals](https://platform.openai.com/docs/guides/evals) — OpenAI docs. Useful for portable eval run, scorer, and dataset concepts even when product details drift.
- [LangSmith Evaluation Concepts](https://docs.smith.langchain.com/evaluation/concepts) — LangSmith docs. Helpful articulation of offline versus online evaluation and feedback loops.
- [Langfuse Scores Overview](https://langfuse.com/docs/scores/overview) — Langfuse docs. Useful evidence that score schemas and evaluator provenance matter as separate objects from traces.
- [Intro | Promptfoo](https://www.promptfoo.dev/docs/intro/) — Promptfoo docs. Good open-source example of file-backed eval cases, assertions, and CI-oriented regression usage.
- [DeepEval documentation](https://deepeval.com/docs/getting-started) — DeepEval docs. Useful example of evaluator composition and test-oriented workflow framing.
- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/) — ACL Anthology, 2020. Strong grounding for case design around behavior and failure modes.
- [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) — arXiv / TMLR noted, 2022/2023. Useful for multi-metric and multi-scenario score design.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634) — arXiv, 2023. Important for LLM-judge usage and evaluator drift caveats.
