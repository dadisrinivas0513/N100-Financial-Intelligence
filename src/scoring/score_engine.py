"""
score_engine.py

Sprint 4

AI Stock Scoring Engine

Reads:
    financial_ratios
    intrinsic_values

Creates:
    stock_scores
"""

import sqlite3
import pandas as pd

from src.scoring.ranking import (
    score_profitability,
    score_growth,
    score_debt,
    score_valuation,
)

from src.scoring.recommendation import (
    recommendation,
)

DB_PATH = "database/n100.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    ratios = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn,
    )

    intrinsic = pd.read_sql(
        "SELECT * FROM intrinsic_values",
        conn,
    )

    df = ratios.merge(
        intrinsic,
        on=["company_id", "year"],
        how="left",
    )

    return conn, df


def calculate_scores(df):

    print("=" * 80)
    print("Generating AI Scores")
    print("=" * 80)

    # -----------------------------
    # Profitability
    # -----------------------------

    df["profitability_score"] = df[
        "return_on_equity_pct"
    ].apply(score_profitability)

    # -----------------------------
    # Growth
    # -----------------------------

    df["growth_score"] = df[
        "revenue_cagr_5yr"
    ].apply(score_growth)

    # -----------------------------
    # Debt
    # -----------------------------

    df["debt_score"] = df[
        "debt_to_equity"
    ].apply(score_debt)

    # -----------------------------
    # Valuation Discount
    # -----------------------------

    def valuation_discount(row):

        fair = row["fair_value"]

        eps = row["earnings_per_share"]

        if pd.isna(fair):
            return None

        if pd.isna(eps):
            return None

        market_price = eps * 20

        if market_price <= 0:
            return None

        return (
            (fair - market_price)
            / market_price
            * 100
        )

    df["discount_percent"] = df.apply(
        valuation_discount,
        axis=1,
    )

    df["valuation_score"] = df[
        "discount_percent"
    ].apply(score_valuation)

    # -----------------------------
    # Overall Score
    # -----------------------------

    df["overall_score"] = (
        df["profitability_score"]
        + df["growth_score"]
        + df["debt_score"]
        + df["valuation_score"]
    ) / 4

    df["overall_score"] = df["overall_score"].round(2)

    # -----------------------------
    # Recommendation
    # -----------------------------

    df["recommendation"] = df[
        "overall_score"
    ].apply(recommendation)

    return df


def save(conn, df):

    final = df[
        [
            "company_id",
            "year",
            "profitability_score",
            "growth_score",
            "debt_score",
            "valuation_score",
            "overall_score",
            "recommendation",
        ]
    ]

    final.to_sql(
        "stock_scores",
        conn,
        if_exists="replace",
        index=False,
    )

    print("=" * 80)
    print("AI STOCK SCORES GENERATED")
    print("=" * 80)
    print(final.head())

    conn.close()


def main():

    conn, df = load_data()

    df = calculate_scores(df)

    save(conn, df)


if __name__ == "__main__":
    main()