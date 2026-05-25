# Core Skills Library

> The execution layer defining exactly *how* agents perform tasks.

---

## Overview

Skills define **how** work is done. While Agents define who does the work (roles, boundaries, contracts), Skills provide the step-by-step procedures, checklists, and decision frameworks to execute a specific task.

### "Agents define responsibility. Skills define execution."

## Progressive Loading Concept

Instead of passing a massive prompt with everything an agent knows how to do, the Universal Orchestrator dynamically loads the exact skills required for the immediate task. This keeps agent context windows clean, reduces hallucination, and ensures tight adherence to specific procedures.

## Relationship with Agents

- The Universal Orchestrator receives a task and identifies required skills.
- The Task Router assigns a Specialist Agent to execute the task.
- The Specialist Agent follows the loaded skill's procedure step-by-step.
- Each skill adheres to the structure in `.agent/templates/skill-template.md`.

## Skill Categories

| Category | Purpose |
|----------|---------|
| [Orchestration](orchestration/README.md) | Skills related to orchestration. |
| [Context](context/README.md) | Skills related to context. |
| [Planning](planning/README.md) | Skills related to planning. |
| [Frontend](frontend/README.md) | Skills related to frontend. |
| [Ui Ux](ui-ux/README.md) | Skills related to ui ux. |
| [Backend](backend/README.md) | Skills related to backend. |
| [Auth](auth/README.md) | Skills related to auth. |
| [Database](database/README.md) | Skills related to database. |
| [Data Bi](data-bi/README.md) | Skills related to data bi. |
| [Ai Agents](ai-agents/README.md) | Skills related to ai agents. |
| [Automation](automation/README.md) | Skills related to automation. |
| [Qa](qa/README.md) | Skills related to qa. |
| [Security](security/README.md) | Skills related to security. |
| [Devops](devops/README.md) | Skills related to devops. |
| [Github](github/README.md) | Skills related to github. |
| [Documentation](documentation/README.md) | Skills related to documentation. |
| [Marketing](marketing/README.md) | Skills related to marketing. |
| [Maintenance](maintenance/README.md) | Skills related to maintenance. |
