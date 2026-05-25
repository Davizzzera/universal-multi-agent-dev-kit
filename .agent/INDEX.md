# Index — Universal Multi-Agent Development Kit

> Human-readable index of all directories and their purposes.

---

## Core Directories

| Directory             | Purpose                                                        | Status              |
|-----------------------|----------------------------------------------------------------|---------------------|
| `.agent/`             | Core agent system root.                                        | ✅ Created          |
| `.agent/agents/`      | Agent definitions and configurations.                          | 📦 Empty (v0.2.0)  |
| `.agent/skills/`      | Reusable skill definitions.                                    | 📦 Empty (v0.3.0)  |
| `.agent/workflows/`   | Workflow definitions and execution orders.                     | 📦 Empty (v0.4.0)  |
| `.agent/rules/`       | Global rules and constraints.                                  | ✅ Populated        |
| `.agent/memory/`      | Shared context and state between agents.                       | 📦 Empty (v0.2.0)  |
| `.agent/templates/`   | Reusable templates for common patterns.                        | ✅ Populated        |
| `.agent/scripts/`     | Validation and automation scripts.                             | 📦 Empty (v0.4.0)  |
| `.agent/indexes/`     | Generated indexes for agent/skill/workflow discovery.          | 📦 Empty (v0.4.0)  |

## Rules and Templates

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Rules** (`.agent/rules/`)                             |                                                              |                     |
| `global-rules.md`                                       | Complete global rules document.                              | ✅ Created          |
| `agent-boundaries.md`                                   | Defines agent boundaries.                                    | ✅ Created          |
| `file-ownership.md`                                     | File ownership matrix.                                       | ✅ Created          |
| `parallel-execution.md`                                 | Parallel execution rules.                                    | ✅ Created          |
| `validation-rules.md`                                   | Validation rules document.                                   | ✅ Created          |
| `security-rules.md`                                     | Defensive security rules.                                    | ✅ Created          |
| `documentation-rules.md`                                | Documentation rules.                                         | ✅ Created          |
| `memory-rules.md`                                       | Memory rules.                                                | ✅ Created          |
| `handoff-rules.md`                                      | Handoff rules document.                                      | ✅ Created          |
| `output-contract-rules.md`                              | Output contract rules.                                       | ✅ Created          |
| **Templates** (`.agent/templates/`)                     |                                                              |                     |
| `agent-template.md`                                     | Template for agents.                                         | ✅ Created          |
| `skill-template.md`                                     | Template for skills.                                         | ✅ Created          |
| `workflow-template.md`                                  | Template for workflows.                                      | ✅ Created          |
| `task-brief-template.md`                                | Task brief template.                                         | ✅ Created          |
| `implementation-plan-template.md`                       | Implementation plan template.                                | ✅ Created          |
| `validation-report-template.md`                         | Validation report template.                                  | ✅ Created          |
| `pr-template.md`                                        | GitHub Pull Request template.                                | ✅ Created          |
| `release-template.md`                                   | Release notes template.                                      | ✅ Created          |
| `handoff-template.md`                                   | Handoff template.                                            | ✅ Created          |
| `agent-output-contract-template.md`                     | Agent output contract template.                              | ✅ Created          |

## Adapter Directories

| Directory               | Purpose                                                      | Status              |
|--------------------------|--------------------------------------------------------------|---------------------|
| `adapters/antigravity/`  | Adapter for the Antigravity AI coding tool.                  | 📦 Empty (v0.5.0)  |
| `adapters/claude-code/`  | Adapter for Claude Code.                                     | 📦 Empty (Future)   |
| `adapters/cursor/`       | Adapter for Cursor.                                          | 📦 Empty (Future)   |
| `adapters/codex/`        | Adapter for OpenAI Codex.                                    | 📦 Empty (Future)   |
| `adapters/generic/`      | Generic adapter template for any AI tool.                    | 📦 Empty (Future)   |

## Pack Directories

| Directory                   | Purpose                                                   | Status              |
|-----------------------------|-----------------------------------------------------------|---------------------|
| `packs/web-app-pack/`       | Agents, skills, and workflows for web applications.       | 📦 Empty (Future)   |
| `packs/landing-page-pack/`  | Agents, skills, and workflows for landing pages.          | 📦 Empty (Future)   |
| `packs/api-pack/`           | Agents, skills, and workflows for API development.        | 📦 Empty (Future)   |
| `packs/data-bi-pack/`       | Agents, skills, and workflows for data/BI projects.       | 📦 Empty (Future)   |
| `packs/automation-pack/`    | Agents, skills, and workflows for automation.             | 📦 Empty (Future)   |
| `packs/ai-agent-pack/`      | Agents, skills, and workflows for AI agent projects.      | 📦 Empty (Future)   |
| `packs/n8n-pack/`           | Agents, skills, and workflows for n8n automation.         | 📦 Empty (Future)   |
| `packs/ecommerce-pack/`     | Agents, skills, and workflows for ecommerce.              | 📦 Empty (Future)   |
| `packs/enterprise-pack/`    | Agents, skills, and workflows for enterprise projects.    | 📦 Empty (Future)   |

## Documentation

| Directory / File                | Purpose                                                | Status              |
|---------------------------------|--------------------------------------------------------|---------------------|
| `docs/getting-started.md`       | How to use the kit.                                    | ✅ Created          |
| `docs/agent-design.md`          | How to design agents.                                  | ✅ Created          |
| `docs/skill-design.md`          | How to design skills.                                  | ✅ Created          |
| `docs/workflow-design.md`       | How to design workflows.                               | ✅ Created          |
| `docs/orchestration-model.md`   | How the orchestration model works.                     | ✅ Created          |
| `docs/validation-model.md`      | How the validation system works.                       | ✅ Created          |
| `docs/antigravity-setup.md`     | How to set up the Antigravity adapter.                 | ✅ Created          |
| `docs/examples.md`              | Usage examples.                                        | ✅ Created          |
| `docs/roadmap.md`               | Project roadmap.                                       | ✅ Created          |

## Root Files

| File               | Purpose                                              | Status              |
|--------------------|------------------------------------------------------|---------------------|
| `README.md`        | Project overview and documentation entry point.      | ✅ Created          |
| `LICENSE`          | MIT License.                                         | ✅ Created          |
| `CHANGELOG.md`     | Version history and changes.                         | ✅ Created          |
| `CONTRIBUTING.md`  | Contribution guidelines.                             | ✅ Created          |
| `package.json`     | Project metadata and scripts.                        | ✅ Created          |
| `.gitignore`       | Git exclusion rules.                                 | ✅ Created          |

---

## Current Phase

> **Foundation Phase (v0.1.0):** The repository structure is established. Directories marked as "Empty" contain only `.gitkeep` files and will be populated in subsequent phases.
