# Antigravity Adapter Troubleshooting

This document outlines common issues encountered when using Antigravity with the Universal Multi-Agent Development Kit, and their safe fixes.

### Python Command Not Found
- **Symptom:** `npm run verify` or `python verify_all.py` fails saying python is not recognized or opens the Windows Store.
- **Likely Cause:** Python is not installed or not in the system PATH.
- **Safe Fix:** Install Python 3.10+ from python.org and check the box "Add Python to PATH". Alternatively, Antigravity can fall back to manual checks or structural checks in Node/Shell until Python is available.
- **What Not To Do:** Do not attempt to run arbitrary scripts downloaded from the internet to "fix" Python.

### Git Authentication Failure
- **Symptom:** Antigravity attempts to commit and push, but the push is rejected with a 403 or authentication error.
- **Likely Cause:** Git credentials are not cached or configured for the terminal session Antigravity is using.
- **Safe Fix:** Open your local terminal, run `git pull` or `git push` manually, and complete the authentication flow (e.g., browser login for GitHub). Then instruct Antigravity to try again.
- **What Not To Do:** Do not paste Personal Access Tokens (PATs) or passwords into the chat for Antigravity to use.

### Repository Not Cloned
- **Symptom:** Antigravity cannot find `.agent/` files.
- **Likely Cause:** The kit was not cloned or copied into the target directory.
- **Safe Fix:** Run the clone command or copy the `.agent/` folder locally as described in `install.md`.
- **What Not To Do:** Do not ask Antigravity to recreate the entire kit from scratch.

### Merge Conflict
- **Symptom:** Antigravity cannot pull or push due to a conflict.
- **Likely Cause:** Remote changes conflict with local changes made by Antigravity.
- **Safe Fix:** Ask Antigravity to use the `coordinate` workflow to identify the conflict, or manually resolve the conflict in your IDE, commit, and resume.
- **What Not To Do:** Do not ask Antigravity to force push (`git push -f`).

### Validation Script Fails
- **Symptom:** `verify_all.py` exits with code 1.
- **Likely Cause:** A rule, frontmatter key, or structural requirement was violated during the last edit.
- **Safe Fix:** Read the explicit failure message provided by the script (e.g., "Missing section # Role in Agent X"). Ask Antigravity to fix that specific issue.
- **What Not To Do:** Do not bypass or disable the validation script.

### False Positive in security_check.py
- **Symptom:** Security check fails on a dummy token or standard documentation phrase.
- **Likely Cause:** The defensive regex triggered on something that looks like an assignment.
- **Safe Fix:** Use environment variables with safe example names, not real values. Or modify the dummy value to explicitly include "example" or "dummy" (e.g., `example_key_name`), which the script ignores.
- **What Not To Do:** Do not remove the regex from `security_check.py`.

### Antigravity Edits Too Much
- **Symptom:** Antigravity rewrote a whole file instead of changing one line, removing comments or existing logic.
- **Likely Cause:** The Scope Guardian was not invoked, or the prompt did not explicitly restrict edits.
- **Safe Fix:** `git restore` the file and provide a tighter prompt: "Use diff replacements only. Do not rewrite the file."
- **What Not To Do:** Do not accept the broad rewrite if you are unsure of the lost context.

### Antigravity Ignores File Ownership
- **Symptom:** A frontend agent modified a backend database schema.
- **Likely Cause:** The agent's boundaries were not clearly defined in `.agent/rules/file-ownership.md`.
- **Safe Fix:** Reject the change, update the file ownership matrix, and re-run.
- **What Not To Do:** Do not let the boundary violation persist in the commit history.

### Wrong Language in Repository Files
- **Symptom:** Antigravity wrote documentation or code comments in Portuguese (or another language) instead of English.
- **Likely Cause:** The prompt did not specify the Language Rule.
- **Safe Fix:** Instruct Antigravity: "Translate the last file changes to English. Remember the Language Rule: Repository files in English, chat in Portuguese."
- **What Not To Do:** Do not leave mixed languages in the codebase.

### Missing Commit Hash
- **Symptom:** Antigravity reports it pushed changes, but doesn't provide a hash.
- **Likely Cause:** The terminal command output was truncated or Antigravity lost context.
- **Safe Fix:** Check `git log` locally to confirm the commit exists. Remind Antigravity to include the hash in future reports.
- **What Not To Do:** Do not assume the push failed without checking `git status`.
