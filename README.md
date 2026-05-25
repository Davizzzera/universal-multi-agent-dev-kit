# Universal Multi-Agent Development Kit

> A professional, reusable and production-ready multi-agent development kit for AI-assisted software engineering.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-early%20foundation-orange.svg)](#repository-status)

---

## What Is This?

The **Universal Multi-Agent Development Kit** is a structured framework that provides reusable agents, skills, workflows, rules, and validation tools for AI-assisted software engineering.

It is designed to work with AI coding tools such as **Antigravity**, Claude Code, Cursor, Codex, and others — providing a universal layer of orchestration, quality control, and best practices that any AI assistant can follow.

This kit is **not a library or an npm package to install**. It is a **repository of structured instructions, agents, skills, and workflows** that AI coding tools can read, follow, and execute.

---

## Core Concepts

| Concept      | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Agent**    | Who does the work. An autonomous unit with a role and responsibilities.     |
| **Skill**    | How the work is done. A reusable, composable procedure or technique.        |
| **Workflow** | When and in which order the work happens. Orchestrated sequences of tasks.  |
| **Rule**     | What must never be violated. Global constraints and safety policies.        |
| **Script**   | How the repository validates itself. Automated checks and verifications.    |
| **Adapter**  | How this kit is used inside a specific AI coding tool.                      |
| **Pack**     | Optional group of agents, skills, and workflows for a specific project type.|

---

## Architecture Overview

The kit follows a **multi-agent orchestration model**:

1. A **Universal Orchestrator** understands the user request.
2. A **Context Reader** analyzes the project structure and state.
3. A **Task Router** identifies the type of work required.
4. **Specialist Agents** are selected based on the task type.
5. **Skills** are loaded and applied based on the task requirements.
6. **Reading, analysis, and research** happen in **parallel**.
7. **Writing and file modifications** are **controlled and sequential** when conflict risk exists.
8. **QA, security, and validation agents** review the result.
9. A **Final Reviewer** consolidates the delivery.

### Parallel and Sequential Execution

| Phase            | Mode       | Reason                                    |
|------------------|------------|-------------------------------------------|
| Research         | Parallel   | No conflict risk, faster execution.       |
| Analysis         | Parallel   | Independent reads, safe to parallelize.   |
| Implementation   | Sequential | File writes must be conflict-free.        |
| Validation       | Parallel   | Independent checks, safe to parallelize.  |

---

## Repository Status

> **Early Foundation — v0.1.0**
>
> This repository is in its initial foundation phase. The directory structure, core documentation, and architectural principles are being established. Agents, skills, workflows, and adapters will be implemented in subsequent phases.

---

## Planned Phases

| Phase   | Description                          | Status         |
|---------|--------------------------------------|----------------|
| v0.1.0  | Repository foundation                | 🟡 In Progress |
| v0.2.0  | Core agents                          | ⬜ Planned     |
| v0.3.0  | Core skills                          | ⬜ Planned     |
| v0.4.0  | Workflows and validation scripts     | ⬜ Planned     |
| v0.5.0  | Antigravity adapter                  | ⬜ Planned     |
| v1.0.0  | Stable release                       | ⬜ Planned     |

---

## Usage with Antigravity

This kit is designed to be read and followed by AI coding assistants. When using **Antigravity** (or another supported AI tool):

1. Clone or reference this repository in your project.
2. The AI assistant reads the `.agent/` directory to understand the orchestration model.
3. Agents, skills, and workflows guide the AI's behavior.
4. Adapters provide tool-specific configuration and integration.

Detailed setup instructions for Antigravity will be provided in a future phase. See [docs/antigravity-setup.md](docs/antigravity-setup.md) for current status.

---

## Documentation

- [Getting Started](docs/getting-started.md)
- [Agent Design](docs/agent-design.md)
- [Skill Design](docs/skill-design.md)
- [Workflow Design](docs/workflow-design.md)
- [Orchestration Model](docs/orchestration-model.md)
- [Validation Model](docs/validation-model.md)
- [Antigravity Setup](docs/antigravity-setup.md)
- [Examples](docs/examples.md)
- [Roadmap](docs/roadmap.md)

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting proposals.

---

## License

This project is licensed under the [MIT License](LICENSE).

Copyright © 2026 Davizzzera.
