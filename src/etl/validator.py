"""
validator.py

Main Data Quality Validator
Calls all DQ Rules and generates validation report.
"""

from pathlib import Path
import pandas as pd

from loader import load_excel, RAW_FOLDER
from dq_rules import (
    dq01,
    dq02,
    dq03,
    dq04,
    dq05,
    dq06,
)

# ======================================================
# Output Folder
# ======================================================

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

REPORT_FILE = OUTPUT_DIR / "validation_failures.csv"

# ======================================================
# Load Datasets
# ======================================================

companies = load_excel(RAW_FOLDER / "companies.xlsx")

profit = load_excel(RAW_FOLDER / "profitandloss.xlsx")

balancesheet = load_excel(RAW_FOLDER / "balancesheet.xlsx")

# ======================================================
# Execute Rules
# ======================================================

failures = []

failures.extend(dq01(companies))

failures.extend(dq02(profit))

failures.extend(dq03(companies, profit))

failures.extend(dq04(balancesheet))

failures.extend(dq05(profit))

failures.extend(dq06(profit))

# ======================================================
# Save Report
# ======================================================

report = pd.DataFrame(failures)

report.to_csv(REPORT_FILE, index=False)

print("\n" + "=" * 60)
print("VALIDATION COMPLETE")
print("=" * 60)

print(f"Total Rules Executed : 6")

print(f"Total Failures : {len(report)}")

print(f"\nReport Saved : {REPORT_FILE}")

if len(report):

    print("\nTop 10 Failures\n")

    print(report.head(10))