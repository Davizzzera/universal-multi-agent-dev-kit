# Index — Universal Multi-Agent Development Kit

> Human-readable index of all directories and their purposes.

---

## Core Directories

| Directory             | Purpose                                                        | Status              |
|-----------------------|----------------------------------------------------------------|---------------------|
| `.agent/`             | Core agent system root.                                        | ✅ Created          |
| `.agent/agents/`      | Agent definitions and configurations.                          | ✅ Populated        |
| `.agent/skills/`      | Reusable skill definitions.                                    | ✅ Populated        |
| `.agent/workflows/`   | Workflow definitions and execution orders.                     | ✅ Populated        |
| `.agent/rules/`       | Global rules and constraints.                                  | ✅ Populated        |
| `.agent/memory/`      | Shared context and state between agents.                       | 📦 Empty (v0.2.0)  |
| `.agent/templates/`   | Reusable templates for common patterns.                        | ✅ Populated        |
| `.agent/scripts/`     | Validation and automation scripts.                             | ✅ Populated        |
| `.agent/indexes/`     | Generated indexes for agent/skill/workflow discovery.          | ✅ Populated        |

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

## Skills

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Skills Root** (`.agent/skills/`)                      |                                                              |                     |
| `README.md`                                             | Skills library overview.                                     | ✅ Created          |
| `orchestration/`                                        | Orchestration skills (e.g. coordinator-mode).                | ✅ Created (6)      |
| `context/`                                              | Context skills (e.g. codebase-map).                          | ✅ Created (5)      |
| `planning/`                                             | Planning skills (e.g. task-breakdown).                       | ✅ Created (6)      |
| `frontend/`                                             | Frontend skills (e.g. react-component-create).               | ✅ Created (6)      |
| `ui-ux/`                                                | UI-UX skills (e.g. ux-flow-audit).                           | ✅ Created (6)      |
| `backend/`                                              | Backend skills (e.g. api-contract-design).                   | ✅ Created (6)      |
| `auth/`                                                 | Auth skills (e.g. auth-flow-design).                         | ✅ Created (4)      |
| `database/`                                             | Database skills (e.g. database-schema-design).               | ✅ Created (6)      |
| `data-bi/`                                              | Data-BI skills (e.g. data-cleaning).                         | ✅ Created (6)      |
| `ai-agents/`                                            | AI-Agents skills (e.g. prompt-architecture).                 | ✅ Created (6)      |
| `automation/`                                           | Automation skills (e.g. python-script-automation).           | ✅ Created (6)      |
| `qa/`                                                   | QA skills (e.g. test-plan-create).                           | ✅ Created (6)      |
| `security/`                                             | Security skills (e.g. secrets-detection).                    | ✅ Created (6)      |
| `devops/`                                               | DevOps skills (e.g. dockerfile-create).                      | ✅ Created (6)      |
| `github/`                                               | GitHub skills (e.g. conventional-commits).                   | ✅ Created (5)      |
| `documentation/`                                        | Documentation skills (e.g. readme-create).                   | ✅ Created (6)      |
| `marketing/`                                            | Marketing skills (e.g. landing-page-copy).                   | ✅ Created (6)      |
| `maintenance/`                                          | Maintenance skills (e.g. technical-debt-detection).          | ✅ Created (6)      |

## Workflows

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Workflows Root** (`.agent/workflows/`)                |                                                              |                     |
| `README.md`                                             | Workflows directory overview.                                | ✅ Created          |
| `plan.workflow.md`                                      | Analyze request and create safe plan.                        | ✅ Created          |
| `coordinate.workflow.md`                                | Coordinate multiple agents for complex tasks.                | ✅ Created          |
| `create-feature.workflow.md`                            | Create a new feature safely.                                 | ✅ Created          |
| `enhance-feature.workflow.md`                           | Improve an existing feature.                                 | ✅ Created          |
| `debug.workflow.md`                                     | Investigate and resolve bugs.                                | ✅ Created          |
| `refactor.workflow.md`                                  | Improve code structure without changing behavior.            | ✅ Created          |
| `test.workflow.md`                                      | Create, improve or run tests.                                | ✅ Created          |
| `verify.workflow.md`                                    | Verify implementation.                                       | ✅ Created          |
| `security-review.workflow.md`                           | Perform defensive security review.                           | ✅ Created          |
| `database-change.workflow.md`                           | Plan and implement database changes.                         | ✅ Created          |
| `api-development.workflow.md`                           | Design and implement API endpoints.                          | ✅ Created          |
| `frontend-ui.workflow.md`                               | Create or improve frontend UI.                               | ✅ Created          |
| `automation.workflow.md`                                | Design and validate automations.                             | ✅ Created          |
| `ai-feature.workflow.md`                                | Design and validate AI-powered features.                     | ✅ Created          |
| `document.workflow.md`                                  | Create or update documentation.                              | ✅ Created          |
| `deploy.workflow.md`                                    | Prepare deployment configuration.                            | ✅ Created          |
| `release.workflow.md`                                   | Prepare repository release.                                  | ✅ Created          |
| `emergency-fix.workflow.md`                             | Handle urgent fixes safely.                                  | ✅ Created          |

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

## Scripts

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Scripts Root** (`.agent/scripts/`)                    |                                                              |                     |
| `README.md`                                             | Scripts directory overview.                                  | ✅ Created          |
| `common.py`                                             | Shared helper functions.                                     | ✅ Created          |
| `validate_structure.py`                                 | Validates expected repository structure.                     | ✅ Created          |
| `validate_agents.py`                                    | Validates all agent files.                                   | ✅ Created          |
| `validate_skills.py`                                    | Validates all skill files.                                   | ✅ Created          |
| `validate_workflows.py`                                 | Validates all workflow files.                                | ✅ Created          |
| `validate_markdown.py`                                  | Performs lightweight Markdown quality validation.            | ✅ Created          |
| `security_check.py`                                     | Defensive repository content scan for secrets.               | ✅ Created          |
| `generate_index.py`                                     | Generates JSON index files.                                  | ✅ Created          |
| `verify_all.py`                                         | Runs all validation scripts and generates indexes.           | ✅ Created          |

## Indexes

| Directory / File                                        | Purpose                                                      | Status              |
|---------------------------------------------------------|--------------------------------------------------------------|---------------------|
| **Indexes Root** (`.agent/indexes/`)                    |                                                              |                     |
| `repository.index.json`                                 | Overall repository statistics and index list.                | ✅ Generated        |
| `agents.index.json`                                     | Generated index of all agents.                               | ✅ Generated        |
| `skills.index.json`                                     | Generated index of all skills.                               | ✅ Generated        |
| `workflows.index.json`                                  | Generated index of all workflows.                            | ✅ Generated        |

## Adapter Directories

| Directory               | Purpose                                                      | Status              |
|--------------------------|--------------------------------------------------------------|---------------------|
| `adapters/antigravity/`  | Adapter for the Antigravity AI coding tool.                  | ✅ Populated        |
| `README.md`              | Antigravity adapter documentation.                           | ✅ Created          |
| `AGENTS.md`              | Antigravity entrypoint file.                                 | ✅ Created          |
| `adapter-manifest.json`  | Adapter manifest configuration.                              | ✅ Created          |
| `install.md`             | Installation and setup guide.                                | ✅ Created          |
| `usage.md`               | Usage guide and instructions.                                | ✅ Created          |
| `quick-start.md`         | Quick start and prompt patterns.                             | ✅ Created          |
| `project-setup.md`       | Project structure customization guide.                       | ✅ Created          |
| `integration-rules.md`   | Antigravity-specific integration rules.                      | ✅ Created          |
| `prompt-library.md`      | Reusable prompt patterns.                                    | ✅ Created          |
| `troubleshooting.md`     | Common issues and safe fixes.                                | ✅ Created          |
| `examples/initialize-kit.prompt.md`     | Prompt to initialize the kit.                 | ✅ Created          |
| `examples/plan-workflow.prompt.md`      | Prompt to use the plan workflow.              | ✅ Created          |
| `examples/coordinate-workflow.prompt.md`| Prompt for complex multi-agent coordination.  | ✅ Created          |
| `examples/create-feature.prompt.md`     | Prompt to create a new feature.               | ✅ Created          |
| `examples/frontend-ui.prompt.md`        | Prompt for frontend UI changes.               | ✅ Created          |
| `examples/api-development.prompt.md`    | Prompt for backend API development.           | ✅ Created          |
| `examples/debug.prompt.md`              | Prompt for bug fixing and debugging.          | ✅ Created          |
| `examples/verify.prompt.md`             | Prompt for verification and testing.          | ✅ Created          |
| `examples/release.prompt.md`            | Prompt for release preparation.               | ✅ Created          |
| `adapters/claude-code/`  | Adapter for Claude Code.                                     | 📦 Empty (Future)   |
| `adapters/cursor/`       | Adapter for Cursor.                                          | 📦 Empty (Future)   |
| `adapters/codex/`        | Adapter for OpenAI Codex.                                    | 📦 Empty (Future)   |
| `adapters/generic/`      | Generic adapter template for any AI tool.                    | 📦 Empty (Future)   |

## Pack Directories

| Directory / File              | Purpose                                                   | Status              |
|-------------------------------|-----------------------------------------------------------|---------------------|
| `packs/README.md`             | Overview of all project packs.                            | ✅ Created          |
| `packs/web-app-pack/`         | Pack for full-stack web applications.                     | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/landing-page-pack/`    | Pack for marketing and landing pages.                     | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/api-pack/`             | Pack for backend APIs and services.                       | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/data-bi-pack/`         | Pack for data processing and BI.                          | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/automation-pack/`      | Pack for Python/browser automation.                       | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/ai-agent-pack/`        | Pack for AI features and prompt systems.                  | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/n8n-pack/`             | Pack for n8n automations.                                 | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/ecommerce-pack/`       | Pack for ecommerce systems.                               | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |
| `packs/enterprise-pack/`      | Pack for enterprise systems.                              | ✅ Populated        |
| `README.md`                   | Pack overview.                                            | ✅ Created          |
| `pack-manifest.json`          | Pack manifest.                                            | ✅ Created          |
| `agents.md`                   | Recommended agents.                                       | ✅ Created          |
| `skills.md`                   | Recommended skills.                                       | ✅ Created          |
| `workflows.md`                | Recommended workflows.                                    | ✅ Created          |
| `usage.md`                    | Usage guide.                                              | ✅ Created          |
| `example.prompt.md`           | Example prompt.                                           | ✅ Created          |

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

> **v0.1.0 (Unreleased):** Core orchestration agents, specialist agents, core skills library, operational workflows, validation scripts/indexes, the Antigravity adapter, and 9 reusable project packs have been implemented.

