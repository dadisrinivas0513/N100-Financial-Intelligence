"""
loader.py

Loads all Excel datasets from data/raw
for the N100 Financial Intelligence Platform.
"""

from pathlib import Path
import pandas as pd

from normaliser import normalize_year, normalize_ticker

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Raw data folder
RAW_FOLDER = PROJECT_ROOT / "data" / "raw"

# Dictionary to store DataFrames
datasets = {}

print("=" * 60)
print("N100 Financial Intelligence - ETL Loader")
print("=" * 60)

# Read every Excel file
for file in RAW_FOLDER.glob("*.xlsx"):

    print(f"\nLoading: {file.name}")

    try:
        df = pd.read_excel(file, header=1)

        # Normalize columns if present
        if "id" in df.columns:
            df["id"] = df["id"].apply(normalize_ticker)

        if "ticker" in df.columns:
            df["ticker"] = df["ticker"].apply(normalize_ticker)

        if "year" in df.columns:
            df["year"] = df["year"].apply(normalize_year)

        datasets[file.stem] = df

        print(f"Rows    : {len(df)}")
        print(f"Columns : {len(df.columns)}")
        print("Status  : Loaded Successfully")

    except Exception as e:
        print(f"Error loading {file.name}")
        print(e)

print("\n" + "=" * 60)
print("Summary")
print("=" * 60)

print(f"Datasets Loaded : {len(datasets)}")

for name, df in datasets.items():
    print(f"{name:<22} {df.shape}")

print("=" * 60)