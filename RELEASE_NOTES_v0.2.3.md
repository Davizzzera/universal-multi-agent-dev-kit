# Universal Multi-Agent Dev Kit v0.2.3

**Release Type:** Auto-Orchestration & Registry Evidence Release  
**Tag:** `v0.2.3`

## Release Summary
This release finalizes Phase 15 and Phase 16 of the Universal Multi-Agent Development Kit. It shifts the operational paradigm from manual orchestration to **Auto-Orchestration Runtime Mode** and enforces strict accountability through **Inline Registry Evidence**. The goal is to make using the kit in any project seamless, natural, and verifiable.

## What Changed Since v0.2.2
- Implemented **Auto-Orchestration Runtime Mode** as the default behavior.
- Added a default project `AGENTS.md` template for easier injection into new codebases.
- Added explicit rules to require **Inline Registry Evidence** for all executed actions.
- Clarified execution mode honesty: Distinguishing between tool-visible subagents and orchestrated agent roles.
- Strengthened the Antigravity default operating mode.

## Auto-Orchestration Runtime Overview
Users no longer need to memorize or manually name agents, skills, workflows, or packs. The kit now operates automatically as a routing layer above the implementation process.
When installed, the Universal Orchestrator is the default entry point, delegating to the Task Router to infer the best workflow and agents based entirely on the user's natural language request.

## How Users Should Use the Kit in New Projects
To use the kit in a new project, follow the **Auto-Orchestration Runtime Mode** setup:
1. Copy `.agent/` and `packs/` directories to the root of the project.
2. Copy `adapters/antigravity/AGENTS.md` (or `.agent/templates/default-project-agents-template.md`) to the root of the project as `AGENTS.md`.
3. Make normal, natural requests. The system will handle the rest.

## How Automatic Routing Works
- The **Task Router** evaluates the user's intent, scope, and constraints.
- It dynamically selects the required workflow, pack, agents, and skills from the `.agent/` and `packs/` registries without explicit user prompting.

## How to Verify the Kit Was Really Used
Since the user doesn't specify agents, the final response MUST contain an **Inline Execution Trace**. This trace must show exactly what the AI tool executed to verify it didn't hallucinate agents or skip the kit entirely.

### Required Registry Evidence
The execution trace must include **exact registry paths**:
- **Workflow path** must point to `.agent/workflows/*.workflow.md`
- **Pack path** must point to `packs/*/pack-manifest.json`
- **Agent path** must point to `.agent/agents/**/*.agent.md`
- **Skill path** must point to `.agent/skills/**/SKILL.md`

## Execution Mode Honesty
The AI must report the **execution mode** honestly in its trace:
- **Tool-visible subagents are not guaranteed.** True parallel subagent execution depends strictly on the underlying AI tool's capabilities.
- **Orchestrated agent roles are valid** when reported honestly. This occurs when the AI tool handles everything within a single model run (context window) but assumes different agent personas systematically.

## Validation Commands Used
The entire system architecture, Markdown files, and defensive security measures have been verified using the built-in validation suite.

### Recommended Validation Command
```bash
npm run verify
```

## Known Remaining Warnings
- **Markdown long-line warnings:** The validation script may output warnings for lines exceeding 160 characters in `.agent/agents/` files. These are expected and non-blocking for AI reading capabilities.

## Known Limitations
- **True parallel subagent execution:** Depends solely on the AI tool support (e.g., whether the AI environment supports spawning multiple physical LLM agent runs).
- **CLI Installer:** The `npx universal-agent-kit init` tool is not implemented yet.
- **Adapters:** Claude Code, Cursor, and Codex adapters are planned but not implemented yet. The Antigravity adapter remains the only official integration.

## Upgrade Notes from v0.2.2
- If you are updating an existing project, replace your root `AGENTS.md` with the new version provided in `adapters/antigravity/AGENTS.md` (or the default template) to activate the Auto-Orchestration Runtime Mode.
- Copy over the new `.agent/rules/` to enforce Inline Registry Evidence.
