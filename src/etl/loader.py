"""
loader.py

Universal ETL Loader
"""

from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_FOLDER = PROJECT_ROOT / "data" / "raw"

DB_PATH = PROJECT_ROOT / "database" / "n100.db"


# =====================================================
# Universal Excel Reader
# =====================================================

def load_excel(file_path):

    file_path = Path(file_path)

    if file_path.stem == "companies":
        df = pd.read_excel(file_path, header=1)

    else:

        df = pd.read_excel(file_path)

        if (
            "Unnamed: 1" in df.columns
            or str(df.columns[0]).startswith("Bluestock")
        ):
            df = pd.read_excel(file_path, header=1)

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


# =====================================================
# Build SQLite Database
# =====================================================

def build_database():

    print("=" * 80)
    print("N100 Financial Intelligence")
    print("ETL Loader")
    print("=" * 80)

    conn = sqlite3.connect(DB_PATH)

    loaded_tables = []

    for file in sorted(RAW_FOLDER.glob("*.xlsx")):

        print(f"\nLoading {file.name}")

        try:

            df = load_excel(file)

            table = file.stem.lower()

            df.to_sql(
                table,
                conn,
                if_exists="replace",
                index=False
            )

            loaded_tables.append(table)

            print(f"Rows   : {len(df)}")
            print(f"Cols   : {len(df.columns)}")
            print("Status : Loaded")

        except Exception as e:

            print("FAILED")
            print(e)

    conn.commit()
    conn.close()

    print("\n" + "=" * 80)
    print("DATABASE CREATED")
    print("=" * 80)

    print(f"Database : {DB_PATH}")

    print("\nTables Loaded")

    for table in loaded_tables:
        print("✓", table)

    print("=" * 80)


if __name__ == "__main__":
    build_database()