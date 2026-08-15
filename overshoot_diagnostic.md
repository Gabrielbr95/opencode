# Script-Tier Overshoot Diagnostic

## Problem Summary

The original goal was a **Script-tier** tool:

1. authenticate to SINPEP
2. search for a `PadraoId`
3. download all available files into a folder named after the `PadraoId`
4. repeat for all `PadraoId`s listed in a text file

The implementation effort overshot that target and drifted toward a small application/toolkit with:
- package structure
- CLI plumbing
- manifest tracking
- multiple modules and abstractions
- broader state handling
- more architecture than the user wanted

This was a mismatch with the user's actual intent:
- one script
- minimal moving parts
- no manifest
- no metadata layer unless strictly required
- no CLI required
- tolerate simple failure handling
- assume input `PadraoId`s are correct

## Diagnostic: Why the Overshoot Happened

### 1. Durable planning bias
The session prompt strongly emphasizes:
- durable truth in `plan/*`
- continuity across long offshore gaps
- documenting decisions and progress

This encouraged a more formal project structure than the task required.

### 2. Planning/execution separation pressure
The prompt strongly enforces:
- explicit planning before broader execution
- structured task breakdown
- plan approval gates

Once planning began, the work expanded into “project mode” instead of staying in “simple script mode”.

### 3. Maintainability/safety bias
The prompt emphasizes:
- loud failures
- solo maintainability
- boring, robust engineering
- clarity after long interruptions

Those are good defaults, but in this case they were applied at the wrong scale, resulting in abstractions and structure that were not justified for Script tier.

### 4. Orchestration/task mechanics
The prompt also emphasizes:
- task-state tracking in `plan/tasks.md`
- marking work in progress before editing
- proportional review
- subagent orchestration

That added process overhead and nudged the work toward a larger architecture.

### 5. Internal API/auth uncertainty
Because the task involved:
- internal corporate auth
- incomplete endpoint knowledge
- payload/path uncertainty
- live validation needs

the implementation shifted into defensive engineering:
- wrappers
- typed structures
- intermediate layers
- richer state handling

For Script tier, uncertainty should have pushed toward a quick direct script first, not a larger architecture.

## Core Failure Mode

The key failure was not the existence of the prompt rules themselves.

The real failure was **mode selection**.

The prompt also explicitly says to:
- choose the **lightest workable mode**
- prefer **direct edit** for small work
- optimize Script tier for **simplicity**
- avoid unnecessary complexity

Those instructions should have dominated, but they were overridden by the planning/maintainability/orchestration pressures above.

## Corrective Guidance for Future Script-Tier Work

For this user, Script tier should default to:

- **one script** unless impossible
- **no package structure** unless clearly needed
- **no CLI** unless explicitly requested
- **no manifest** unless the user asks for resumability/state tracking
- **no tests** unless needed to unblock a real integration issue
- **no abstractions** unless the same pattern repeats and the benefit is obvious
- solve today's problem first, refactor later only if forced by real pain

## Better Constraint Template

A useful future instruction pattern for this user is:

> Script tier, strict minimalism.  
> One file unless impossible.  
> No package.  
> No CLI unless requested.  
> No manifest.  
> No tests unless needed to unblock.  
> No abstractions unless repeated twice.  
> Solve the immediate problem first.

## Current Recommended Reset

The project should be refactored down to:
- one runnable script
- one input text file of `PadraoId`s
- one output directory
- minimal auth call to `petro-auth`
- minimal SINPEP calls to list/download available files
- plain logging to console
- “if file fails, log and move on”

Everything else is optional.
