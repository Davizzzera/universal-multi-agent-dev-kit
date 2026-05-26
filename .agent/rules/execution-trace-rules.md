# Execution Trace Rules

This document outlines the rules for execution traceability and agent visibility in the Universal Multi-Agent Dev Kit.

## Why Execution Trace Exists
The Execution Trace exists to provide absolute transparency to the user. Since the orchestration is automatic and the user doesn't manually call agents, they need a clear, structured final report to understand what decisions the kit made, who worked on the task, what they did, and what execution mode was used.

## Definitions
- **Selected agents**: The agents the Orchestrator or Task Router initially decided to involve based on the request.
- **Actually used agents**: The agents that genuinely performed work (e.g. modified files, ran commands, or analyzed code). An agent might be selected but skipped if the task didn't require them after all.
- **Recommended agents**: Agents that were not used but could be beneficial for follow-up tasks or future phases.
- **Tool-visible subagents**: Agents that the AI model physically spawns as separate, independent processes using a multi-agent tool or API, providing concrete parallel execution and isolated state.
- **Orchestrated agent roles**: The AI model assumes different personas sequentially or conceptually in its context, without actually spawning independent sub-processes. 

## Execution Trace Requirements
- The agent must not claim true parallel subagent execution unless the tool provides evidence (e.g., separate task IDs, separate agent instances spawned).
- When the UI only shows "working", the final report must still provide an orchestration trace, clarifying that roles were orchestrated within a single run.
- **Every implementation task** (including debugging, refactoring, validation, or release) must include an Execution Trace in the final response.
- **Every complex task** must include an Orchestration Plan before implementation when possible.

## What Must Be Identified
Every execution trace must clearly identify:
- **Workflow used**: Which workflow from `.agent/workflows` guided the execution.
- **Pack used**: Which project pack (if any) provided the context.
- **Agents selected**: The list of all agents initially selected.
- **Agents actually used**: The subset of agents that did the work.
- **Skills selected**: The skills chosen from `.agent/skills`.
- **Skills actually used**: The skills that were effectively utilized.
- **Files analyzed**: Files read for context.
- **Files created**: New files generated.
- **Files modified**: Existing files changed.
- **Parallel work**: Tasks executed simultaneously (requires tool evidence).
- **Sequential work**: Tasks executed one after another.
- **Validation evidence**: Concrete proof that quality checks passed (e.g., test output, command results).

## Anti-Patterns
- **Vague claims**: Saying "I used multiple agents" without explicitly listing them.
- **Unsubstantiated quality**: Saying "QA passed" without providing execution evidence or command outputs.
- **Vague security reviews**: Saying "Security reviewed" without describing what was checked.
- **Fake parallelism**: Claiming subagents acted independently or in parallel without evidence from the tool interface.

## Mandatory Final Response
The final response block MUST follow the structure defined in `.agent/templates/execution-trace-template.md`.
