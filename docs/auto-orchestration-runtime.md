# Auto-Orchestration Runtime Mode

## What is Auto-Orchestration Runtime Mode?
The Auto-Orchestration Runtime Mode is the default operating state of the Universal Multi-Agent Dev Kit when properly installed in a project. It allows you to make natural language requests to an AI coding tool (like Antigravity) without manually specifying which agents, skills, workflows, or packs to use. The kit handles the routing and orchestration for you automatically.

## How it Works in New Projects
Once the kit is injected into a new project, the AI tool reads the root `AGENTS.md` file, which points it to the `.agent/` directory. The AI assumes the role of the **Universal Orchestrator** and delegates the classification of your request to the **Task Router**.

## Automatic Routing vs. Actual Tool-Visible Subagents vs. Orchestrated Roles

It is crucial to understand the execution mechanics of the kit:
- **Automatic Routing:** The capability of the Task Router to read your request and infer the required resources from the registry without you naming them.
- **Actual Tool-Visible Subagents:** When the underlying AI tool has native support for spawning separate, visible subprocesses or distinct context windows that run in true parallel.
- **Orchestrated Agent Roles:** When the AI tool executes everything within a single model run (one context window), but systematically assumes the persona and rules of different agents sequentially or conceptually.

The kit supports both subagent types, but requires honesty. It will use Orchestrated Roles if true subagents are not supported by the environment.

## You Don't Need to Memorize Agents
Because of automatic routing, you can stop treating agents like separate programs you have to invoke. Just state your goal. The orchestrator will find the best agents for the job.

## How to Install it in a New Project
To enable Auto-Orchestration in any project:
1. Copy the `.agent/` folder into your project root.
2. Copy the `packs/` folder into your project root (optional but recommended).
3. Copy `adapters/antigravity/AGENTS.md` (or `.agent/templates/default-project-agents-template.md`) to the project root and name it `AGENTS.md`.

## How to Verify it is Working
When the system is correctly operating in this mode, every completed task will include an **Inline Execution Trace** in the AI's final response. This trace will contain:
- Exact registry paths for the workflow, pack, agents, and skills used.
- Explicit validation evidence showing commands run and passed.
- An honest declaration of the execution mode (orchestrated roles vs true subagents).

## Examples of Natural Requests

### Create Feature
*Request:* "Build a user profile page with a settings form."
*Result:* Automatically routes to `create-feature` workflow, selects Frontend Specialist and React Specialist, loads UI skills, and creates the component.

### Fix Bug
*Request:* "The login button is not triggering the submit event."
*Result:* Automatically routes to `debug` workflow, selects Bug Hunter and Frontend Specialist, identifies the missing handler, and fixes it safely.

### Improve UI
*Request:* "Make the dashboard hero section look more modern and spaced out."
*Result:* Automatically routes to `frontend-ui` workflow, selects UI/UX Designer and Design System Specialist, and updates CSS classes.

### Validate Project
*Request:* "Check if the codebase is healthy and tests pass."
*Result:* Automatically routes to `verify` workflow, selects QA Tester and Codebase Analyst, runs validation commands, and reports results.

## Common Mistakes

If Auto-Orchestration fails or the AI hallucinates, it's usually due to one of these mistakes:
- **Not copying `.agent/`:** The AI has no rules or registry to read.
- **Not copying `packs/`:** The AI misses context for specific domains.
- **Missing root `AGENTS.md`:** The AI does not know it should use the kit.
- **No inline trace:** The AI completed the work without proving how it did it.
- **Invented resources:** The AI claims to use agents or skills that do not exist in the `.agent/` directory.
- **No validation evidence:** The AI claims it works without showing the output of test commands.
