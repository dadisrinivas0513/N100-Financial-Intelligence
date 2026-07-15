"""
edge_case_logger.py

Sprint 2
Day 13
"""

import sqlite3
import pandas as pd

DB = "database/n100.db"


conn = sqlite3.connect(DB)

companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

conn.close()


log = []


for _, company in companies.iterrows():

    cid = company["id"]

    source_roe = company["roe_percentage"]
    source_roce = company["roce_percentage"]

    company_ratio = ratios[
        ratios["company_id"] == cid
    ]

    if len(company_ratio) == 0:
        continue

    calc_roe = company_ratio[
        "return_on_equity_pct"
    ].mean()

    if abs(calc_roe - source_roe) > 5:

        log.append(
            f"{cid} | ROE | Source={source_roe} | Engine={round(calc_roe,2)}"
        )


with open(
    "output/ratio_edge_cases.log",
    "w",
    encoding="utf-8"
) as f:

    for line in log:
        f.write(line + "\n")


print("=" * 70)
print("EDGE CASE LOG GENERATED")
print("=" * 70)
print("Entries :", len(log))