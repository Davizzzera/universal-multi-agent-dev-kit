# Automation Pack: Agents

## Purpose
This document defines the agent ensemble required to safely build and review automation scripts.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers script locations |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces script-only boundaries |
| `conflict-controller` | Manages file locks |
| `final-reviewer` | Signs off on delivery |
| `python-automation-specialist` | Writes the core scripts |
| `integration-specialist` | Handles API connections |
| `qa-tester` | Writes regression tests |
| `security-reviewer` | Audits for secrets/logging |
| `documentation-writer` | Writes usage instructions |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `n8n-automation-specialist` | If moving from code to low-code |
| `webhook-specialist` | If the script triggers webhooks |
| `devops-specialist` | For cron jobs or CI/CD runs |
| `dependency-security-auditor` | For pip package audits |

## Agent Selection Logic
- For web scraping: `python-automation-specialist` + `security-reviewer`.
- For API polling: `python-automation-specialist` + `integration-specialist`.

## Handoff Notes
The `python-automation-specialist` must hand off to the `security-reviewer` before the script is executed for the first time, to ensure no credentials were leaked.

## Boundary Notes
These agents MUST NOT touch frontend UI components or database schemas (unless explicitly authorized).
