# Evaluation Method Comparison

This document compares the main evaluation methods already identified in the research base.

Its purpose is decision support:

- what each method is good at
- what it misses
- when to use it
- when not to trust it alone
- how to combine methods without creating fake confidence

The durable rule is:

> **Use the most objective method that can measure the thing you actually care about, then add more subjective methods only where they add real signal.**

---

## Quick Selection Heuristic

If the question is:

- **Did it match the expected answer exactly?** -> use **Exact Match**
- **Did it satisfy explicit qualitative criteria?** -> use **Rubric**
- **Which of two options is better?** -> use **Pairwise Comparison**
- **Is the output good on nuanced semantic criteria at scale?** -> consider **LLM Judge**
- **Is the consequence high or the judgment ambiguous?** -> use **Human Review**

If two methods seem plausible, prefer the one with:

1. clearer grading rules
2. less evaluator drift
3. easier reproducibility
4. lower risk of hidden bias

---

## Comparison Matrix

| Method | Core idea | Best fit | Main strengths | Main costs | Common failure modes | Good default? |
|---|---|---|---|---|---|---|
| **Exact Match** | Compare against a known correct answer or label | Deterministic tasks, classification, exact fields, canonical outputs | Objective, cheap, repeatable, easy to automate | Too brittle for valid paraphrases or partial correctness | Penalizes acceptable variation; encourages overfitting to formatting | **Yes** when exactness matters |
| **Rubric** | Score against explicit criteria | Structured qualitative judgment with stable dimensions | More flexible than exact match; criteria stay visible | Requires rubric design and calibration | Rubric drift; vague criteria; inconsistent scoring | **Yes** when criteria are clear |
| **Pairwise Comparison** | Compare A vs B on same case | Prompt/model/version comparison where absolute scoring is hard | Good for relative improvement decisions; easier than absolute scoring | Needs baselines and repeated comparisons | Preference instability; ties hidden as forced wins; style bias | **Yes** for change comparison |
| **LLM Judge** | Use a model as evaluator | Large-scale semantic judgment, nuanced text quality, workflow review support | Scalable, flexible, useful for fuzzy qualities | Bias, instability, prompt sensitivity, extra cost | Judge agrees with style not substance; leakage from prompt setup; false confidence | **Sometimes** |
| **Human Review** | A person judges the result | High-stakes, ambiguous, domain-heavy, policy-sensitive cases | Best for nuance, context, consequence, and final arbitration | Slow, expensive, inconsistent, hard to scale | Reviewer fatigue; inconsistent standards; shallow spot-checking | **Required** at consequential boundaries |

---

## Method-by-Method Notes

## 1. Exact Match

### Shape
Expected output exists -> compare predicted output directly against it.

### Best fit
- categorical classification
- exact extraction fields
- structured labels
- strict formatting or schema requirements
- canonical short answers

### Why it works
- objective and easy to reproduce
- excellent for regression checks
- cheap enough for frequent use

### When not to use it
- when many correct answers are possible
- when style or explanation quality matters
- when semantic equivalence matters more than literal match

### Typical failure modes
- valid paraphrases marked wrong
- benchmark teaches the system one canonical wording
- exact string checks hide partial correctness

### Practical repository fit
Strong first layer for deterministic checks, formatting, tool behavior, and structured outputs.

---

## 2. Rubric

### Shape
Define scoring dimensions -> score each output against them.

### Best fit
- summaries
- plans
- explanations
- draft quality checks
- tasks with visible quality dimensions such as completeness, clarity, or grounding

### Why it works
- makes success criteria explicit
- supports more nuance than pass/fail checks
- keeps evaluation interpretable

### When not to use it
- when the rubric is vague or unstable
- when reviewers cannot apply it consistently
- when a simpler deterministic check already answers the question

### Typical failure modes
- criteria are too fuzzy to produce reliable scores
- scores collapse into subjective taste
- different evaluators apply dimensions differently

### Practical repository fit
Very useful for research notes, syntheses, and workflow outputs where exact match is too narrow.

---

## 3. Pairwise Comparison

### Shape
Show two outputs for the same case -> decide which is better.

### Best fit
- A/B comparison of prompt versions
- selecting among candidate drafts
- deciding whether a change actually improved something
- cases where relative quality is easier than absolute scoring

### Why it works
- often easier and more stable than assigning absolute scores
- directly supports change decisions
- useful when “better” is visible even if numeric scoring is awkward

### When not to use it
- when no strong baseline exists
- when the output count is too large for practical comparison
- when ties or mixed tradeoffs matter more than a forced winner

### Typical failure modes
- evaluator prefers style over substance
- pairwise winner is only locally better on one dimension
- repeated comparisons become expensive or inconsistent

### Practical repository fit
Strong method for prompt or workflow iteration, especially before adopting a new default.

---

## 4. LLM Judge

### Shape
Prompt a model to evaluate another model’s output using instructions, criteria, or rubric.

### Best fit
- nuanced text quality at moderate scale
- semantic comparisons not handled by exact checks
- draft triage before human review
- workflow traces where some context-sensitive judgment is needed

### Why it works
- flexible and scalable
- can judge dimensions that are expensive to annotate manually
- can support rubric scoring or pairwise comparison

### When not to use it
- as the only evaluator for high-stakes decisions
- when deterministic checks already answer the question
- when evaluator prompt quality is poor or unstable

### Typical failure modes
- judge bias toward verbosity or certain styles
- poor calibration across domains or over time
- evaluator prompt leaks assumptions that distort scoring
- false confidence because outputs look precise

### Practical repository fit
Useful as a middle layer, but should sit beside deterministic checks and sometimes human review.

---

## 5. Human Review

### Shape
A human reads the output or trace and decides whether it is acceptable, preferable, safe, or policy-compliant.

### Best fit
- consequential durable changes
- policy-sensitive outputs
- domain-specific nuance
- ambiguous cases where automation is not trustworthy enough
- final arbitration when evaluators disagree

### Why it works
- best at contextual judgment
- can weigh tradeoffs that are hard to formalize
- can catch subtle business or policy errors

### When not to use it alone
- for high-volume repetitive checks that a deterministic grader could handle
- as the only feedback loop for frequent iteration
- when the human has no stable rubric or comparison basis

### Typical failure modes
- reviewers are inconsistent
- review becomes a shallow checkbox ritual
- cost and delay prevent real reuse

### Practical repository fit
Essential at consequential boundaries, but should be reserved for places where human judgment adds signal.

---

## Tradeoff Summary by Dimension

| Dimension | Exact Match | Rubric | Pairwise | LLM Judge | Human Review |
|---|---|---|---|---|---|
| Objectivity | High | Medium | Medium | Low to medium | Variable |
| Flexibility | Low | Medium | Medium | High | High |
| Scalability | High | Medium | Medium | High | Low |
| Cost | Low | Medium | Medium | Medium | High |
| Reproducibility | High | Medium | Medium | Low to medium | Low to medium |
| Best for nuanced quality | Poor | Good | Good | Good | Strong |
| Best for regression gates | Strong | Moderate | Strong for A/B | Moderate | Weak alone |
| Bias risk | Low | Medium | Medium | High | Medium |

---

## Layering Rules

The best pattern is usually not one evaluator. It is a stack.

### Good default stack
1. **Exact/rule/schema checks** for objective failures
2. **Rubric or pairwise** for quality comparison
3. **LLM judge** where semantic scale matters
4. **Human review** at consequential or ambiguous boundaries

### Why layering works
- objective checks catch cheap failures fast
- rubrics and pairwise methods add structured quality signal
- LLM judges scale nuanced review
- humans arbitrate what should not be left to automation

---

## Selection Rules

### Prefer Exact Match when
- correctness is literal
- outputs are structured or canonical
- you need stable regression checks

### Prefer Rubric when
- quality dimensions are known
- you need interpretable scoring
- “good” can be broken into criteria

### Prefer Pairwise when
- the question is whether a change is better than a baseline
- absolute scoring is awkward or noisy

### Prefer LLM Judge when
- you need scalable semantic judgment
- deterministic checks are too narrow
- human-only review would be too slow

### Prefer Human Review when
- stakes are high
- policy or domain nuance dominates
- automated evaluators disagree or cannot be trusted enough

---

## Anti-Patterns

- Do **not** use exact match for tasks with many valid phrasings.
- Do **not** use a rubric whose criteria cannot be applied consistently.
- Do **not** treat pairwise wins as absolute truth across all dimensions.
- Do **not** let an LLM judge become the only authority for high-stakes evaluation.
- Do **not** rely on human review as a substitute for cheap deterministic checks.
- Do **not** confuse observability data with evaluation results; traces provide evidence, not judgment.

---

## Recommended Default Order

When designing an eval loop, try methods in roughly this order:

1. **Exact Match / rule-based checks**
2. **Rubric**
3. **Pairwise Comparison**
4. **LLM Judge**
5. **Human Review** where consequence or ambiguity justifies it

This is not a maturity ladder. It is a bias toward objective evidence first, then more subjective methods only where needed.

---

## Relationship to Other Documents

- `research/topics/evaluation-prompt-testing.md`
- `research/principles-only.md`
- `research/observability-schema.md`
- `research/vocabulary.md`
