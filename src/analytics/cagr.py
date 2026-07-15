"""
cagr.py

Compound Annual Growth Rate (CAGR) Engine
Sprint 2 – Day 10
"""

from math import pow


# ==========================================================
# CAGR FLAGS
# ==========================================================

NORMAL = "NORMAL"
DECLINE_TO_LOSS = "DECLINE_TO_LOSS"
TURNAROUND = "TURNAROUND"
BOTH_NEGATIVE = "BOTH_NEGATIVE"
ZERO_BASE = "ZERO_BASE"
INSUFFICIENT = "INSUFFICIENT"


# ==========================================================
# CAGR FUNCTION
# ==========================================================

def calculate_cagr(start_value, end_value, years):
    """
    CAGR Formula

    ((End / Start)^(1 / Years) - 1) * 100

    Returns
    -------
    tuple
        (value, flag)
    """

    # -------------------------
    # Insufficient history
    # -------------------------

    if years <= 0:
        return None, INSUFFICIENT

    # -------------------------
    # Zero Base
    # -------------------------

    if start_value == 0:
        return None, ZERO_BASE

    # -------------------------
    # Positive -> Positive
    # -------------------------

    if start_value > 0 and end_value > 0:

        value = (
            pow(end_value / start_value, 1 / years) - 1
        ) * 100

        return round(value, 2), NORMAL

    # -------------------------
    # Positive -> Negative
    # -------------------------

    if start_value > 0 and end_value < 0:
        return None, DECLINE_TO_LOSS

    # -------------------------
    # Negative -> Positive
    # -------------------------

    if start_value < 0 and end_value > 0:
        return None, TURNAROUND

    # -------------------------
    # Negative -> Negative
    # -------------------------

    if start_value < 0 and end_value < 0:
        return None, BOTH_NEGATIVE

    return None, INSUFFICIENT


# ==========================================================
# Helper Wrappers
# ==========================================================

def revenue_cagr(start, end, years):
    return calculate_cagr(start, end, years)


def pat_cagr(start, end, years):
    return calculate_cagr(start, end, years)


def eps_cagr(start, end, years):
    return calculate_cagr(start, end, years)