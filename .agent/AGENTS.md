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

## Current Status

> **Foundation Phase (v0.1.0):** The agent system structure is established. Individual agents, skills, and workflows will be implemented in subsequent phases.
