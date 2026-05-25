# Context Skills

> Procedures for context tasks.

---

## Purpose
This category contains execution procedures for tasks in the context domain.

## When Used
Loaded when a task specifically targets context requirements.

## Typical Owner Agents
These skills are typically assigned to agents in the context category, or orchestration agents.

## Skills

| Skill | Primary Purpose | Typical Owner Agents | Validation Level |
|-------|-----------------|----------------------|------------------|
| [project-intake](project-intake/SKILL.md) | Understand project goals, stack, current state, constraints and expected outcome. | project-context-reader, universal-orchestrator, product-manager | manual-and-automated |
| [codebase-map](codebase-map/SKILL.md) | Map folder structure, key files, modules and ownership areas. | project-context-reader, codebase-analyst, technical-lead | manual-and-automated |
| [dependency-scan](dependency-scan/SKILL.md) | Identify package managers, dependencies, frameworks and runtime constraints. | project-context-reader, dependency-security-auditor, devops-specialist | manual-and-automated |
| [existing-patterns-detection](existing-patterns-detection/SKILL.md) | Detect existing coding, architecture, naming and documentation patterns. | codebase-analyst, frontend-specialist, backend-specialist | manual-and-automated |
| [business-context-extraction](business-context-extraction/SKILL.md) | Extract business rules, product behavior and operational logic from docs or code. | business-analyst, requirements-engineer, product-manager | manual-and-automated |
