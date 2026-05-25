# Antigravity Adapter Usage

This guide explains how to effectively control Antigravity AI using the components of the Universal Multi-Agent Development Kit.

## Core Concepts in Action

When speaking to Antigravity, you are speaking to the **Universal Orchestrator**. 
You must provide prompts that trigger the correct workflows, which will in turn select the appropriate agents and skills.

### How to ask for a Workflow
Explicitly state the workflow name in your prompt. 
*Example:* "I want you to use the `create-feature` workflow to build a new login page."

### How to ask for Agents
The Task Router normally handles this, but you can override or hint at required agents.
*Example:* "Make sure the `security-reviewer` agent checks the authentication flow."

### How to ask for Skills
You can direct agents to use specific skills if you know exactly what procedure they should follow.
*Example:* "Follow the `react-component-create` skill exactly."

## Recommended Prompt Pattern

To get the most reliable results, structure your Antigravity prompts using this pattern:

1. **Context:** What is the current state?
2. **Goal:** What are we trying to achieve?
3. **Workflow:** Which workflow from `.agent/workflows/` should govern this task?
4. **Scope:** What files are allowed to be touched? What is off-limits?
5. **Constraints:** Are there specific rules, templates, or skills to enforce?
6. **Validation:** How do we prove it works?
7. **Output Expected:** What should the final summary look like?

## Execution Strategies

### End-to-End Execution
You can pass one complete prompt requesting Antigravity to execute from planning to validation. 
This is best for low-to-medium risk tasks (e.g., UI tweaks, new test cases).

### Incremental Execution (Recommended)
For complex tasks, keep Antigravity incremental:
1. **Phase 1 (Plan):** "Use the `plan` workflow. Do not modify files. Give me an implementation plan."
2. **Phase 2 (Execute):** "I approve the plan. Use the `create-feature` workflow to implement it."
3. **Phase 3 (Verify):** "Use the `verify` workflow to run tests and validate."

### Commit and Push Control
Always include explicit instructions on whether Antigravity is allowed to commit and push.
*Example:* "After validation passes, commit with the message 'feat: add login' and push to main."

## Example Triggers

- **Planning only:** "Use the `plan` workflow to assess..."
- **Create feature:** "Use the `create-feature` workflow to build..."
- **Debug:** "Use the `debug` workflow to investigate the issue with..."
- **Verify:** "Use the `verify` workflow to run the test suite and confirm..."
- **Security review:** "Use the `security-review` workflow to audit..."
- **Documentation update:** "Use the `document` workflow to update the README."
