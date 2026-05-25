# API Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to build backend APIs safely.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For initial schema and contract planning. |
| `api-development.workflow.md` | For building endpoints. |
| `database-change.workflow.md` | For writing and testing migrations. |
| `security-review.workflow.md` | For auditing auth and inputs. |
| `test.workflow.md` | For executing the test suite. |
| `verify.workflow.md` | For pre-commit health checks. |
| `deploy.workflow.md` | For updating server environments. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New endpoints: `api-development.workflow.md`.
- Schema changes: `database-change.workflow.md`.
- Auth changes: MUST include `security-review.workflow.md`.

## Parallel/Sequential Strategy
- API Contract design and database schema design must happen sequentially and be approved before implementation.
- Testing and security reviews can happen in parallel after implementation.

## Validation Strategy
- Validation requires integration tests that hit the actual endpoints (e.g., using Supertest, Postman, or Pytest).
