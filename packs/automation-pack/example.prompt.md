# Automation Pack: Example Prompt

**Copy and paste the following into Antigravity:**

```text
Goal: Create a Python script that polls an API every 5 minutes and saves new records.
Pack: `automation-pack`
Workflow: `automation`

Scope: `scripts/`
Instructions:
1. Use the Python Automation Specialist to write the script using requests.
2. Ensure the script reads the API key from a `.env` file.
3. Include retry logic for 500/503 errors.
4. Use the Security Reviewer to ensure no API keys are logged or hardcoded.
Validation: Provide the code for my review, do not run it directly.
Commit: Do not commit until I review the code.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
