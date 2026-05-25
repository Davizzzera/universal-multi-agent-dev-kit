---
name: create-feature
type: workflow
description: Create a new feature safely using the appropriate specialist agents and validation path.
trigger: ["create feature", "add feature", "implement feature", "build feature", "new functionality"]
primary_agent: universal-orchestrator
required_agents: ["project-context-reader", "task-router", "scope-guardian", "conflict-controller", "final-reviewer", "qa-tester"]
optional_agents: ["product-manager", "requirements-engineer", "frontend-specialist", "backend-specialist", "database-specialist", "api-designer", "security-reviewer", "documentation-writer", "devops-specialist"]
required_skills: ["project-intake", "task-breakdown", "implementation-plan", "acceptance-criteria-writing", "definition-of-done", "file-ownership-locking", "build-validation", "regression-test-checklist", "change-impact-summary"]
validation_required: manual-and-automated
risk_level: high
related_rules: [global-rules.md, file-ownership.md, parallel-execution.md]
---

# Workflow Purpose
Create a new feature safely using the appropriate specialist agents and validation path.

## Important Behavior
- Must define acceptance criteria before implementation.
- Must select specialist agents based on feature type.
- Must require QA validation for code changes.
- Must require security review when auth, data, API, dependencies or permissions are involved.

# Trigger Conditions
This workflow is initiated when the Universal Orchestrator identifies any of the following triggers in the user request:
- create feature
- add feature
- implement feature
- build feature
- new functionality

# Required Inputs
- Clear user request or task description.
- Repository context and current state.
- (If applicable) Previous analysis or bug reports.

# Agents Involved
- **Primary Agent:** universal-orchestrator
- **Required Agents:** project-context-reader, task-router, scope-guardian, conflict-controller, final-reviewer, qa-tester
- **Optional Agents:** product-manager, requirements-engineer, frontend-specialist, backend-specialist, database-specialist, api-designer, security-reviewer, documentation-writer, devops-specialist

# Skills Involved
- project-intake
- task-breakdown
- implementation-plan
- acceptance-criteria-writing
- definition-of-done
- file-ownership-locking
- build-validation
- regression-test-checklist
- change-impact-summary

# Execution Steps
1. **Trigger Reception**: The Orchestrator identifies the user intent mapping to the `create-feature` workflow.
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
*User Request:* "Please perform a create feature operation."
*Execution:* The Orchestrator routes the request to this workflow, loads the required agents and skills, executes the steps sequentially/in parallel as defined, validates the output, and hands the final summary back to the user.
