# Data & BI Pack: Usage

## How to use this pack
1. Determine if you are defining requirements or processing data.
2. Select this pack in your prompt to inform the Orchestrator.
3. Select a primary workflow (e.g., `document` or `automation`).
4. Specify your data sources and constraints.

## Recommended Prompt Structure
- **Context:** Brief intro to the business need.
- **Goal:** Description of the output.
- **Pack:** `data-bi-pack`.
- **Workflow:** The chosen workflow.
- **Scope:** Which folders are allowed (e.g., `scripts/` or `docs/`).
- **Validation:** What data integrity checks to run.

## Step-by-Step Usage
1. Ask the AI to `plan` the BI requirements.
2. Review the proposed KPIs and metrics.
3. Instruct the AI to write the processing script (`automation`).
4. Run validation on a sample dataset (`verify`).

## How to use with Antigravity
Include the pack reference in your initial prompt. Antigravity will map this pack to its internal context and pre-load the necessary agent personas (Business Analyst, Python Automation Specialist).

## How to validate
For a Data & BI pack, validation usually means:
- Reviewing the generated Markdown documentation.
- Running the generated Python script against a small, safe CSV file.
- Confirming the output matches the expected deduplication and cleaning rules.

## Common Mistakes
- Processing PII (Personally Identifiable Information) without anonymization.
- Running untested scripts against production databases.
- Skipping the KPI definition phase before writing code.
