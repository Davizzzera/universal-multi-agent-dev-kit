# Automation Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to build resilient automation scripts.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For planning the script logic. |
| `automation.workflow.md` | For writing the script. |
| `debug.workflow.md` | For fixing failing scripts. |
| `test.workflow.md` | For writing tests. |
| `verify.workflow.md` | For running dry-runs. |
| `document.workflow.md` | For writing usage instructions. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New script: `automation.workflow.md`.
- Broken script: `debug.workflow.md`.
- Documenting how to run a script: `document.workflow.md`.

## Parallel/Sequential Strategy
- Writing the script and documenting its usage can happen sequentially.
- Security review must happen sequentially AFTER the script is written, but BEFORE it is executed against live systems.

## Validation Strategy
- Validation requires dry-runs (executing the script without making state changes).
- Scripts must handle missing environment variables gracefully.
