# Data & BI Pack: Workflows

## Purpose
This document defines the sequences in which agents and skills operate to process data and document BI needs.

## Primary Workflows
| Workflow | Usage |
|----------|-------|
| `plan.workflow.md` | For initial requirement gathering. |
| `automation.workflow.md` | For writing processing scripts. |
| `database-change.workflow.md` | For schema/view creation. |
| `document.workflow.md` | For writing BI requirements. |
| `verify.workflow.md` | For final data QA checks. |

## Optional Workflows
(None defined by default).

## Workflow Selection Logic
- New KPIs: `document.workflow.md`.
- New script: `automation.workflow.md`.
- Review existing data: `verify.workflow.md`.

## Parallel/Sequential Strategy
- Requirements gathering and schema reading can happen in parallel.
- Data cleaning scripts must be executed sequentially and reviewed before being merged.

## Validation Strategy
- Validation requires visual or programmatic confirmation of data integrity (e.g., "no nulls in required columns", "no duplicates").
