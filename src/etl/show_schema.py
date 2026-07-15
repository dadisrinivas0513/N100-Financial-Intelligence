import sqlite3
import pandas as pd

conn = sqlite3.connect("database/n100.db")

tables = [
    "profitandloss",
    "balancesheet",
    "cashflow",
    "companies"
]

for table in tables:
    print("\n" + "=" * 80)
    print(table.upper())
    print("=" * 80)

    df = pd.read_sql(f"SELECT * FROM {table} LIMIT 3", conn)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nSample:")
    print(df)

conn.close()