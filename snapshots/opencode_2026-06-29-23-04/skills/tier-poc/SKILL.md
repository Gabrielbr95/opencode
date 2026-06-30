---
name: tier-poc
description: >-
  Coding guidelines for the proof-of-concept tier. Use when the builder agent
  is working on a task whose tier is "poc" in plan/tasks.md. Minimal throwaway code
  to answer "can this be done?" and prove feasibility.
---

# Tier: PoC (Proof of Concept)

Build the smallest possible snippet to prove feasibility. This is exploratory, throwaway code.

## Rules

1. Focus exclusively on the riskiest unknown variable (e.g., parsing a complex sensor output, interfacing with a new library).
2. Stub, fake, or hardcode all surrounding systems (databases, network, standard file I/O).
3. Do not spend time optimizing, styling, abstracting, or structuring.
4. Insert clear uppercase warning comments next to hardcoded or stubbed components:
   - `# POC ONLY: Hardcoded database connection`
   - `# POC ONLY: Stubbed API response`
5. Explicitly list the core assumptions or risk factors being verified.
6. Minimal error handling — only what prevents a false positive result.
7. No tests unless testing is the point of the POC.

## Feasibility Verdict

After the standard task report, also output:

```
Feasibility: SUCCESS / FAILED / RISKY
Proven: <what the POC confirmed>
Risks: <what remains unproven or could break in production>
```

## Example

Question: "Can pdfplumber extract text from our scanned maintenance records?"

```python
import pdfplumber

with pdfplumber.open("sample_record.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(repr(text[:500]))
```

Feasibility: SUCCESS with caveats
Proven: pdfplumber opens the file and returns text from machine-generated PDFs.
Risks: scanned-only pages return None — OCR preprocessing (e.g. pytesseract) required for those.
