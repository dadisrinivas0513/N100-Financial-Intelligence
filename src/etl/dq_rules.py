"""
dq_rules.py

Contains all Data Quality Rules.

Currently:
DQ-01
DQ-02
DQ-03
DQ-04
DQ-05
DQ-06
"""

import pandas as pd


def log(rule, severity, dataset, row, message):
    return {
        "Rule": rule,
        "Severity": severity,
        "Dataset": dataset,
        "Row": row,
        "Message": message,
    }


# ==========================================================
# DQ-01
# Company ID uniqueness
# ==========================================================

def dq01(companies):

    failures = []

    duplicates = companies[
        companies["id"].duplicated(keep=False)
    ]

    for idx, row in duplicates.iterrows():

        failures.append(
            log(
                "DQ-01",
                "CRITICAL",
                "companies",
                idx + 2,
                f"Duplicate Company ID : {row['id']}"
            )
        )

    return failures


# ==========================================================
# DQ-02
# Duplicate Company-Year
# ==========================================================

def dq02(profit):

    failures = []

    profit = profit.copy()

    profit["year"] = (
        profit["year"]
        .astype(str)
        .str.extract(r"(\d{4})")[0]
    )

    duplicates = profit[
        profit.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    for idx, row in duplicates.iterrows():

        failures.append(
            log(
                "DQ-02",
                "CRITICAL",
                "profitandloss",
                idx + 2,
                f"{row['company_id']} {row['year']}"
            )
        )

    return failures


# ==========================================================
# DQ-03
# Foreign Key Validation
# ==========================================================

def dq03(companies, profit):

    failures = []

    valid_ids = set(companies["id"])

    for idx, row in profit.iterrows():

        if row["company_id"] not in valid_ids:

            failures.append(
                log(
                    "DQ-03",
                    "CRITICAL",
                    "profitandloss",
                    idx + 2,
                    f"Unknown Company : {row['company_id']}"
                )
            )

    return failures


# ==========================================================
# DQ-04
# Balance Sheet Equation
# ==========================================================

def dq04(balance):

    failures = []

    balance = balance.copy()

    balance["difference"] = (
        balance["total_assets"] -
        balance["total_liabilities"]
    ).abs()

    for idx, row in balance.iterrows():

        if row["difference"] > 1:

            failures.append(
                log(
                    "DQ-04",
                    "WARNING",
                    "balancesheet",
                    idx + 2,
                    f"{row['company_id']} Difference={row['difference']}"
                )
            )

    return failures


# ==========================================================
# DQ-05
# Operating Profit Margin
# ==========================================================

def dq05(profit):

    failures = []

    for idx, row in profit.iterrows():

        if pd.isna(row["operating_profit"]):
            continue

        if row["sales"] == 0:
            continue

        if pd.isna(row["opm_percentage"]):
            continue

        calculated = round(
            row["operating_profit"] /
            row["sales"] * 100,
            2
        )

        if abs(calculated - row["opm_percentage"]) > 1:

            failures.append(
                log(
                    "DQ-05",
                    "WARNING",
                    "profitandloss",
                    idx + 2,
                    f"{row['company_id']} OPM mismatch"
                )
            )

    return failures


# ==========================================================
# DQ-06
# Positive Sales
# ==========================================================

def dq06(profit):

    failures = []

    invalid = profit[
        profit["sales"] <= 0
    ]

    for idx, row in invalid.iterrows():

        failures.append(
            log(
                "DQ-06",
                "CRITICAL",
                "profitandloss",
                idx + 2,
                f"{row['company_id']} Negative Sales"
            )
        )

    return failures