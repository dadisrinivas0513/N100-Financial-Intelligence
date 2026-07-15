"""
capital_allocation.py

Sprint 2
Day 11

Capital Allocation Pattern Generator
"""

import sqlite3
import pandas as pd

DB = "database/n100.db"

conn = sqlite3.connect(DB)

cashflow = pd.read_sql(
    "SELECT * FROM cashflow",
    conn
)

conn.close()


def sign(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"


def classify(cfo, cfi, cff):

    pattern = (cfo, cfi, cff)

    mapping = {

        ("+", "-", "-"): "Reinvestor",

        ("+", "+", "-"): "Liquidating Assets",

        ("-", "+", "+"): "Distress Signal",

        ("-", "-", "+"): "Growth Funded by Debt",

        ("+", "+", "+"): "Cash Accumulator",

        ("-", "-", "-"): "Pre-Revenue",

        ("+", "-", "+"): "Mixed",

        ("0", "0", "0"): "Inactive"

    }

    return mapping.get(pattern, "Other")


cashflow["cfo_sign"] = cashflow["operating_activity"].apply(sign)

cashflow["cfi_sign"] = cashflow["investing_activity"].apply(sign)

cashflow["cff_sign"] = cashflow["financing_activity"].apply(sign)

cashflow["pattern_label"] = cashflow.apply(

    lambda x: classify(

        x["cfo_sign"],

        x["cfi_sign"],

        x["cff_sign"]

    ),

    axis=1

)

output = cashflow[

    [

        "company_id",

        "year",

        "cfo_sign",

        "cfi_sign",

        "cff_sign",

        "pattern_label"

    ]

]

output.to_csv(

    "output/capital_allocation.csv",

    index=False

)

print("=" * 70)
print("CAPITAL ALLOCATION GENERATED")
print("=" * 70)

print("Rows :", len(output))

print("\nSample")

print(output.head())