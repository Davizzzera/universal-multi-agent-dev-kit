# API Pack: Agents

## Purpose
This document defines the agent ensemble required to safely plan, build, and secure backend APIs.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers backend architecture |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces backend-only boundaries |
| `conflict-controller` | Manages file locks |
| `final-reviewer` | Signs off on delivery |
| `backend-specialist` | Implements core logic |
| `api-designer` | Designs REST/GraphQL contracts |
| `auth-specialist` | Handles login/RBAC |
| `integration-specialist` | Connects to external APIs |
| `webhook-specialist` | Handles incoming events |
| `database-specialist` | Modifies schemas |
| `migration-specialist` | Writes safe DB migrations |
| `qa-tester` | Writes integration tests |
| `security-reviewer` | Audits for vulnerabilities |
| `auth-security-reviewer` | Specific auth layer audits |
| `documentation-writer` | Updates Swagger/OpenAPI docs |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `devops-specialist` | For CI/CD updates |
| `dependency-security-auditor` | For checking npm/pip packages |
| `performance-engineer` | For query optimization |
| `release-manager` | For API versioning |

## Agent Selection Logic
- New endpoints: `api-designer` + `backend-specialist`.
- DB changes: `database-specialist` + `migration-specialist`.
- Auth features: `auth-specialist` + `auth-security-reviewer`.

## Handoff Notes
The `api-designer` must establish the contract before the `backend-specialist` implements the logic.

## Boundary Notes
These agents MUST NOT touch frontend UI components.
