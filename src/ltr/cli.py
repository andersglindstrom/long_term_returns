import click
import ltr.plot_accumulation
import ltr.plot_rolling_returns
import ltr.plot_holding_period_distribution


@click.group()
def main():
    pass


@main.command()
def plot_accumulation():
    ltr.plot_accumulation.main()


@main.command()
@click.argument("holding-years", type=click.IntRange(min=2))
def plot_rolling_returns(holding_years):
    ltr.plot_rolling_returns.main(holding_years)


@main.command()
@click.argument("holding-years", type=click.IntRange(min=2))
def plot_holding_period_distribution(holding_years):
    ltr.plot_holding_period_distribution.main(holding_years)
