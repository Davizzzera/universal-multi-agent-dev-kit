# n8n Pack: Agents

## Purpose
This document defines the agent ensemble required to safely build and review n8n automations.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers JSON exports |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces n8n-only boundaries |
| `final-reviewer` | Signs off on delivery |
| `n8n-automation-specialist` | Designs the node logic |
| `webhook-specialist` | Configures webhook triggers |
| `integration-specialist` | Defines external API calls |
| `business-analyst` | Defines the process flow |
| `qa-tester` | Writes test cases for nodes |
| `security-reviewer` | Audits exported JSON for secrets |
| `documentation-writer` | Documents the workflow |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `python-automation-specialist` | If combining n8n with scripts |
| `backend-specialist` | If triggering internal APIs |
| `data-quality-specialist` | For ETL flows |
| `devops-specialist` | For hosting n8n |

## Agent Selection Logic
- For defining the process: `business-analyst` + `documentation-writer`.
- For designing nodes: `n8n-automation-specialist` + `integration-specialist`.
- For reviewing exports: `security-reviewer`.

## Handoff Notes
The `business-analyst` must map the logical flow before the `n8n-automation-specialist` translates it into n8n nodes.

## Boundary Notes
These agents MUST NOT touch frontend UI components or database schemas (unless explicitly authorized).
