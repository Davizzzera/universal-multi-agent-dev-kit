# Automation Pack: Usage

## How to use this pack
1. Determine what needs to be automated.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `automation`).
4. Specify your environment variable requirements.

## Recommended Prompt Structure
- **Context:** Brief intro to the manual process.
- **Goal:** Automation description.
- **Pack:** `automation-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `scripts/`).
- **Validation:** Dry-run requirements.

## Step-by-Step Usage
1. Ask the AI to `plan` the script.
2. Review the proposed logic and environment variables.
3. Instruct the AI to write the script (`automation`).
4. Ask the AI to run a `security-review`.
5. Run a dry-run validation (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Python Automation Specialist, Security Reviewer).

## How to validate
For an Automation pack, validation usually means:
- Running the script with a `--dry-run` flag.
- Verifying the `.env.example` file is created.
- Ensuring the `security-reviewer` confirms no credentials are leaked.

## Common Mistakes
- Hardcoding passwords or API keys in the script.
- Printing raw API responses that might contain tokens.
- Not implementing retry logic for flaky APIs.
