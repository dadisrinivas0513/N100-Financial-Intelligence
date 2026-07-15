"""
ratios.py

Sprint 2
Financial Ratio Engine

Contains profitability ratio calculations.
"""

from typing import Optional


def net_profit_margin(net_profit: float, sales: float) -> Optional[float]:
    """
    Net Profit Margin %

    Formula:
    Net Profit / Sales × 100
    """

    if sales == 0:
        return None

    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit: float, sales: float) -> Optional[float]:
    """
    Operating Profit Margin %

    Formula:
    Operating Profit / Sales × 100
    """

    if sales == 0:
        return None

    return round((operating_profit / sales) * 100, 2)


def return_on_equity(
    net_profit: float,
    equity_capital: float,
    reserves: float
) -> Optional[float]:
    """
    Return on Equity (ROE)

    Formula:
    Net Profit / (Equity + Reserves) ×100
    """

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


def return_on_assets(
    net_profit: float,
    total_assets: float
) -> Optional[float]:
    """
    Return on Assets (ROA)

    Formula:
    Net Profit / Total Assets ×100
    """

    if total_assets == 0:
        return None

    return round((net_profit / total_assets) * 100, 2)


def return_on_capital_employed(
    ebit: float,
    equity_capital: float,
    reserves: float,
    borrowings: float
) -> Optional[float]:
    """
    Return on Capital Employed (ROCE)

    Formula:
    EBIT /
    (Equity + Reserves + Borrowings)
    ×100
    """

    capital = equity_capital + reserves + borrowings

    if capital <= 0:
        return None

    return round((ebit / capital) * 100, 2)


def compare_opm(
    calculated_opm: float,
    source_opm: float
) -> bool:
    """
    Cross-check Operating Margin.

    Returns True if mismatch >1%.
    """

    return abs(calculated_opm - source_opm) > 1
# ============================================================
# DAY 09
# LEVERAGE & EFFICIENCY RATIOS
# ============================================================

def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt to Equity Ratio

    borrowings / (equity + reserves)

    Rule:
    Debt free company returns 0
    """

    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round(borrowings / equity, 2)


def high_leverage_flag(de_ratio, broad_sector):
    """
    High leverage warning

    Financial companies are exempt.
    """

    if de_ratio is None:
        return False

    if broad_sector == "Financials":
        return False

    return de_ratio > 5


def interest_coverage_ratio(
    operating_profit,
    other_income,
    interest
):
    """
    Interest Coverage Ratio

    (Operating Profit + Other Income)
    -------------------------------
            Interest
    """

    if interest == 0:
        return None

    return round(
        (operating_profit + other_income) / interest,
        2
    )


def icr_label(icr):

    if icr is None:
        return "Debt Free"

    return ""


def icr_warning_flag(icr):

    if icr is None:
        return False

    return icr < 1.5


def net_debt(
    borrowings,
    investments
):
    """
    Net Debt

    Borrowings - Investments
    """

    return round(
        borrowings - investments,
        2
    )


def asset_turnover(
    sales,
    total_assets
):
    """
    Asset Turnover

    Sales / Total Assets
    """

    if total_assets == 0:
        return None

    return round(
        sales / total_assets,
        2
    )