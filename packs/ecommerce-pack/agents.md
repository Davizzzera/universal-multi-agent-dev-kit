# Ecommerce Pack: Agents

## Purpose
This document defines the agent ensemble required to safely build commerce-oriented workflows, balancing frontend aesthetics with backend data integrity.

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
| `business-analyst` | Maps commerce flows |
| `frontend-specialist` | UI structure and logic |
| `react-specialist` | React component state (e.g. Cart state) |
| `ui-ux-designer` | Design consistency |
| `backend-specialist` | Pricing and order logic |
| `api-designer` | Checkout/Catalog API contracts |
| `database-specialist` | Inventory schema updates |
| `data-quality-specialist` | Product data imports |
| `qa-tester` | Writes end-to-end tests |
| `security-reviewer` | Audits pricing manipulation risks |
| `copywriter` | Writes product descriptions |
| `landing-page-strategist` | Optimizes product pages |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `auth-specialist` | For customer accounts |
| `integration-specialist` | For payment gateways |
| `devops-specialist` | For caching layers |
| `seo-specialist` | For product SEO |
| `growth-specialist` | For cart abandonment logic |
| `visual-regression-specialist` | For pixel-perfect UI |

## Agent Selection Logic
- For catalog updates: `database-specialist` + `backend-specialist`.
- For product UI updates: `ui-ux-designer` + `frontend-specialist`.
- For checkout logic: `backend-specialist` + `security-reviewer`.

## Handoff Notes
Frontend and backend agents must agree on the API contract *before* either begins implementation, especially for cart and order state.

## Boundary Notes
Frontend agents MUST NOT calculate final prices or discounts. Backend agents must treat all frontend pricing data as untrusted.
