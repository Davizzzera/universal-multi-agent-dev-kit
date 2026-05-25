# Web App Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to build web application features safely.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For initial architecture. |
| `coordinate.workflow.md` | For managing frontend + backend tasks. |
| `create-feature.workflow.md` | For building new UI or endpoints. |
| `frontend-ui.workflow.md` | For styling and React tweaks. |
| `api-development.workflow.md` | For new API routes. |
| `database-change.workflow.md` | For schema migrations. |
| `test.workflow.md` | For writing and running tests. |
| `verify.workflow.md` | For final pre-commit health checks. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- Pure UI: `frontend-ui.workflow.md`
- Pure Backend: `api-development.workflow.md`
- Full feature involving both: `coordinate.workflow.md`

## Parallel/Sequential Strategy
- Frontend and backend discovery/reading can happen in parallel.
- Database schema changes MUST be sequential and committed before frontend API integration begins.

## Validation Strategy
- Validation requires running the test suite (`npm test`, `pytest`, etc.).
- UI changes require visual confirmation or component testing (e.g., Jest/RTL).
