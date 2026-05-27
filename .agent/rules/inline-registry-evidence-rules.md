# Inline Registry Evidence Rules

These rules enforce strict, verifiable, and inline registry evidence to prove how the Universal Multi-Agent Dev Kit was utilized for a given task. 

## Core Requirement: Inline Execution Trace

The Execution Trace **must** be included directly within the final chat response. 
- Creating a separate artifact (like `walkthrough.md`) or a standalone Markdown file is permitted and encouraged for extended details, but **an artifact-only trace is not valid**. It cannot replace the inline final response trace.
- **No inline trace, no completion.**

## Registry-Backed Evidence Definitions

To claim usage of any kit component, you must provide registry-backed evidence with exact paths:

- **Registry-backed workflow evidence:** Must point to `.agent/workflows/*.workflow.md`.
- **Registry-backed pack evidence:** Must point to `packs/*/pack-manifest.json`.
- **Registry-backed agent evidence:** Must point to `.agent/agents/**/*.agent.md`.
- **Registry-backed skill evidence:** Must point to `.agent/skills/**/SKILL.md`.

## Strict Rules

- **No registry path, no usage claim.** You cannot claim to have used an agent or workflow without providing its exact registry file path.
- **No `SKILL.md` path, no skill usage claim.** If you claim a skill, it must be backed by a `SKILL.md` file.
- **No `pack-manifest.json` path, no pack usage claim.** A pack folder path is not enough; point to the manifest.
- **No validation evidence, no success claim.** You must provide the command executed, the exit code (if available), and a summary of the output.
- **No visible subagents, no true parallelism claim.** If the underlying LLM platform executes linearly without spawning distinct subagents, do not claim true parallel execution.
- **Execution mode evidence:** Be honest about whether tools and subagents were visibly utilized or if actions were completed linearly.

## Classifying Orchestration Agents

When citing orchestration agents, classify their status clearly:
- **selected:** Agent was chosen for the task.
- **used:** Agent was actively engaged.
- **conceptually applied:** Agent rules were applied by the primary LLM context, but a separate subagent was not instantiated.
- **not tool-visible:** The agent execution was not visible as a separate tool call in the platform.
- **validation-only:** Agent rules were used only to validate the output.

## Anti-Patterns to Avoid

- ❌ "See `walkthrough.md` for the Execution Trace." (Without an inline trace).
- ❌ "I used agents to complete this." (Without specifying paths).
- ❌ "The workflow was UI Enhancement." (If no `.workflow.md` file exists for it).
- ❌ "Skill used: Tailwind Mastery." (If it is not registry-backed with a `SKILL.md`).
- ❌ "Validation passed." (Without showing the exact command, exit code, or summary evidence).
