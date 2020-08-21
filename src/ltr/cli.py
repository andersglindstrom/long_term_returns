import click
import ltr.plot_accumulation
import ltr.plot_rolling_returns


@click.group()
def main():
    pass


@main.command()
def plot_accumulation():
    ltr.plot_accumulation.main()


@main.command()
@click.argument("holding-years", type=int)
def plot_rolling_returns(holding_years):
    ltr.plot_rolling_returns.main(holding_years)
