import sqlite3
import pandas as pd

conn = sqlite3.connect("database/n100.db")

print("=" * 80)
print("FINANCIAL_RATIOS TABLE")
print("=" * 80)

df = pd.read_sql("SELECT * FROM financial_ratios LIMIT 5", conn)

print("\nColumns:\n")
print(df.columns.tolist())

print("\nSample:\n")
print(df)

conn.close()