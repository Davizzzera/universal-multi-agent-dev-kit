# Auto-Orchestration Rules

## Purpose
This document defines the Auto-Orchestration Runtime Mode, ensuring the Universal Multi-Agent Dev Kit operates automatically and effectively without requiring manual user intervention for routing and selection.

## Default Operating Mode
The Universal Multi-Agent Dev Kit must operate as the **default project operating mode** when installed in a project. Users should not need to manually name agents, skills, workflows, or packs to get work done.

## Mandatory Routing Rule
Every user request must be automatically routed through the **Universal Orchestrator** unless the user explicitly disables the kit.

## Automatic Selection Rule
The **Task Router** must infer the required workflows, packs, agents, and skills from the natural language of the user request.

## No-Manual-Agent-Selection Rule
The user may name specific agents if they desire, but **the user is not required to do so**. The system must confidently infer the best agents for the task.

## Default Request Lifecycle
The standard execution flow for any request is:
1. Read root `AGENTS.md`
2. Read `.agent/AGENTS.md`
3. Read project context
4. Classify the request
5. Select workflow
6. Select pack if useful
7. Select agents
8. Select skills
9. Define scope
10. Plan execution
11. Implement or analyze
12. Validate
13. Produce inline Execution Trace

## Subagent Honesty Rule
Do not claim tool-visible subagents were spawned unless the underlying AI tool actually and visibly spawned them, or provides direct evidence of doing so.

## Orchestrated Roles Rule
If the execution happens within a single model run (a single context window or prompt cycle), the agents selected must be marked as **orchestrated agent roles**, not independent parallel subagents.

## Final Response Requirements
The final response delivered to the user must always include:
- **Orchestration Plan** before complex implementation.
- **Inline Execution Trace** for completed work.
- **Inline Registry Evidence** (exact registry paths) for all cited resources (agents, skills, workflows, packs).

## Anti-Patterns
Avoid the following behaviors:
- Asking the user which agent to use when the Task Router can decide.
- Saying "I used agents" without providing exact registry paths.
- Saying "subagents worked in parallel" without tool-provided evidence.
- Skipping the Execution Trace in the final response.
- Redirecting only to artifacts without providing an inline summary and trace.
