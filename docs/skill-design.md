# Skill Design

> How to design skills for the Universal Multi-Agent Development Kit.

---

## What Is a Skill?

A skill is a reusable, composable procedure that agents execute to perform specific tasks. Skills are the building blocks of agent behavior — they define **how** work is done, while workflows define **when** work is done.

---

## Skill Structure

Every skill definition must include:

### Required Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `name`             | Unique identifier for the skill (kebab-case).                  |
| `purpose`          | One-sentence description of what the skill does.               |
| `inputs`           | List of required inputs with types and descriptions.           |
| `outputs`          | List of expected outputs with types and descriptions.          |
| `steps`            | Ordered list of actions the skill performs.                     |

### Optional Fields

| Field              | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `preconditions`    | Conditions that must be true before the skill can run.         |
| `postconditions`   | Conditions that should be true after the skill completes.      |
| `error-handling`   | How the skill handles errors or unexpected situations.         |
| `examples`         | Usage examples showing input/output pairs.                     |

---

## Skill File Format

Skill definitions are stored as Markdown files in `.agent/skills/`. Each file follows this template:

```markdown
# Skill: <Skill Name>

## Purpose
<One-sentence description>

## Inputs
- `<input_name>` (<type>): <description>
- `<input_name>` (<type>): <description>

## Outputs
- `<output_name>` (<type>): <description>

## Preconditions
- <Condition that must be true>

## Steps
1. <Step 1 description>
2. <Step 2 description>
3. <Step 3 description>

## Postconditions
- <Condition that should be true after completion>

## Error Handling
- <Error scenario>: <How to handle it>

## Examples

### Example 1: <Scenario>
**Input:** <input values>
**Output:** <expected output>
```

---

## Design Principles

1. **Single Purpose.** Each skill should do one thing well. If a skill is doing multiple unrelated tasks, split it.

2. **Explicit Inputs and Outputs.** Every skill must clearly declare what it needs and what it produces. No hidden dependencies.

3. **Composability.** Skills should be designed to work together. The output of one skill should be usable as input to another.

4. **Idempotency Where Possible.** Running the same skill with the same inputs should produce the same results when feasible.

5. **Error Awareness.** Skills must define how they handle errors. Silent failures are not acceptable.

6. **No Side Effects Beyond Declared Outputs.** A skill should only produce its declared outputs. Unexpected modifications are violations.

---

## Skill Categories

### Reading Skills

| Skill                    | Purpose                                    |
|--------------------------|--------------------------------------------|
| Read File                | Read the contents of a file.               |
| Read Directory Structure | Map the structure of a directory.          |
| Read Dependencies        | Identify project dependencies.             |
| Read Configuration       | Parse configuration files.                 |

### Analysis Skills

| Skill                    | Purpose                                    |
|--------------------------|--------------------------------------------|
| Analyze Code Quality     | Assess code quality metrics.               |
| Analyze Security         | Check for security vulnerabilities.        |
| Analyze Performance      | Identify performance issues.               |
| Analyze Dependencies     | Review dependency health and updates.      |

### Writing Skills

| Skill                    | Purpose                                    |
|--------------------------|--------------------------------------------|
| Write File               | Create or overwrite a file.                |
| Modify File              | Edit specific sections of a file.          |
| Create Component         | Generate a new code component.             |
| Write Documentation      | Create documentation content.              |

### Validation Skills

| Skill                    | Purpose                                    |
|--------------------------|--------------------------------------------|
| Validate Structure       | Check repository structure.                |
| Validate Secrets         | Detect secrets or credentials.             |
| Validate Formatting      | Check code formatting.                     |
| Validate Tests           | Run and verify test results.               |

> **Note:** These are planned skill categories. Individual skill files will be created in Phase 3 (v0.3.0).

---

## Naming Convention

- Skill file names use kebab-case: `read-file.md`, `analyze-code-quality.md`.
- Skill names in content use Title Case: "Read File", "Analyze Code Quality".
- Skill identifiers in references use kebab-case: `read-file`, `analyze-code-quality`.

---

## Current Status

> **Foundation Phase (v0.1.0):** Skill design principles are documented. Individual skill implementations will be created in Phase 3 (v0.3.0).
