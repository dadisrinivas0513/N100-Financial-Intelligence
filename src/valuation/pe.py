"""
pe.py

PE Based Valuation
"""


def pe_based_price(eps, pe_ratio=20):
    """
    PE Based Fair Price

    Formula:
        Fair Price = EPS × PE Ratio

    Parameters
    ----------
    eps : float
    pe_ratio : float

    Returns
    -------
    float | None
    """

    if eps is None:
        return None

    if eps <= 0:
        return None

    return round(eps * pe_ratio, 2)