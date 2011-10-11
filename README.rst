statio
======
statio is a MIT licensed statistical libary implemented in Python.

Generates statistical series of values by running computations across a sliding window of values.


Usage Model
-----------
Most statistical libraries are based on a single point in 
time.  The -1 index of a list of values is the point in time
in which the calculation is made.

statio is based on multiple points in time.  Each index is
considered a point in time in which the calculation is made.

* Useful for simulation application types.
* Useful for plotting or graphing applications types.


Overview
--------
Each function below iterates over a list of values and computes a series of running statistics over a sliding window.

* sum_values():
    Running Sum
* sma_values():
    Running Simple Moving Average
* ema_values():
    Running Exponential Moving Average
* wwma_values():
    Running Welles Wilder Moving Average
* varp_values():
    Running Population Variance
* var_values():
    Running Sample Variance
* stdp_values():
    Running Population Standard Deviation
* std_values():
    Running Sample Standard Deviation
* max_values():
    Running Maximum Value
* min_values():
    Running Minimum Value
* top_values():
    Running Top Values
* bottom_values():
    Running Bottom Values


Usage
-----
Import the library::
    >>> import statio

1. Calculate a running **sum** over a 3 period window::
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> statio.sum_values(values, 3)
    [34, 64, 93, 93, 101, 97, 98]

2. Calculate a running **sma** over a 3 period window::
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = statio.sma_values(values, 3)
    >>> ["%.2f" % x for x in results]
    ['34.00', '32.00', '31.00', '31.00', '33.67', '32.33', '32.67']

Roadmap
-------
* Add median_values.
* Add recentmax_values: the index of the most recent max value.
* Add sincemax_values: the number of bars since recent max value.
* Add recentmin_values: the index of the most recent min value.
* Add sincemin_values: the number of bars since recent min value.
* Add covariance, correlation, alpha, beta computations.


For additional information, please email:
    mike@taylortree.com