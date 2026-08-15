# Decision Log

## [001] OMP will be evaluated as a parallel run, not a replacement
- **Date:** 2026-08-06
- **Context:** The user wants a migration plan for OMP but does not want OMP to replace this repository or become the active harness here.
- **Options Considered:** Replace the current repo runtime vs run OMP separately in parallel.
- **Decision:** Plan for a separate-folder OMP setup that runs alongside the current opencode harness.
- **Rationale:** This preserves the working repo, lowers risk, and keeps the evaluation bounded to similarity of configuration rather than immediate cutover.

## [002] The planning tier is POC
- **Date:** 2026-08-06
- **Context:** The user asked for a migration/configuration plan focused on feasibility rather than a full long-lived migration program.
- **Options Considered:** POC vs Script vs Application.
- **Decision:** Treat the planning work as POC tier.
- **Rationale:** The core question is whether OMP can be configured similarly enough to justify a side-by-side trial. That is a feasibility question, so the lighter planning tier fits.

## [003] Success boundary is similar-enough configuration, not full parity
- **Date:** 2026-08-06
- **Context:** The user defined the migration endpoint as only needing OMP configured similarly to the current setup.
- **Options Considered:** Full workflow reproduction vs default-runtime cutover vs similar-enough config behavior.
- **Decision:** Aim only for similar-enough configuration behavior in the first pass.
- **Rationale:** This keeps the trial small and honest, avoids premature parity chasing, and matches the stated user goal.

## [004] Configuration-first approach before extension work
- **Date:** 2026-08-06
- **Context:** OMP exposes extensions and broader built-ins, but the user asked for a plan on configuring it similarly to the current setup.
- **Options Considered:** Start with custom OMP extensions vs start with documented config surfaces and built-ins.
- **Decision:** The plan will prioritize documented config, settings, context files, MCP, skills, and approval surfaces before any extension development is considered.
- **Rationale:** This is the lightest useful path for a POC and gives a cleaner answer to whether OMP can be adopted by configuration alone.

## [005] Separate-folder isolation is part of the plan, not an optional detail
- **Date:** 2026-08-06
- **Context:** The user explicitly wants OMP in another folder and does not want it to replace this repo.
- **Options Considered:** Reuse this repository directly vs set up a dedicated OMP trial workspace.
- **Decision:** The plan assumes a dedicated OMP trial folder/workspace separate from this repository.
- **Rationale:** This reduces accidental drift, keeps the active harness stable, and makes rollback trivial.
