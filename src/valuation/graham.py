"""
graham.py

Benjamin Graham Intrinsic Value Formula
"""

import math


def graham_intrinsic_value(eps, book_value):
    """
    Graham Intrinsic Value

    Formula:
        sqrt(22.5 × EPS × Book Value)

    Returns
    -------
    float | None
    """

    if eps is None or book_value is None:
        return None

    if eps <= 0:
        return None

    if book_value <= 0:
        return None

    value = math.sqrt(22.5 * eps * book_value)

    return round(value, 2)