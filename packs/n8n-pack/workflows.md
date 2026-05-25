# n8n Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to design and export n8n automations safely.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For planning the logical flow. |
| `automation.workflow.md` | For generating the JSON schema. |
| `api-development.workflow.md` | For ensuring the n8n nodes match the API. |
| `debug.workflow.md` | For fixing failing nodes. |
| `verify.workflow.md` | For security auditing the export. |
| `document.workflow.md` | For writing usage instructions. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New workflow: `plan.workflow.md` then `automation.workflow.md`.
- Broken node: `debug.workflow.md`.
- Exporting to git: `verify.workflow.md` (mandatory).

## Parallel/Sequential Strategy
- Planning and mapping the APIs can happen in parallel.
- Security review MUST happen sequentially AFTER the JSON is generated, BEFORE it is committed.

## Validation Strategy
- Validation requires checking the exported JSON structure.
- Execution validation requires importing the JSON into n8n and running a test execution manually.
