# Debug Prompt

**Purpose:** Use this prompt to instruct Antigravity to find and fix a bug with minimal collateral damage and strict validation.

---

**Copy and paste the following into Antigravity:**

```text
Goal: [INSERT YOUR GOAL HERE, e.g., Fix the null reference exception in the data parser]
Workflow: `debug`

Scope: Only the files directly related to the reported issue.
Constraints:
1. Ensure the `qa-tester` agent is involved to verify the fix.
2. Provide a minimal, scoped fix. Do not rewrite or refactor the entire file.
3. Keep changes as small as possible.
Validation: Run the specific tests related to this module. Show the output proving the error is gone.
Commit: If successful, commit with "fix: [short description]" and push.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
