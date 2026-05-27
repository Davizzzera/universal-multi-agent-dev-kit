# Universal Multi-Agent Dev Kit v0.2.2

**Release Type:** Execution Trace Release
**Tag:** v0.2.2

## Release Summary
The v0.2.2 release introduces the Execution Trace and Agent Visibility layer. This release focuses on providing transparency to users by ensuring AI agents formally document their orchestration choices, executed skills, and validation evidence after completing tasks.

## What Changed Since v0.2.1
- Added Execution Trace rules and template.
- Added Orchestration Plan template for complex tasks.
- Added Agent Activity Report template.
- Improved agent visibility requirements in the core architecture.
- Updated the Antigravity adapter to enforce visible Execution Traces.

## Execution Trace Overview
Execution Trace is a structured output format that acts as a "receipt" of AI execution. It provides a clear summary of which workflow, pack, agents, and skills were used, along with what files were affected and what validations were performed.

## Orchestration Plan Overview
For complex tasks, agents are now required to produce an Orchestration Plan before making changes. This ensures the execution scope, parallelization limits, and selected agents are explicitly defined beforehand.

## Agent Activity Report Overview
This report offers a concise table view of what each participating agent did, the files they managed, and their validation outcomes.

## Agent Visibility Improvements
Agents are no longer allowed to claim ambiguous collaboration without concrete evidence. The reporting enforces a strict distinction between the agents initially selected and the ones that actually did the work.

## Antigravity Adapter Improvements
The Antigravity integration rules and prompt library were updated to strictly require an Execution Trace and Orchestration Plan, explicitly banning vague statements like "I used multiple agents".

## Terminology Distinctions
- **Selected agents:** Agents chosen initially based on the request.
- **Actually used agents:** Agents that effectively performed tasks or validations.
- **Recommended agents:** Agents suggested for follow-up but not used in the current task.
- **Tool-visible subagents:** Separate processes physically spawned by the AI tool offering true parallel execution.
- **Orchestrated agent roles:** The AI model conceptually acts out different personas sequentially without spawning true parallel subprocesses.

## Validation Commands Used
- `npm run generate:index`
- `npm run verify`

## Known Remaining Warnings
- Markdown long-line warnings are currently non-blocking and acceptable.

## Known Limitations
- True parallel subagent execution depends strictly on the underlying AI tool's capabilities.
- The kit can require detailed text reporting, but the AI client UI may still show a generic "working" indicator.
- CLI installer is not implemented yet.
- Claude Code, Cursor, Codex, and other additional adapters are planned but not implemented yet.

## Upgrade Notes from v0.2.1
To upgrade, simply pull the latest `v0.2.2` tag. No architectural breaking changes were introduced, only added visibility rules and templates.

**Recommended Validation Command:**
```bash
npm run verify
```
