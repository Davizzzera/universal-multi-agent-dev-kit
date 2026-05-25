# Antigravity Prompt Library

Use these reusable prompt patterns to control Antigravity effectively. Copy and paste them into your Antigravity chat.

*Note: All prompts are written in English to enforce repository behavior correctly. You can append the Language Rule to receive chat responses in Portuguese.*

## Language Rule Add-on
Append this to any prompt if you want Portuguese responses:
```text
Answer me in Brazilian Portuguese, but write repository files in English.
```

---

## 1. Repository Foundation
```text
Goal: Initialize the base project structure.
Workflow: `plan`
Scope: Root directory.
Constraint: Do not create implementation code yet. Create folders for src, docs, and tests.
Validation: List the created directories.
```

## 2. Rules and Templates
```text
Goal: Create a custom project rule for database access.
Workflow: `document`
Scope: `.agent/rules/`
Constraint: Use the standard rule format. Prohibit direct database access from the frontend.
Validation: Ensure the rule file is valid Markdown.
```

## 3. Agents
```text
Goal: Create a custom agent for translating text.
Workflow: `document`
Scope: `.agent/agents/`
Constraint: Use `.agent/templates/agent-template.md`.
Validation: Run `npm run verify` to ensure the agent is recognized by the index.
```

## 4. Skills
```text
Goal: Create a custom skill for translating JSON files.
Workflow: `document`
Scope: `.agent/skills/`
Constraint: Use `.agent/templates/skill-template.md`.
Validation: Run `npm run verify`.
```

## 5. Workflows
```text
Goal: Create a custom workflow for bulk translation.
Workflow: `document`
Scope: `.agent/workflows/`
Constraint: Use `.agent/templates/workflow-template.md`. Require the translation agent.
Validation: Run `npm run verify`.
```

## 6. Validation
```text
Goal: Run the full validation pipeline.
Workflow: `verify`
Scope: Repository validation scripts.
Constraint: If Python is unavailable, report the specific error.
Validation: Provide the exit code and summary of the script execution.
```

## 7. Adapter Creation
```text
Goal: Create a new adapter for Cursor.
Workflow: `document`
Scope: `adapters/cursor/`
Constraint: Follow the structure of the Antigravity adapter.
Validation: Ensure the manifest is valid JSON.
```

## 8. Feature Implementation
```text
Goal: Implement the user settings page.
Workflow: `create-feature`
Scope: `src/pages/` and `src/components/`.
Constraint: Use React and Tailwind. Do not modify the API.
Validation: Run UI tests and provide the output.
Commit: If successful, commit with "feat: add user settings page" and push.
```

## 9. Bugfix
```text
Goal: Fix the null reference error in the login flow.
Workflow: `debug`
Scope: `src/auth/`
Constraint: Provide a minimal, scoped fix. Do not rewrite the file.
Validation: Run the auth tests.
Commit: If tests pass, commit with "fix: resolve null reference in login" and push.
```

## 10. Verification
```text
Goal: Verify the overall health of the codebase.
Workflow: `verify`
Scope: Entire project.
Constraint: Run linters, type checks, and unit tests. Do not modify files.
Validation: Provide terminal output of all checks.
```
