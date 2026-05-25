# Parallel Execution

> Rules governing how and when tasks can be executed concurrently.

---

## Purpose

Parallel execution maximizes efficiency by allowing multiple agents to work simultaneously. However, uncoordinated parallel writes cause file conflicts, state corruption, and unpredictable behavior. This document defines the rules for safe parallel execution.

---

## Core Rule

> "Parallelize discovery. Serialize conflicting edits. Parallelize verification."

---

## Safe Parallel Work

Work that is strictly read-only, analytical, or affects completely disjointed parts of the system is safe to parallelize.

### Parallel Reading
Agents may read the repository concurrently.
- Context gathering.
- Dependency mapping.
- Code base searching.

### Parallel Analysis
Agents may analyze data concurrently.
- Code quality analysis.
- Security vulnerability scanning.
- Architectural review.

### Parallel Validation
Agents may validate results concurrently.
- Running independent test suites.
- Checking code style.
- Verifying documentation completeness.

---

## Unsafe Parallel Work

Work that modifies the same files, depends on shared state, or relies on the output of concurrent tasks is unsafe to parallelize.

### Sequential Writing
Agents must not write to the same file or closely coupled files concurrently.
- Modifying the same configuration file.
- Editing a component and its immediate test file simultaneously if the implementation drives the tests.
- Changing database schema while another agent writes the queries depending on that schema.

---

## Conflict Prevention

To prevent conflicts during implementation phases:

1. **File Locking Concept:** When an agent is assigned to modify a file (as per `file-ownership.md`), that file is conceptually "locked" for that agent's exclusive write access during the step.
2. **Multi-Agent Dispatch Rules:** The Universal Orchestrator must dispatch write tasks sequentially if they involve the same files or dependent systems.

---

## Examples

### Examples of Safe Parallel Execution
- Agent A reads `src/auth.ts` while Agent B reads `src/billing.ts`.
- Agent A runs the unit tests while Agent B checks the code formatting.
- Agent A creates a new component `src/Header.tsx` while Agent B creates a new component `src/Footer.tsx` (assuming neither requires modifying a shared index file concurrently).

### Examples of Unsafe Parallel Execution
- ❌ Agent A adds a new route to `routes.ts` while Agent B adds a different route to `routes.ts`.
- ❌ Agent A updates the database schema while Agent B writes the API endpoints querying that schema.
- ❌ Agent A updates `package.json` to add a dependency while Agent B updates `package.json` to modify a script.
