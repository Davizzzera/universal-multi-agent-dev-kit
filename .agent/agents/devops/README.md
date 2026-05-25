# Devops Agents

> Deployment, Docker, CI/CD pipelines, cloud infrastructure and release management.

---

## Purpose
This category contains specialist agents focused on deployment, docker, ci/cd pipelines, cloud infrastructure and release management.

## When Used
These agents are invoked by the Task Router when a request involves devops domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router, Scope Guardian.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Devops Specialist](devops-specialist.agent.md) | Prepare deployment, infrastructure, environments and operational readiness. | devops specialist tasks. | AgentOutputContract |
| [Docker Specialist](docker-specialist.agent.md) | Create and review Dockerfiles, docker-compose files and container workflows. | docker specialist tasks. | AgentOutputContract |
| [Ci Cd Specialist](ci-cd-specialist.agent.md) | Create and review CI/CD pipelines, GitHub Actions and validation automation. | ci cd specialist tasks. | AgentOutputContract |
| [Cloud Specialist](cloud-specialist.agent.md) | Plan cloud deployment and infrastructure usage across common platforms. | cloud specialist tasks. | AgentOutputContract |
| [Release Manager](release-manager.agent.md) | Prepare releases, versioning, changelogs and release readiness checks. | release manager tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
