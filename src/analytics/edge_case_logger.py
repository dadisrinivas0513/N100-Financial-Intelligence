"""
edge_case_logger.py

Logs ratio anomalies for manual review.
"""

import sqlite3

DB_PATH = "database/n100.db"


def generate_edge_case_log():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    rows = []

    cur.execute("""
    SELECT
    fr.company_id,
    fr.year,
    fr.return_on_equity_pct,
    c.roe_percentage,
    fr.return_on_capital_employed_pct,
    c.roce_percentage
    FROM financial_ratios fr
    JOIN companies c
    ON fr.company_id = c.id
    """)

    for row in cur.fetchall():

        company = row[0]
        year = row[1]

        roe_calc = row[2]
        roe_source = row[3]

        roce_calc = row[4]
        roce_source = row[5]

        if (
            roe_calc is not None
            and roe_source is not None
            and abs(roe_calc - roe_source) > 5
        ):
            rows.append(
    f"""
============================================================
Company  : {company}
Year     : {year}

Metric   : ROE

Calculated Value : {roe_calc}
Source Value     : {roe_source}

Difference : {round(abs(roe_calc-roe_source),2)}

Category   : Source Data Issue

Explanation:
Computed ROE differs from companies.xlsx.
Ratio Engine calculation retained.
Source value kept for reference.

------------------------------------------------------------
"""
)
        if (
            roce_calc is not None
            and roce_source is not None
            and abs(roce_calc - roce_source) > 5
        ):
            rows.append(
    f"""
============================================================
Company  : {company}
Year     : {year}

Metric   : ROCE

Calculated Value : {roce_calc}
Source Value     : {roce_source}

Difference : {round(abs(roce_calc-roce_source),2)}

Category   : Version Difference

Explanation:
Calculated ROCE differs from the source file.
Likely due to reporting-period or formula differences.

------------------------------------------------------------
"""
)

    conn.close()

    with open(
        "output/ratio_edge_cases.log",
        "w",
        encoding="utf-8",
    ) as f:

        for line in rows:
            f.write(line + "\n")

    print("=" * 80)
    print("EDGE CASE LOG GENERATED")
    print("=" * 80)
    print("Total Issues :", len(rows))


if __name__ == "__main__":
    generate_edge_case_log()