# Contributing to Universal Multi-Agent Development Kit

Thank you for your interest in contributing to this project. This document outlines the principles, rules, and expectations for all contributions.

---

## Project Principles

1. **Clarity over cleverness.** All agents, skills, and workflows must be easy to read, understand, and maintain.
2. **Reusability first.** Every component should be designed for reuse across different projects and AI tools.
3. **Safety by default.** Security, validation, and defensive practices are mandatory, not optional.
4. **Incremental progress.** Contributions should be focused, well-scoped, and testable independently.
5. **Professional standards.** This repository follows production-grade quality expectations.

---

## Language Rule

> **All repository content must be written in English.**
>
> This includes: file names, folder names, documentation, code comments, Markdown content, commit messages, package metadata, and GitHub content.

---

## How to Propose Agents

To propose a new agent:

1. Open an issue with the title: `[Agent Proposal] <Agent Name>`.
2. Describe the agent's role, responsibilities, and expected behavior.
3. Specify which skills the agent will use.
4. Specify which workflows the agent participates in.
5. Describe how the agent interacts with the orchestrator.
6. Include examples of when the agent should be invoked.
7. Follow the agent design guidelines in [docs/agent-design.md](docs/agent-design.md).

---

## How to Propose Skills

To propose a new skill:

1. Open an issue with the title: `[Skill Proposal] <Skill Name>`.
2. Describe the skill's purpose and the task it performs.
3. Specify input requirements and expected outputs.
4. Describe any preconditions or dependencies.
5. Provide a usage example.
6. Follow the skill design guidelines in [docs/skill-design.md](docs/skill-design.md).

---

## How to Propose Workflows

To propose a new workflow:

1. Open an issue with the title: `[Workflow Proposal] <Workflow Name>`.
2. Describe the workflow's purpose and trigger conditions.
3. List the steps in execution order.
4. Specify which agents and skills are involved in each step.
5. Indicate which steps are parallel and which are sequential.
6. Follow the workflow design guidelines in [docs/workflow-design.md](docs/workflow-design.md).

---

## Safety and Security Rules

All contributions must follow these security rules:

- **No secrets, tokens, credentials, or private keys** may be added to the repository.
- **No personal data** may be included in any file.
- **No offensive security content.** Security-related content must be defensive only: auditing, validation, hardening, secrets detection, dependency review, secure configuration, and safe development practices.
- **No external dependencies** unless explicitly approved and documented.
- **No generated junk files** (build artifacts, cache files, logs).

---

## Validation Expectations

Before submitting a contribution:

1. Ensure the folder structure is consistent with the project architecture.
2. Ensure all Markdown files are well-formed and readable.
3. Ensure no secrets or sensitive data are included.
4. Ensure no unexpected or unrelated files are added.
5. Run `npm run verify` if validation scripts are available.
6. Use a clear [Conventional Commit](https://www.conventionalcommits.org/) message.

---

## Commit Message Format

Use Conventional Commits:

```
<type>: <short description>

[optional body]
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `ci`.

Examples:
- `feat: add context-reader agent`
- `docs: update orchestration-model documentation`
- `fix: correct skill loading order in workflow`

---

## Code of Conduct

Be respectful, professional, and constructive. Contributions that violate these principles will not be accepted.
