# Coordinate Workflow Prompt

**Purpose:** Use this prompt for complex tasks requiring multiple specialist agents to work together and coordinate state.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Implement the full authentication flow including UI and database schema]
Workflow: `coordinate`

Scope: Frontend and Backend directories.
Constraints:
1. Orchestrator must divide tasks between Frontend Specialist and Backend Specialist.
2. Parallelize discovery (reading files). Serialize conflicting edits (writing files). Parallelize verification.
3. Use the `.agent/memory/` directory to share state between agents if necessary.
4. QA Agent must review the integrated result.
Validation: Both frontend and backend unit tests must pass. Provide test output as evidence.
Commit: If successful, commit with message "feat: implement full auth flow" and push.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
