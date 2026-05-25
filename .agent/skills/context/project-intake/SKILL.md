---
name: project-intake
type: skill
category: context
description: Understand project goals, stack, current state, constraints and expected outcome.
when_to_use: When performing tasks related to project intake.
do_not_use_when: When the task falls outside this domain or requires a different skill entirely.
risk_level: medium
owner_agents: [project-context-reader, universal-orchestrator, product-manager]
required_inputs: [Task brief, relevant context]
expected_outputs: [Executed action, validated output, summary report]
validation_level: manual-and-automated
related_rules: [global-rules.md, agent-boundaries.md]
---

# Project Intake

## Purpose
Understand project goals, stack, current state, constraints and expected outcome.

## When to Use
Use this skill when tasked with executing a project intake operation to ensure consistency and correctness.

## When Not to Use
Do not use this skill if the task does not involve project intake, or if a more specific alternative skill exists.

## Required Inputs
- Clear definition of the task scope.
- Access to relevant files or project context.

## Procedure
1. Analyze the request and identify the specific requirements for project intake.
2. Review existing patterns or codebase constraints before taking action.
3. Formulate a plan to execute the project intake operation safely.
4. Execute the operation, ensuring adherence to global rules and specific decision logic.
5. Validate the changes or output using the defined validation requirements.
6. Document the outcome and prepare the handoff artifact.

## Decision Rules
- IF the task is ambiguous, THEN ask for clarification before proceeding.
- IF an error or conflict occurs, THEN document it and escalate to the Orchestrator.
- ALWAYS prefer safe, non-destructive defaults.

## Checklist
- [ ] Understand the exact goal of the project intake request.
- [ ] Verify required inputs are present.
- [ ] Ensure no boundaries or global rules will be violated.
- [ ] Complete all steps in the execution procedure.
- [ ] Validate output against expected results.
- [ ] Finalize artifact or code modifications.

## Validation
Output must be checked to ensure it meets the expected criteria. Validation may involve reviewing diffs, running tests, or manual inspection.

## Expected Output
- A completed operation aligned with the purpose.
- Documentation or a report summarizing the changes.

## Common Mistakes
- Skipping the initial context analysis phase.
- Violating boundaries or attempting destructive operations.
- Failing to validate the final output against acceptance criteria.
- Not providing a clear summary in the handoff.

## Example Usage
*Scenario:* An agent is tasked with project intake.
*Action:* The agent loads this skill, follows the 6-step procedure, completes the checklist, and produces the validated output.
