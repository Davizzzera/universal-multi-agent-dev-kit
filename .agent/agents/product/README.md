# Product Agents

> Product strategy, business analysis, requirements engineering and risk assessment.

---

## Purpose
This category contains specialist agents focused on product strategy, business analysis, requirements engineering and risk assessment.

## When Used
These agents are invoked by the Task Router when a request involves product domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Product Manager](product-manager.agent.md) | Translate ideas, goals and user needs into product direction, feature scope and delivery priorities. | product manager tasks. | AgentOutputContract |
| [Business Analyst](business-analyst.agent.md) | Understand business processes, operational rules, data flows and stakeholder requirements. | business analyst tasks. | AgentOutputContract |
| [Requirements Engineer](requirements-engineer.agent.md) | Transform requests into structured requirements, acceptance criteria and delivery-ready specifications. | requirements engineer tasks. | AgentOutputContract |
| [Risk Analyst](risk-analyst.agent.md) | Identify technical, operational, security, delivery and maintenance risks before execution. | risk analyst tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
