# Agent System — Global Entrypoint

> This file is the global entrypoint for the Universal Multi-Agent Development Kit's agent system. AI coding tools should start by reading this file to understand the orchestration model.

---

## Purpose

The agent system provides a structured, multi-agent framework for AI-assisted software engineering. Instead of relying on a single monolithic AI assistant, this kit decomposes work into specialized agents, each with a clear role, defined skills, and governed by explicit rules.

---

## The Universal Orchestrator

The **Universal Orchestrator** is the central coordinator of all agent activity. It is responsible for:

1. **Understanding the user request.** Parsing intent, scope, and constraints.
2. **Reading project context.** Delegating to the Context Reader to understand the current project state.
3. **Routing tasks.** Delegating to the Task Router to identify the type of work.
4. **Selecting specialists.** Choosing the appropriate specialist agents based on the task type.
5. **Loading skills.** Ensuring agents have the correct skills for their assigned tasks.
6. **Coordinating execution.** Managing parallel and sequential work phases.
7. **Reviewing results.** Delegating to QA, security, and validation agents.
8. **Consolidating delivery.** Ensuring the final result meets quality standards.

The orchestrator does **not** do the work itself. It delegates to specialist agents and coordinates their activity.

---

## Core Orchestration Agents

The multi-agent system is managed by six core orchestration agents that ensure rules and templates are enforced:

1. **[Universal Orchestrator](agents/orchestration/universal-orchestrator.agent.md):** The primary coordinator.
2. **[Project Context Reader](agents/orchestration/project-context-reader.agent.md):** Scans the repository for context.
3. **[Task Router](agents/orchestration/task-router.agent.md):** Classifies the task and selects agents.
4. **[Scope Guardian](agents/orchestration/scope-guardian.agent.md):** Protects boundaries and prevents scope creep.
5. **[Conflict Controller](agents/orchestration/conflict-controller.agent.md):** Manages file ownership and parallel execution locks.
6. **[Final Reviewer](agents/orchestration/final-reviewer.agent.md):** Validates and synthesizes the final delivery.

The typical orchestration sequence is:
`Universal Orchestrator` → `Context Reader` → `Task Router` → `Scope Guardian` → `Conflict Controller` → *(Specialist Agents)* → *(Validators)* → `Final Reviewer`

*(Note: Specialist and Validation agents will be added in later phases.)*

---

## Multi-Agent Execution Model

The execution model follows a structured lifecycle:

```
User Request
    │
    ▼
┌─────────────────────┐
│ Universal Orchestrator│
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
Context     Task
Reader      Router
    │           │
    └─────┬─────┘
          │
          ▼
  Specialist Agents
  (with loaded Skills)
          │
    ┌─────┴─────┐
    ▼           ▼
 Parallel   Sequential
 (read)     (write)
    │           │
    └─────┬─────┘
          │
          ▼
  Validation Agents
  (QA, Security, Review)
          │
          ▼
  Final Reviewer
          │
          ▼
  Delivery
```

---

## Parallel and Sequential Execution Rule

This is a **critical rule** that all agents must follow:

| Operation Type                    | Execution Mode | Reason                                         |
|-----------------------------------|----------------|-------------------------------------------------|
| Reading files                     | Parallel       | No conflict risk.                              |
| Research and analysis             | Parallel       | Independent operations, safe to parallelize.   |
| Mapping project structure         | Parallel       | Read-only operation.                           |
| Writing files                     | Sequential     | Conflict risk, must be controlled.             |
| Editing existing files            | Sequential     | Conflict risk, must be controlled.             |
| Creating new files                | Sequential     | Naming and placement must be coordinated.      |
| Validation and QA                 | Parallel       | Independent checks, safe to parallelize.       |

**Summary:**
- **Parallel** for reading, research, mapping, and analysis.
- **Sequential** for writing, editing, and file changes.
- **Parallel** for validation after implementation.

---

## Validation-First Principle

Every agent operation must be validated before it is considered complete. This means:

1. **Pre-validation:** Check preconditions before starting work.
2. **In-process validation:** Verify intermediate results during execution.
3. **Post-validation:** Confirm the final result meets expectations.
4. **Cross-validation:** QA and security agents independently review the output.

No work is considered done until it passes validation.

---

## Agent Behavior Rules

All agents must:

1. **Follow global rules** defined in `.agent/rules/`.
2. **Follow assigned workflows** defined in `.agent/workflows/`.
3. **Use only assigned skills** defined in `.agent/skills/`.
4. **Report their actions** to the orchestrator.
5. **Never bypass validation.**
6. **Never introduce secrets, credentials, or sensitive data.**
7. **Write all repository content in English.**
8. **Use defensive security practices only.**

---

## Directory Structure

| Directory           | Purpose                                      |
|---------------------|----------------------------------------------|
| `.agent/agents/`    | Agent definitions and configurations.        |
| `.agent/skills/`    | Reusable skill definitions.                  |
| `.agent/workflows/` | Workflow definitions and execution orders.   |
| `.agent/rules/`     | Global rules and constraints.                |
| `.agent/memory/`    | Shared context and state between agents.     |
| `.agent/templates/` | Reusable templates for common patterns.      |
| `.agent/scripts/`   | Validation and automation scripts.           |
| `.agent/indexes/`   | Generated indexes for discovery.             |

---

## Core Specialist Agents

Specialist agents are selected by the Task Router based on the domain of the user request. They must:
- Follow all rules in `.agent/rules/`.
- Adhere to `.agent/templates/agent-template.md`.
- Respect file ownership (`.agent/rules/file-ownership.md`).
- Fulfill their Output Contract (`.agent/rules/output-contract-rules.md`).
- Defer all coordination to the Universal Orchestrator.

| Category | Agents | Description |
|----------|--------|-------------|
| Product | 4 | Product Manager, Business Analyst, Requirements Engineer, Risk Analyst. |
| Architecture | 5 | Software Architect, Technical Lead, Codebase Analyst, Refactor Specialist, Performance Engineer. |
| Frontend | 6 | Frontend Specialist, React Specialist, UI/UX Designer, Design System Specialist, Responsive Layout Specialist, Accessibility Specialist. |
| Backend | 5 | Backend Specialist, API Designer, Auth Specialist, Integration Specialist, Webhook Specialist. |
| Database | 4 | Database Specialist, SQL Specialist, Migration Specialist, Data Quality Specialist. |
| AI & Automation | 6 | AI Engineer, Prompt Engineer, Agent Engineer, RAG Specialist, n8n Automation Specialist, Python Automation Specialist. |
| QA | 5 | QA Tester, Unit Test Specialist, E2E Test Specialist, Visual Regression Specialist, Bug Hunter. |
| Security | 5 | Security Reviewer, Secrets Scanner, Dependency Security Auditor, Auth Security Reviewer, Privacy Compliance Reviewer. |
| DevOps | 5 | DevOps Specialist, Docker Specialist, CI/CD Specialist, Cloud Specialist, Release Manager. |
| Documentation | 5 | Documentation Writer, Technical Writer, GitHub Repository Manager, Pull Request Writer, Changelog Maintainer. |
| Marketing | 4 | Copywriter, SEO Specialist, Landing Page Strategist, Growth Specialist. |

---

## Core Skills Library

Skills (`.agent/skills/`) define *how* work is executed. They are procedural checklists and guidelines loaded progressively by agents.

- **Progressive Loading:** Instead of overloading an agent's base prompt, the Universal Orchestrator and Task Router identify and provide specific skills relevant to the current task.
- **Execution Over Identity:** Skills are not agents; they are the tools/manuals agents use.
- **Specialist Adherence:** When assigned a task, specialist agents must follow the loaded skills step-by-step to ensure safe and correct execution.

For a complete list of all 18 skill categories and 104 core skills, see `.agent/skills/README.md`.

---

## Operational Workflows

Workflows (`.agent/workflows/`) define *when* and *in which order* work happens. They are selected by the Universal Orchestrator to coordinate the execution of agents and skills.

Workflows must enforce global rules, file ownership, handoffs, and output contracts.

| Workflow | Purpose |
|----------|---------|
| `plan` | Analyze a request and create a safe implementation plan. |
| `coordinate` | Coordinate multiple agents for complex tasks. |
| `create-feature` | Create a new feature safely using specialist agents. |
| `enhance-feature` | Improve an existing feature without changing its intended behavior. |
| `debug` | Investigate, reproduce and resolve bugs with minimal changes. |
| `refactor` | Improve code structure without changing behavior. |
| `test` | Create, improve or run tests. |
| `verify` | Verify that the implementation actually works. |
| `security-review` | Perform a defensive security review. |
| `database-change` | Plan, implement and validate database changes safely. |
| `api-development` | Design, implement and validate API endpoints. |
| `frontend-ui` | Create or improve frontend UI safely. |
| `automation` | Design and validate automation scripts and flows. |
| `ai-feature` | Design and validate AI-powered features. |
| `document` | Create, update or validate documentation. |
| `deploy` | Prepare deployment configuration and production readiness. |
| `release` | Prepare versioning, changelog, and release notes. |
| `emergency-fix` | Handle urgent fixes safely. |

---

## Validation Scripts

Validation scripts (`.agent/scripts/`) enforce repository structure, agent contracts, skill contracts, workflow contracts, and defensive safety checks. They generate the indexes located in `.agent/indexes/`.

Agents should use validation before claiming completion of their tasks, following the Validation-First Delivery approach.

---

## Adapter Usage

Adapters (`adapters/`) provide tool-specific instructions on how to load and interact with this kit, without changing the core agnostic architecture. 

**Antigravity** is the first implemented adapter. You can find its specific entrypoint and integration rules in `adapters/antigravity/`.

---

## Project Packs

Project Packs (`packs/`) are **advisory presets** that help the Universal Orchestrator and Task Router select agents, skills, and workflows faster for specific project domains. They are NOT replacements for orchestration — the Orchestrator still governs execution.

**Key rules:**
- Packs are recommendations, not mandates.
- Global rules ALWAYS take precedence over any pack recommendation.
- Packs reference existing agents, skills, and workflows — they do not create new ones.
- Multiple packs can be combined safely by unioning their recommended resources.

---

## Current Status

> **v0.1.0 (Unreleased):** Core orchestration agents, specialist agents, core skills library, operational workflows, validation scripts/indexes, the Antigravity adapter, and 9 reusable project packs have been implemented.

