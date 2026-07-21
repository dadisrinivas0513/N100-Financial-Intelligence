"""
cashflow_kpis.py

Sprint 2 - Day 11
Cash Flow KPI Engine
"""

from statistics import mean


def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow

    FCF = Operating Activity + Investing Activity
    """

    if operating_activity is None or investing_activity is None:
        return None

    return operating_activity + investing_activity


def cfo_quality_score(cfo_list, pat_list):
    """
    Average CFO/PAT Ratio
    """

    ratios = []

    for cfo, pat in zip(cfo_list, pat_list):

        if pat == 0:
            continue

        ratios.append(cfo / pat)

    if len(ratios) == 0:
        return None

    score = mean(ratios)

    if score > 1:
        label = "High Quality"

    elif score >= 0.5:
        label = "Moderate"

    else:
        label = "Accrual Risk"

    return round(score, 2), label

def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity

    Formula:
    abs(Investing Activity) / Sales × 100
    """

    if sales == 0:
        return None

    intensity = abs(investing_activity) / sales * 100

    if intensity < 3:
        label = "Asset Light"

    elif intensity <= 8:
        label = "Moderate"

    else:
        label = "Capital Intensive"

    return round(intensity, 2), label


def fcf_conversion(fcf, operating_profit):
    """
    FCF Conversion Rate
    """

    if operating_profit == 0:
        return None

    return round((fcf / operating_profit) * 100, 2)


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Capital Allocation Pattern
    """

    s1 = "+" if cfo >= 0 else "-"
    s2 = "+" if cfi >= 0 else "-"
    s3 = "+" if cff >= 0 else "-"

    pattern = f"{s1},{s2},{s3}"

    mapping = {

        "+,-,-": "Reinvestor",

        "+,+,-": "Liquidating Assets",

        "-,+,+": "Distress Signal",

        "-,-,+": "Growth Funded by Debt",

        "+,+,+": "Cash Accumulator",

        "-,-,-": "Pre-Revenue",

        "+,-,+": "Mixed",

        "-,+,-": "Unknown"

    }

    return mapping.get(pattern, "Unknown")