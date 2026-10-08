# Data Dictionary: `seo_metrics.db`

This document defines the schema architecture, structural constraints, and field definitions for the relational analytics database engine compiled in this pipeline.

---

## Table Schema: `keyword_analytics`

**Storage Engine:** SQLite3
**Description:** Stores cleaned, normalized organic search query parameters, traffic acquisition indexes, and custom-engineered performance metrics.

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY`, `AUTOINCREMENT` | Unique auto-generated tracking identifier for each individual keyword row log. |
| `keyword` | `TEXT` | `NOT NULL` | Cleaned, lowercased, and whitespace-stripped search term phrase. |
| `avg_monthly_searches` | `REAL` | None | Average search queries generated per month, normalized via median imputation for missing items. |
| `competition` | `REAL` | None | Indexed search market competitiveness score ranging granularly between `0.10` and `0.95`. |
| `est_clicks` | `INTEGER` | None | Total estimated raw traffic click actions recorded across the keyword cluster. |
| `click_through_efficiency` | `REAL` | Calculated Field | Engine-calculated efficiency metric measuring traffic pull performance against total search volume. |

---

## Field Engineering Formulas

### Click-Through Efficiency (CTE)
The `Click_through_efficiency` column is a custom business intelligence metric calculated during the data transformation pipeline phase using Vectorized Pandas array operations:
\[\text{CTE} = \text{round}\left(\left(\frac{\text{Est\_Clicks}}{\text{Avg\_Monthly\_Searches} + 1}\right) \times 100, \, 2\right)\]

*Note: A \(+1\) modifier is applied to the denominator constraint inside the source pipeline code logic to safeguard calculations from math breakdown due to zero-value tracking logs.*
