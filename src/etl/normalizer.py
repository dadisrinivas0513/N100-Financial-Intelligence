"""
normalizer.py

Universal data normalization utilities for
N100 Financial Intelligence Platform.
"""

import re
import pandas as pd


# ==========================================================
# Normalize Company ID
# ==========================================================

def normalize_company_id(value):
    """
    Convert company id into a standard format.

    Example:
        abb
        ABB
        ABB.NS

    becomes

        ABB
    """

    if pd.isna(value):
        return None

    value = str(value).upper().strip()

    value = value.replace(".NS", "")

    value = value.replace(".BO", "")

    value = value.replace(" ", "")

    return value


# ==========================================================
# Normalize Year
# ==========================================================

def normalize_year(value):
    """
    Converts

    Dec 2012
    Mar-2014
    FY2018
    2019

    into

    2012
    2014
    2018
    2019
    """

    if pd.isna(value):
        return None

    value = str(value)

    match = re.search(r"\d{4}", value)

    if match:

        return int(match.group())

    return None


# ==========================================================
# Normalize Date
# ==========================================================

def normalize_date(value):

    if pd.isna(value):
        return None

    try:

        return pd.to_datetime(value)

    except:

        return None


# ==========================================================
# Normalize Text
# ==========================================================

def normalize_text(value):

    if pd.isna(value):
        return None

    value = str(value)

    value = value.strip()

    value = " ".join(value.split())

    return value


# ==========================================================
# Normalize Numeric
# ==========================================================

def normalize_numeric(value):

    if pd.isna(value):
        return None

    if isinstance(value, str):

        value = value.replace(",", "")

        value = value.replace("%", "")

        value = value.strip()

    try:

        return float(value)

    except:

        return None


# ==========================================================
# Normalize Boolean
# ==========================================================

def normalize_boolean(value):

    if pd.isna(value):
        return False

    value = str(value).strip().lower()

    return value in [
        "true",
        "yes",
        "1",
        "y"
    ]