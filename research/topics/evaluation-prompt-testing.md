# Evaluation / Prompt Testing

## Summary
- Prompts and agent workflows should be treated like software artifacts that need tests, baselines, and regression checks.
- The durable ideas are: define success criteria first, test representative and edge-case behavior, evaluate more than answer quality, and feed failures back into the test set.
- For agentic systems, evaluation must include workflow behavior such as tool use, handoffs, stopping decisions, latency, and cost.

## Motivation
- This repository will only improve if changes to prompts, skills, and orchestration patterns can be compared against evidence instead of anecdotes.
- Evaluation keeps the system from drifting as prompts, models, tools, and repo structure evolve.

## Problem Statement
- AI systems can sound good while being wrong, inconsistent, unsafe, or operationally inefficient.
- The design problem is how to make prompt and agent changes measurable, comparable, and regression-resistant over time.

## Key Concepts
- Success criteria
- Offline vs online evaluation
- Datasets / fixtures
- Traces
- Graders / evaluators
- Behavioral testing
- Multi-metric evaluation
- LLM-as-judge
- Regression testing

## Principles vs Implementations
### Principles
- Define measurable success before tuning prompts.
- Test behaviors and failure modes, not just average accuracy.
- Use multiple metrics where the task demands it.
- Start with objective graders where possible, then use LLM judges selectively.
- Evaluate agent workflows through traces, not only final answers.
- Feed real failures back into the benchmark set.
- Keep the durable truth in portable datasets, rubrics, and grader logic rather than vendor dashboards.

### Implementations / Examples
- Anthropic prompt eval guidance
- OpenAI eval and agent-eval docs
- LangSmith offline/online eval workflow
- Promptfoo test-driven prompt development
- CheckList behavioral testing
- HELM multi-metric evaluation
- G-Eval for LLM-as-judge

## Design Patterns
- **Success-criteria-first**: define the scorecard before prompt iteration.
- **Golden dataset + edge-case suite**: representative cases plus targeted failures.
- **Trace-first, benchmark-second**: inspect workflow traces, then formalize tests.
- **Layered graders**: exact match → rule/schema checks → LLM judge → human review.
- **Pairwise comparison**: compare prompt A vs prompt B on the same cases.
- **Offline-to-online feedback loop**: benchmark pre-release, monitor real traffic, add failures back to tests.
- **Multi-metric release gate**: task score, safety, latency, cost, workflow correctness.

## Advantages
- Reduces prompt-tuning guesswork.
- Catches workflow bugs beyond answer quality.
- Makes changes comparable over time.
- Improves edge-case coverage.
- Supports regression testing and disciplined iteration.
- Creates durable evidence for architectural decisions.

## Disadvantages
- Building good datasets takes work.
- Poor graders can create false confidence.
- LLM-as-judge is useful but biased and less stable than objective checks.
- Online evaluation increases operational cost.
- Teams can overfit to the benchmark instead of the actual job.

## Tradeoffs
- **Exact checks vs semantic judges**: objective and narrow versus flexible and subjective.
- **Offline vs online**: controlled and repeatable versus realistic and noisy.
- **Broad benchmark vs task-specific suite**: general perspective versus shipping relevance.
- **Large dataset vs high annotation quality**: more coverage versus cleaner signal.
- **Trace debugging vs dashboards**: why it failed versus whether the new version is better overall.

## Relationships to Other Topics
- Evaluation should compare [Agent Architectures](./agent-architectures.md) instead of choosing by taste.
- It is necessary for testing context sufficiency in [Context Engineering](./context-engineering.md).
- It should measure planning quality and orchestration behavior from [Planning Systems](./planning-systems.md).
- It can test skill triggering, usefulness, and boundaries from [Skill Systems](./skill-systems.md).

## Practical Applications for This Repository
- Treat every prompt, skill, or workflow change as something that should have at least lightweight evidence.
- Keep reusable fixtures for happy-path, edge-case, safety, and workflow-behavior tests.
- Maintain a small evaluator library: format checks, exact/categorical checks, safety checks, tool-use checks, and rubric-based quality checks.
- Capture production or review failures as permanent regression cases.
- Keep representative traces or trace summaries for agent workflows.
- Gate major workflow changes on a scorecard, not a single subjective opinion.

## Open Questions
- How reliable are LLM judges across different domains and over time?
- How should workflow-level success be scored when quality, latency, cost, and safety all matter?
- How much synthetic data should be used in eval sets?
- How can benchmark overfitting be detected early?
- What is the right balance between automated volume and human review?

## Clarifications and Common Misconceptions
- **Prompt testing is not just manual spot-checking.** Real evaluation needs explicit criteria, repeatable cases, and regression tracking.
- **Evaluation is not only about final answer quality.** For agents, tool choice, tool arguments, retrieval quality, handoffs, latency, and side effects matter too.
- **Observability is not the same as evaluation.** Traces supply evidence; evaluators decide whether the run was good.
- **LLM-as-judge is useful but not universal.** It should sit beside deterministic checks, pairwise comparisons, and human review—not replace them all.
- **Offline success does not guarantee production success.** Offline and online evaluation answer different questions and operate under different evidence constraints.

## References
- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/) — ACL Anthology, 2020. Foundational paper for software-style behavioral testing.
- [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) — arXiv / TMLR noted, 2022/2023. Strong source for multi-metric and multi-scenario evaluation.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634) — arXiv, 2023. Useful for LLM-as-judge strengths and bias caveats.
- [Define success criteria and build evaluations](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success) — Anthropic Docs, year not visible. Practical guide for measurable success criteria and task-specific evals.
- [Working with evals](https://platform.openai.com/docs/guides/evals) — OpenAI API Docs, year not visible. Programmatic eval concepts and notes about platform deprecation timeline.
- [Evaluate agent workflows](https://platform.openai.com/docs/guides/agent-evals) — OpenAI API Docs, year not visible. Strong source for trace-based and workflow-level evaluation.
- [LangSmith Evaluation](https://docs.smith.langchain.com/evaluation/concepts) — LangSmith Docs, year not visible. Useful framing of offline vs online evaluation and production feedback loops.
- [Intro | Promptfoo](https://www.promptfoo.dev/docs/intro/) — Promptfoo Docs, 2026 update shown. Practical open-source approach for test-driven LLM development and CI-oriented prompt testing.
- [Reduce prompt leak](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak) — Anthropic docs, year not clearly visible. Useful example that extra defensive complexity must itself be evaluated.
