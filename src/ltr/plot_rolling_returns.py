import ltr.lib
import matplotlib.pyplot as plt

def main(holding_years):
    data = ltr.lib.load_accumulation_index()

    rolling_annual_returns = ltr.lib.rolling_annual_returns(
        data, args.holding_years
    )
    summary = ltr.lib.summarise(rolling_annual_returns, args.holding_years)

    fig, ax = plt.subplots()

    ax.bar(rolling_annual_returns.index, rolling_annual_returns.values)
    analysis.add_title(ax, args.holding_years)
    analysis.add_summary(ax, summary)

    plt.show()
