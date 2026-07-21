"""
ratio_engine.py

Sprint 2
Financial Ratio Engine

Computes all KPI values and populates financial_ratios table.
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

from src.analytics.cagr import (
    calculate_cagr,
)

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion,
)


DB_PATH = "database/n100.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    pnl = pd.read_sql(
        "SELECT * FROM profitandloss",
        conn
    ).drop(columns=["id"])

    bs = pd.read_sql(
        "SELECT * FROM balancesheet",
        conn
    ).drop(columns=["id"])

    cf = pd.read_sql(
        "SELECT * FROM cashflow",
        conn
    ).drop(columns=["id"])

    companies = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    df = pnl.merge(
        bs,
        on=["company_id", "year"],
        how="left",
    )

    df = df.merge(
        cf,
        on=["company_id", "year"],
        how="left",
    )

    companies = companies.rename(columns={"id": "company_id"})

    df = df.merge(
        companies,
        on="company_id",
        how="left",
    )

    return conn, df

def compute_ratios(df):

    print("=" * 80)
    print("Computing Financial Ratios")
    print("=" * 80)

    # ----------------------------------------------------
    # Profitability Ratios
    # ----------------------------------------------------

    df["net_profit_margin_pct"] = df.apply(
        lambda x: net_profit_margin(
            x["net_profit"],
            x["sales"],
        ),
        axis=1,
    )

    df["operating_profit_margin_pct"] = df.apply(
        lambda x: operating_profit_margin(
            x["operating_profit"],
            x["sales"],
        ),
        axis=1,
    )

    df["return_on_equity_pct"] = df.apply(
        lambda x: return_on_equity(
            x["net_profit"],
            x["equity_capital"],
            x["reserves"],
        ),
        axis=1,
    )

    df["return_on_capital_employed_pct"] = df.apply(
        lambda x: return_on_capital_employed(
            x["operating_profit"],
            x["equity_capital"],
            x["reserves"],
            x["borrowings"],
        ),
        axis=1,
    )

    df["return_on_assets_pct"] = df.apply(
        lambda x: return_on_assets(
            x["net_profit"],
            x["total_assets"],
        ),
        axis=1,
    )

    # ----------------------------------------------------
    # Leverage Ratios
    # ----------------------------------------------------

    df["debt_to_equity"] = df.apply(
        lambda x: debt_to_equity(
            x["borrowings"],
            x["equity_capital"],
            x["reserves"],
        ),
        axis=1,
    )

    df["interest_coverage"] = df.apply(
        lambda x: interest_coverage_ratio(
            x["operating_profit"],
            x["other_income"],
            x["interest"],
        ),
        axis=1,
    )

    df["asset_turnover"] = df.apply(
        lambda x: asset_turnover(
            x["sales"],
            x["total_assets"],
        ),
        axis=1,
    )

    # ----------------------------------------------------
    # Cash Flow KPIs
    # ----------------------------------------------------

    df["free_cash_flow_cr"] = df.apply(
        lambda x: free_cash_flow(
            x["operating_activity"],
            x["investing_activity"],
        ),
        axis=1,
    )

    df["capex_cr"] = df["investing_activity"].abs()

    df["cash_from_operations_cr"] = df["operating_activity"]

    df["total_debt_cr"] = df["borrowings"]

    df["earnings_per_share"] = df["eps"]

    df["book_value_per_share"] = df["book_value"]

    df["dividend_payout_ratio_pct"] = df["dividend_payout"]

    # ----------------------------------------------------
    # Quality Scores
    # ----------------------------------------------------

    df["cfo_quality_score"] = 1.0

    df["fcf_conversion_rate"] = df.apply(
        lambda x: fcf_conversion(
            x["free_cash_flow_cr"],
            x["operating_profit"],
        ),
        axis=1,
    )
        # ----------------------------------------------------
    # CapEx Intensity
    # ----------------------------------------------------

    def get_capex_value(row):

        result = capex_intensity(
            row["investing_activity"],
            row["sales"],
        )

        if result is None:
            return pd.Series([None, None])

        return pd.Series(result)

    df[
        [
            "capex_intensity_pct",
            "capex_label",
        ]
    ] = df.apply(
        get_capex_value,
        axis=1,
    )

    # ----------------------------------------------------
    # CAGR Columns
    # ----------------------------------------------------

    df = df.sort_values(
        ["company_id", "year"]
    ).reset_index(drop=True)

    df["revenue_cagr_5yr"] = None
    df["pat_cagr_5yr"] = None
    df["eps_cagr_5yr"] = None

    for company in df["company_id"].unique():

        idx = df[df["company_id"] == company].index.tolist()

        if len(idx) < 6:
            continue

        for i in range(5, len(idx)):

            current = idx[i]
            previous = idx[i - 5]

            value, _ = calculate_cagr(
                df.loc[previous, "sales"],
                df.loc[current, "sales"],
                5,
            )
            df.loc[current, "revenue_cagr_5yr"] = value

            value, _ = calculate_cagr(
                df.loc[previous, "net_profit"],
                df.loc[current, "net_profit"],
                5,
            )
            df.loc[current, "pat_cagr_5yr"] = value

            value, _ = calculate_cagr(
                df.loc[previous, "eps"],
                df.loc[current, "eps"],
                5,
            )
            df.loc[current, "eps_cagr_5yr"] = value

    return df

def save_to_database(conn, df):

    final_df = df[
        [
            "company_id",
            "year",
            "net_profit_margin_pct",
            "operating_profit_margin_pct",
            "return_on_equity_pct",
            "return_on_capital_employed_pct",
            "return_on_assets_pct",
            "debt_to_equity",
            "interest_coverage",
            "asset_turnover",
            "free_cash_flow_cr",
            "capex_cr",
            "earnings_per_share",
            "book_value_per_share",
            "dividend_payout_ratio_pct",
            "total_debt_cr",
            "cash_from_operations_cr",
            "cfo_quality_score",
            "fcf_conversion_rate",
            "capex_intensity_pct",
            "revenue_cagr_5yr",
            "pat_cagr_5yr",
            "eps_cagr_5yr",
        ]
    ]

    final_df.to_sql(
        "financial_ratios",
        conn,
        if_exists="replace",
        index=False,
    )

    print("=" * 80)
    print("FINANCIAL RATIOS TABLE UPDATED")
    print("=" * 80)
    print(f"Rows Written : {len(final_df)}")
    print(f"Columns      : {len(final_df.columns)}")

    conn.close()


def main():

    conn, df = load_data()

    df = compute_ratios(df)

    save_to_database(conn, df)

if __name__ == "__main__":
    main()