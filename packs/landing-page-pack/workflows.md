# Landing Page Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to build marketing and landing pages safely.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For initial structure and copy planning. |
| `frontend-ui.workflow.md` | For building out the page visually. |
| `enhance-feature.workflow.md` | For optimizing conversion rates or SEO. |
| `verify.workflow.md` | For final accessibility and responsiveness checks. |
| `document.workflow.md` | For updating component libraries or guidelines. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New page: `plan.workflow.md` followed by `frontend-ui.workflow.md`.
- Optimizing an existing page: `enhance-feature.workflow.md`.

## Parallel/Sequential Strategy
- Copywriting and UX design can happen in parallel during the planning phase.
- Implementing the HTML/CSS must be sequential.
- QA testing (visual, responsive, accessibility) can happen in parallel.

## Validation Strategy
- Validation requires visual confirmation.
- Output from accessibility tools or build scripts is required as evidence.
