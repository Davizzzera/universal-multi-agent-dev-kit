# Backend Agents

> Server-side development, API design, authentication, external integrations and webhook management.

---

## Purpose
This category contains specialist agents focused on server-side development, api design, authentication, external integrations and webhook management.

## When Used
These agents are invoked by the Task Router when a request involves backend domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router, Conflict Controller.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Backend Specialist](backend-specialist.agent.md) | Implement server-side logic, services, APIs and backend behavior. | backend specialist tasks. | AgentOutputContract |
| [Api Designer](api-designer.agent.md) | Design clear, consistent and maintainable API contracts. | api designer tasks. | AgentOutputContract |
| [Auth Specialist](auth-specialist.agent.md) | Design and review authentication, authorization, sessions, tokens and permissions. | auth specialist tasks. | AgentOutputContract |
| [Integration Specialist](integration-specialist.agent.md) | Integrate external APIs, services, CRMs, ERPs, webhooks and third-party tools. | integration specialist tasks. | AgentOutputContract |
| [Webhook Specialist](webhook-specialist.agent.md) | Design, implement and validate webhook receivers and senders. | webhook specialist tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
