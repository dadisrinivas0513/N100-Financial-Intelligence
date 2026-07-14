"""
inspect_datasets.py

Inspects all Excel datasets and prints:
- File name
- Rows
- Columns
- Column names
- Missing values
- First 3 rows

Sprint 1 - Day 3
"""

from pathlib import Path
import pandas as pd

RAW_FOLDER = Path("data/raw")

print("=" * 90)
print("N100 Financial Intelligence - Dataset Inspector")
print("=" * 90)

for file in sorted(RAW_FOLDER.glob("*.xlsx")):

    print("\n" + "=" * 90)
    print(file.name)
    print("=" * 90)

    try:
        df = pd.read_excel(file, header=1)

        print(f"Rows    : {len(df)}")
        print(f"Columns : {len(df.columns)}")

        print("\nCOLUMN NAMES")
        print("-" * 40)

        for col in df.columns:
            print(col)

        print("\nMISSING VALUES")
        print("-" * 40)

        print(df.isna().sum())

        print("\nFIRST 3 ROWS")
        print("-" * 40)

        print(df.head(3))

    except Exception as e:

        print("ERROR")
        print(e)

print("\n" + "=" * 90)
print("Inspection Completed")
print("=" * 90)