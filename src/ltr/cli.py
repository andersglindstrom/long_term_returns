import click
import ltr.plot_log_prices
import ltr.plot_rolling_returns


@click.group()
def main():
    pass


@main.command()
def plot_log_prices():
    ltr.plot_log_prices.main()


@main.command()
@click.argument("holding-years", type=int)
def plot_rolling_returns(holding_years):
    ltr.plot_rolling_returns.main(holding_years)
