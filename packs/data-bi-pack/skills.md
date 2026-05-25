# Data & BI Pack: Skills

## Purpose
This document defines the core procedures and techniques required to process data and document BI needs.

## Core Skills
| Skill | Usage |
|-------|-------|
| `project-intake` | Initial discovery |
| `business-context-extraction` | Understanding the "why" |
| `csv-excel-ingestion` | Reading flat files |
| `data-cleaning` | Normalizing values |
| `deduplication-rules` | Removing duplicates |
| `kpi-definition` | Standardizing metrics |
| `dashboard-requirements` | Wireframing reports |
| `reporting-automation` | Generating recurring reports |
| `data-integrity-check` | Ensuring data quality |
| `test-plan-create` | QA strategy |
| `validation-report` | Presenting findings |
| `troubleshooting-guide` | Documenting edge cases |

## Optional Skills
(None defined by default).

## Skill Loading Logic
- Requirement phase: Load `business-context-extraction`, `kpi-definition`, `dashboard-requirements`.
- Processing phase: Load `csv-excel-ingestion`, `data-cleaning`, `deduplication-rules`.
- QA phase: Load `data-integrity-check`, `validation-report`.

## Progressive Loading Notes
Only load `python-automation-specialist` skills if the task requires writing executable scripts.

## Validation Notes
`data-integrity-check` and `validation-report` must be completed before delivering data products.
