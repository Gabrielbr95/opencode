---
name: gen-poc
description: Apply POC tier rules. Validate feasibility with the smallest possible throwaway code.
---

# gen-poc

## When to load

Load when tier is `poc`. The goal is to answer a specific unknown — not to build something usable.

## Rules

- Focus strictly on the unknown or risky variable. Stub, fake, or hardcode everything surrounding it.
- No optimization, abstraction, style, or packaging.
- No tests unless testing is the point of the POC.
- Minimal error handling — only what prevents a false positive result.
- Minimal dependencies — use only what is necessary to probe the unknown.
- Technical debt is irrelevant. This code is intended to be discarded.

## What to produce

The simplest snippet that gives a clear yes/no on the feasibility question.

Conclude with:
- **Verdict**: can it be done? (yes / no / yes with caveats)
- **Proven facts**: what the POC confirmed
- **Key risks**: what remains unproven or could break in production

## What to skip

- Error handling beyond "does it explode immediately"
- Generalization
- Cleanup
- Documentation

## Example

Question: "Can pdfplumber extract text from our scanned maintenance records?"

```python
import pdfplumber

with pdfplumber.open("sample_record.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(repr(text[:500]))
```

Verdict: YES with caveats
Proven: pdfplumber opens the file and returns text from machine-generated PDFs.
Key risks: scanned-only pages return None — OCR preprocessing (e.g. pytesseract) required for those.
