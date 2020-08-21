#!/usr/bin/env python3

import ltr.lib
import matplotlib.pyplot as plt


def main(holding_years):
    data = ltr.lib.load_accumulation_index()

    rolling_annual_returns = ltr.lib.rolling_annual_returns(data, holding_years)

    summary = ltr.lib.summarise(rolling_annual_returns, holding_years)

    fig, ax = plt.subplots()

    ltr.lib.one_holding_period_plot(ax, rolling_annual_returns, holding_years)
    ltr.lib.add_title(ax, holding_years)
    ltr.lib.add_summary(ax, summary)

    plt.show()
