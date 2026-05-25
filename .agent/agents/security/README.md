# Security Agents

> Defensive security review, secrets scanning, dependency auditing, auth security and privacy compliance.

---

## Purpose
This category contains specialist agents focused on defensive security review, secrets scanning, dependency auditing, auth security and privacy compliance.

## When Used
These agents are invoked by the Task Router when a request involves security domain work.

## Orchestration
Coordinated by: Universal Orchestrator, Final Reviewer.

## Agents

| Agent | Primary Responsibility | When Used | Main Output |
|-------|------------------------|-----------|-------------|
| [Security Reviewer](security-reviewer.agent.md) | Perform defensive security review across code, configuration, dependencies and data handling. | security reviewer tasks. | AgentOutputContract |
| [Secrets Scanner](secrets-scanner.agent.md) | Detect accidental secrets, tokens, credentials and private keys in repository content. | secrets scanner tasks. | AgentOutputContract |
| [Dependency Security Auditor](dependency-security-auditor.agent.md) | Review dependencies for known vulnerability risk and unsafe usage patterns. | dependency security auditor tasks. | AgentOutputContract |
| [Auth Security Reviewer](auth-security-reviewer.agent.md) | Review authentication and authorization flows for defensive security. | auth security reviewer tasks. | AgentOutputContract |
| [Privacy Compliance Reviewer](privacy-compliance-reviewer.agent.md) | Review personal data exposure, privacy risks and safe data handling practices. | privacy compliance reviewer tasks. | AgentOutputContract |

---

## Rules
All agents in this category must follow:
- `.agent/rules/global-rules.md`
- `.agent/rules/agent-boundaries.md`
- `.agent/rules/file-ownership.md`
- `.agent/rules/output-contract-rules.md`
- `.agent/rules/validation-rules.md`
