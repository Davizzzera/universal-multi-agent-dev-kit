# Operational Workflows

> Workflows define the operational execution sequence of tasks.

---

## Overview

Workflows define **when** and **in which order** work happens. They are selected by the Universal Orchestrator and Task Router based on the user's request.

### "Agents define responsibility. Skills define execution. Workflows define operating sequence."

## Relationship with Agents and Skills

- **Workflow** orchestrates the sequence of steps.
- **Agents** are assigned to the steps based on their responsibilities.
- **Skills** are loaded and executed by the agents during their steps.

## Execution Rules

### Parallel / Sequential Execution Rule

- **Parallel Work:** Reading, research, mapping, and analysis MUST happen in parallel whenever possible.
- **Sequential Work:** Writing, editing, and file modifications MUST be controlled and sequential if there is conflict risk, managed by the Conflict Controller.
- **Parallel Validation:** After implementation, QA, security, and validation agents review the result independently and in parallel before the Final Reviewer steps in.

### Validation-First Delivery

Every workflow demands validation before declaring completion. Deliverables are only finalized once evidence of validation is provided.

## Available Workflows

| Workflow | Purpose | Primary Agent | Typical Risk Level | Validation Type |
|----------|---------|---------------|--------------------|-----------------|
| [`plan`](plan.workflow.md) | Analyze a request and create a safe implementation plan without modifying project files. | universal-orchestrator | low | manual |
| [`coordinate`](coordinate.workflow.md) | Coordinate multiple agents for complex tasks that require multi-agent analysis, execution and validation. | universal-orchestrator | high | manual-and-automated |
| [`create-feature`](create-feature.workflow.md) | Create a new feature safely using the appropriate specialist agents and validation path. | universal-orchestrator | high | manual-and-automated |
| [`enhance-feature`](enhance-feature.workflow.md) | Improve an existing feature without changing its intended behavior or breaking existing functionality. | universal-orchestrator | medium | manual-and-automated |
| [`debug`](debug.workflow.md) | Investigate, reproduce and resolve bugs with minimal, evidence-based changes. | universal-orchestrator | medium | manual-and-automated |
| [`refactor`](refactor.workflow.md) | Improve code structure, readability and maintainability without changing behavior. | universal-orchestrator | medium | manual-and-automated |
| [`test`](test.workflow.md) | Create, improve or run tests for existing behavior, new features or critical flows. | universal-orchestrator | medium | manual-and-automated |
| [`verify`](verify.workflow.md) | Verify that the repository, feature or implementation actually works before claiming completion. | final-reviewer | medium | manual-and-automated |
| [`security-review`](security-review.workflow.md) | Perform a defensive security review of code, configuration, dependencies, data handling and release readiness. | security-reviewer | high | manual-and-automated |
| [`database-change`](database-change.workflow.md) | Plan, implement and validate database schema, migration or data integrity changes safely. | universal-orchestrator | critical | manual-and-automated |
| [`api-development`](api-development.workflow.md) | Design, implement and validate API endpoints, contracts and integration behavior. | universal-orchestrator | high | manual-and-automated |
| [`frontend-ui`](frontend-ui.workflow.md) | Create, improve or validate frontend UI safely with design, responsiveness and accessibility considerations. | universal-orchestrator | medium | manual-and-automated |
| [`automation`](automation.workflow.md) | Design, implement and validate automation scripts, file processors, n8n flows or browser automations. | universal-orchestrator | high | manual-and-automated |
| [`ai-feature`](ai-feature.workflow.md) | Design, implement and validate AI-powered features, prompts, agents, RAG systems or LLM workflows. | universal-orchestrator | high | manual-and-automated |
| [`document`](document.workflow.md) | Create, update or validate documentation so it matches actual repository behavior. | documentation-writer | low | manual |
| [`deploy`](deploy.workflow.md) | Prepare deployment configuration, environment handling, CI/CD and production readiness. | universal-orchestrator | critical | manual-and-automated |
| [`release`](release.workflow.md) | Prepare versioning, changelog, release notes and final readiness for a repository release. | release-manager | high | manual-and-automated |
| [`emergency-fix`](emergency-fix.workflow.md) | Handle urgent fixes safely while preserving scope, validation and rollback discipline. | universal-orchestrator | critical | manual-and-automated |
