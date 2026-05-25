# Security Skills

> Procedures for security tasks.

---

## Purpose
This category contains execution procedures for tasks in the security domain.

## When Used
Loaded when a task specifically targets security requirements.

## Typical Owner Agents
These skills are typically assigned to agents in the security category, or orchestration agents.

## Skills

| Skill | Primary Purpose | Typical Owner Agents | Validation Level |
|-------|-----------------|----------------------|------------------|
| [secrets-detection](secrets-detection/SKILL.md) | Detect accidental secrets, tokens, credentials or private keys. | secrets-scanner, security-reviewer | manual-and-automated |
| [dependency-vulnerability-check](dependency-vulnerability-check/SKILL.md) | Review dependencies for known risks and unsafe usage patterns. | dependency-security-auditor | manual-and-automated |
| [input-sanitization](input-sanitization/SKILL.md) | Review and improve input validation and sanitization. | security-reviewer, backend-specialist | manual-and-automated |
| [authz-review](authz-review/SKILL.md) | Review authorization boundaries and permission checks. | auth-security-reviewer, security-reviewer | manual-and-automated |
| [secure-logging-review](secure-logging-review/SKILL.md) | Ensure logs do not expose sensitive data and remain useful. | security-reviewer, observability style agents | manual-and-automated |
| [security-release-checklist](security-release-checklist/SKILL.md) | Review security readiness before release or deployment. | security-reviewer, release-manager | manual-and-automated |
