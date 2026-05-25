# Web App Pack: Skills

## Purpose
This document defines the core procedures and techniques required to implement web application features securely and consistently.

## Core Skills
| Skill | Usage |
|-------|-------|
| `project-intake` | Initial discovery |
| `codebase-map` | Directory scanning |
| `existing-patterns-detection` | Finding existing UI/API patterns |
| `task-breakdown` | Planning |
| `implementation-plan` | Documenting the plan |
| `acceptance-criteria-writing` | Defining success |
| `definition-of-done` | Ensuring completeness |
| `react-component-create` | Building UI |
| `frontend-api-integration` | Connecting UI to API |
| `api-contract-design` | Designing JSON structures |
| `rest-api-implementation` | Building endpoints |
| `request-validation` | Input sanitization |
| `database-schema-design` | Table/collection changes |
| `build-validation` | Running npm run build |
| `regression-test-checklist` | Preventing breakage |
| `security-release-checklist` | Final security check |
| `readme-create` | Updating docs |

## Optional Skills
(None defined by default. Add custom skills for specific libraries if needed, e.g., `redux-state-management`).

## Skill Loading Logic
- Planning phase: Load `project-intake`, `codebase-map`, `implementation-plan`.
- Frontend phase: Load `react-component-create`, `frontend-api-integration`.
- Backend phase: Load `api-contract-design`, `rest-api-implementation`, `request-validation`.

## Progressive Loading Notes
Do not load database design skills if the task is purely frontend UI styling.

## Validation Notes
`build-validation` and `regression-test-checklist` are strictly required before any web app task can be considered complete.
