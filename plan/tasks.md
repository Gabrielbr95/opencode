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
