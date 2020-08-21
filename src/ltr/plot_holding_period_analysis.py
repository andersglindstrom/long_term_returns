#!/usr/bin/env python3

import ltr.lib
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = ltr.lib.load_accumulation_index()

    rolling_returns = {}
    for holding_years in [5,10,15,25,30]:
        rolling_returns[holding_years] = ltr.lib.rolling_annual_returns(data, holding_years)

    last_years = sorted([returns.index[-1] for returns in rolling_returns.values()])
    min_last_year = min(last_years)

    # Only use common years
    rolling_returns = {
        holding_years:returns[returns.index <= min_last_year]
        for holding_years, returns in rolling_returns.items()
    }

    summaries = [
        ltr.lib.summarise(returns, holding_years)
        for holding_years, returns in rolling_returns.items()
    ]

    boxes = []
    for summary in summaries:
        boxes.append({
            "label": summary["holding_years"],
            "whislo": summary["worst"],
            "q1": summary["q10"],
            "med": summary["median"],
            "q3": summary["q90"],
            "whishi": summary["best"],
            "fliers": []
        })

    fix, ax = plt.subplots()
    ax.bxp(boxes, showfliers=False)
    plt.show()
