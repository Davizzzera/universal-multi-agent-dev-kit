# Agent Design

> How to design agents for the Universal Multi-Agent Development Kit.

---

## What Is an Agent?

An agent is an autonomous unit within the multi-agent system that performs a specific role. Each agent has clear boundaries, defined responsibilities, and operates under the coordination of the Universal Orchestrator.

---

## Agent Structure

Every agent definition must include:

### Required Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `name`             | Unique identifier for the agent (kebab-case).                  |
| `role`             | One-sentence description of what the agent does.               |
| `responsibilities` | List of specific tasks the agent is accountable for.           |
| `skills`           | List of skills the agent can use.                              |
| `triggers`         | Conditions under which the agent is activated.                 |

### Optional Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `rules`            | Additional rules specific to this agent.                       |
| `dependencies`     | Other agents this agent depends on.                            |
| `outputs`          | What the agent produces as a result.                           |
| `priority`         | Execution priority relative to other agents.                   |

---

## Agent File Format

Agent definitions are stored as Markdown files in `.agent/agents/`. Each file follows this template:

```markdown
# Agent: <Agent Name>

## Role
<One-sentence description>

## Responsibilities
- <Responsibility 1>
- <Responsibility 2>
- <Responsibility 3>

## Skills
- <skill-name-1>
- <skill-name-2>

## Triggers
- <Trigger condition 1>
- <Trigger condition 2>

## Rules
- <Agent-specific rule 1>

## Dependencies
- <Other agent name>

## Outputs
- <Output description>
```

---

## Design Principles

1. **Single Responsibility.** Each agent should have one clear role. If an agent does too many things, split it into multiple agents.

2. **Explicit Skills.** An agent must declare which skills it uses. It cannot use undeclared skills.

3. **Orchestrator Coordination.** Agents do not call each other directly. The orchestrator manages all inter-agent coordination.

4. **Stateless by Default.** Agents should not maintain internal state between invocations. Shared state is stored in `.agent/memory/`.

5. **Validation Awareness.** Every agent must be aware that its output will be validated. Design outputs to be verifiable.

6. **Defensive Behavior.** Agents should handle edge cases, report errors clearly, and never silently fail.

---

## Agent Categories

### Orchestration Agents

| Agent               | Role                                               |
|---------------------|-----------------------------------------------------|
| Universal Orchestrator | Coordinates all agent activity.                   |
| Context Reader      | Analyzes project structure and state.               |
| Task Router         | Identifies the type of work required.               |
| Final Reviewer      | Consolidates and validates the delivery.            |

### Specialist Agents

| Agent               | Role                                               |
|---------------------|-----------------------------------------------------|
| Code Writer         | Writes new code based on specifications.            |
| Code Reviewer       | Reviews code for quality and correctness.           |
| Refactoring Agent   | Improves code structure without changing behavior.  |
| Documentation Agent | Creates and updates documentation.                  |
| Test Agent          | Writes and runs tests.                              |

### Validation Agents

| Agent               | Role                                               |
|---------------------|-----------------------------------------------------|
| QA Agent            | Verifies functional correctness.                    |
| Security Agent      | Checks for security vulnerabilities.                |
| Style Agent         | Verifies code style and conventions.                |
| Structure Agent     | Validates repository structure.                     |

> **Note:** These are planned agent categories. Individual agent files will be created in Phase 2 (v0.2.0).

---

## Naming Convention

- Agent file names use kebab-case: `context-reader.md`, `code-writer.md`.
- Agent names in content use Title Case: "Context Reader", "Code Writer".
- Agent identifiers in references use kebab-case: `context-reader`, `code-writer`.

---

## Current Status

> **Foundation Phase (v0.1.0):** Agent design principles are documented. Individual agent implementations will be created in Phase 2 (v0.2.0).
