# Project Packs

> Presets and curated selections of agents, skills, and workflows for specific project types.

---

## What are Project Packs?

Project Packs are **advisory presets**. They are designed to help you (or the Universal Orchestrator) quickly 
select the right combination of agents, skills, and workflows for a given project domain. 

They **do not** duplicate agents or skills. They simply reference existing resources in `.agent/agents/` and `.agent/skills/`.

## How Orchestration Works with Packs

1. **Selection:** The Universal Orchestrator and Task Router read a pack to understand the optimal configuration for a domain.
2. **Execution:** The Task Router dispatches the recommended primary workflows.
3. **Validation:** Validation rules defined in the pack ensure domain-specific health.

## When to use a Pack?

You should use a pack when starting a new project or moving into a new domain within an existing project.
If your project spans multiple domains (e.g., a Web App with an API and an AI Agent feature), you can **safely combine packs**.

### Safely Combining Packs

When combining packs:
- Union the recommended agents.
- Union the recommended skills.
- The highest risk level dictates the validation requirements.

## Core Rule

> **Packs select the operating preset. They do not override global rules.**

Global rules, security rules, file ownership rules, and validation rules ALWAYS take precedence over any recommendation within a pack.

---

## Available Packs

| Pack | Purpose | Recommended for | Typical Workflows | Risk Level |
|------|---------|-----------------|-------------------|------------|
| `web-app-pack` | Full-stack web applications and SaaS interfaces. | React/Next apps, dashboards | plan, create-feature | High |
| `landing-page-pack` | Marketing, product, and lead capture pages. | Static sites, marketing | frontend-ui, enhance-feature | Medium |
| `api-pack` | Backend APIs, REST endpoints, and service layers. | Webhooks, auth flows | api-development | High |
| `data-bi-pack` | Data processing, CSV/Excel ingest, BI reporting. | KPI analysis, dashboards | automation, document | Medium |
| `automation-pack` | Python scripts, browser automation, scheduled jobs. | Scripts, scraping | automation, debug | High |
| `ai-agent-pack` | AI features, RAG pipelines, prompt systems. | Multi-agent workflows, LLMs | ai-feature, coordinate | High |
| `n8n-pack` | n8n automations, webhook flows, integrations. | Low-code, CRM syncing | automation, api-development | High |
| `ecommerce-pack` | Product catalogs, inventory, checkout flows. | Ecommerce systems | create-feature, security-review | High |
| `enterprise-pack` | Large, multi-domain, high-risk projects. | Internal business platforms | coordinate, release | Critical |
