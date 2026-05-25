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

### Template Layer

**Templates** enforce consistency across all components and agent outputs. They provide a standardized structure for defining agents, skills, workflows, task briefs, handoff requests, and validation reports.

**Location:** `.agent/templates/`

### Global Rules Layer

The **Global Rules Layer** defines the non-negotiable principles governing the entire repository. This includes security policies, parallel execution boundaries, validation mandates, and file ownership matrices. These rules override any agent's default behavior.

**Location:** `.agent/rules/`


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

### 8. Final Review & Output Contract

The Final Reviewer agent consolidates all results:
- Confirms all validations passed
- Verifies completeness
- Ensures consistency
- Prepares the delivery summary adhering to the Output Contract

### Handoff Protocol

During any phase, if an agent reaches its boundary or encounters a blocker requiring different skills, it initiates a **Handoff Request**. The orchestrator intercepts this request, provisions the target agent, and passes the context seamlessly.

---

## File Ownership

Every file in the repository has a clear owner defined in the file ownership matrix (`.agent/rules/file-ownership.md`). File ownership prevents conflicts by ensuring:
- Only the **Primary Owner** can write to a file during implementation.
- The **Secondary Reviewer** can validate or suggest changes.

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

## Parallel Execution

Execution follows the core rule: **"Parallelize discovery. Serialize conflicting edits. Parallelize verification."**
- **Safe:** Reading files, code analysis, dependency mapping, independent validation.
- **Unsafe:** Concurrent writes to the same or closely coupled files.

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

## Specialist Agent Layer

Specialist agents are domain experts that perform implementation work under orchestration control.

### Agent Category Model

Agents are grouped into 11 functional categories:

| Category | Focus Area |
|----------|-----------|
| Product | Strategy, analysis, requirements, risk. |
| Architecture | Design, tech leadership, analysis, refactoring, performance. |
| Frontend | UI, React, UX, design systems, responsive, accessibility. |
| Backend | Server logic, APIs, auth, integrations, webhooks. |
| Database | Schema, SQL, migrations, data quality. |
| AI & Automation | AI features, prompts, agents, RAG, n8n, Python. |
| QA | Testing, unit, E2E, visual regression, bug hunting. |
| Security | Security review, secrets, dependencies, auth, privacy. |
| DevOps | Deployment, Docker, CI/CD, cloud, releases. |
| Documentation | Docs, technical writing, GitHub, PRs, changelog. |
| Marketing | Copy, SEO, landing pages, growth. |

### Orchestration-to-Specialist Relationship

- The **Task Router** classifies requests and selects required specialist categories.
- The **Scope Guardian** restricts which files and areas specialists can touch.
- The **Conflict Controller** manages file ownership locks and parallel/sequential scheduling.
- Specialists execute within their boundaries and return Output Contracts.
- The **Final Reviewer** validates specialist outputs before delivery.

### Specialist Agent Boundaries

- Specialists do not make high-level routing decisions.
- Specialists do not bypass the Orchestrator.
- Specialists follow file ownership rules.
- Specialists must validate their work before declaring completion.

### Skills Layer

Agents utilize **Skills** (`.agent/skills/`) to define step-by-step procedures for common tasks.
- Skills use YAML frontmatter to define purpose, owner agents, expected outputs, and validation levels.
- **Progressive Loading:** Instead of being loaded with all skills at once, agents are given specific skills by the Orchestrator/Task Router at execution time.
- **Validation Support:** Each skill defines specific validation criteria, ensuring agents can self-correct and QA agents know exactly what to check.
- **Adapter & Pack Readiness:** The separation of Skills from Agents makes the system easily extensible via Adapters (different IDEs) and Packs (different domains).

### Workflows Layer

Workflows (`.agent/workflows/`) define the operational execution sequences of the system.
- Workflows use YAML frontmatter to define triggers, primary agents, required agents, required skills, validation rules, and risk levels.
- **Execution Over Identity:** While Agents define responsibility and Skills define specific actions, Workflows orchestrate *when* and *in which order* they are applied.
- **Validation-First Delivery:** All workflows explicitly require validation steps (QA, Security, build checks) before claiming completion.
- **Parallel / Sequential Rules:** Workflows enforce parallel execution for discovery/analysis and sequential execution for file writing/conflict resolution.

### Scripts Layer

Validation scripts (`.agent/scripts/`) ensure the integrity of the kit.
- **Self-Checking:** Scripts validate repository structure, agent files, skill files, and workflows to ensure they follow their respective templates and rules.
- **Indexes:** The validation pipeline generates JSON indexes (`.agent/indexes/`) which map the entire repository for fast discovery by adapters and other tooling.
- **Validation Pipeline:** Scripts are executed via `python .agent/scripts/verify_all.py` or npm shortcuts to enforce strict compliance before delivery.

### Adapter Layer

Adapters (`adapters/`) provide tool-specific integration guidelines while preserving the agnostic nature of the core repository.
- **Antigravity Adapter:** The primary adapter mapping the kit concepts to Antigravity AI workflows. It provides the `AGENTS.md` entrypoint, integration rules, and prompt patterns.
- **Agnostic Core:** Adapters do NOT change the core architecture. They only describe *how* a specific tool should read and interact with the `.agent/` folder.
- **Safety Overrides:** Adapter-specific instructions must NEVER override global safety rules or file ownership scopes.

### Specialist Participation in Validation

QA and Security agents act as cross-cutting validators. After any specialist completes work, the Orchestrator dispatches QA and/or Security agents to independently review the output before the Final Reviewer synthesizes the delivery.

---

## Current Status

> **Phase 8 (v0.8.0):** Core orchestration agents, specialist agents, core skills library, operational workflows, validation scripts/indexes, and the Antigravity adapter have been implemented.

