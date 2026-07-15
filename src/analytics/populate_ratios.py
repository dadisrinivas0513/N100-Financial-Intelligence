"""
populate_ratios.py

Sprint 2
Day 12

Loads financial datasets,
computes KPI values,
prepares final dataframe for SQLite.
"""

import sqlite3
import pandas as pd

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    capex_intensity,
    cfo_quality_score,
    fcf_conversion_rate,
)

from src.analytics.cagr import CAGR


DATABASE = "database/n100.db"


def load_tables():

    conn = sqlite3.connect(DATABASE)

    pnl = pd.read_sql(
        "SELECT * FROM profitandloss",
        conn
    )

    bs = pd.read_sql(
        "SELECT * FROM balancesheet",
        conn
    )

    cf = pd.read_sql(
        "SELECT * FROM cashflow",
        conn
    )

    companies = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    return pnl, bs, cf, companies


def merge_tables():

    pnl, bs, cf, companies = load_tables()

    df = pnl.merge(
        bs,
        on=["company_id", "year"],
        how="left"
    )

    df = df.merge(
        cf,
        on=["company_id", "year"],
        how="left"
    )

    df = df.merge(
        companies,
        left_on="company_id",
        right_on="id",
        how="left",
        suffixes=("", "_company")
    )

    return df


def calculate_ratios(df):

    df["net_profit_margin_pct"] = df.apply(
        lambda r: net_profit_margin(
            r["net_profit"],
            r["sales"]
        ),
        axis=1
    )

    df["operating_profit_margin_pct"] = df.apply(
        lambda r: operating_profit_margin(
            r["operating_profit"],
            r["sales"]
        ),
        axis=1
    )

    df["return_on_equity_pct"] = df.apply(
        lambda r: return_on_equity(
            r["net_profit"],
            r["equity_capital"],
            r["reserves"]
        ),
        axis=1
    )

    df["return_on_capital_employed_pct"] = df.apply(
        lambda r: return_on_capital_employed(
            r["operating_profit"],
            r["equity_capital"],
            r["reserves"],
            r["borrowings"]
        ),
        axis=1
    )

    df["return_on_assets_pct"] = df.apply(
        lambda r: return_on_assets(
            r["net_profit"],
            r["total_assets"]
        ),
        axis=1
    )

    df["debt_to_equity"] = df.apply(
        lambda r: debt_to_equity(
            r["borrowings"],
            r["equity_capital"],
            r["reserves"]
        ),
        axis=1
    )

    df["interest_coverage"] = df.apply(
        lambda r: interest_coverage_ratio(
            r["operating_profit"],
            r["other_income"],
            r["interest"]
        ),
        axis=1
    )

    df["asset_turnover"] = df.apply(
        lambda r: asset_turnover(
            r["sales"],
            r["total_assets"]
        ),
        axis=1
    )

    return df