# Documentation Agents

> Technical writing, documentation, GitHub management, pull requests and changelog maintenance.

---

## Purpose
This category contains specialist agents focused on technical writing, documentation, github management, pull requests and changelog maintenance.

## When Used
These agents are invoked by the Task Router when a request involves documentation domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Task Router.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Documentation Writer](documentation-writer.agent.md) | Create and maintain user-facing and developer-facing documentation. | documentation writer tasks. | AgentOutputContract |
| [Technical Writer](technical-writer.agent.md) | Write deeper technical documentation, architecture explanations and implementation guides. | technical writer tasks. | AgentOutputContract |
| [Github Repository Manager](github-repository-manager.agent.md) | Manage repository structure, GitHub conventions, issues, pull requests and contribution standards. | github repository manager tasks. | AgentOutputContract |
| [Pull Request Writer](pull-request-writer.agent.md) | Create clear pull request summaries, checklists and reviewer notes. | pull request writer tasks. | AgentOutputContract |
| [Changelog Maintainer](changelog-maintainer.agent.md) | Maintain changelog entries and release history. | changelog maintainer tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
