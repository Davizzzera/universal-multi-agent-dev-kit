# File Ownership

> Defines which agents are responsible for which files to prevent conflicts and ensure quality.

---

## Purpose

File ownership establishes clear lines of responsibility within the repository. It defines which agent is primarily responsible for creating, modifying, and maintaining specific categories of files, and which agent acts as the secondary reviewer. This prevents multiple agents from making conflicting changes to the same file.

---

## File Ownership Concept

Every file or directory in the repository has assigned owners.

- **Primary Owner:** The agent authorized to write to or modify the file.
- **Secondary Reviewer:** The agent authorized to review, validate, and suggest changes to the file, but not write to it directly without orchestration.

If an agent needs to modify a file it does not own, it must request the change through the Universal Orchestrator, which delegates the task to the Primary Owner.

---

## Conflict Handling

- **Prevention:** Only the Primary Owner may modify a file during the implementation phase.
- **Resolution:** If a conflict occurs (e.g., two tasks require changes to the same file by different owners), the Universal Orchestrator serializes the tasks, assigning them to the Primary Owner in order.

---

## Safe Parallel Editing Rules

Parallel editing is only safe when:
1. Agents are working on completely distinct, non-overlapping files.
2. The files do not have immediate, breaking dependencies on each other.

If two agents need to edit files that depend heavily on each other (e.g., an interface definition and its implementation), the execution must be sequential.

---

## File Category Ownership Table

| Directory / File Category                                      | Primary Owner             | Secondary Reviewer            |
|----------------------------------------------------------------|---------------------------|-------------------------------|
| `README.md`, `docs/`                                           | documentation-writer      | technical-writer              |
| `.agent/AGENTS.md`, `.agent/ARCHITECTURE.md`                   | universal-orchestrator    | technical-writer              |
| `.agent/agents/`                                               | agent-engineer            | universal-orchestrator        |
| `.agent/skills/`                                               | skill-designer            | agent-engineer                |
| `.agent/workflows/`                                            | workflow-architect        | universal-orchestrator        |
| `.agent/rules/`                                                | scope-guardian            | universal-orchestrator        |
| `.agent/templates/`                                            | documentation-writer      | technical-lead                |
| `.agent/scripts/`                                              | devops-specialist         | qa-tester                     |
| `src/components/`, `components/`, `app/`, `pages/`             | frontend-specialist       | technical-lead                |
| `api/`, `server/`, `routes/`, `controllers/`                   | backend-specialist        | technical-lead                |
| `database/`, `migrations/`, `prisma/`, `drizzle/`, `sql/`      | database-specialist       | backend-specialist            |
| `tests/`, `__tests__`, `playwright/`, `cypress/`               | qa-tester                 | technical-lead                |
| `Dockerfile`, `docker-compose.yml`, `.github/workflows/`       | devops-specialist         | security-reviewer             |
| `.env.example`                                                 | environment-manager       | security-reviewer             |
| `package.json`, `requirements.txt`, `pyproject.toml`           | technical-lead            | dependency-security-auditor   |

---

## Notes on Specific Roles

- **technical-lead:** Acts as a high-level reviewer ensuring architectural consistency.
- **universal-orchestrator:** Owns the core orchestration logic and high-level agent architecture.
- **security-reviewer:** Ensures no sensitive data or insecure configurations are introduced.
