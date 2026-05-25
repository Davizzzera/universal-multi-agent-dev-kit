---
name: database-change
type: workflow
description: Plan, implement and validate database schema, migration or data integrity changes safely.
trigger: ["database change", "migration", "schema update", "add table", "change table", "optimize query"]
primary_agent: universal-orchestrator
required_agents: ["database-specialist", "migration-specialist", "scope-guardian", "conflict-controller", "final-reviewer"]
optional_agents: ["sql-specialist", "data-quality-specialist", "backend-specialist", "security-reviewer", "devops-specialist", "qa-tester"]
required_skills: ["database-schema-design", "migration-create", "migration-review", "data-integrity-check", "backup-restore-plan", "query-optimization", "rollback-plan", "security-review"]
validation_required: manual-and-automated
risk_level: critical
related_rules: [global-rules.md, file-ownership.md, parallel-execution.md]
---

# Workflow Purpose
Plan, implement and validate database schema, migration or data integrity changes safely.

## Important Behavior
- Data-destructive operations require explicit approval.
- Rollback plan is mandatory.
- Backup/restore plan must be considered for risky changes.
- Backend/API dependencies must be coordinated.

# Trigger Conditions
This workflow is initiated when the Universal Orchestrator identifies any of the following triggers in the user request:
- database change
- migration
- schema update
- add table
- change table
- optimize query

# Required Inputs
- Clear user request or task description.
- Repository context and current state.
- (If applicable) Previous analysis or bug reports.

# Agents Involved
- **Primary Agent:** universal-orchestrator
- **Required Agents:** database-specialist, migration-specialist, scope-guardian, conflict-controller, final-reviewer
- **Optional Agents:** sql-specialist, data-quality-specialist, backend-specialist, security-reviewer, devops-specialist, qa-tester

# Skills Involved
- database-schema-design
- migration-create
- migration-review
- data-integrity-check
- backup-restore-plan
- query-optimization
- rollback-plan
- security-review

# Execution Steps
1. **Trigger Reception**: The Orchestrator identifies the user intent mapping to the `database-change` workflow.
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
*User Request:* "Please perform a database change operation."
*Execution:* The Orchestrator routes the request to this workflow, loads the required agents and skills, executes the steps sequentially/in parallel as defined, validates the output, and hands the final summary back to the user.
