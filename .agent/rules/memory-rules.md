# Memory Rules

> Governs how agents store, retrieve, and manage shared context and state.

---

## Purpose

Agents are stateless by default. However, complex workflows require shared context. The `.agent/memory/` directory serves as the persistent memory for the multi-agent system. This document defines what can and cannot be stored there.

---

## What Memory Is

Memory consists of Markdown or JSON files stored in `.agent/memory/` that record:
- Project-wide decisions.
- Coding conventions established during the project.
- User preferences.
- Context summaries from long-running workflows.

---

## Allowed Memory

Agents may store the following in memory:
- **Project Decisions:** Architectural choices, library selections, and the reasoning behind them.
- **Conventions:** Naming conventions, preferred design patterns, or formatting rules specific to this repository.
- **User Preferences:** "The user prefers functional components over class components."
- **Workflow State:** High-level summaries of completed phases for handoff purposes.

---

## Prohibited Memory

- **Never store secrets:** Passwords, API keys, database URLs, tokens, or private keys must NEVER be written to memory files.
- **Never store unnecessary personal data:** Do not store PII, user emails, or names unless explicitly required for a mock data schema (and even then, use fake data).
- **No massive logs:** Do not dump raw compilation logs or massive JSON payloads into memory. Summarize them instead.

---

## Memory Update Protocol

1. **Read First:** Before adding to memory, agents must read existing memory to avoid duplication or contradictory rules.
2. **Be Concise:** Memory files must be short and easily scannable.
3. **Explicit Updates:** When a decision changes, the memory file must be explicitly updated to reflect the new decision, rather than appending conflicting information.

---

## Memory Review Checklist

Before committing a memory update, agents must verify:
- [ ] Does this contain any secrets or credentials? (Must be NO)
- [ ] Is this information persistent and relevant for future tasks?
- [ ] Is it concise and well-structured?
- [ ] Does it contradict existing memory? If so, was the conflict resolved?
