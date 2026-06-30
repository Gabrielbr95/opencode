---
name: gen-playwright-mode
description: Apply browser automation best practices. Robust selectors, logged interactions, screenshot on failure.
---

# gen-playwright_mode

## When to load

Load when implementing browser automation with Playwright (Python). Particularly relevant when automating legacy web UIs that weren't designed for programmatic access.

## Selector Priority

Prefer selectors in this order — stop at the first that works reliably:

1. **ARIA role + accessible name**: `page.get_by_role("button", name="Submit")`
2. **Label text**: `page.get_by_label("Work Order Number")`
3. **Placeholder text**: `page.get_by_placeholder("Enter tag...")`
4. **Test ID** (if present): `page.get_by_test_id("submit-btn")`
5. **Text content**: `page.get_by_text("Approve")`
6. **CSS selector** (stable class, not generated): `page.locator(".work-order-form")`
7. **XPath** (last resort, avoid unless nothing else works)

Never use positional selectors like `nth-child` or index-based locators unless the position is semantically meaningful (e.g., "the first unread row in this table").

## Reliability Rules

- Add explicit waits for elements that appear after async operations: `locator.wait_for(state="visible")`
- Do not use `time.sleep()`. Use Playwright's built-in wait mechanisms.
- After navigation, wait for a known stable element before proceeding.
- For forms, fill fields in the order a human would — some legacy systems have field-dependency logic.

## Logging

Log every significant interaction:

```python
log.info("Navigating to %s", url)
log.info("Filling Work Order field: %s", wo_number)
log.info("Clicking Submit button")
log.info("Waiting for confirmation message")
```

## Error Handling

- On any exception, capture a screenshot before re-raising:

```python
except Exception as e:
    page.screenshot(path=f"error_{timestamp}.png")
    log.error("Failed at step '%s': %s", step_name, e)
    raise
```

- Use descriptive step names so screenshots are traceable to the operation that failed.

## Resilience to UI Changes

- Avoid brittle selectors that break when a developer renames a CSS class.
- If the UI changes frequently, wrap each major interaction in a named function so fixes are localized:

```python
def submit_work_order(page, wo_number):
    page.get_by_label("Work Order").fill(wo_number)
    page.get_by_role("button", name="Submit").click()
```

## Windows / Corporate Environment Notes

- Playwright installs browsers locally — no network connectivity required at runtime.
- Use `playwright install chromium` (or the specific browser needed) — full browser install requires ~150MB.
- If admin is not available for system-level install, use `pip install playwright` in a virtualenv and run `python -m playwright install chromium`.
