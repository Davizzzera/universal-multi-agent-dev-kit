# Data & BI Pack: Example Prompt

**Copy and paste the following into Antigravity:**

```text
Goal: Create a Python script to ingest, clean, and deduplicate sales data from a CSV file.
Pack: `data-bi-pack`
Workflow: `automation`

Scope: `scripts/data_processing/` and `data/samples/`.
Instructions:
1. Use the Business Analyst to define the cleaning rules based on standard KPI needs.
2. Use the Python Automation Specialist to write the script using pandas.
3. Ensure the script logs errors but does not crash on malformed rows.
4. Use the Data Quality Specialist to define the validation checks.
Validation: Run the script against `data/samples/test_sales.csv` and show the output summary.
Commit: Do not commit until I review the validation output.

Language Rule: Answer me in Brazilian Portuguese, but write repository files in English.
```
