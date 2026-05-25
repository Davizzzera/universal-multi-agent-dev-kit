# Data & BI Pack: Agents

## Purpose
This document defines the agent ensemble required to safely process data, define KPIs, and document BI requirements.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers data sources |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces data boundaries |
| `final-reviewer` | Signs off on delivery |
| `business-analyst` | Defines KPIs and requirements |
| `data-quality-specialist` | Ensures data integrity |
| `python-automation-specialist` | Writes processing scripts |
| `documentation-writer` | Writes BI documentation |
| `technical-writer` | Writes technical specs |
| `qa-tester` | Writes data validation tests |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `database-specialist` | For querying databases directly |
| `sql-specialist` | For writing complex SQL |
| `performance-engineer` | For optimizing slow queries/scripts |
| `devops-specialist` | For scheduling tasks |
| `security-reviewer` | For auditing PII handling |

## Agent Selection Logic
- For defining metrics: `business-analyst` + `documentation-writer`.
- For cleaning data: `python-automation-specialist` + `data-quality-specialist`.
- For new dashboards: All primary agents coordinated by the `business-analyst`.

## Handoff Notes
The `business-analyst` must define the expected output before the `python-automation-specialist` writes the script.

## Boundary Notes
These agents MUST NOT touch frontend UI components or unrelated backend APIs.
