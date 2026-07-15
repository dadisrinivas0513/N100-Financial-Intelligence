import pytest

from src.analytics.ratios import *


def test_net_profit_margin():

    assert net_profit_margin(100, 1000) == 10.0


def test_net_profit_margin_zero_sales():

    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():

    assert operating_profit_margin(150, 1000) == 15.0


def test_return_on_equity():

    assert return_on_equity(200, 500, 500) == 20.0


def test_negative_equity():

    assert return_on_equity(100, -500, 100) is None


def test_return_on_assets():

    assert return_on_assets(200, 2000) == 10.0


def test_zero_assets():

    assert return_on_assets(200, 0) is None


def test_compare_opm():

    assert compare_opm(20, 18) is True


# =====================================================
# DAY 09 TESTS
# =====================================================

from src.analytics.ratios import (
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    icr_warning_flag,
    net_debt,
    asset_turnover,
)


def test_de_ratio():

    assert debt_to_equity(200,100,100)==1


def test_debt_free():

    assert debt_to_equity(0,100,50)==0


def test_negative_equity():

    assert debt_to_equity(100,-100,-10) is None


def test_high_leverage():

    assert high_leverage_flag(6,"Technology")==True


def test_financial_exempt():

    assert high_leverage_flag(8,"Financials")==False


def test_interest_zero():

    assert interest_coverage_ratio(100,20,0) is None


def test_icr_label():

    assert icr_label(None)=="Debt Free"


def test_asset_turnover():

    assert asset_turnover(1000,500)==2