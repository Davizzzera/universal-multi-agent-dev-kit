# Automation Pack

> A preset for Python scripts, browser automation, scheduled jobs, file processors, API polling and operational automation.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to build resilient scripts and automations that interact with APIs, files, or browsers, ensuring they handle errors gracefully and log securely.

## When to use this pack
- Python automation
- File processing
- Browser automation
- API integrations
- Scheduled jobs
- Reporting scripts
- Local automations

## When NOT to use this pack
- Pure static documentation
- UI-only landing pages
- Enterprise architecture planning without implementation

## Recommended Agents
This pack utilizes python automation specialists, integration specialists, and security reviewers. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on browser automation techniques, retry strategies, and secure logging. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to scripting, such as `automation` and `debug`. See `workflows.md` for the full list.

## Validation Expectations
Scripts must be tested via dry-runs when possible. Environment variables must be audited to ensure no secrets are hardcoded.

## Safety and Scope Notes
- Scripts must strictly use environment variables for all credentials.
- Ensure the `security-reviewer` audits the code for hardcoded secrets before execution.

## Example Use Cases
- "Write a Playwright script to log into a portal and download the daily report."
- "Create a Python script that polls an API every 5 minutes and saves new records to a CSV."

## Related Packs
- `data-bi-pack`
