# Index — Universal Multi-Agent Development Kit

> Human-readable index of all directories and their purposes.

---

## Core Directories

| Directory             | Purpose                                                        | Status              |
|-----------------------|----------------------------------------------------------------|---------------------|
| `.agent/`             | Core agent system root.                                        | ✅ Created          |
| `.agent/agents/`      | Agent definitions and configurations.                          | ✅ Populated        |
| `.agent/skills/`      | Reusable skill definitions.                                    | 📦 Empty (v0.3.0)  |
| `.agent/workflows/`   | Workflow definitions and execution orders.                     | 📦 Empty (v0.4.0)  |
| `.agent/rules/`       | Global rules and constraints.                                  | ✅ Populated        |
| `.agent/memory/`      | Shared context and state between agents.                       | 📦 Empty (v0.2.0)  |
| `.agent/templates/`   | Reusable templates for common patterns.                        | ✅ Populated        |
| `.agent/scripts/`     | Validation and automation scripts.                             | 📦 Empty (v0.4.0)  |
| `.agent/indexes/`     | Generated indexes for agent/skill/workflow discovery.          | 📦 Empty (v0.4.0)  |

## Agents

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Agents Root** (`.agent/agents/`)                      |                                                              |                     |
| `README.md`                                             | Agents directory overview.                                   | ✅ Created          |
| **Orchestration** (`.agent/agents/orchestration/`)      |                                                              |                     |
| `README.md`                                             | Orchestration agents overview.                               | ✅ Created          |
| `universal-orchestrator.agent.md`                       | Primary coordinator of the system.                           | ✅ Created          |
| `project-context-reader.agent.md`                       | Analyzes the repository before execution.                    | ✅ Created          |
| `task-router.agent.md`                                  | Classifies requests and determines workflow.                 | ✅ Created          |
| `scope-guardian.agent.md`                               | Protects boundaries and prevents scope creep.                | ✅ Created          |
| `conflict-controller.agent.md`                          | Manages file locks and parallel execution.                   | ✅ Created          |
| `final-reviewer.agent.md`                               | Validates and synthesizes final delivery.                    | ✅ Created          |
| **Product** (`.agent/agents/product/`)                  |                                                              |                     |
| `README.md`                                             | Product agents overview.                                     | ✅ Created          |
| `product-manager.agent.md`                              | Product direction and priorities.                            | ✅ Created          |
| `business-analyst.agent.md`                             | Business process and rules analysis.                         | ✅ Created          |
| `requirements-engineer.agent.md`                        | Structured requirements and acceptance criteria.             | ✅ Created          |
| `risk-analyst.agent.md`                                 | Risk identification and mitigation.                          | ✅ Created          |
| **Architecture** (`.agent/agents/architecture/`)        |                                                              |                     |
| `README.md`                                             | Architecture agents overview.                                | ✅ Created          |
| `software-architect.agent.md`                           | System design and architecture.                              | ✅ Created          |
| `technical-lead.agent.md`                               | Technical direction and standards.                           | ✅ Created          |
| `codebase-analyst.agent.md`                             | Codebase structure analysis.                                 | ✅ Created          |
| `refactor-specialist.agent.md`                          | Code refactoring without behavior change.                    | ✅ Created          |
| `performance-engineer.agent.md`                         | Performance analysis and optimization.                       | ✅ Created          |
| **Frontend** (`.agent/agents/frontend/`)                |                                                              |                     |
| `README.md`                                             | Frontend agents overview.                                    | ✅ Created          |
| `frontend-specialist.agent.md`                          | UI implementation.                                           | ✅ Created          |
| `react-specialist.agent.md`                             | React-specific development.                                  | ✅ Created          |
| `ui-ux-designer.agent.md`                               | Usability and UX improvements.                               | ✅ Created          |
| `design-system-specialist.agent.md`                     | Visual consistency and design tokens.                        | ✅ Created          |
| `responsive-layout-specialist.agent.md`                 | Responsive layout across devices.                            | ✅ Created          |
| `accessibility-specialist.agent.md`                     | Accessibility and semantic structure.                        | ✅ Created          |
| **Backend** (`.agent/agents/backend/`)                  |                                                              |                     |
| `README.md`                                             | Backend agents overview.                                     | ✅ Created          |
| `backend-specialist.agent.md`                           | Server-side logic and APIs.                                  | ✅ Created          |
| `api-designer.agent.md`                                 | API contract design.                                         | ✅ Created          |
| `auth-specialist.agent.md`                              | Authentication and authorization.                            | ✅ Created          |
| `integration-specialist.agent.md`                       | External API integrations.                                   | ✅ Created          |
| `webhook-specialist.agent.md`                           | Webhook design and validation.                               | ✅ Created          |
| **Database** (`.agent/agents/database/`)                |                                                              |                     |
| `README.md`                                             | Database agents overview.                                    | ✅ Created          |
| `database-specialist.agent.md`                          | Schema design and data integrity.                            | ✅ Created          |
| `sql-specialist.agent.md`                               | SQL query writing and optimization.                          | ✅ Created          |
| `migration-specialist.agent.md`                         | Database migration management.                               | ✅ Created          |
| `data-quality-specialist.agent.md`                      | Data quality validation and cleaning.                        | ✅ Created          |
| **AI & Automation** (`.agent/agents/ai-automation/`)    |                                                              |                     |
| `README.md`                                             | AI and automation agents overview.                           | ✅ Created          |
| `ai-engineer.agent.md`                                  | AI feature design and implementation.                        | ✅ Created          |
| `prompt-engineer.agent.md`                              | Prompt design and optimization.                              | ✅ Created          |
| `agent-engineer.agent.md`                               | Agent and multi-agent design.                                | ✅ Created          |
| `rag-specialist.agent.md`                               | RAG system design.                                           | ✅ Created          |
| `n8n-automation-specialist.agent.md`                    | n8n workflow design.                                         | ✅ Created          |
| `python-automation-specialist.agent.md`                 | Python automation scripts.                                   | ✅ Created          |
| **QA** (`.agent/agents/qa/`)                            |                                                              |                     |
| `README.md`                                             | QA agents overview.                                          | ✅ Created          |
| `qa-tester.agent.md`                                    | Quality assurance testing.                                   | ✅ Created          |
| `unit-test-specialist.agent.md`                         | Unit test creation and review.                               | ✅ Created          |
| `e2e-test-specialist.agent.md`                          | End-to-end test creation.                                    | ✅ Created          |
| `visual-regression-specialist.agent.md`                 | Visual regression validation.                                | ✅ Created          |
| `bug-hunter.agent.md`                                   | Bug investigation and root cause analysis.                   | ✅ Created          |
| **Security** (`.agent/agents/security/`)                |                                                              |                     |
| `README.md`                                             | Security agents overview.                                    | ✅ Created          |
| `security-reviewer.agent.md`                            | Defensive security review.                                   | ✅ Created          |
| `secrets-scanner.agent.md`                              | Secrets and credentials detection.                           | ✅ Created          |
| `dependency-security-auditor.agent.md`                  | Dependency vulnerability audit.                              | ✅ Created          |
| `auth-security-reviewer.agent.md`                       | Auth flow security review.                                   | ✅ Created          |
| `privacy-compliance-reviewer.agent.md`                  | Privacy and data handling review.                            | ✅ Created          |
| **DevOps** (`.agent/agents/devops/`)                    |                                                              |                     |
| `README.md`                                             | DevOps agents overview.                                      | ✅ Created          |
| `devops-specialist.agent.md`                            | Deployment and infrastructure.                               | ✅ Created          |
| `docker-specialist.agent.md`                            | Docker and container workflows.                              | ✅ Created          |
| `ci-cd-specialist.agent.md`                             | CI/CD pipeline creation.                                     | ✅ Created          |
| `cloud-specialist.agent.md`                             | Cloud deployment planning.                                   | ✅ Created          |
| `release-manager.agent.md`                              | Release and versioning management.                           | ✅ Created          |
| **Documentation** (`.agent/agents/documentation/`)      |                                                              |                     |
| `README.md`                                             | Documentation agents overview.                               | ✅ Created          |
| `documentation-writer.agent.md`                         | User and developer documentation.                            | ✅ Created          |
| `technical-writer.agent.md`                             | Technical documentation and guides.                          | ✅ Created          |
| `github-repository-manager.agent.md`                    | Repository structure and GitHub conventions.                 | ✅ Created          |
| `pull-request-writer.agent.md`                          | PR summaries and checklists.                                 | ✅ Created          |
| `changelog-maintainer.agent.md`                         | Changelog and release history.                               | ✅ Created          |
| **Marketing** (`.agent/agents/marketing/`)              |                                                              |                     |
| `README.md`                                             | Marketing agents overview.                                   | ✅ Created          |
| `copywriter.agent.md`                                   | Product and conversion copy.                                 | ✅ Created          |
| `seo-specialist.agent.md`                               | SEO structure and metadata.                                  | ✅ Created          |
| `landing-page-strategist.agent.md`                      | Landing page strategy.                                       | ✅ Created          |
| `growth-specialist.agent.md`                            | Growth and conversion analysis.                              | ✅ Created          |

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

> **Phase 4 (v0.4.0):** Core orchestration and specialist agents have been implemented.

