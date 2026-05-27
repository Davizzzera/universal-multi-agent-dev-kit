# Execution Trace and Agent Visibility

This document explains the Execution Trace feature, which provides transparency into how the Universal Multi-Agent Dev Kit orchestrates tasks.

## What is Execution Trace?
Execution Trace is a mandatory reporting format that AI tools (like Antigravity) must provide after completing a task. Since the kit routes and selects agents automatically, the trace acts as a "receipt" of what exactly happened under the hood.

## Why it Matters
When you ask an AI tool to "build a feature", you need to know:
- Did it write tests?
- Which agents actually reviewed the code?
- Was it just one single model pretending to be multiple agents, or did it spawn actual parallel processes?
- What validation was run?

Execution Trace answers these questions explicitly, preventing vague claims like "I used agents" or "QA passed."

## Terminology

### Selected vs Used Agents
- **Selected Agents:** The agents the Orchestrator initially thought might be needed based on your request.
- **Used Agents:** The agents that *actually* performed work (modified files, ran checks).

### Recommended vs Used Agents
- **Recommended Agents:** Agents suggested for future steps but not used in the current task (e.g., suggesting a QA agent for a follow-up test phase).
- **Used Agents:** Agents that actively participated in the current task.

### Tool-Visible Subagents vs Orchestrated Roles
- **Tool-Visible Subagents:** Actual separate processes spawned by the AI tool, offering true parallel execution and isolated state.
- **Orchestrated Roles:** The AI tool executes everything in a single process but assumes different agent personas conceptually to follow rules and workflows.

## How to Read the Trace
The trace contains sections for Request Classification, Execution Mode, Agents, Skills, Files, and Validation Evidence. 
Always look for the **Execution Mode** to see if true parallelism was achieved, and check **Validation Evidence** to ensure quality.

## Inline Registry Evidence

The trace must appear directly in the chat response. Artifacts alone (like `walkthrough.md`) are not enough because the user needs immediate proof of what the agent executed.

**Correct path examples:**
- `.agent/workflows/frontend-ui.workflow.md`
- `packs/web-app-pack/pack-manifest.json`
- `.agent/agents/frontend/react-specialist.agent.md`
- `.agent/skills/frontend/react-component-create/SKILL.md`

**Example of an incorrect trace:**
"I used the React agent and the Web pack. Validation passed."

**Example of a correct trace:**
See the examples below.

## Examples

### Frontend Task Example
```markdown
# Execution Trace
- **Workflow:** create-feature
- **Pack:** web-app-pack
- **Execution Mode:** Orchestrated roles (sequential)
- **Agents Used:** Frontend Specialist, UI/UX Designer
- **Agents Selected but Skipped:** React Specialist (Task was vanilla JS)
- **Files Modified:** `index.html`, `style.css`
- **Validation:** Ran `npm run lint`. Output: `[OK] No errors`.
```

### API Task Example
```markdown
# Execution Trace
- **Workflow:** api-development
- **Pack:** api-pack
- **Execution Mode:** Tool-visible subagents (parallelized validation)
- **Agents Used:** API Designer, Backend Specialist, QA Tester
- **Files Created:** `src/routes/users.ts`, `tests/users.test.ts`
- **Validation:** Ran `npm test tests/users.test.ts`. Output: `1 passing (45ms)`.
```

### Bugfix Task Example
```markdown
# Execution Trace
- **Workflow:** debug
- **Execution Mode:** Orchestrated roles
- **Agents Used:** Bug Hunter, Backend Specialist
- **Files Modified:** `src/auth.ts`
- **Validation:** Ran specific auth test suite. Output: `All tests passed`.
```

### Validation Task Example
```markdown
# Execution Trace
- **Workflow:** verify
- **Execution Mode:** Orchestrated roles
- **Agents Used:** CI/CD Specialist
- **Agents Recommended:** QA Tester (for deeper e2e testing)
- **Validation:** Ran `npm run verify`. Output: `[OK] ALL VALIDATIONS PASSED`.
```

## Limitations
- **The Kit Enforces Reporting, not UI:** The kit forces the model to output the trace text, but the chat UI might still just show a generic "Working..." spinner during execution.
- **Parallelism is Tool-Dependent:** True parallelism depends entirely on whether your AI client (like Cursor, GitHub Copilot, etc.) supports spawning separate subagent processes.

## Best Practices
- **Always ask for the Execution Trace** if you are auditing complex work.
- **Require validation evidence.** Never accept "it works" without a command output or a completed checklist.
