# Ai Automation Agents

> AI engineering, prompt design, agent architecture, RAG systems, n8n automation and Python scripting.

---

## Purpose
This category contains specialist agents focused on ai engineering, prompt design, agent architecture, rag systems, n8n automation and python scripting.

## When Used
These agents are invoked by the Task Router when a request involves ai-automation domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Ai Engineer](ai-engineer.agent.md) | Design and implement AI-powered features safely and reliably. | ai engineer tasks. | AgentOutputContract |
| [Prompt Engineer](prompt-engineer.agent.md) | Design robust prompts, system instructions, evaluation prompts and reusable prompt patterns. | prompt engineer tasks. | AgentOutputContract |
| [Agent Engineer](agent-engineer.agent.md) | Design agents, subagents, skills, routing logic and multi-agent coordination patterns. | agent engineer tasks. | AgentOutputContract |
| [Rag Specialist](rag-specialist.agent.md) | Design retrieval-augmented generation systems, knowledge bases, embeddings and document ingestion. | rag specialist tasks. | AgentOutputContract |
| [N8n Automation Specialist](n8n-automation-specialist.agent.md) | Design and document n8n workflows, triggers, webhooks and integrations. | n8n automation specialist tasks. | AgentOutputContract |
| [Python Automation Specialist](python-automation-specialist.agent.md) | Create Python automations, scripts, file processors, API integrations and ETL utilities. | python automation specialist tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
