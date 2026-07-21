"""
Intrinsic Valuation Engine

Runs DCF valuation
Runs Graham valuation
Runs PE valuation

Stores results into SQLite
"""

import sqlite3
import pandas as pd

from src.valuation.dcf import discounted_cash_flow
from src.valuation.graham import graham_intrinsic_value
from src.valuation.fair_value import average_intrinsic_value
from src.valuation.pe import pe_based_price

DB_PATH = "database/n100.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    ratios = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn,
    )

    return conn, ratios


def calculate(df):

    print("=" * 80)
    print("Calculating Intrinsic Values")
    print("=" * 80)

    # -------------------------------------------------
    # DCF Value
    # -------------------------------------------------
    df["dcf_value"] = df["free_cash_flow_cr"].apply(
        lambda x: discounted_cash_flow(x)
        if pd.notna(x) else None
    )

    # -------------------------------------------------
    # Graham Value
    # -------------------------------------------------
    df["graham_value"] = df.apply(
        lambda x: graham_intrinsic_value(
            x["earnings_per_share"],
            x["book_value_per_share"],
        ),
        axis=1,
    )

    # -------------------------------------------------
    # PE Value
    # -------------------------------------------------
    df["pe_target"] = df["earnings_per_share"].apply(
        lambda x: pe_based_price(x)
        if pd.notna(x) else None
    )

    # -------------------------------------------------
    # Final Fair Value
    # -------------------------------------------------
    df["fair_value"] = df.apply(
        lambda x: average_intrinsic_value(
            x["dcf_value"],
            x["graham_value"],
            x["pe_target"],
        ),
        axis=1,
    )

    return df


def save(conn, df):

    final = df[
        [
            "company_id",
            "year",
            "dcf_value",
            "graham_value",
            "pe_target",
            "fair_value",
        ]
    ]

    final.to_sql(
        "intrinsic_values",
        conn,
        if_exists="replace",
        index=False,
    )

    print("=" * 80)
    print("INTRINSIC VALUES GENERATED")
    print("=" * 80)
    print(final.head())

    conn.close()


def main():

    conn, df = load_data()

    df = calculate(df)

    save(conn, df)


if __name__ == "__main__":
    main()