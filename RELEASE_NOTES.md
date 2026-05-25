# Universal Multi-Agent Dev Kit v0.1.0

**Release type:** Foundation Release

## Release Summary
Welcome to the first public foundation release of the **Universal Multi-Agent Dev Kit** (v0.1.0). This release establishes the core agnostic architecture for integrating advanced AI coding agents into any project. It is designed to enforce strict file ownership, validation-first delivery, and multi-agent coordination boundaries.

## What is Included
This release delivers the complete foundational architecture, ready to be used via manual prompts or with supported tools.

### Core Architecture
- **Global Rules:** Strict boundaries for safe AI execution (`file-ownership`, `security-rules`, `handoff-contract`, `output-contract`).
- **Templates:** Standardized markdown templates for agent creation, skills, workflows, plans, and tasks.
- **Orchestration Agents:** The core management layer (e.g., `universal-orchestrator`, `task-router`, `scope-guardian`, `final-reviewer`).
- **Specialist Agents:** Personas covering the entire software lifecycle (Frontend, Backend, DB, QA, Security, AI, DevOps, Docs, Product, Marketing).
- **Core Skills Library:** Granular, reusable techniques spanning 18 categories.
- **Operational Workflows:** 18 documented workflows to guide multi-agent interactions for common tasks (e.g., `create-feature`, `bug-fix`, `security-review`).
- **Validation Scripts:** Built-in Python scripts to verify repository integrity and markdown formatting.
- **Antigravity Adapter:** The first officially supported adapter, providing integration rules and prompts specifically for Antigravity AI.
- **Project Packs:** 9 curated presets (`web-app`, `api`, `ecommerce`, `enterprise`, etc.) to accelerate agent and workflow selection.

### Main Numbers
- **6** Orchestration Agents
- **54** Specialist Agents
- **104** Core Skills
- **18** Operational Workflows
- **9** Project Packs
- **1** Implemented Adapter (Antigravity)

## How to Use
1. Clone this repository or copy the `.agent/`, `packs/`, and `adapters/` directories into your target project.
2. Read the `.agent/AGENTS.md` and `docs/getting-started.md` guides.
3. If using Antigravity, refer to `adapters/antigravity/README.md` and the provided example prompts.
4. Provide the Orchestrator with your goal and specify a recommended Project Pack and Workflow.

## Validation Notes
The kit is self-validating. You can run `npm run verify` to execute a suite of structural and markdown checks.

## Known Limitations
- **No CLI installer yet:** The kit must currently be copied manually or cloned. A CLI is planned for future releases.
- **Python requirement:** The included validation scripts (`.agent/scripts/`) require **Python 3.10+**. 
- **Environment Configuration:** The local environment may need Python configured in the PATH to run `npm run verify` successfully. No external Python dependencies (like `pip` installs) are required; it uses the standard library.
- **Adapters:** Only the Antigravity adapter is fully implemented. Adapters for Claude Code, Cursor, Codex, and a Generic template are planned but not yet implemented.

## Safety Notes
This kit enforces a "Validation-First" approach. Agents are instructed not to deliver code without passing validation, and not to modify files outside their designated scope. The `security-reviewer` and `privacy-compliance-reviewer` agents are available for high-risk changes.

## Next Roadmap Items
- **v0.2.0:** Quality hardening and Python validation improvements.
- **v0.3.0:** Additional adapters (Claude Code, Cursor, Codex).
- **v0.4.0:** Optional CLI installer (`npx universal-agent-kit init`).

---
**Tag:** v0.1.0
