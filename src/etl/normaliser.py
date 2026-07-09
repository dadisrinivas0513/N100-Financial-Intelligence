"""
normaliser.py

Contains helper functions to clean data before loading into SQLite.
"""

import re
import pandas as pd


def normalize_year(year):
    """
    Convert year into integer.

    Examples:
    "2024" -> 2024
    2024 -> 2024
    2024.0 -> 2024
    """

    if pd.isna(year):
        return None

    try:
        return int(float(year))
    except:
        return None


def normalize_ticker(ticker):
    """
    Standardize stock ticker.

    Examples:
    " tcs " -> "TCS"
    " Reliance " -> "RELIANCE"
    """

    if pd.isna(ticker):
        return None

    ticker = str(ticker)

    ticker = ticker.strip()

    ticker = ticker.upper()

    ticker = re.sub(r"\s+", "", ticker)

    return ticker