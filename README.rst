statio
======
**statio** is a statistical Python libary geared towards series building by running computations across a sliding window of values.

:Download: http://pypi.python.org/pypi/statio/0.0.1
:Source: https://github.com/TaylorTree/statio


Usage Model
-----------
Most statistical libraries are based on a single point in time.  The -1 index of a list of values is the point in time in which the calculation is made.

**statio** is based on multiple points in time.  Each index is considered a point in time in which the calculation is made.

* Useful for simulation application types.
* Useful for plotting or graphing applications types.


Overview
--------
The major functions of **statio**:

* **sum_values():**
    Builds a list of Running Sums over a sliding list of values.

* **sma_values():**
    Builds a list of Simple Moving Averages over a sliding list of values.

* **ema_values():**
    Builds a list of Exponential Moving Averages over a sliding list of values.

* **wwma_values():**
    Builds a list of Welles Wilder Moving Averages over a sliding list of values.

* **psa_values():**
    Builds a list of Power Sum Averages over a sliding list of values.

* **varp_values():**
    Builds a list of Population Variances over a sliding list of values.

* **var_values():**
    Builds a list of Sample Variances over a sliding list of values.

* **stdp_values():**
    Builds a list of Population Standard Deviations over a sliding list of values.

* **std_values():**
    Builds a list of Sample Standard Deviations over a sliding list of values.

* **max_values():**
    Builds a list of the Maximum Values over a sliding list of values.

* **min_values():**
    Builds a list of the Minimum Values over a sliding list of values.
    
* **top_values():**
    Builds a list of the Top X Values over a sliding list of values.

* **bottom_values():**
    Builds a list of the Bottom X Values over a sliding list of values.


License
-------
Made available under the MIT License.


Usage
-----
Import the library:

>>> import statio

1. Build list of running **sums** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> statio.sum_values(values, 3)
[34, 64, 93, 93, 101, 97, 98]

2. Build list of **Simple Moving Averages** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.sma_values(values, 3)
>>> ["%.2f" % x for x in results]
['34.00', '32.00', '31.00', '31.00', '33.67', '32.33', '32.67']

3. Build list of **Exponential Moving Averages** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.ema_values(values, 3)
>>> ["%.2f" % x for x in results]
['34.00', '32.00', '31.00', '32.50', '35.25', '30.13', '32.56']

4. Build list of **Welles Wilder Averages** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.wwma_values(values, 3)
>>> ["%.2f" % x for x in results]
['34.00', '32.00', '31.00', '32.00', '34.00', '31.00', '32.33']

5. Build list of **Population Variances** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.varp_values(values, 3)
>>> ["%.2f" % x for x in results]
['0.00', '4.00', '4.67', '4.67', '13.56', '29.56', '30.89']

6. Build list of **Sample Variances** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.var_values(values, 3)
>>> ["%.2f" % x for x in results]
['0.00', '8.00', '7.00', '7.00', '20.33', '44.33', '46.33']

7. Build list of **Population Standard Deviations** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.stdp_values(values, 3)
>>> ["%.2f" % x for x in results]
['0.00', '2.00', '2.16', '2.16', '3.68', '5.44', '5.56']

8. Build list of **Sample Standard Deviations** using a 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.std_values(values, 3)
>>> ["%.2f" % x for x in results]
['0.00', '2.83', '2.65', '2.65', '4.51', '6.66', '6.81']

9. Build list of the **Maximum Value** of 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> results = statio.max_values(values, 3)
>>> ["%.2f" % x for x in results]
['34.00', '34.00', '34.00', '34.00', '38.00', '38.00', '38.00']

10. Build list of the **Minimum Value** of 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> statio.min_values(values, 3)
[34, 30, 29, 29, 29, 25, 25]

11. Build list of the **Top X Values** of 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> statio.top_values(values, 3, 2)
[[34], [30, 34], [30, 34], [30, 34], [34, 38], [34, 38], [35, 38]]

12. Build list of the **Bottom X Values** of 3 period window:

>>> values = [34, 30, 29, 34, 38, 25, 35]
>>> statio.bottom_values(values, 3, 2)
[[34], [30, 34], [29, 30], [29, 30], [29, 34], [25, 34], [25, 35]]


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