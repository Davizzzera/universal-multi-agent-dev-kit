# Landing Page Pack: Agents

## Purpose
This document defines the agent ensemble required to safely plan, build, and optimize landing pages.

## Primary Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `universal-orchestrator` | Overall request handling |
| `project-context-reader` | Discovers UI/branding boundaries |
| `task-router` | Selects workflows |
| `scope-guardian` | Enforces frontend-only boundaries |
| `final-reviewer` | Signs off on delivery |
| `landing-page-strategist` | Defines page structure and goals |
| `copywriter` | Writes persuasive copy |
| `seo-specialist` | Optimizes metadata |
| `growth-specialist` | Reviews conversion potential |
| `ui-ux-designer` | Design consistency |
| `frontend-specialist` | HTML/CSS structure |
| `responsive-layout-specialist` | Mobile/tablet optimization |
| `accessibility-specialist` | Contrast and screen reader checks |
| `visual-regression-specialist` | Layout integrity |
| `qa-tester` | Functional UI testing |

## Optional Agents
| Agent | Role in this Pack |
|-------|-------------------|
| `react-specialist` | For React-based SSG/SSR frameworks |
| `design-system-specialist` | For reusing existing UI libraries |
| `documentation-writer` | For updating component docs |

## Agent Selection Logic
- For copy/SEO updates: `copywriter` + `seo-specialist`.
- For layout changes: `frontend-specialist` + `responsive-layout-specialist`.
- For new pages: All primary agents coordinated by the `landing-page-strategist`.

## Handoff Notes
The `copywriter` and `ui-ux-designer` must establish the content and wireframe before the `frontend-specialist` writes the code.

## Boundary Notes
These agents MUST NOT touch database files, backend APIs, or CI/CD pipelines outside of static site generation configurations.
