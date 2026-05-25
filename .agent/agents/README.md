# Agents Directory

> Central repository for all agent definitions in the Universal Multi-Agent Development Kit.

---

## Purpose

This directory contains the definitions for all agents that operate within the multi-agent system. Every agent is defined as a Markdown file with YAML frontmatter, ensuring both machine-readability for the Orchestrator and human-readability for contributors.

---

## Agent Categories

Agents are divided into several functional categories:

1. **Orchestration Agents:** The core managers of the system. They coordinate tasks, define scopes, prevent conflicts, and validate final outputs.
2. **Specialist Agents (Planned):** The agents that actually perform the technical implementation (e.g., Code Writer, Database Specialist). These will be added in later phases.
3. **Validation Agents (Planned):** Specialized agents focused purely on QA, Security, and Code Style.

---

## Orchestration vs. Specialist Agents

- **Orchestration Agents** understand *what* needs to be done, *who* should do it, and *when* it is complete. They do not write production code or directly modify application files.
- **Specialist Agents** understand *how* to implement a technical solution within their domain. They write code but do not make high-level project routing decisions.

---

## Rules and Compliance

Every agent defined in this directory MUST:
- Follow the global rules defined in `.agent/rules/`.
- Adhere to the structural template defined in `.agent/templates/agent-template.md`.
- Fulfill its required Output Contract upon completing a task.

---

## Orchestration Agents (Phase 3)

The following orchestration agents are currently implemented:

| Agent | Category | Role |
|-------|----------|------|
| [Universal Orchestrator](orchestration/universal-orchestrator.agent.md) | Orchestrator | Primary coordinator of the multi-agent system. |
| [Project Context Reader](orchestration/project-context-reader.agent.md) | Orchestrator | Analyzes the existing repository before implementation. |
| [Task Router](orchestration/task-router.agent.md) | Orchestrator | Classifies requests and determines required agents and workflows. |
| [Scope Guardian](orchestration/scope-guardian.agent.md) | Orchestrator | Protects the project from unauthorized or out-of-scope changes. |
| [Conflict Controller](orchestration/conflict-controller.agent.md) | Orchestrator | Prevents collisions between agents and files. |
| [Final Reviewer](orchestration/final-reviewer.agent.md) | Orchestrator | Validates, consolidates, and prepares final delivery. |

---

## Agent Relationship and Flow

The standard execution flow of orchestration agents is:

`Universal Orchestrator` → `Context Reader` → `Task Router` → `Scope Guardian` → `Conflict Controller` → *(Specialist Agents)* → *(Validators)* → `Final Reviewer`
