#!/usr/bin/env python3

import collections
import importlib.resources as resources

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_accumulation_index():
    with resources.open_text("ltr", "sp500tr.csv") as data_file:
        data = pd.read_csv(data_file).set_index("Year").sort_index()/100
    return data.TotalReturn

def rolling_annual_returns(data, holding_years, last_year=None):

    rolling_final_value = (data+1).rolling(window=holding_years).apply(np.prod, raw=True)
    rolling_final_value = rolling_final_value.dropna()
    rolling_annual_return = np.log(rolling_final_value)/holding_years

    rolling_annual_return.index = data.index[:-holding_years+1]

    if last_year:
        rolling_annual_return = rolling_annual_return[rolling_annual_return.index <= last_year]

    return rolling_annual_return

def summarise(rolling_annual_returns, holding_years):

    first_year = rolling_annual_returns.index[0]
    last_year = rolling_annual_returns.index[-1]
    mean = rolling_annual_returns.mean()
    median = rolling_annual_returns.median()
    stdev = rolling_annual_returns.std()
    worst = rolling_annual_returns.min()
    best = rolling_annual_returns.max()
    q10 = rolling_annual_returns.quantile(0.1)
    q90 = rolling_annual_returns.quantile(0.9)

    return {
        "holding_years":holding_years,
        "first_year":first_year,
        "last_year":last_year,
        "mean":mean,
        "median":median,
        "stdev":stdev,
        "worst":worst,
        "best":best,
        "q10":q10,
        "q90":q90,
    }

def add_title(ax, holding_years):
    ax.set_title(f"Holding period: {holding_years} years")

def one_holding_period_plot(ax, rolling_annual_returns, holding_years):
    ax.hist(rolling_annual_returns)

def add_summary(ax, summary):
    text = "\n".join((
        f"First year: {summary['first_year']}",
        f"Last year: {summary['last_year']}",
        f"Mean: {summary['mean']:0.2%}",
        f"Median: {summary['median']:0.2%}",
        f"Stdev: {summary['stdev']:0.2%}",
        f"Worst: {summary['worst']:0.2%}",
        f"Best: {summary['best']:0.2%}",
        f"Quantile 10%: {summary['q10']:0.2%}",
        f"Quantile 90%: {summary['q90']:0.2%}",
    ))

    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=9, verticalalignment="top")
