# n8n Pack

> A preset for n8n automations, webhook flows, integrations, trigger-based workflows and operational process automation.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to design, document, and review n8n low-code automations safely.

## When to use this pack
- n8n workflows
- Webhook flows
- Google Sheets integrations
- CRM automations
- Notification flows
- API-based automations
- Low-code process automation

## When NOT to use this pack
- Full custom frontend-only apps
- Database schema-heavy backend projects without automation
- Static marketing pages

## Recommended Agents
This pack utilizes n8n automation specialists, webhook specialists, and business analysts. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on n8n workflow design, webhook handling, and secure logging. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to automation, such as `automation` and `debug`. See `workflows.md` for the full list.

## Validation Expectations
n8n workflows must be validated to ensure nodes execute successfully and handle errors (e.g., using "Continue On Fail" settings where appropriate).

## Safety and Scope Notes
- **CRITICAL:** Exported n8n workflow JSON files MUST NOT contain live credentials. Always verify exports before committing to the repository.
- Ensure the `security-reviewer` audits the exported JSON.

## Example Use Cases
- "Design an n8n workflow to listen for a Stripe webhook and create a record in Salesforce."
- "Debug the failing node in our Slack notification workflow."

## Related Packs
- `automation-pack`
