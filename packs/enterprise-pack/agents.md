# Enterprise Pack: Agents

## Purpose
This document defines the agent ensemble required to safely govern, plan, build, and deliver enterprise-grade changes with maximum oversight.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers all module boundaries |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces strict module boundaries |
| `conflict-controller` | Manages file locks across teams |
| `final-reviewer` | Signs off on delivery |
| `software-architect` | Designs cross-module solutions |
| `technical-lead` | Leads implementation strategy |
| `product-manager` | Ensures business alignment |
| `business-analyst` | Maps requirements to features |
| `requirements-engineer` | Writes technical requirements |
| `risk-analyst` | Identifies and mitigates risks |
| `security-reviewer` | Audits for vulnerabilities |
| `privacy-compliance-reviewer` | Checks PII and regulatory concerns |
| `devops-specialist` | Manages CI/CD and infrastructure |
| `qa-tester` | Writes comprehensive test suites |
| `documentation-writer` | Updates all project docs |
| `release-manager` | Manages versioning and releases |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| All specialist agents | Depending on the specific task classification |

## Agent Selection Logic
- For architecture decisions: `software-architect` + `technical-lead` + `risk-analyst`.
- For implementation: Route to the appropriate specialist agent based on `task-router` classification.
- For release: `release-manager` + `devops-specialist` + `qa-tester`.

## Handoff Notes
Every handoff between agents MUST produce a written handoff document following the handoff-contract template. No verbal or implicit handoffs are permitted in the enterprise tier.

## Boundary Notes
All agents MUST respect file ownership rules. Cross-module changes require explicit authorization from the `software-architect`.
