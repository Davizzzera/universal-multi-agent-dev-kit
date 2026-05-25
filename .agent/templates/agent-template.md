---
name: agent-name-kebab-case
type: agent
category: specialist # orchestrator | specialist | validation
description: A short one-sentence description of the agent.
when_to_use: When this agent should be invoked.
do_not_use_when: When this agent should NOT be invoked.
risk_level: low # low | medium | high
allowed_operations: [read, write, execute]
disallowed_operations: [delete, format]
required_skills: [skill-1, skill-2]
optional_skills: [skill-3]
input_contract: TaskBrief
output_contract: AgentOutputContract
owner: universal-orchestrator
reviewers: [qa-tester, security-reviewer]
---

# Agent: Name in Title Case

## Role
A concise description of the agent's persona and primary function.

## Mission
The ultimate goal this agent strives to achieve.

## Responsibilities
- Responsibility 1
- Responsibility 2
- Responsibility 3

## Boundaries
- What the agent is explicitly prohibited from doing.
- What systems or files the agent must not touch.

## Required Context
- What information this agent needs to start working (e.g., specific files, workflow state).

## Operating Procedure
1. Step-by-step description of how the agent thinks and acts.
2. ...

## Tool Usage Guidelines
- Specific instructions on how the agent should use its assigned skills.

## Validation Requirements
- What the agent must validate before declaring a task complete.

## Handoff Rules
- Who this agent typically hands off to, and under what conditions.

## Output Contract
- Specific requirements for this agent's final response (references `output-contract-rules.md`).

## Failure Handling
- What the agent should do if it encounters an error it cannot resolve.

## Examples
- Example scenario and expected behavior.
