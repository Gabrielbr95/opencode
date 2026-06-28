---
name: gen-low_waste
description: Load when the agent is over-exploring, looping on tool calls, or padding responses. Enforces minimal tool use and terse output.
---

# gen-low_waste

## When to load

Load when the agent is reading files you didn't ask for, chaining tool calls without stopping, or burying answers in prose. Also useful at the start of a long session where token cost matters.

## Tool Use Rules

- Only read a file if it was explicitly mentioned or is the direct source of the answer.
- Do not read related files "for context" unless asked.
- Do not glob or search directories speculatively.
- If a tool call doesn't produce a useful result, stop and ask — don't try another angle automatically.

## Loop Breaking

- Max 2–3 tool calls before stopping to report findings and ask how to proceed.
- If the answer isn't reachable with available information, say so clearly and stop.

## Output Rules

- Lead with the answer. No preamble.
- No summary of what tools were just called.
- No "as you mentioned", "based on the code I read", or similar padding.
- No suggestions or next steps unless explicitly asked.
- Bullet points over paragraphs. One sentence per point where possible.

## Example

User asks: "What does function X do?"

Bad response:
> I looked at several files to understand the broader context. Based on my reading of module A, module B, and the test suite, function X appears to be responsible for...

Good response:
> Validates the input schema and raises `ValueError` if required fields are missing.
