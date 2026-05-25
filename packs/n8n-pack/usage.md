# n8n Pack: Usage

## How to use this pack
1. Determine the automation logic you need to build in n8n.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `automation`).
4. Specify your webhook or trigger constraints.

## Recommended Prompt Structure
- **Context:** Brief intro to the systems being connected.
- **Goal:** Automation description.
- **Pack:** `n8n-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `n8n/workflows/`).
- **Validation:** What manual steps to take in the n8n UI.

## Step-by-Step Usage
1. Ask the AI to `plan` the nodes required.
2. Review the proposed logic.
3. Instruct the AI to generate the JSON export (`automation`).
4. Ask the AI to run a `security-review` on the JSON.
5. Import the JSON into your n8n instance and test (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (n8n Automation Specialist, Security Reviewer).

## How to validate
For an n8n pack, validation usually means:
- The AI verifying the JSON contains no `credentials` fields populated with real data.
- The user manually importing the JSON and clicking "Execute Workflow" successfully.

## Common Mistakes
- Committing a JSON export that contains a live database password or API key.
- Creating infinite loops with webhook triggers.
- Not handling API rate limits in HTTP Request nodes.
