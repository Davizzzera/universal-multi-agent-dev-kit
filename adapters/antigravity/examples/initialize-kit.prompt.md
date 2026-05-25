# Initialize Kit Prompt

**Purpose:** Use this prompt to ask Antigravity to clone or copy the Universal Multi-Agent Development Kit into your target project and verify it.

---

**Copy and paste the following into Antigravity:**

```text
Goal: Initialize the Universal Multi-Agent Development Kit in this project.
Workflow: `plan` (first phase)

Instructions:
1. Check if the `.agent/` folder exists in this project root.
2. If it does not exist, clone `https://github.com/Davizzzera/universal-multi-agent-dev-kit.git` into a temporary folder, copy the `.agent/` folder into this project root, and delete the temporary folder.
3. Ensure `adapters/antigravity/AGENTS.md` is present or its contents are understood.
4. Run validation: If Node/Python are available, run the verification scripts (`python .agent/scripts/verify_all.py` or `npm run verify`).
5. Stop and wait for my confirmation before proceeding to other tasks.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
