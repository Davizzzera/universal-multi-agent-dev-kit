# Enterprise Pack: Skills

## Purpose
This document defines the core procedures and techniques required to govern, plan, and deliver enterprise-grade changes safely.

## Core Skills
| Skill | Usage |
|-------|-------|
| `coordinator-mode` | Multi-agent orchestration |
| `agent-routing` | Dispatching to specialists |
| `parallel-work-planning` | Parallelizing safe reads |
| `file-ownership-locking` | Preventing edit conflicts |
| `handoff-protocol` | Formal handoff documents |
| `project-intake` | Initial discovery |
| `codebase-map` | Full repository scan |
| `dependency-scan` | Checking for vulnerable packages |
| `implementation-plan` | Detailed plan document |
| `acceptance-criteria-writing` | Defining success |
| `definition-of-done` | Ensuring completeness |
| `rollback-plan` | Documenting how to revert |
| `technical-decision-record` | Documenting architectural choices |
| `security-release-checklist` | Final security check |
| `production-readiness-check` | Pre-deploy validation |
| `architecture-docs-create` | Updating architecture docs |
| `validation-report` | Presenting findings |
| `semantic-versioning` | Managing version numbers |

## Optional Skills
(All skills in the repository are available on-demand depending on the task classification.)

## Skill Loading Logic
- Governance phase: Load `project-intake`, `codebase-map`, `implementation-plan`, `rollback-plan`.
- Implementation phase: Load task-specific skills via the Task Router.
- Release phase: Load `production-readiness-check`, `security-release-checklist`, `semantic-versioning`.

## Progressive Loading Notes
Always load governance skills first. Task-specific skills are loaded only after the implementation plan is approved.

## Validation Notes
`production-readiness-check` and `security-release-checklist` are strictly required before any enterprise deployment.
