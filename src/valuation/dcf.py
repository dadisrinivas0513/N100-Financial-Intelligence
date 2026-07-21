"""
dcf.py

Discounted Cash Flow Calculator
"""


def discounted_cash_flow(
    free_cash_flow,
    growth_rate=0.12,
    discount_rate=0.10,
    terminal_growth=0.04,
    years=5,
):
    """
    Returns estimated intrinsic value.
    """

    if free_cash_flow is None:
        return None

    if free_cash_flow <= 0:
        return None

    value = 0

    current_fcf = free_cash_flow

    for year in range(1, years + 1):

        current_fcf *= (1 + growth_rate)

        value += current_fcf / ((1 + discount_rate) ** year)

    terminal_value = (
        current_fcf
        * (1 + terminal_growth)
        / (discount_rate - terminal_growth)
    )

    terminal_value /= ((1 + discount_rate) ** years)

    value += terminal_value

    return round(value, 2)