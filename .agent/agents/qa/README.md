# Qa Agents

> Quality assurance testing, unit tests, end-to-end tests, visual regression and bug investigation.

---

## Purpose
This category contains specialist agents focused on quality assurance testing, unit tests, end-to-end tests, visual regression and bug investigation.

## When Used
These agents are invoked by the Task Router when a request involves qa domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Final Reviewer.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Qa Tester](qa-tester.agent.md) | Validate that implemented work satisfies requirements and does not break existing behavior. | qa tester tasks. | AgentOutputContract |
| [Unit Test Specialist](unit-test-specialist.agent.md) | Create and review unit tests for isolated logic. | unit test specialist tasks. | AgentOutputContract |
| [E2e Test Specialist](e2e-test-specialist.agent.md) | Create and review end-to-end tests for critical user flows. | e2e test specialist tasks. | AgentOutputContract |
| [Visual Regression Specialist](visual-regression-specialist.agent.md) | Validate visual consistency, layout changes and UI regressions. | visual regression specialist tasks. | AgentOutputContract |
| [Bug Hunter](bug-hunter.agent.md) | Investigate difficult bugs, reproduce failures and isolate root causes. | bug hunter tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
