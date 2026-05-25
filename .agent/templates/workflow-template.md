---
name: workflow-name-kebab-case
type: workflow
description: A short description of the workflow.
trigger: Event or condition that starts the workflow.
primary_agent: universal-orchestrator
required_agents: [agent-1, agent-2]
optional_agents: [agent-3]
required_skills: [skill-1, skill-2]
validation_required: true
risk_level: medium
---

# Workflow: Name in Title Case

## Workflow Purpose
Detailed explanation of what the workflow achieves.

## Trigger Conditions
- Exact events, user requests, or system states that initiate this workflow.

## Inputs
- Expected data or context required to start.

## Agents Involved
- `primary_agent`: Role in this workflow.
- `required_agents`: Roles in this workflow.

## Skills Involved
- Skills that will be utilized during execution.

## Execution Steps

### Phase 1: Preparation (Parallel)
1. **Agent:** name
   **Action:** description
2. ...

### Phase 2: Implementation (Sequential)
1. **Agent:** name
   **Action:** description
   **Validation Gate:** Must pass X before proceeding.
2. ...

### Phase 3: Review (Parallel)
1. **Agent:** name
   **Action:** description

## Parallelization Strategy
- Which parts of the workflow run concurrently and why it is safe.

## File Ownership Strategy
- How file modifications are coordinated to prevent conflicts.

## Validation Steps
- The specific checkpoints where validation occurs.

## Output Contract
- What the workflow produces upon completion.

## Failure Handling
- Rollback procedures or escalation paths if a step fails.

## Example Run
- A brief narrative of a successful execution.
