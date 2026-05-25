# Orchestration Skills

> Procedures for orchestration tasks.

---

## Purpose
This category contains execution procedures for tasks in the orchestration domain.

## When Used
Loaded when a task specifically targets orchestration requirements.

## Typical Owner Agents
These skills are typically assigned to agents in the orchestration category, or orchestration agents.

## Skills

| Skill | Primary Purpose | Typical Owner Agents | Validation Level |
|-------|-----------------|----------------------|------------------|
| [coordinator-mode](coordinator-mode/SKILL.md) | Coordinate multi-agent execution from request interpretation to final synthesis. | universal-orchestrator, task-router, conflict-controller | manual-and-automated |
| [agent-routing](agent-routing/SKILL.md) | Decide which agents should be selected for a task. | task-router, universal-orchestrator | manual-and-automated |
| [handoff-protocol](handoff-protocol/SKILL.md) | Transfer work safely between agents with complete context. | universal-orchestrator, final-reviewer, all specialist agents | manual-and-automated |
| [parallel-work-planning](parallel-work-planning/SKILL.md) | Separate tasks that can run in parallel from tasks that must run sequentially. | conflict-controller, universal-orchestrator, technical-lead | manual-and-automated |
| [file-ownership-locking](file-ownership-locking/SKILL.md) | Assign file ownership and prevent simultaneous conflicting edits. | conflict-controller, scope-guardian, technical-lead | manual-and-automated |
| [change-impact-summary](change-impact-summary/SKILL.md) | Summarize the impact of proposed or completed changes. | final-reviewer, technical-lead, documentation-writer | manual-and-automated |
