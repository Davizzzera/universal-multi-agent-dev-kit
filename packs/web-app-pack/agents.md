# Web App Pack: Agents

## Purpose
This document defines the agent ensemble required to safely plan, build, and test full-stack web application features.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers full-stack boundaries |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces frontend vs backend boundaries |
| `conflict-controller` | Manages file locks |
| `final-reviewer` | Signs off on delivery |
| `product-manager` | Ensures business requirements |
| `requirements-engineer` | Writes technical requirements |
| `software-architect` | Designs cross-stack solutions |
| `technical-lead` | Leads implementation strategy |
| `frontend-specialist` | UI structure and logic |
| `react-specialist` | React component state |
| `ui-ux-designer` | Design consistency |
| `backend-specialist` | API logic |
| `api-designer` | API contracts |
| `database-specialist` | Schema updates |
| `qa-tester` | Writes unit and integration tests |
| `security-reviewer` | Audits auth and data layers |
| `documentation-writer` | Updates READMEs |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `auth-specialist` | For authentication flows |
| `devops-specialist` | For deployment setups |
| `performance-engineer` | For slow queries/pages |
| `accessibility-specialist` | For ADA/WCAG compliance |
| `visual-regression-specialist` | For pixel-perfect UI |
| `release-manager` | For version bumps |

## Agent Selection Logic
- For isolated UI work: `frontend-specialist` + `react-specialist`
- For isolated API work: `backend-specialist` + `database-specialist`
- For full features: All primary agents coordinated by the `software-architect`.

## Handoff Notes
Frontend and backend agents must agree on the API contract *before* either begins implementation.

## Boundary Notes
Frontend agents MUST NOT modify database schemas. Backend agents MUST NOT modify UI components.
