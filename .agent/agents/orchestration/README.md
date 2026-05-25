# Orchestration Agents

> The core management layer of the Universal Multi-Agent Development Kit.

---

## What are Orchestration Agents?

Orchestration agents are the managers and coordinators of the multi-agent system. Unlike Specialist Agents (which write code or design databases), Orchestration Agents are responsible for the meta-work: understanding requests, defining scope, planning execution, preventing conflicts, and ensuring quality.

---

## Why are they required before Specialist Agents?

Specialist Agents are powerful but narrowly focused. If a Code Writer is unleashed without orchestration, it might overwrite files, ignore project architecture, or skip validation. Orchestration agents establish the strict control framework required to make Specialist Agents safe, predictable, and effective.

---

## How Orchestration Agents Cooperate

Orchestration agents work in a highly structured, sequential chain of command at the start and end of every workflow. They pass structured data to one another using explicit Output Contracts and Handoff Protocols.

---

## The Core Orchestration Lifecycle

1. **Understand request:** Universal Orchestrator receives user intent.
2. **Read context:** Project Context Reader analyzes the repository state.
3. **Classify work:** Task Router determines what needs to be done.
4. **Define scope:** Scope Guardian sets strict boundaries.
5. **Plan execution:** Conflict Controller determines file locks and parallel/sequential steps.
6. **Control conflicts:** File ownership is enforced before execution begins.
7. **Dispatch specialists:** (Hand off to Specialist Agents).
8. **Validate:** (Hand off to Validation Agents).
9. **Synthesize final result:** Final Reviewer consolidates all outputs into a single delivery.

---

## The Orchestration Agents

| Agent | Primary responsibility | When used | Main output |
|-------|------------------------|-----------|-------------|
| **Universal Orchestrator** | High-level system coordination. | Start of every interaction. | Dispatch plan & final handoffs. |
| **Project Context Reader** | Repository analysis. | Before any task classification. | Context summary & constraints. |
| **Task Router** | Request classification. | After context is gathered. | Required agents & skills list. |
| **Scope Guardian** | Scope definition and protection. | Before execution planning. | In-scope and Out-of-scope lists. |
| **Conflict Controller** | Execution order & file locking. | Before specialist dispatch. | File ownership mapping & step sequence. |
| **Final Reviewer** | Output validation & synthesis. | End of every workflow. | Validated final delivery report. |
