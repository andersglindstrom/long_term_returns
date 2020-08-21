import click
import ltr.plot_log_prices


@click.group()
def main():
    pass


@main.command()
def plot_log_prices():
    ltr.plot_log_prices.main()
