# Skill Systems

## Summary
- A skill system packages reusable capability so an agent can apply the same procedure repeatedly without re-explaining it every time.
- The durable principle is broader than any one product feature: make reusable, scoped capabilities first-class objects in the system.
- In practice, skills often combine instructions, metadata, scripts, templates, and optional reference files with on-demand loading.

## Motivation
- This repository already uses skills heavily, so it needs a clearer design language for what a skill is, what belongs in it, and what does not.
- A good skill system reduces repetition, context bloat, and prompt drift.

## Problem Statement
- Without a skill system, procedures get repeated in large prompts, outputs become inconsistent, and reusable know-how gets mixed together with one-off task instructions.
- The design problem is how to package procedural knowledge so agents can discover, load, execute, and compose it reliably.

## Key Concepts
- Reusable capability
- Skill metadata and discovery
- Progressive disclosure
- Instruction + script + resources split
- Skill registry / library
- Composition
- Temporal abstraction
- Separation of procedure from connectivity

## Principles vs Implementations
### Principles
- Package expertise once and reuse it many times.
- Keep discovery lightweight and explicit.
- Load detailed instructions only when needed.
- Separate procedure from access/connectivity.
- Prefer narrow, composable skills over giant monoliths.
- Use executable helpers where determinism matters.

### Implementations / Examples
- Anthropic Agent Skills
- Voyager skill library
- RL options / temporal abstraction
- Local repo skill folders with instructions + scripts + reference files

## Design Patterns
- **Folder-per-skill**: one directory per capability.
- **Metadata-driven discovery**: the description determines whether a skill is relevant.
- **Progressive disclosure**: load metadata first, then instructions/resources only if triggered.
- **Instruction + script split**: language for judgment, code for deterministic work.
- **Reference-file pattern**: keep schemas, examples, and templates beside the skill.
- **Skill composition**: chain multiple narrow skills for larger workflows.

## Advantages
- Less repeated prompting.
- More consistent behavior across sessions.
- Better context efficiency.
- Easier reuse of templates, scripts, and domain guidance.
- Cleaner separation between current task and reusable procedure.

## Disadvantages
- Discovery can fail when metadata is vague or overlapping.
- Skills can drift and become stale.
- Overlapping skills create ambiguity.
- Bundled scripts or instructions introduce trust and permission risks.
- The term itself is not fully standardized across the field.

## Tradeoffs
- **Broad vs narrow skills**: broad skills are easier to trigger; narrow skills compose better.
- **Natural language vs executable code**: language is flexible; code is more reliable for fixed operations.
- **Always-loaded vs on-demand**: always-loaded is simple; on-demand scales better.
- **Skill vs prompt**: prompt is one-off instruction; skill is reusable capability.
- **Skill vs MCP/connectivity**: skill is procedure; connectivity is how the system reaches data/tools.

## Relationships to Other Topics
- Skills are often invoked within [Agent Architectures](./agent-architectures.md).
- Skill loading is a form of [Context Engineering](./context-engineering.md).
- Skill invocation and composition should be checked through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).
- Many skills encode reusable planning procedures; see [Planning Systems](./planning-systems.md).

## Practical Applications for This Repository
- Keep skill metadata short, explicit, and trigger-oriented.
- Prefer one skill per capability instead of omnibus “god skills.”
- Separate connectivity docs from procedural skill instructions.
- Bundle examples, scripts, and reference files, but load them lazily.
- Review skills like code: provenance, side effects, permissions, and failure modes.

## Open Questions
- How should agents choose the right skill from a large library?
- How should overlapping skills be resolved?
- What is the right granularity for a skill?
- How should skill usefulness and trigger quality be evaluated over time?

## Clarifications and Common Misconceptions
- **A skill is not just another tool.** Tools perform actions; skills package reusable procedural knowledge, resources, and sometimes helper scripts.
- **A skill is not the same as a subagent.** Skills usually augment one agent context; subagents create a separate worker/context boundary.
- **A skill is not always high-authority policy.** In some systems, skill content is treated more like user-level task input than system-level instruction.
- **Progressive disclosure is the main point.** Skills help by avoiding always-loaded context, not just by improving file organization.
- **Skills have security implications.** Bundled scripts, resources, and instructions can become attack surfaces or exfiltration paths if treated like harmless docs.

## References
- [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — Anthropic Developer Docs, year not visible. Official documentation for a concrete skill-system implementation.
- [Skills](https://www.claude.com/skills) — Claude / Anthropic, year not visible. Product-level summary of reusable expertise and composition.
- [Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](https://claude.com/blog/skills-explained) — Anthropic blog, 2026. Clear distinctions between adjacent concepts.
- [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) — Anthropic blog, 2026. Practical guidance on planning, structuring, testing, and distributing skills.
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anthropic News, 2024. Useful contrast point: MCP is connectivity, not procedure packaging.
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) — arXiv, 2023. Example of a reusable executable skill library inside an autonomous agent.
- [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0004370299000521) — Artificial Intelligence / Elsevier, 1999. Classic precursor for “skills” as temporally extended actions.
- [OpenAI tools and skills](https://platform.openai.com/docs/guides/tools-skills) — OpenAI docs, year not clearly visible. Helpful distinctions between skills, tools, and skill loading behavior.
- [LangChain skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills) — LangChain docs, year not clearly visible. Useful clarification that skills are lighter-weight than subagents.
