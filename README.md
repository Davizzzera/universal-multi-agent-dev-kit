# Universal Multi-Agent Development Kit

> A professional, reusable and production-ready multi-agent development kit for AI-assisted software engineering.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-brightgreen.svg)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-foundation_release-orange.svg)](#repository-status)

---

## What Is This?

The **Universal Multi-Agent Development Kit** is a structured framework that provides reusable agents, skills, workflows, rules, and validation tools for AI-assisted software engineering.

It is designed to work with AI coding tools such as **Antigravity** (with planned support for Claude Code, Cursor, Codex, and others) — providing a universal layer of orchestration, quality control, and best practices that any AI assistant can follow.

This kit is **not a library or an npm package to install**. It is a **repository of structured instructions, agents, skills, and workflows** that AI coding tools can read, follow, and execute.

## Why it Exists

As AI coding agents become more capable, they need structure to operate safely on large codebases. Without governance, AI agents often overwrite files concurrently, ignore architectural boundaries, or fail to validate their output. This kit solves those problems by enforcing strict file ownership, validation-first delivery, and clear multi-agent coordination.

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

## Repository Status

> **v0.1.0 Foundation Release**
>
> This repository provides the complete structural foundation. It is a strong foundation release, not a fully automated CLI product yet.

### What is Included

- **6 Orchestration Agents:** Managing the multi-agent lifecycle (`universal-orchestrator`, `task-router`, etc.).
- **54 Specialist Agents:** Covering Frontend, Backend, Database, AI, Security, QA, and more.
- **104 Skills:** Reusable procedures across 18 categories.
- **18 Workflows:** Step-by-step processes for common tasks (e.g., `create-feature`, `bug-fix`).
- **9 Project Packs:** Domain-specific presets (e.g., `web-app-pack`, `enterprise-pack`).
- **1 Adapter:** Official integration rules for **Antigravity AI**.
- **Validation Scripts:** Built-in Python scripts for structural checking.

---

## Quick Start for Antigravity

This kit is ready to be used with Antigravity AI today:

1. Clone this repository locally.
2. Ask Antigravity to review `adapters/antigravity/README.md`.
3. Use the prompts in `adapters/antigravity/examples/` to instruct Antigravity using the kit's workflows and packs.
4. Or, copy the `.agent/`, `packs/`, and `adapters/` directories into your own target project to enable the orchestration model there.

*Note: A CLI installer (`npx universal-agent-kit init`) is planned for a future release to automate this process.*

---

## Safety Principles

This kit enforces a **"Validation-First"** approach:
- **No untested delivery:** Agents are instructed not to deliver code without passing validation.
- **Scope restriction:** Agents cannot modify files outside their designated scope (`scope-guardian`).
- **Conflict prevention:** Write operations are strictly sequential to prevent file corruption (`conflict-controller`).

---

## Validation

The repository is self-checking. You can run the validation scripts using `npm` shortcuts:

```bash
npm run verify
npm run generate:index
```

**Note:** Python 3.10+ is required for the validation scripts. No external Python dependencies are required (uses standard library only). If your local environment does not have Python configured in the PATH, these automated scripts will not run, but the kit's Markdown instructions remain fully functional for the AI.

---

## Project Packs

Project Packs are advisory presets that help the Orchestrator select the right agents and workflows. See [packs/README.md](packs/README.md).

| Pack | Purpose |
|------|---------|
| `web-app-pack` | Full-stack web applications and SaaS interfaces. |
| `landing-page-pack` | Marketing, product, and lead capture pages. |
| `api-pack` | Backend APIs, REST endpoints, and service layers. |
| `data-bi-pack` | Data processing, CSV/Excel ingest, BI reporting. |
| `automation-pack` | Python scripts, browser automation, scheduled jobs. |
| `ai-agent-pack` | AI features, RAG pipelines, prompt systems. |
| `n8n-pack` | n8n automations, webhook flows, integrations. |
| `ecommerce-pack` | Product catalogs, inventory, checkout flows. |
| `enterprise-pack` | Large, multi-domain, high-risk projects. |

---

## Roadmap Summary

- **v0.2.0:** Quality hardening and Python validation improvements *(In Progress)*.
- **v0.3.0:** Additional adapters (Claude Code, Cursor, Codex, Generic).
- **v0.4.0:** Optional CLI installer.
- **v0.5.0:** Pack expansion and examples.
- **v1.0.0:** Stable public release.

See [docs/roadmap.md](docs/roadmap.md) for full details.

---

## Key Links

- [Agents List](.agent/AGENTS.md)
- [Architecture Details](.agent/ARCHITECTURE.md)
- [Antigravity Adapter](adapters/antigravity/README.md)
- [Project Packs](packs/README.md)
- [Release Notes](RELEASE_NOTES.md)
- [Getting Started Guide](docs/getting-started.md)
- [Full Roadmap](docs/roadmap.md)

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting proposals.

## License

This project is licensed under the [MIT License](LICENSE).

Copyright © 2026 Davizzzera.
