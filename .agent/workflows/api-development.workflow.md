---
name: api-development
type: workflow
description: Design, implement and validate API endpoints, contracts and integration behavior.
trigger: ["create API", "API endpoint", "backend route", "REST API", "API integration"]
primary_agent: universal-orchestrator
required_agents: ["backend-specialist", "api-designer", "qa-tester", "final-reviewer", "security-reviewer"]
optional_agents: ["database-specialist", "auth-specialist", "integration-specialist", "webhook-specialist", "documentation-writer"]
required_skills: ["api-contract-design", "rest-api-implementation", "request-validation", "error-handling-standard", "pagination-filtering-sorting", "input-sanitization", "authz-review", "openapi-style documentation if applicable"]
validation_required: manual-and-automated
risk_level: high
related_rules: [global-rules.md, file-ownership.md, parallel-execution.md]
---

# Workflow Purpose
Design, implement and validate API endpoints, contracts and integration behavior.

## Important Behavior
- API contract must be defined before implementation.
- Request validation and safe error handling are required.
- Security review is mandatory when auth, data or permissions are involved.

# Trigger Conditions
This workflow is initiated when the Universal Orchestrator identifies any of the following triggers in the user request:
- create API
- API endpoint
- backend route
- REST API
- API integration

# Required Inputs
- Clear user request or task description.
- Repository context and current state.
- (If applicable) Previous analysis or bug reports.

# Agents Involved
- **Primary Agent:** universal-orchestrator
- **Required Agents:** backend-specialist, api-designer, qa-tester, final-reviewer, security-reviewer
- **Optional Agents:** database-specialist, auth-specialist, integration-specialist, webhook-specialist, documentation-writer

# Skills Involved
- api-contract-design
- rest-api-implementation
- request-validation
- error-handling-standard
- pagination-filtering-sorting
- input-sanitization
- authz-review
- openapi-style documentation if applicable

# Execution Steps
1. **Trigger Reception**: The Orchestrator identifies the user intent mapping to the `api-development` workflow.
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
*User Request:* "Please perform a api development operation."
*Execution:* The Orchestrator routes the request to this workflow, loads the required agents and skills, executes the steps sequentially/in parallel as defined, validates the output, and hands the final summary back to the user.
