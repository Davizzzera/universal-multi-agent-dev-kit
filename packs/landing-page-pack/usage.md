# Landing Page Pack: Usage

## How to use this pack
1. Determine the goal of your marketing page.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `frontend-ui`).
4. Specify your brand guidelines or tone of voice constraints.

## Recommended Prompt Structure
- **Context:** Brief intro to the product/campaign.
- **Goal:** Page description.
- **Pack:** `landing-page-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `public/` and `src/pages/`).
- **Validation:** Visual and accessibility checks.

## Step-by-Step Usage
1. Ask the AI to `plan` the copy and structure using this pack.
2. Review the proposed copy and wireframe.
3. Instruct the AI to build the UI (`frontend-ui`).
4. Run validation (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Landing Page Strategist, Copywriter, Frontend Specialist).

## How to validate
For a Landing Page pack, validation usually means:
- Responsiveness checks (ensure it looks good on mobile).
- Accessibility checks (contrast, alt tags).
- Build checks (`npm run build`).

## Common Mistakes
- Building the UI before the copy is finalized.
- Ignoring mobile responsiveness.
- Forgetting SEO meta tags.
