import sqlite3
import pandas as pd

DB_PATH = "database/n100.db"

conn = sqlite3.connect(DB_PATH)

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
]

for table in tables:

    print("=" * 70)
    print(table.upper())
    print("=" * 70)

    df = pd.read_sql(f"SELECT * FROM {table}", conn)

    before = len(df)

    df = df.drop_duplicates(
        subset=["company_id", "year"],
        keep="first",
    )

    after = len(df)

    print("Before :", before)
    print("After  :", after)
    print("Removed:", before - after)

    # Replace the table with cleaned data
    conn.execute(f"DROP TABLE IF EXISTS {table}")

    df.to_sql(
        table,
        conn,
        index=False,
        if_exists="replace",
    )

print("\n")
print("=" * 70)
print("DATABASE CLEANED SUCCESSFULLY")
print("=" * 70)

conn.close()