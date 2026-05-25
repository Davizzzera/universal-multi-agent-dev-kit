# Architecture

> This document describes the architecture of the Universal Multi-Agent Development Kit.

---

## Repository Architecture

The repository is organized into four top-level areas:

```
universal-multi-agent-dev-kit/
├── .agent/          → Core agent system (agents, skills, workflows, rules, scripts)
├── adapters/        → Tool-specific adapters (Antigravity, Claude Code, Cursor, etc.)
├── packs/           → Optional project-type packs (web-app, API, ecommerce, etc.)
└── docs/            → Documentation for humans and contributors
```

Each area has a distinct responsibility and can evolve independently.

---

## Core Concepts

### Agent

An **Agent** is an autonomous unit that performs a specific role in the development process. Each agent has:

- **Name:** A unique identifier.
- **Role:** A clear description of what the agent does.
- **Responsibilities:** Specific tasks the agent is accountable for.
- **Skills:** A list of skills the agent can use.
- **Rules:** Constraints the agent must follow.
- **Triggers:** Conditions under which the agent is activated.

Agents do not operate in isolation. They are coordinated by the Universal Orchestrator and work within defined workflows.

**Location:** `.agent/agents/`

### Skill

A **Skill** is a reusable, composable procedure that an agent can execute. Skills are:

- **Task-focused:** Each skill performs one specific type of work.
- **Input-defined:** Skills declare their required inputs.
- **Output-defined:** Skills declare their expected outputs.
- **Composable:** Skills can be combined in workflows.
- **Reusable:** Multiple agents can use the same skill.

Skills do **not** make decisions about when to run. That is the workflow's job.

**Location:** `.agent/skills/`

### Workflow

A **Workflow** defines the execution order for a series of tasks. Workflows specify:

- **Trigger conditions:** When the workflow starts.
- **Steps:** Ordered list of operations.
- **Agent assignments:** Which agent handles each step.
- **Skill loading:** Which skills are used at each step.
- **Execution mode:** Whether each step runs in parallel or sequentially.
- **Validation gates:** Checkpoints that must pass before proceeding.

**Location:** `.agent/workflows/`

### Rule

A **Rule** is a global constraint that all agents, skills, and workflows must follow. Rules are:

- **Non-negotiable:** Rules cannot be bypassed or overridden.
- **Universal:** Rules apply to all components equally.
- **Explicit:** Rules are clearly documented and easy to verify.

Examples of rules:
- All repository content must be written in English.
- No secrets, credentials, or private keys may be added.
- All file modifications must be validated.
- Security content must be defensive only.

**Location:** `.agent/rules/`

### Script

A **Script** is an automated validation or utility tool that the repository uses to check itself. Scripts include:

- **Structure verification:** Ensures the folder structure is correct.
- **Content validation:** Checks for secrets, forbidden patterns, or malformed files.
- **Index generation:** Creates machine-readable indexes of agents, skills, and workflows.
- **Quality checks:** Verifies documentation completeness and formatting.

**Location:** `.agent/scripts/`

### Adapter

An **Adapter** is a tool-specific integration layer that translates the universal kit into the format expected by a specific AI coding tool. Adapters handle:

- **Configuration mapping:** Translating kit settings into tool-specific formats.
- **Entry point definition:** Telling the tool where to start reading.
- **Capability mapping:** Mapping kit features to tool capabilities.
- **Constraint translation:** Expressing kit rules in the tool's language.

Each supported tool has its own adapter directory.

**Location:** `adapters/`

### Pack

A **Pack** is an optional, self-contained group of agents, skills, and workflows designed for a specific project type. Packs provide:

- **Specialized agents:** Agents tailored to the project type.
- **Specialized skills:** Skills specific to the project's technology stack.
- **Specialized workflows:** Workflows optimized for the project's development process.
- **Templates:** Ready-to-use templates for common project patterns.

Packs are modular and optional. A project can use zero, one, or multiple packs.

**Location:** `packs/`

---

## Orchestration Lifecycle

The complete orchestration lifecycle follows these stages:

### 1. Request Intake

The Universal Orchestrator receives a user request and parses it to understand:
- Intent (what the user wants to achieve)
- Scope (which parts of the project are affected)
- Constraints (time, quality, safety requirements)

### 2. Context Analysis

The Context Reader agent analyzes the current project state:
- File structure and organization
- Existing code and dependencies
- Configuration and environment
- Recent changes and history

### 3. Task Routing

The Task Router agent identifies the type of work:
- New feature implementation
- Bug fix
- Refactoring
- Documentation
- Testing
- Security review
- Deployment

### 4. Agent Selection

Based on the task type, the orchestrator selects the appropriate specialist agents and loads their required skills.

### 5. Parallel Research Phase

All selected agents perform research, analysis, and planning in **parallel**:
- Reading existing files
- Analyzing code structure
- Researching solutions
- Mapping dependencies

### 6. Sequential Implementation Phase

Agents perform file modifications in a **controlled, sequential** manner:
- Creating new files
- Modifying existing files
- Updating configurations
- Writing documentation

### 7. Parallel Validation Phase

Validation agents run their checks in **parallel**:
- QA agent verifies functionality
- Security agent checks for vulnerabilities
- Style agent checks formatting and conventions
- Test agent runs automated tests

### 8. Final Review

The Final Reviewer agent consolidates all results:
- Confirms all validations passed
- Verifies completeness
- Ensures consistency
- Prepares the delivery summary

---

## File Ownership

Every file in the repository has a clear owner:

| Path               | Owner                    |
|--------------------|--------------------------|
| `.agent/agents/`   | Agent definitions team   |
| `.agent/skills/`   | Skill definitions team   |
| `.agent/workflows/`| Workflow definitions team|
| `.agent/rules/`    | Architecture team        |
| `.agent/scripts/`  | Tooling team             |
| `adapters/`        | Integration team         |
| `packs/`           | Pack maintainers         |
| `docs/`            | Documentation team       |
| Root files         | Project maintainers      |

File ownership prevents conflicts and ensures accountability.

---

## Validation Model

The validation model operates at three levels:

### 1. Component-Level Validation

Each agent, skill, and workflow is individually validated:
- Schema compliance
- Required fields present
- References resolved
- No circular dependencies

### 2. Integration-Level Validation

The system is validated as a whole:
- Workflow steps reference valid agents
- Agents reference valid skills
- Rules are not contradicted
- No orphaned components

### 3. Repository-Level Validation

The repository itself is validated:
- Folder structure is correct
- Required files exist
- No secrets or sensitive data
- No unexpected files
- Documentation is complete

---

## Current Status

> **Foundation Phase (v0.1.0):** The architecture is documented and the directory structure is established. Implementation of individual components will begin in Phase 2 (v0.2.0).
