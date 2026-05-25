# Automation Pack: Skills

## Purpose
This document defines the core procedures and techniques required to write resilient automation scripts.

## Core Skills
| Skill | Usage |
|-------|-------|
| `python-script-automation` | Writing the core logic |
| `browser-automation-playwright` | UI interactions via Playwright |
| `browser-automation-selenium` | UI interactions via Selenium |
| `error-retry-strategy` | Exponential backoff logic |
| `reporting-automation` | Generating summary outputs |
| `secure-logging-review` | Ensuring tokens aren't printed |
| `environment-variable-management` | Loading `.env` files safely |
| `test-plan-create` | QA strategy |
| `regression-test-checklist` | Preventing breakage |
| `troubleshooting-guide` | Documenting edge cases |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Scripting phase: Load `python-script-automation`, `environment-variable-management`.
- Browser phase: Load `browser-automation-playwright` or `browser-automation-selenium`.
- Resilience phase: Load `error-retry-strategy`, `secure-logging-review`.

## Progressive Loading Notes
Only load browser automation skills if the script actually needs to interact with a web page. Use direct API calls instead whenever possible.

## Validation Notes
`secure-logging-review` must be completed before the script is merged to ensure no credentials are hardcoded or printed.
