---
name: duplicate-code-detection
type: skill
category: maintenance
description: Detect duplicated logic and recommend safe consolidation.
when_to_use: When performing tasks related to duplicate code detection.
do_not_use_when: When the task falls outside this domain or requires a different skill entirely.
risk_level: medium
owner_agents: [refactor-specialist, codebase-analyst]
required_inputs: [Task brief, relevant context]
expected_outputs: [Executed action, validated output, summary report]
validation_level: manual-and-automated
related_rules: [global-rules.md, agent-boundaries.md]
---

# Duplicate Code Detection

## Purpose
Detect duplicated logic and recommend safe consolidation.

## When to Use
Use this skill when tasked with executing a duplicate code detection operation to ensure consistency and correctness.

## When Not to Use
Do not use this skill if the task does not involve duplicate code detection, or if a more specific alternative skill exists.

## Required Inputs
- Clear definition of the task scope.
- Access to relevant files or project context.

## Procedure
1. Analyze the request and identify the specific requirements for duplicate code detection.
2. Review existing patterns or codebase constraints before taking action.
3. Formulate a plan to execute the duplicate code detection operation safely.
4. Execute the operation, ensuring adherence to global rules and specific decision logic.
5. Validate the changes or output using the defined validation requirements.
6. Document the outcome and prepare the handoff artifact.

## Decision Rules
- IF the task is ambiguous, THEN ask for clarification before proceeding.
- IF an error or conflict occurs, THEN document it and escalate to the Orchestrator.
- ALWAYS prefer safe, non-destructive defaults.

## Checklist
- [ ] Understand the exact goal of the duplicate code detection request.
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
*Scenario:* An agent is tasked with duplicate code detection.
*Action:* The agent loads this skill, follows the 6-step procedure, completes the checklist, and produces the validated output.
