import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

import pytest

from src.etl.normalizer import normalize_year, normalize_ticker
# -------------------------
# normalize_year Tests
# -------------------------

@pytest.mark.parametrize(
    "input_year, expected",
    [
        ("2024", 2024),
        ("2023", 2023),
        (2022, 2022),
        (2021.0, 2021),
        ("2020", 2020),
        ("2019", 2019),
        ("2018", 2018),
        ("2017", 2017),
        ("2016", 2016),
        ("2015", 2015),
        ("2014", 2014),
        ("2013", 2013),
        ("2012", 2012),
        ("2011", 2011),
        ("2010", 2010),
        ("2009", 2009),
        ("2008", 2008),
        ("2007", 2007),
        ("2006", 2006),
        ("2005", 2005),
    ]
)
def test_normalize_year(input_year, expected):
    assert normalize_year(input_year) == expected


# -------------------------
# normalize_ticker Tests
# -------------------------

@pytest.mark.parametrize(
    "ticker, expected",
    [
        ("tcs", "TCS"),
        (" infy ", "INFY"),
        ("Reliance", "RELIANCE"),
        ("hdfcbank", "HDFCBANK"),
        (" axisbank ", "AXISBANK"),
        ("icicibank", "ICICIBANK"),
        ("sbin", "SBIN"),
        ("lt", "LT"),
        ("wipro", "WIPRO"),
        ("tatasteel", "TATASTEEL"),
        ("asianpaint", "ASIANPAINT"),
        ("maruti", "MARUTI"),
        ("sunpharma", "SUNPHARMA"),
        ("nestle", "NESTLE"),
        ("ultracemco", "ULTRACEMCO"),
    ]
)
def test_normalize_ticker(ticker, expected):
    assert normalize_ticker(ticker) == expected