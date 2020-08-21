import ltr.lib
import matplotlib.pyplot as plt

def main(holding_years):

    assert holding_years >= 2

    data = ltr.lib.load_accumulation_index()

    rolling_annual_returns = ltr.lib.rolling_annual_returns(
        data, holding_years
    )
    print(rolling_annual_returns)
    summary = ltr.lib.summarise(rolling_annual_returns, holding_years)

    fig, ax = plt.subplots()

    ax.bar(rolling_annual_returns.index, rolling_annual_returns.values)
    ltr.lib.add_title(ax, holding_years)
    ltr.lib.add_summary(ax, summary)

    plt.show()
