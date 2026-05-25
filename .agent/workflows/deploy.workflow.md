---
name: deploy
type: workflow
description: Prepare deployment configuration, environment handling, CI/CD and production readiness.
trigger: ["deploy", "deployment", "publish", "production", "CI/CD", "Docker", "Vercel", "Render", "cloud"]
primary_agent: universal-orchestrator
required_agents: ["devops-specialist", "security-reviewer", "final-reviewer"]
optional_agents: ["docker-specialist", "ci-cd-specialist", "cloud-specialist", "backend-specialist", "frontend-specialist", "release-manager"]
required_skills: ["dockerfile-create", "docker-compose-create", "github-actions-ci", "environment-variable-management", "production-readiness-check", "healthcheck-endpoint", "security-release-checklist", "build-validation"]
validation_required: manual-and-automated
risk_level: critical
related_rules: [global-rules.md, file-ownership.md, parallel-execution.md]
---

# Workflow Purpose
Prepare deployment configuration, environment handling, CI/CD and production readiness.

## Important Behavior
- Do not expose secrets.
- Do not deploy destructive changes without approval.
- Validate environment variables and production readiness.

# Trigger Conditions
This workflow is initiated when the Universal Orchestrator identifies any of the following triggers in the user request:
- deploy
- deployment
- publish
- production
- CI/CD
- Docker
- Vercel
- Render
- cloud

# Required Inputs
- Clear user request or task description.
- Repository context and current state.
- (If applicable) Previous analysis or bug reports.

# Agents Involved
- **Primary Agent:** universal-orchestrator
- **Required Agents:** devops-specialist, security-reviewer, final-reviewer
- **Optional Agents:** docker-specialist, ci-cd-specialist, cloud-specialist, backend-specialist, frontend-specialist, release-manager

# Skills Involved
- dockerfile-create
- docker-compose-create
- github-actions-ci
- environment-variable-management
- production-readiness-check
- healthcheck-endpoint
- security-release-checklist
- build-validation

# Execution Steps
1. **Trigger Reception**: The Orchestrator identifies the user intent mapping to the `deploy` workflow.
2. **Context Gathering**: The Project Context Reader analyzes the repository state relevant to the request.
3. **Agent Selection**: The Task Router selects required specialist agents for the task.
4. **Scope Definition**: The Scope Guardian defines boundaries and rules to follow.
5. **Planning & Strategy**: Formulate the implementation plan safely.
6. **Execution Control**: The Conflict Controller assigns file locks if changes are necessary.
7. **Specialist Action**: Assigned agents execute the task following loaded skills.
8. **Consolidation**: The Final Reviewer synthesizes the results, reviews QA/Security feedback, and delivers the outcome.

# Parallelization Strategy
- **Parallel:** Context reading, map building, analysis, and post-implementation validation.
- **Sequential:** Any writing, structural updates, or modifications to project files must be sequential and controlled via file locks.

# File Ownership Strategy
Agents must respect file ownership as defined in `.agent/rules/file-ownership.md`. Specialists only touch files within their domain. The Conflict Controller manages locks.

# Validation Steps
- QA and/or Security agents perform independent reviews based on the workflow's risk level.
- Ensure all outputs match the accepted criteria.
- Automated tests or manual checklists are executed and evidence is reported.

# Output Contract
- Concrete deliverables appropriate to the task (e.g., plan document, code changes, bug fix, test suite).
- A final summary report outlining what was changed, validation results, and next steps.

# Failure Handling
- If conflicts arise, the Conflict Controller suspends execution and escalates to the Orchestrator.
- If validation fails, the task is routed back to the responsible specialist for correction.
- Do not proceed with high-risk operations if critical context is missing.

# Example Run
*User Request:* "Please perform a deploy operation."
*Execution:* The Orchestrator routes the request to this workflow, loads the required agents and skills, executes the steps sequentially/in parallel as defined, validates the output, and hands the final summary back to the user.
