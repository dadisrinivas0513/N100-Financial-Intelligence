"""
Sprint 2 - Day 11

Generate capital_allocation.csv
"""

import os
import sqlite3
import pandas as pd

from src.analytics.cashflow_kpis import capital_allocation_pattern

DB_PATH = "database/n100.db"

OUTPUT = "output/capital_allocation.csv"


def generate():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("""
    SELECT
        company_id,
        year,
        operating_activity,
        investing_activity,
        financing_activity
    FROM cashflow
    """, conn)

    conn.close()

    df["cfo_sign"] = df["operating_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    df["cfi_sign"] = df["investing_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    df["cff_sign"] = df["financing_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    df["pattern_label"] = df.apply(
        lambda x: capital_allocation_pattern(
            x["operating_activity"],
            x["investing_activity"],
            x["financing_activity"],
        ),
        axis=1,
    )

    os.makedirs("output", exist_ok=True)

    final = df[
        [
            "company_id",
            "year",
            "cfo_sign",
            "cfi_sign",
            "cff_sign",
            "pattern_label",
        ]
    ]

    final.to_csv(
        OUTPUT,
        index=False,
    )

    print("=" * 80)
    print("CAPITAL ALLOCATION FILE GENERATED")
    print("=" * 80)
    print(final.head())


if __name__ == "__main__":
    generate()