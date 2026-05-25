# Agents Directory

> Central repository for all agent definitions in the Universal Multi-Agent Development Kit.

---

## Purpose

This directory contains the definitions for all agents that operate within the multi-agent system. Every agent is defined as a Markdown file with YAML frontmatter, ensuring both machine-readability for the Orchestrator and human-readability for contributors.

---

## Agent Categories

Agents are organized into functional categories:

1. **Orchestration Agents:** The core managers. They coordinate tasks, define scopes, prevent conflicts, and validate final outputs.
2. **Specialist Agents:** Domain experts that perform the actual technical work (code, design, testing, security, etc.) under orchestration control.

---

## Orchestration vs. Specialist Agents

- **Orchestration Agents** understand *what* needs to be done, *who* should do it, and *when* it is complete. They do not write production code or directly modify application files.
- **Specialist Agents** understand *how* to implement a technical solution within their domain. They execute work but do not make high-level project routing decisions.

Orchestration agents coordinate specialist agents through the standard lifecycle. Specialist agents defer all coordination to the Universal Orchestrator and follow the rules, templates, file ownership matrix, and output contracts.

---

## Rules and Compliance

Every agent defined in this directory MUST:
- Follow the global rules defined in `.agent/rules/`.
- Adhere to the structural template defined in `.agent/templates/agent-template.md`.
- Fulfill its required Output Contract upon completing a task.

---

## Orchestration Agents (Phase 3)

| Agent | Role |
|-------|------|
| [Universal Orchestrator](orchestration/universal-orchestrator.agent.md) | Primary coordinator of the multi-agent system. |
| [Project Context Reader](orchestration/project-context-reader.agent.md) | Analyzes the existing repository before implementation. |
| [Task Router](orchestration/task-router.agent.md) | Classifies requests and determines required agents and workflows. |
| [Scope Guardian](orchestration/scope-guardian.agent.md) | Protects the project from unauthorized or out-of-scope changes. |
| [Conflict Controller](orchestration/conflict-controller.agent.md) | Prevents collisions between agents and files. |
| [Final Reviewer](orchestration/final-reviewer.agent.md) | Validates, consolidates, and prepares final delivery. |

---

## Specialist Agent Categories (Phase 4)

| Category | Agents | Description |
|----------|--------|-------------|
| [Product](product/) | 4 | Product strategy, business analysis, requirements, risk. |
| [Architecture](architecture/) | 5 | Software architecture, tech lead, codebase analysis, refactoring, performance. |
| [Frontend](frontend/) | 6 | UI implementation, React, UX, design systems, responsive, accessibility. |
| [Backend](backend/) | 5 | Server-side logic, API design, auth, integrations, webhooks. |
| [Database](database/) | 4 | Schema design, SQL, migrations, data quality. |
| [AI & Automation](ai-automation/) | 6 | AI engineering, prompts, agents, RAG, n8n, Python automation. |
| [QA](qa/) | 5 | Testing, unit tests, E2E, visual regression, bug hunting. |
| [Security](security/) | 5 | Security review, secrets scanning, dependency audit, auth security, privacy. |
| [DevOps](devops/) | 5 | Deployment, Docker, CI/CD, cloud, releases. |
| [Documentation](documentation/) | 5 | Docs writing, technical writing, GitHub management, PRs, changelog. |
| [Marketing](marketing/) | 4 | Copywriting, SEO, landing pages, growth. |
| **Total** | **54** | |

Skills will be implemented in later phases. Agents currently reference planned skill names.

---

## Agent Relationship and Flow

`Universal Orchestrator` → `Context Reader` → `Task Router` → `Scope Guardian` → `Conflict Controller` → *(Specialist Agents)* → *(Validators)* → `Final Reviewer`
