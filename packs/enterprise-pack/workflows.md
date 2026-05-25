# Enterprise Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to deliver enterprise-grade changes safely with full governance.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For detailed architectural planning. |
| `coordinate.workflow.md` | For managing multi-module tasks. |
| `create-feature.workflow.md` | For building new features. |
| `security-review.workflow.md` | For auditing vulnerabilities. |
| `database-change.workflow.md` | For schema migrations. |
| `deploy.workflow.md` | For updating environments. |
| `release.workflow.md` | For version bumps and changelogs. |
| `verify.workflow.md` | For pre-commit health checks. |
| `emergency-fix.workflow.md` | For critical production hotfixes. |

## Optional Workflows
(All workflows in the repository are available on-demand depending on the task classification.)

## Workflow Selection Logic
- New features: `plan.workflow.md` → `coordinate.workflow.md` → `create-feature.workflow.md`.
- Releases: `verify.workflow.md` → `release.workflow.md` → `deploy.workflow.md`.
- Hotfixes: `emergency-fix.workflow.md` → `verify.workflow.md`.

## Parallel/Sequential Strategy
- Discovery and context reading can happen in parallel.
- All implementation edits must be serialized under the `conflict-controller`.
- Verification and security reviews can happen in parallel after implementation.

## Validation Strategy
- Full regression testing is mandatory.
- Security review is mandatory.
- Production-readiness check is mandatory.
- Rollback plan must be documented before deployment.
