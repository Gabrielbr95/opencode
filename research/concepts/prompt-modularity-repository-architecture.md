# Prompt Modularity / Repository Architecture

## Summary
- Prompt repositories work better when prompts are treated as maintainable software artifacts rather than magic strings.
- The durable architecture is modular: separate stable policy from runtime context, keep prompts close to the features they support, use clear override rules, and back changes with evals.
- Good structure reduces duplication, drift, and hidden behavior changes.

## Motivation
- This repository is itself a prompt/agent repository, so structure and modularity are not abstract concerns here.
- Better prompt architecture makes the repo easier to understand, change, and audit after long gaps.

## Problem Statement
- Prompt repositories decay when instructions are copied instead of composed, overrides are implicit, dynamic context is baked into stable prompts, and prompt changes are not tested.
- The design problem is how to organize prompts, templates, tools, examples, and evals so the system stays understandable and evolvable.

## Key Concepts
- Prompts as code-managed artifacts
- Layered instructions
- Prompt templating
- Prompt repositories
- Evaluation matrix
- Sectioned prompts
- Late-bound context
- Typed dynamic inputs
- Override precedence

## Principles vs Implementations
### Principles
- Keep prompts near the feature or agent they support.
- Separate stable instructions from volatile runtime data.
- Prefer composition over copy-paste.
- Make override precedence explicit.
- Back changes with fixtures and evals.
- Keep repo-wide guidance small and local guidance specific.

### Implementations / Examples
- AGENTS.md-style layered instructions
- Prompt builders/modules in code
- Prompt templates with variables
- Promptfoo-style prompt/eval matrix
- PromptSource-style repository of prompt artifacts
- Sectioned prompt formats with roles/examples/context

## Design Patterns
- **Layered instruction stack**: global defaults, repo-level norms, local overrides.
- **Prompt builder module**: build prompts from structured inputs.
- **Sectioned prompt format**: identity, instructions, examples, context.
- **Template + schema pairing**: wording handled by template, values handled by typed inputs.
- **Context late binding**: inject dynamic context at runtime.
- **Prompt + eval co-location**: keep tests close to prompts.
- **Directory-scoped specialization**: local rules close to the work area.

## Advantages
- Easier review and change tracking.
- Less duplication and drift.
- Better reuse across workflows.
- Clearer ownership and override rules.
- Safer experimentation with eval-backed changes.

## Disadvantages
- More upfront structure.
- Too much templating can hurt readability.
- Layering can confuse contributors if precedence is unclear.
- Excess modularity can fragment intent across too many files.

## Tradeoffs
- **Locality vs centralization**: relevance versus consistency.
- **Plain text vs templating**: readability versus reuse.
- **Few large prompts vs many modules**: context continuity versus composability.
- **Static instructions vs dynamic context**: predictability versus power.

## Relationships to Other Topics
- Repository architecture affects how [Skill Systems](./skill-systems.md) are defined and invoked.
- It provides the structural home for [Tool-Use Policy and Permission Systems](./tool-use-policy-and-permission-systems.md).
- It benefits from [Observability / Traceability](./observability-traceability.md) when tracing prompt versions and behavior changes.
- It should be stabilized through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).

## Relevance to This Repository
- Keep top-level operating rules small and stable.
- Add local overrides only where behavior genuinely differs.
- Separate policy prompts from task prompts.
- Keep dynamic context loaders separate from base prompt text.
- Co-locate prompts, examples, and eval fixtures when practical.
- Document precedence rules explicitly so contributors know which file wins.
- Distinguish wording refactors from behavioral or safety changes in review.

## Open Questions
- What is the right unit of reuse: whole prompt, section, example set, or policy fragment?
- How much templating is too much?
- Should prompt repositories version prompts like APIs?
- What metadata should prompt files carry: owner, risk level, dependencies, model assumptions?

## Clarifications and Common Misconceptions
- **Prompt modularity is not just splitting text into smaller files.** The real issue is scope, loading behavior, authority, and override rules.
- **Repository instructions, prompt files, skills, and config are different layers.** Ambient repo guidance, task-specific prompts, on-demand capability modules, and runtime control-plane settings should not be collapsed into one bucket.
- **More modularity is not automatically better.** Too many tiny fragments can make behavior harder to inspect and review.
- **Central registries are not the only or default answer.** Many current recommendations prefer prompts/versioning near the feature or workflow they support.
- **Prompt architecture does not replace policy or CI.** Some rules belong in enforcement, tests, or tooling rather than in always-injected instructions.

## References
- [PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts](https://arxiv.org/abs/2202.01279) — arXiv / ACL Demo, 2022. Foundational paper on prompts as shareable, data-linked artifacts.
- [Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — OpenAI docs, year not visible. Recommends code-managed prompts, sectioning, and eval-backed iteration.
- [Custom instructions with AGENTS.md](https://developers.openai.com/codex/agent-configuration/agents-md) — OpenAI docs, year not visible. Documents layered instruction discovery and root-to-leaf precedence.
- [Prompt template syntax](https://learn.microsoft.com/en-us/semantic-kernel/concepts/prompts/prompt-template-syntax) — Microsoft Learn / Semantic Kernel, 2024. Concrete example of prompt modularity through variables and templates.
- [Promptfoo configuration guide](https://www.promptfoo.dev/docs/configuration/guide/) — Promptfoo docs, 2026. Practical example of repository-scale eval organization around prompts and tests.
- [Codex build skills](https://learn.chatgpt.com/codex/build-skills) — OpenAI Codex docs, year not clearly visible. Helpful distinction between always-on repo guidance and progressively loaded skills.
- [GitHub Copilot response customization](https://docs.github.com/en/copilot/concepts/prompting/response-customization) — GitHub docs, year not clearly visible. Useful distinction between repo-wide instructions, prompt files, and precedence.
