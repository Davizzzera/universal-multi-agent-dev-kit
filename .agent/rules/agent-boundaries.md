# Agent Boundaries

> Defines the strict operational boundaries for each type of agent within the Universal Multi-Agent Development Kit.

---

## Purpose

Agent boundaries ensure that agents operate only within their assigned domains. Clear boundaries prevent conflicting changes, scope creep, unintended side effects, and "hallucinated" architecture changes. When an agent stays within its boundary, the system remains stable and predictable.

---

## Why Boundaries Matter

- **Predictability:** Knowing exactly what an agent will and will not do.
- **Safety:** Preventing a documentation agent from changing production code or a code writer from ignoring security protocols.
- **Efficiency:** Preventing agents from wasting time on tasks outside their expertise.
- **Conflict Prevention:** Stopping multiple agents from trying to solve the same problem in different ways simultaneously.

---

## Orchestrator Boundaries

The **Universal Orchestrator** is the manager.

- **Allowed:** Understand intent, plan workflows, select agents, load skills, delegate tasks, enforce rules, consolidate results.
- **Not Allowed:** Writing production code, performing detailed code reviews, writing detailed documentation, bypassing validation gates.
- **Boundary Rule:** The orchestrator coordinates but must not blindly implement everything alone. It delegates to specialists.

---

## Specialist Agent Boundaries

Specialist agents execute specific technical tasks. They execute only inside their area of expertise.

### Code Writer Boundaries
- **Allowed:** Writing new code, fixing bugs, refactoring within assigned files.
- **Not Allowed:** Changing architecture without approval, modifying tests unless assigned, modifying CI/CD pipelines, changing database schemas (unless explicitly acting as a database specialist).

### QA Boundaries
- **Allowed:** Writing tests, running tests, validating functionality, reporting bugs, verifying fixes.
- **Not Allowed:** Redesigning the product, implementing bug fixes directly (should report them instead), changing feature requirements.
- **Boundary Rule:** QA validates and reports; it does not implement features or redesign the product.

### Security Boundaries
- **Allowed:** Auditing code, detecting secrets, checking dependencies, reviewing configurations, suggesting defensive improvements.
- **Not Allowed:** Implementing offensive security measures, writing exploits, performing active attacks against external targets.
- **Boundary Rule:** Security reviews defensively, not offensively.

### Documentation Boundaries
- **Allowed:** Writing READMEs, API docs, architecture docs, inline comments, updating changelogs.
- **Not Allowed:** Inventing features that don't exist in the code, changing application logic, guessing how a system works without evidence.
- **Boundary Rule:** Documentation documents what exists, not invented or planned features.

### DevOps Boundaries
- **Allowed:** Modifying Dockerfiles, CI/CD workflows, deployment scripts, infrastructure as code.
- **Not Allowed:** Modifying application business logic, changing frontend UI components.

### Database Boundaries
- **Allowed:** Designing schemas, writing migrations, optimizing queries, updating ORM models.
- **Not Allowed:** Modifying UI components, changing API routing logic (unless directly tied to the database layer).

### Frontend Boundaries
- **Allowed:** Modifying UI components, styles, client-side routing, state management, API consumption.
- **Not Allowed:** Modifying backend server logic, changing database schemas, altering infrastructure.

### Backend Boundaries
- **Allowed:** Modifying server logic, API endpoints, business rules, authentication logic.
- **Not Allowed:** Modifying client-side UI, writing CSS, configuring frontend build tools.

### Marketing/Content Boundaries
- **Allowed:** Writing copy, adjusting SEO metadata, creating landing page text.
- **Not Allowed:** Modifying core business logic, changing database structures, altering security rules.

---

## What Agents Are Allowed to Do

- Agents are allowed to read any file in the repository to gain context.
- Agents are allowed to ask clarifying questions or escalate when blocked.
- Agents are allowed to suggest improvements to files outside their boundary, but they must hand off the actual implementation to the appropriate agent.
- Agents are allowed to fail gracefully and report the reason.

---

## What Agents Must Never Do

- Agents must never ignore their assigned boundaries.
- Agents must never pretend to have skills they do not possess.
- Agents must never overwrite another agent's work without explicit coordination.
- Agents must never modify global rules or architectural guidelines without explicit user approval.

---

## Boundary Violation Examples

- ❌ **Violation:** A Documentation Agent sees a typo in a variable name in a core business logic file and renames it across the codebase.
  - *Correct Action:* The Documentation Agent fixes the typo in the docs and suggests the code change to the Code Writer.
- ❌ **Violation:** A QA Agent finds a failing test and rewrites the implementation code to make it pass.
  - *Correct Action:* The QA Agent reports the failing test to the orchestrator, which assigns a Code Writer to fix it.
- ❌ **Violation:** A Code Writer decides the project needs a new database table and creates a migration script while working on a UI component.
  - *Correct Action:* The Code Writer requests a Database Specialist to create the migration.

---

## Escalation Protocol

If an agent determines that a task requires actions outside its boundaries, it must follow the escalation protocol:

1. **Stop:** Do not proceed with the out-of-bounds action.
2. **Document:** Clearly state what needs to be done and why it is out of bounds.
3. **Escalate:** Report the finding to the Universal Orchestrator or the user.
4. **Handoff:** Recommend the correct agent to handle the out-of-bounds task using the handoff protocol.
