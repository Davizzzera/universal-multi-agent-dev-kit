# Orchestration Model

> How the multi-agent orchestration system works in the Universal Multi-Agent Development Kit.

---

## Overview

The orchestration model defines how multiple agents work together to fulfill a user request. It is the central coordination mechanism that ensures tasks are completed efficiently, safely, and with proper validation.

---

## The Universal Orchestrator

The Universal Orchestrator is the entry point for all agent activity. It does not perform tasks itself — instead, it coordinates specialist agents by:

1. **Parsing** the user request to understand intent, scope, and constraints.
2. **Delegating** context analysis to the Context Reader.
3. **Routing** the task to the Task Router for classification.
4. **Selecting** the appropriate specialist agents.
5. **Loading** the required skills for each agent.
6. **Managing** the execution flow (parallel/sequential).
7. **Enforcing** validation gates between phases.
8. **Consolidating** the final delivery through the Final Reviewer.

---

## Execution Lifecycle

```
┌─────────────────────────────────────────────────────┐
│                   USER REQUEST                       │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              UNIVERSAL ORCHESTRATOR                  │
│  Parse intent → Identify scope → Set constraints    │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
┌──────────────────┐  ┌──────────────────┐
│  CONTEXT READER  │  │   TASK ROUTER    │
│  (Parallel)      │  │   (Parallel)     │
└────────┬─────────┘  └────────┬─────────┘
         │                     │
         └──────────┬──────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│           SPECIALIST AGENT SELECTION                 │
│  Select agents → Load skills → Assign tasks         │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
┌──────────────────┐  ┌──────────────────┐
│  PARALLEL PHASE  │  │                  │
│  • Research      │  │                  │
│  • Analysis      │  │                  │
│  • Mapping       │  │                  │
└────────┬─────────┘  │                  │
         │            │                  │
         ▼            │                  │
┌──────────────────┐  │  VALIDATION      │
│ SEQUENTIAL PHASE │  │  GATE            │
│  • Writing       │──│                  │
│  • Editing       │  │                  │
│  • Creating      │  │                  │
└────────┬─────────┘  └──────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────┐
│            PARALLEL VALIDATION PHASE                 │
│  QA Agent │ Security Agent │ Style Agent │ Tests    │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│               FINAL REVIEWER                         │
│  Consolidate → Verify → Deliver                     │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│                   DELIVERY                           │
└─────────────────────────────────────────────────────┘
```

---

## Phase Details

### Phase 1: Request Intake

The orchestrator receives the user request and extracts:
- **Intent:** What does the user want to achieve?
- **Scope:** Which files, components, or systems are affected?
- **Constraints:** Are there time limits, quality requirements, or safety concerns?
- **Context:** Is there relevant history or prior work?

### Phase 2: Context Analysis (Parallel)

The Context Reader and Task Router work in **parallel** to understand the current state:

| Agent           | Activity                                  |
|-----------------|-------------------------------------------|
| Context Reader  | Reads project structure, code, and config.|
| Task Router     | Classifies the task type and complexity.  |

### Phase 3: Agent Selection

Based on the task classification, the orchestrator:
- Selects the specialist agents needed for the task.
- Loads the required skills for each agent.
- Assigns specific responsibilities to each agent.
- Determines the execution plan.

### Phase 4: Research and Analysis (Parallel)

All selected agents perform their research and analysis work in **parallel**:
- Reading existing code and documentation.
- Analyzing dependencies and impacts.
- Researching solutions and approaches.
- Planning their implementation steps.

This phase is safe to parallelize because all operations are read-only.

### Phase 5: Implementation (Sequential)

Agents perform file modifications in a **controlled, sequential** manner:
- One agent writes at a time.
- Each write operation is validated before the next begins.
- File conflicts are prevented by design.
- The orchestrator manages the write queue.

### Phase 6: Validation (Parallel)

Validation agents run their checks in **parallel**:
- **QA Agent:** Functional correctness.
- **Security Agent:** Vulnerability detection.
- **Style Agent:** Code style and conventions.
- **Structure Agent:** Repository organization.

### Phase 7: Final Review

The Final Reviewer consolidates the delivery:
- Confirms all validations passed.
- Verifies the work matches the original request.
- Creates a delivery summary.
- Recommends any follow-up actions.

---

## Conflict Prevention

The orchestration model prevents conflicts through:

1. **Phase Separation:** Reading and writing happen in distinct phases.
2. **Sequential Writes:** Only one agent writes at a time.
3. **File Ownership:** Each file has a clear owner during a workflow.
4. **Validation Gates:** Results are validated between phases.
5. **Orchestrator Control:** The orchestrator manages all coordination.

---

## Current Status

> **Foundation Phase (v0.1.0):** The orchestration model is documented. Implementation of the orchestrator and agent coordination will begin in Phase 2 (v0.2.0).
