# Implementation Plan

## Slice 1: Research workspace foundation
- [x] 1. Create the initial `research/` directory structure and index files for incremental topic-based research. (Verification: `research/` contains a README/index plus clear locations for topic notes and backlog items.)
- [x] 2. Define a consistent note template for topic research with required sections and citation handling. (Verification: at least one created note or template shows the agreed structure, including references.)

## Slice 2: First batch of foundational research notes
- [x] 3. Research agent architectures and skill systems from web sources and write cited topic notes. (Verification: both topic files exist, are structured, and include traceable references.)
- [x] 4. Research context engineering and planning systems from web sources and write cited topic notes. (Verification: both topic files exist, are structured, and include traceable references.)
- [x] 5. Research evaluation / prompt testing from web sources and write a cited topic note. (Verification: the topic file exists, is structured, and includes traceable references.)

## Slice 3: Repository coherence and next-step backlog
- [x] 6. Cross-link the initial notes, update the index, and record follow-up questions or future topics. (Verification: `research/index.md` and backlog entries point to the created notes and identify next research directions.)

## Slice 4: High-value backlog expansion
- [x] 7. Select the next high-value backlog and adjacent discovered topics, then record the expanded research slice in the plan. (Verification: the chosen topics are reflected in `plan/tasks.md` and align with the existing backlog and discovered concepts.)
- [x] 8. Research memory systems and human-in-the-loop control points from web sources and write cited topic notes. (Verification: both topic files exist, are structured, and include traceable references.)
- [x] 9. Research tool-use policy design / permission systems and prompt modularity / repository architecture from web sources and write cited topic notes. (Verification: both topic files exist, are structured, and include traceable references.)
- [x] 10. Research observability / traceability for agent systems as a newly discovered adjacent topic and write a cited topic note. (Verification: the topic file exists, is structured, and includes traceable references.)

## Slice 5: Index and backlog refresh after expansion
- [x] 11. Cross-link the expanded topic set, update reading order/index, and refresh backlog items based on the new findings. (Verification: `research/index.md` and `research/backlog.md` reflect the added notes and new follow-up directions.)

## Slice 6: Deepening and misconception audit
- [x] 12. Identify likely misconceptions, oversimplifications, and blurred boundaries across the existing research topics, then record the refinement scope. (Verification: the refinement focus is reflected in the plan and targets the existing topic set rather than expanding breadth.)
- [x] 13. Research deeper distinctions and common misconceptions for architecture, context, memory, planning, skills, permissions, HITL, evaluation, observability, and prompt repository structure. (Verification: research findings clearly distinguish adjacent concepts and surface important caveats.)
- [x] 14. Revise the existing topic notes with clarified definitions, misconception callouts, and stronger conceptual boundaries. (Verification: updated notes contain explicit clarifications without replacing the original topics.)

## Slice 7: Vocabulary synthesis
- [x] 15. Synthesize a repository vocabulary from the researched topics and define clear boundaries between adjacent terms. (Verification: a `research/vocabulary.md` file exists and distinguishes the main concepts without collapsing them together.)
- [x] 16. Update the research index and backlog to point to the vocabulary as a synthesis artifact. (Verification: `research/index.md` and/or `research/backlog.md` reference the vocabulary document.)

## Slice 8: Control-boundaries synthesis
- [x] 17. Synthesize the practical control-boundary model across permissions, approvals, HITL, guardrails, side effects, and durable memory writes. (Verification: a `research/control-boundaries.md` file exists and clearly distinguishes these control layers.)
- [x] 18. Update the research index and backlog to point to the control-boundaries synthesis. (Verification: `research/index.md` and/or `research/backlog.md` reference the control-boundaries document.)

## Slice 9: Principles-only synthesis
- [x] 19. Distill the durable, implementation-agnostic design principles from the researched topics into a single synthesis note. (Verification: a `research/principles-only.md` file exists and extracts reusable rules rather than repeating topic summaries.)
- [x] 20. Update the research index and backlog to point to the principles-only synthesis. (Verification: `research/index.md` and/or `research/backlog.md` reference the principles-only document.)

## Slice 10: Memory and observability policy foundation
- [x] 21. Synthesize a repository memory policy from the existing research and write `research/memory-policy.md`. (Verification: the note defines memory tiers, durable-write gates, provenance requirements, and retirement/supersession rules grounded in the current research base.)
- [x] 22. Update the research index and backlog to point to the memory-policy synthesis and capture any new follow-up questions it reveals. (Verification: `research/index.md` and `research/backlog.md` reference the new artifact and remain consistent with its scope.)
- [x] 23. Synthesize the minimum useful observability schema for this workflow and write `research/observability-schema.md`. (Verification: the note defines canonical trace or event fields for sessions, tasks, tool calls, approvals, durable writes, decisions, and failures.)
- [x] 24. Update the research index and backlog to point to the observability-schema synthesis and record any newly exposed gaps. (Verification: `research/index.md` and `research/backlog.md` reference the new artifact and stay aligned with the existing observability research.)

## Slice 11: Decision-support comparison matrices
- [x] 25. Create a workflow-pattern comparison matrix covering chain, route, parallelize, orchestrator-worker, evaluator-optimizer, and ReAct. (Verification: a comparison artifact exists and makes the tradeoffs, fit criteria, and failure modes easy to compare.)
- [x] 26. Create an evaluation-method comparison matrix covering exact match, rubric, pairwise, LLM judge, and human review, then update the index/backlog as needed. (Verification: a comparison artifact exists and the research navigation points to it clearly enough for future reuse.)

## Slice 12: Governance and architecture expansion
- [ ] 27. Research the next expansion topics — likely policy-as-code, multi-agent collaboration, reflection/self-critique, model routing, and RAG for prompt repositories — and refine this slice when one becomes active. (Verification: the chosen topic is justified against the backlog and broken into concrete tasks before execution begins.)

## Slice 13: Workflow-to-operational alignment kickoff
- [x] 28. Re-anchor the durable plan around the workflow-alignment implementation phase and keep the next slice small, explicit, and grounded in the revised `workflow.md`. (Verification: `plan/spec.md` and `plan/tasks.md` describe the alignment objective, scope, and immediate sequence without stale research-only framing.)
- [x] 29. Review `AGENTS.md` and all files under `agents/*`, then identify where the agent layer drifts from the revised workflow intent. (Verification: the main drift points and their relative priority are summarized clearly enough to justify the next prompt edits.)
- [x] 30. Align `agents/generalist.md` with the revised workflow responsibilities, especially session ownership, work-mode selection, planning vs execution boundaries, delegation limits, and pragmatic solo-maintainable defaults. (Verification: the prompt clearly encodes these responsibilities without importing procedural detail that belongs in skills.)
- [x] 31. Align `agents/reviewer.md` and any small follow-up agent prompts needed so review expectations stay proportional to work type, tier, and durable-write risk. (Verification: the prompt distinguishes adversarial review from blanket maximal review and any follow-up agent edits remain small and justified.)
- [x] 33. Remove harness-edit-specific instructions from the agent layer so `agents/*` stays general and procedural detail is deferred to later skills. (Verification: `agents/generalist.md` and `agents/reviewer.md` keep general role boundaries without instructions aimed specifically at editing prompts, skills, rules, or config.)
- [x] 32. Reassess the key workflow skills only after the agent-layer alignment is complete, then define the next skill-edit slice before modifying those skills. (Verification: the next skill scope is explicitly identified from observed drift rather than broadened preemptively.)

## Slice 14: Workflow-skill alignment planning
- [x] 39. Review all top-level workflow skills before proposing changes, using the research syntheses and revised `workflow.md` as the comparison frame. (Verification: the full skill set has been inspected, good existing ideas are preserved, and the main drift patterns are summarized before any skill-edit proposal is made.)
- [x] 34. Align `skills/plan-project/SKILL.md` with the revised workflow's planning sufficiency rules, progressive disclosure, and proportional ceremony expectations. (Verification: the planning skill requires enough structure for the tier and scope, frames planning as broader than just pre-coding work, and avoids forcing unnecessary planning for small or low-risk work.)
- [x] 35. Align `skills/workflow-execute/SKILL.md` so it stays within the approved execution scope and uses right-sized verification without becoming open-ended orchestration. (Verification: the execution skill stays implementation-focused, treats scope as the controlling boundary, distinguishes bounded execution from autonomous batch orchestration, avoids hardcoding single-task or multi-task wording into the procedure, and does not direct subagents into orchestration loops.)
- [x] 36. Decide and record whether harness-edit-specific procedure should live in a dedicated later skill or as a narrowly scoped branch in existing skills before editing review/reconciliation procedures. (Verification: the future procedure location is explicit enough to avoid smuggling harness-maintenance instructions into general-purpose skills.)
- [x] 37. Align `skills/review-code/SKILL.md`, `skills/review-plan/SKILL.md`, and `skills/reconcile-work/SKILL.md` as a coordinated review/reconciliation set with proportional boundaries and revised workflow terminology. (Verification: the skills distinguish code review from plan review, use consistent terminology and escalation boundaries, stay strict where consequence is high, and avoid unnecessary full-project convergence on every micro-step.)
- [x] 41. Clean up stale skill descriptions so frontmatter and trigger wording match the updated workflow behavior. (Verification: touched skill descriptions no longer contradict their current body text or the revised workflow boundaries.)

## Slice 15: Tier-skill cleanup planning
- [x] 40. Reassess `skills/tier-poc/SKILL.md`, `skills/tier-script/SKILL.md`, and `skills/tier-application/SKILL.md` after the core workflow skills are aligned, then decide whether their current guidance is too absolute for the revised proportional workflow. (Verification: the tier-skill follow-up is explicitly deferred, and any later edits are justified by concrete wording drift rather than broad stylistic cleanup.)

## Slice 17: Tier-skill alignment follow-up
- [x] 42. Align `skills/tier-poc/SKILL.md` so it preserves the POC bias toward speed and learning without hardcoding unnecessary absolutes about tests, edge cases, or code shape. (Verification: the guidance stays lightweight and POC-friendly while leaving room for proportional judgment based on scope and consequence.)
- [x] 43. Align `skills/tier-script/SKILL.md` so it keeps simplicity and reliability goals without turning preferences like logging, configuration, or function style into universal mandates. (Verification: the guidance remains practical for recurring automation while allowing the lightest boring solution that preserves reliability.)
- [x] 44. Align `skills/tier-application/SKILL.md` so it emphasizes maintainability and safety without forcing blanket ceremony on every task inside an Application-tier project. (Verification: the guidance reflects proportional rigor, work-type sensitivity, and solo-maintainable practicality rather than universal heavyweight rules.)

## Slice 18: Light consistency pass across operational files
- [x] 45. Lightly review `AGENTS.md`, `agents/*`, and `skills/*` for stale wording, small boundary leaks, and obvious consistency drift; make only minor corrections in this pass. (Verification: any touched files receive only narrow fixes, and the remaining next-step improvement points are summarized explicitly rather than folded into an unbounded rewrite.)

## Slice 19: Deferred operational polish backlog
- [x] 46. Decide whether `AGENTS.md` should explicitly name the direct-edit / human-in-the-loop / autonomous mode spectrum and a short side-effects-drive-friction rule. (Verification: either the ambient file gains a clearly justified small refinement, or the current omission is consciously retained.)
- [x] 47. Harmonize `agents/explorer.md` and `agents/researcher.md` slightly further so their role, search, and output expectations read as a cleaner parallel pair without over-specializing them. (Verification: any edits stay narrow and improve symmetry/clarity without changing their core boundaries.)
- [x] 48. Review the formatter skills as a set — `format-spec`, `format-tasks`, `format-decisions`, `format-architecture`, and `format-active-context` — to confirm their rigidity still matches the revised workflow. (Verification: either no change is needed, or only clearly justified schema/boundary adjustments are made.)
- [x] 49. Lightly harmonize `skills/diagnose-bug/SKILL.md` with the newer workflow terminology if doing so improves consistency without weakening its evidence-first loop. (Verification: any wording change preserves the strict root-cause discipline while aligning terms like scope, escalation, or evidence.)
- [x] 50. Review `skills/orchestrate-batch/SKILL.md` specifically for ownership, scope, and recursion-loop safety now that `workflow-execute` was tightened around session-owner escalation. (Verification: any changes preserve user-invoked autonomy while making ownership boundaries and loop resistance more explicit.)
- [x] 51. Recheck `skills/wrap-session/SKILL.md` against the current resume-baton policy to confirm its reread/update instructions are still the lightest useful version. (Verification: the wrap behavior remains aligned with `activeContext.md` as a short baton rather than a durable log.)

## Slice 16: Deferred harness-maintenance workflow follow-up
- [ ] 38. Design a dedicated AI self-improvement or harness-maintenance skill later, after the general workflow skills are aligned and the need is still justified by observed maintenance work. (Verification: the deferred skill scope is explicit, not implemented prematurely, and clearly separated from the general-purpose planning, execution, review, and reconciliation skills.)
