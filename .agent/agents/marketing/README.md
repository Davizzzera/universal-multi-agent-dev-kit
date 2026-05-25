# Marketing Agents

> Copywriting, SEO optimization, landing page strategy and growth analysis.

---

## Purpose
This category contains specialist agents focused on copywriting, seo optimization, landing page strategy and growth analysis.

## When Used
These agents are invoked by the Task Router when a request involves marketing domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Copywriter](copywriter.agent.md) | Create clear, persuasive and conversion-oriented copy for product pages, campaigns and interfaces. | copywriter tasks. | AgentOutputContract |
| [Seo Specialist](seo-specialist.agent.md) | Improve SEO structure, metadata, semantic content and discoverability. | seo specialist tasks. | AgentOutputContract |
| [Landing Page Strategist](landing-page-strategist.agent.md) | Plan landing pages focused on clarity, conversion and user journey. | landing page strategist tasks. | AgentOutputContract |
| [Growth Specialist](growth-specialist.agent.md) | Analyze acquisition, activation, conversion and retention opportunities. | growth specialist tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
