"""
ranking.py

Functions to convert financial metrics
into normalized scores.
"""


def score_profitability(roe):
    if roe is None:
        return 0

    if roe >= 20:
        return 100

    if roe >= 15:
        return 80

    if roe >= 10:
        return 60

    if roe >= 5:
        return 40

    return 20


def score_growth(cagr):
    if cagr is None:
        return 0

    if cagr >= 25:
        return 100

    if cagr >= 15:
        return 80

    if cagr >= 10:
        return 60

    if cagr >= 5:
        return 40

    return 20


def score_debt(de_ratio):
    if de_ratio is None:
        return 0

    if de_ratio <= 0.30:
        return 100

    if de_ratio <= 0.60:
        return 80

    if de_ratio <= 1.00:
        return 60

    if de_ratio <= 2.00:
        return 40

    return 20


def score_valuation(discount_percent):
    if discount_percent is None:
        return 0

    if discount_percent >= 40:
        return 100

    if discount_percent >= 25:
        return 80

    if discount_percent >= 10:
        return 60

    if discount_percent >= 0:
        return 40

    return 20