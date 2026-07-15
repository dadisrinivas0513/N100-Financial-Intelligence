import pytest

from src.analytics.cagr import (
    calculate_cagr,
    NORMAL,
    TURNAROUND,
    DECLINE_TO_LOSS,
    BOTH_NEGATIVE,
    ZERO_BASE,
    INSUFFICIENT,
)


def test_normal_cagr():

    value, flag = calculate_cagr(
        100,
        200,
        5
    )

    assert flag == NORMAL
    assert value is not None


def test_turnaround():

    value, flag = calculate_cagr(
        -100,
        100,
        5
    )

    assert value is None
    assert flag == TURNAROUND


def test_decline_to_loss():

    value, flag = calculate_cagr(
        100,
        -100,
        5
    )

    assert value is None
    assert flag == DECLINE_TO_LOSS


def test_both_negative():

    value, flag = calculate_cagr(
        -100,
        -50,
        5
    )

    assert value is None
    assert flag == BOTH_NEGATIVE


def test_zero_base():

    value, flag = calculate_cagr(
        0,
        100,
        5
    )

    assert value is None
    assert flag == ZERO_BASE


def test_insufficient():

    value, flag = calculate_cagr(
        100,
        200,
        0
    )

    assert value is None
    assert flag == INSUFFICIENT


def test_large_growth():

    value, flag = calculate_cagr(
        100,
        1000,
        10
    )

    assert flag == NORMAL


def test_small_growth():

    value, flag = calculate_cagr(
        100,
        110,
        5
    )

    assert flag == NORMAL


def test_same_values():

    value, flag = calculate_cagr(
        100,
        100,
        5
    )

    assert flag == NORMAL
    assert value == 0


def test_wrapper():

    value, flag = calculate_cagr(
        50,
        100,
        5
    )

    assert flag == NORMAL