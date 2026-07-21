"""
fair_value.py

Combines all intrinsic valuation methods
into one final fair value.
"""


def average_intrinsic_value(
    dcf_value,
    graham_value,
    pe_value,
):
    """
    Average all available valuation methods.
    Ignores missing values.
    """

    values = []

    if dcf_value is not None:
        values.append(dcf_value)

    if graham_value is not None:
        values.append(graham_value)

    if pe_value is not None:
        values.append(pe_value)

    if len(values) == 0:
        return None

    return round(sum(values) / len(values), 2)