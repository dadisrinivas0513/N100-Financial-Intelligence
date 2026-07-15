import pytest

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion,
    capital_allocation_pattern
)


def test_free_cash_flow():

    assert free_cash_flow(100, -40) == 60


def test_free_cash_flow_negative():

    assert free_cash_flow(50, -100) == -50


def test_capex():

    value, label = capex_intensity(-40, 1000)

    assert label == "Moderate"


def test_capex_asset_light():

    value, label = capex_intensity(-10, 1000)

    assert label == "Asset Light"


def test_capex_high():

    value, label = capex_intensity(-150, 1000)

    assert label == "Capital Intensive"


def test_fcf_conversion():

    assert fcf_conversion(100, 200) == 50.0


def test_pattern():

    assert capital_allocation_pattern(10, -5, -3) == "Reinvestor"


def test_pattern_growth():

    assert capital_allocation_pattern(-10, -5, 3) == "Growth Funded by Debt"


def test_quality():

    score, label = cfo_quality_score(
        [100, 120, 110],
        [80, 100, 90]
    )

    assert label == "High Quality"


def test_quality_none():

    assert cfo_quality_score([100], [0]) is None