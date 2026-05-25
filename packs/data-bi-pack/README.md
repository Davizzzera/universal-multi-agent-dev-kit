# Data & BI Pack

> A preset for data processing, CSV/Excel ingestion, data cleaning, BI requirements, dashboards, KPI definitions and reporting automation.

## Pack Overview
This pack curates the optimal configuration of agents, skills, and workflows to build reliable data pipelines, clean messy data, define business metrics, and automate reporting without the overhead of full application stacks.

## When to use this pack
- Data cleaning
- CSV/Excel processing
- KPI definitions
- BI documentation
- Dashboard requirements
- Reporting automation
- Data quality analysis

## When NOT to use this pack
- UI-only projects
- Complex authentication systems
- Pure marketing landing pages

## Recommended Agents
This pack utilizes business analysts, data quality specialists, and python automation specialists. See `agents.md` for the full list.

## Recommended Skills
This pack relies heavily on data cleaning, KPI definition, and business context extraction. See `skills.md` for the full list.

## Recommended Workflows
This pack uses workflows tailored to data processing, such as `automation` and `document`. See `workflows.md` for the full list.

## Validation Expectations
Data integrity checks are paramount. Output must be validated against expected formats and deduplication rules.

## Safety and Scope Notes
- Do not perform destructive operations on production data. Always test data cleaning on safe subsets.
- Ensure the `scope-guardian` restricts edits to scripts, reports, and data directories.

## Example Use Cases
- "Write a Python script to ingest, clean, and merge three different CSV files."
- "Define the KPIs and write the requirements for the new Sales Dashboard."

## Related Packs
- `automation-pack`
