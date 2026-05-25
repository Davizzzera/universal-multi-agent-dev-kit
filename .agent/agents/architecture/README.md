# Architecture Agents

> Software architecture, technical leadership, codebase analysis, refactoring and performance optimization.

---

## Purpose
This category contains specialist agents focused on software architecture, technical leadership, codebase analysis, refactoring and performance optimization.

## When Used
These agents are invoked by the Task Router when a request involves architecture domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router, Conflict Controller.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Software Architect](software-architect.agent.md) | Design software structure, module boundaries, system patterns and scalable technical direction. | software architect tasks. | AgentOutputContract |
| [Technical Lead](technical-lead.agent.md) | Provide technical direction, implementation standards and engineering judgment across agents. | technical lead tasks. | AgentOutputContract |
| [Codebase Analyst](codebase-analyst.agent.md) | Analyze existing codebase structure, patterns, conventions and dependencies before changes. | codebase analyst tasks. | AgentOutputContract |
| [Refactor Specialist](refactor-specialist.agent.md) | Improve code structure without changing external behavior. | refactor specialist tasks. | AgentOutputContract |
| [Performance Engineer](performance-engineer.agent.md) | Analyze and improve performance across frontend, backend, database and build systems. | performance engineer tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
