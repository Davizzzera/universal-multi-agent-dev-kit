# Handoff Rules

> Defines the protocol for transferring responsibility between agents.

---

## Purpose

Agents frequently need to pass work to one another. A code writer might need QA to test its work, or a backend agent might need a database agent to create a schema. Handoff rules ensure context is preserved, duplicate work is avoided, and accountability is maintained during these transfers.

---

## What a Handoff Is

A handoff is a formal transfer of task responsibility from a **Source Agent** to a **Target Agent**, mediated by the **Universal Orchestrator**.

---

## When to Use Handoff

- An agent reaches the limit of its boundaries (e.g., Code Writer needs Documentation).
- A task requires specialized skills the current agent lacks.
- A workflow step completes and the next sequential step belongs to a different agent.
- An agent encounters an error it cannot resolve but another agent might (e.g., QA finds a bug, hands off to Code Writer).

---

## When Not to Use Handoff

- Do not handoff for tasks within the current agent's boundaries and capabilities.
- Do not handoff to avoid doing assigned work.
- Do not handoff if the workflow specifically mandates the current agent must complete the step.

---

## Orchestrator-Controlled Handoffs

Agents **do not** directly invoke other agents.
When an agent needs a handoff, it outputs a Handoff Request to the Universal Orchestrator. The Orchestrator then provisions the Target Agent and passes the context.

---

## Required Handoff Fields

Every handoff request must include the following information using the standard handoff template:

- **Source Agent:** Who is initiating the handoff.
- **Target Agent:** Who should receive the handoff.
- **Task Summary:** What needs to be done.
- **Context Already Gathered:** What has been analyzed or completed so far.
- **Files Involved:** Which files the target agent needs to look at or modify.
- **Constraints:** Any rules or limitations specific to this task.
- **Risks:** Potential issues the target agent should watch out for.
- **Expected Output:** What the source agent expects back (if applicable).
- **Validation Required:** How the target agent should validate its work.

---

## Agent-to-Agent Handoff Protocol

1. **Source Agent** completes its immediate scope.
2. **Source Agent** identifies out-of-scope work.
3. **Source Agent** generates a Handoff Request.
4. **Universal Orchestrator** reads the request and instantiates the **Target Agent**.
5. **Target Agent** reads the Handoff Request as its primary context.
6. **Target Agent** executes the requested task.

---

## Handoff Examples

**Good Handoff:**
"Code-Writer to QA-Tester: I have implemented the `login()` function in `src/auth.ts`. I need you to write unit tests for it covering success, invalid password, and missing user scenarios. Constraints: Use Jest. Validation: Run the tests and ensure 100% coverage on the new function."

**Bad Handoff:**
"Code-Writer to QA: I wrote some code, test it." *(Missing files, constraints, expected output, and context).*

---

## Handoff Anti-Patterns

- **Ping-Pong Handoffs:** Agents continuously handing the same task back and forth without resolution. If a handoff bounces back twice, escalate to the Orchestrator for human intervention.
- **Context Loss:** Failing to provide the research or decisions made by the Source Agent, forcing the Target Agent to start from scratch.
- **Over-Prescriptive Handoffs:** Telling the Target Agent exactly *how* to do its job (e.g., Code Writer telling QA exactly which assertions to write, rather than what behavior to test).
