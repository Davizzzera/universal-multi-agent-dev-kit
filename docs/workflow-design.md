# Workflow Design

> How to design workflows for the Universal Multi-Agent Development Kit.

---

## What Is a Workflow?

A workflow defines the execution order for a series of tasks within the multi-agent system. Workflows orchestrate **when** and **in what order** agents and skills are activated, ensuring tasks are completed efficiently and safely.

---

## Workflow Structure

Every workflow definition must include:

### Required Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `name`             | Unique identifier for the workflow (kebab-case).               |
| `purpose`          | One-sentence description of what the workflow achieves.        |
| `trigger`          | What causes this workflow to start.                            |
| `steps`            | Ordered list of steps with agent and skill assignments.        |

### Optional Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `preconditions`    | Conditions required before the workflow can start.             |
| `postconditions`   | Expected state after the workflow completes.                   |
| `error-handling`   | How the workflow handles failures at any step.                 |
| `rollback`         | Steps to undo changes if the workflow fails.                   |
| `timeout`          | Maximum allowed execution time.                                |

---

## Workflow File Format

Workflow definitions are stored as Markdown files in `.agent/workflows/`. Each file follows this template:

```markdown
# Workflow: <Workflow Name>

## Purpose
<One-sentence description>

## Trigger
<What causes this workflow to start>

## Preconditions
- <Required condition 1>
- <Required condition 2>

## Steps

### Step 1: <Step Name>
- **Agent:** <agent-name>
- **Skill:** <skill-name>
- **Mode:** Parallel | Sequential
- **Description:** <What this step does>

### Step 2: <Step Name>
- **Agent:** <agent-name>
- **Skill:** <skill-name>
- **Mode:** Parallel | Sequential
- **Description:** <What this step does>

### Validation Gate
- **Required:** All previous steps must pass.
- **Validator:** <validation-agent>
- **Criteria:** <What must be true to proceed>

### Step 3: <Step Name>
- **Agent:** <agent-name>
- **Skill:** <skill-name>
- **Mode:** Sequential
- **Description:** <What this step does>

## Postconditions
- <Expected state after completion>

## Error Handling
- <Error scenario>: <Recovery action>

## Rollback
- <Undo step 1>
- <Undo step 2>
```

---

## Execution Modes

### Parallel Mode

Steps in parallel mode run simultaneously. Use for:
- Reading files and gathering context.
- Research and analysis tasks.
- Independent validation checks.

**Rule:** Only read-only or independent operations may run in parallel.

### Sequential Mode

Steps in sequential mode run one after another. Use for:
- Writing or modifying files.
- Operations with dependencies on previous step outputs.
- Tasks where order matters for correctness.

**Rule:** All write operations must be sequential to prevent conflicts.

### Validation Gates

Validation gates are checkpoints between workflow phases. A validation gate:
- Requires all preceding steps to complete.
- Runs validation checks on intermediate results.
- Blocks progress until validation passes.
- Triggers error handling if validation fails.

---

## Design Principles

1. **Clear Triggers.** Every workflow must have an explicit trigger. Workflows should not start without a clear reason.

2. **Ordered Steps.** Steps must be in a logical, dependency-respecting order. No step should require output from a later step.

3. **Explicit Modes.** Every step must declare whether it runs in parallel or sequential mode. Default to sequential if uncertain.

4. **Validation Gates.** Include validation gates between major phases (research → implementation → review).

5. **Error Recovery.** Define what happens when a step fails. Include rollback procedures for destructive operations.

6. **Composability.** Workflows can reference other workflows as sub-workflows, enabling reuse.

---

## Workflow Categories

### Core Workflows

| Workflow                    | Purpose                                              |
|-----------------------------|------------------------------------------------------|
| Feature Implementation      | End-to-end workflow for implementing a new feature.  |
| Bug Fix                     | Workflow for diagnosing and fixing a bug.            |
| Code Review                 | Workflow for reviewing code changes.                 |
| Refactoring                 | Workflow for restructuring code.                     |
| Documentation Update        | Workflow for updating documentation.                 |

### Validation Workflows

| Workflow                    | Purpose                                              |
|-----------------------------|------------------------------------------------------|
| Full Validation             | Complete validation of the repository.               |
| Security Audit              | Security-focused validation pass.                    |
| Structure Check             | Validates repository structure and organization.     |

> **Note:** These are planned workflow categories. Individual workflow files will be created in Phase 4 (v0.4.0).

---

## Naming Convention

- Workflow file names use kebab-case: `feature-implementation.md`, `bug-fix.md`.
- Workflow names in content use Title Case: "Feature Implementation", "Bug Fix".
- Workflow identifiers in references use kebab-case: `feature-implementation`, `bug-fix`.

---

## Current Status

> **Foundation Phase (v0.1.0):** Workflow design principles are documented. Individual workflow implementations will be created in Phase 4 (v0.4.0).
