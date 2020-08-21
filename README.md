# Set up virtual environment

```
$ virtualenv -p 38 .venv/ltr
```

# Activate virtual environment

```
$ source .venv/ltr/bin/activate
```

# Install
```
$ pip install -e .
```

# Plot the accumulation index

The accumulation index is the cumulative return since the first date in the
series.
```
$ ltr plot-accumulation
```

# Plot rolling returns

Rolling returns for a 2 year period is the annualised return for holding the
accumulation index for very 2 year period from the start of the data. Ditto for
25 years.  The longer the holding period, the lower the variability of the
annualised return because a longer period smooths out the ups and downs.

```
$ ltr plot-rolling returns 2 &
$ ltr plot-rolling returns 25 &
```

# Plot the distribution of the rolling returns

The distribution of rolling returns is simply a histogram of the rolling
returns from the previous section. Note that the summary includes mean return,
median return, worst return, best return, and the 10% and 90% quantiles. The
quantiles are a measure of the variability of the returns. If you look at
the quantiles for a 2 year and 25 year holding period you will see that the
median return is about the same but that the quantiles (the variability) is
different.

```
$ ltr plot-holding-period-distribution 2 &
$ ltr plot-holding-period-distribution 25 &
```

# Perform a holding period analysis

For a number of different holding periods, a distribution is calculated as per
the previous section. Each holding period has max, min, median, 10% and 90%
quantiles. These are represented by a whisker plot for each holding period.
```
$ ltr plot-holding-period-analysis
```
