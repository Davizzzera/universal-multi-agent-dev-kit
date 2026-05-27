# Universal Multi-Agent Project Operating Mode

This project uses the Universal Multi-Agent Dev Kit. As an AI assistant or coding tool operating within this project, you must follow these rules for every request.

## Core Directives

- **Always use the kit by default.** This is the primary operating mode for this project.
- **Do not wait for the user to manually name agents.** The user expects you to handle routing.
- **Automatically select workflow, pack, agents, and skills** using the Task Router and Universal Orchestrator.
- **Use Registry-Locked Execution.** Only use resources that actually exist in the `.agent/` or `packs/` directories.
- **Use Inline Registry Evidence.** Always cite the exact paths to the agents, skills, workflows, or packs you used.
- **Use Execution Trace in the final response.** Detail the execution process visibly.
- **Be honest about tool-visible subagents.** If you are a single model running orchestrated roles, state it clearly. Do not claim true parallel subagents without tool-provided evidence.
- **Do not invent resources.** If an agent or skill doesn't exist in the registry, don't use it.
- **Do not edit outside scope.** Stick to the files requested or fundamentally required for the task.
- **Validate before claiming success.** Run tests or validation commands before concluding.

## No inline trace, no completion.
You must always provide an inline trace in your final response to the user.

## Required Final Response Format
When completing a task, your final response must include the following information inline:

1. Summary
2. Workflow used
3. Pack used
4. Agents selected
5. Agents actually used
6. Skills selected
7. Skills actually used
8. Files analyzed/created/modified
9. Validation evidence
10. Execution mode (orchestrated roles vs true subagents)
11. Risks or limitations
12. Next step
