#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012, Mike Taylor
#
# This file is part of statio released under MIT license.
# See the LICENSE for more information.
"""

Collection of functions used to calculate statistics.

The _values functions typically run over a sliding window and return
a list of computed stats.

The _value functions return a single computed stat.

"""

import math
import bisect


def sum_values(values, period=None):
    """Returns list of running sums.

    :param values: list of values to iterate.
    :param period: (optional) # of values to include in computation.
        * None - includes all values in computation.
    :rtype: list of summed values.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> sum_values(values, 3)  #using 3 period window.
    [34, 64, 93, 93, 101, 97, 98]
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    results = []
    lastval = None
    for bar, newx in enumerate(values):
        if lastval == None:
            lastval = newx

        elif (not period) or (bar < period):
            lastval += newx

        else:
            oldx = values[bar - period]
            lastval += (newx - oldx)

        results.append(lastval)

    return results


def sum_value(values, period=None):
    """Returns the final sum.

    :param values: list of values to iterate.
    :param period: (optional) # of values to include in computation.
        * None - includes all values in computation.
    :rtype: the final sum.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = sum_value(values, 3)  #using 3 period window.
    >>> print "%.2f" % result
    98.00
    """
    if not values:
        return None

    maxbar = len(values)

    beg = 0
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        beg = maxbar - int(period)
        if beg < 0:
            beg = 0

    return sum(values[beg:])


def sma_values(values, period=None):
    """Returns list of running simple moving averages.

    :param values: list of values to iterate and compute stats.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of simple moving averages.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = sma_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['34.00', '32.00', '31.00', '31.00', '33.67', '32.33', '32.67']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period_n = float(period)
        period = int(period)

    results = []
    lastval = None
    for bar, newx in enumerate(values):
        if lastval == None:
            lastval = float(newx)

        elif (not period) or (bar < period):
            lastval += ((newx - lastval) / (bar + 1.0))

        else:
            lastval += ((newx - values[bar - period]) / period_n)

        results.append(lastval)

    return results


def sma_value(values, period=None):
    """Returns the final simple moving average.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: the final simple moving average.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = sma_value(values, 3)  #using 3 period window.
    >>> print "%.2f" % result
    32.67
    """
    if not values:
        return None

    maxbar = len(values)

    beg = 0
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        beg = maxbar - int(period)
        if beg < 0:
            beg = 0

    return sum(values[beg:]) / float(len(values[beg:]))


def ema_values(values, period=None, smoothing=None):
    """Returns list of running exponential moving averages.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :param smoothing: (optional) smoothing factor.
        * valid values: between 0 - 1.
        * None - (default) use formula = 2.0 / (period + 1.0).
        * closer to 0 - greater weight to older values - more smooth.
        * closer to 1 - greater weight to recent values - less smooth.
    :rtype: list of windowed exponential moving averages.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = ema_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['34.00', '32.00', '31.00', '32.50', '35.25', '30.13', '32.56']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        if smoothing == None:
            smoothing = 2.0 / (period + 1.0)

        elif (smoothing < 0) or (smoothing > 1):
            msg = "smoothing outside of 0 to 1 range: "
            msg = ''.join((msg, str(smoothing)))
            raise ValueError(msg)

        period = int(period)

    results = []
    lastval = None
    for bar, newx in enumerate(values):
        if lastval == None:
            lastval = float(newx)

        elif (not period) or (bar < period):
            lastval = lastval + ((newx - lastval) / (bar + 1.0))

        else:
            lastval = lastval + smoothing * (newx - lastval)

        results.append(lastval)

    return results


def wwma_values(values, period=None):
    """Returns list of running Welles Wilder moving averages.

    Approximation of the ema.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed Welles Wilder moving averages.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = wwma_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['34.00', '32.00', '31.00', '32.00', '34.00', '31.00', '32.33']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    results = []
    lastval = None
    for bar, newx in enumerate(values):
        if lastval == None:
            lastval = float(newx)

        elif (not period) or (bar < period):
            lastval = lastval + ((newx - lastval) / (bar + 1.0))

        else:
            lastval = (newx + lastval * (period - 1.0)) / period

        results.append(lastval)

    return results


def psa_values(values, period=None):
    """Returns list of running Power Sum averages.

    Used to derive running variances.  Based on the blog post from
    Subliminal Messages:
    http://subluminal.wordpress.com/2008/07/31/running-standard-deviations/

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed Power Sum averages.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = psa_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['1156.00', '1028.00', '965.67', '965.67', '1147.00', '1075.00', '1098.00']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period_n = float(period)
        period = int(period)

    results = []
    lastval = None
    for bar, newx in enumerate(values):
        if lastval == None:
            lastval = (newx * newx) / (bar + 1.0)

        elif (not period) or (bar < period):
            lastval += ((newx * newx - lastval) / (bar + 1.0))

        else:
            oldx = values[bar - period]
            lastval += (((newx * newx) - (oldx * oldx)) / period_n)

        results.append(lastval)

    return results


def _varbases(values, period=None, population=False):
    """
    Returns list of running variances or standard deviations.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :param population:
        * True - entire population, n.
        * False - sample set, n - 1 (default).

    Examples:
    >>> values = [32.47, 32.70, 32.77, 33.11, 33.25, 33.23, 33.23]
    >>> results = _varbases(values, 3, population=True)
    >>> ["%.2f" % x for x in results]
    ['0.00', '0.01', '0.02', '0.03', '0.04', '0.00', '0.00']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    _smas = sma_values(values, period)
    _psas = psa_values(values, period)

    results = []
    lastval = None
    sample_adjust = 0.0
    if not population:
        sample_adjust = 1.0

    if period:
        period_n = float(period)

    for bar, row in enumerate(zip(_smas, _psas)):
        if lastval == None:
            lastval = 0.0
            results.append(lastval)
            continue

        sma_x, psa_x = row

        if (not period) or (bar < period):
            size = bar + 1.0

        else:
            size = period_n

        n = size - sample_adjust

        lastval = (psa_x * size - size * sma_x * sma_x) / n

        results.append(lastval)

    return results


def _varbase(values, period=None, population=False):
    """
    Returns final variance.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :param population:
        * True - entire population, n.
        * False - sample set, n - 1 (default).

    Examples:
    >>> values = [32.47, 32.70, 32.77, 33.11, 33.25, 33.23, 33.23]
    >>> result = _varbase(values, 3, population=True)
    >>> print "%.2f" % result
    0.00
    """
    if not values:
        return None

    maxbar = len(values)

    beg = 0
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        beg = maxbar - int(period)
        if beg < 0:
            beg = 0

    itemcnt = len(values[beg:])

    if itemcnt < 2:
        return 0.0

    sample_adjust = 0.0
    if not population:
        sample_adjust = 1.0

    n = 0
    meandiffs = 0.0
    mean = 0.0

    for x in values[beg:]:
        n += 1
        delta = x - mean
        mean += delta / n
        meandiffs += delta * (x - mean)

    return meandiffs / (itemcnt - sample_adjust)


def varp_values(values, period=None):
    """Returns list of running population variances.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed population variances.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = varp_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['0.00', '4.00', '4.67', '4.67', '13.56', '29.56', '30.89']
    """
    return _varbases(values, period, population=True)


def varp_value(values, period=None):
    """Returns the final population variance.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: the final population variance.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = varp_value(values, 3)  #using 3 period window.
    >>> "%.2f" % result
    '30.89'
    """
    return _varbase(values, period, population=True)


def var_values(values, period=None):
    """Returns list of running sample variances.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed sample variances.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = var_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['0.00', '8.00', '7.00', '7.00', '20.33', '44.33', '46.33']
    """
    return _varbases(values, period)


def var_value(values, period=None):
    """Returns the final sample variance.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: final sample variance.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = var_value(values, 3)  #using 3 period window.
    >>> "%.2f" % result
    '46.33'
    """
    return _varbase(values, period)


def stdp_values(values, period=None):
    """Returns list of running population standard deviations.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed population standard deviations.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = stdp_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['0.00', '2.00', '2.16', '2.16', '3.68', '5.44', '5.56']
    """
    results = _varbases(values, period, population=True)

    _sqrt = math.sqrt

    return [_sqrt(x) for x in results]


def stdp_value(values, period=None):
    """Returns final population standard deviation.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: final population standard deviation.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = stdp_value(values, 3)  #using 3 period window.
    >>> "%.2f" % result
    '5.56'
    """
    result = _varbase(values, period, population=True)

    if result:
        result = math.sqrt(result)

    return result


def std_values(values, period=None):
    """Returns list of running sample standard deviations.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed sample standard deviations.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = std_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['0.00', '2.83', '2.65', '2.65', '4.51', '6.66', '6.81']
    """
    results = _varbases(values, period)

    _sqrt = math.sqrt

    return [_sqrt(x) for x in results]


def std_value(values, period=None):
    """Returns final sample standard deviation.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: final sample standard deviation.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> result = std_value(values, 3)  #using 3 period window.
    >>> "%.2f" % result
    '6.81'
    """
    result = _varbase(values, period)

    if result:
        result = math.sqrt(result)

    return result


def max_values(values, period=None):
    """Returns list of running maximums.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed maximums.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> results = max_values(values, 3)  #using 3 period window.
    >>> ["%.2f" % x for x in results]
    ['34.00', '34.00', '34.00', '34.00', '38.00', '38.00', '38.00']
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    results = []
    recs = []
    _additem = bisect.insort
    _search = bisect.bisect_left

    for bar, newx in enumerate(values):
        if period and (bar >= period):
            item = values[bar - period]
            idx = _search(recs, item)
            del recs[idx]

        _additem(recs, newx)

        lastval = recs[-1]

        results.append(lastval)

    return results


def top_values(values, period=None, num=1):
    """Returns list of top num items.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :param num: the num in the top num items.
    :rtype: list of windowed top num items.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> top_values(values, 3, 2)  #3 period window and top 2 items.
    [[34], [30, 34], [30, 34], [30, 34], [34, 38], [34, 38], [35, 38]]
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    if num:
        num = int(num)

    results = []
    recs = []
    _additem = bisect.insort
    _search = bisect.bisect_left

    for bar, newx in enumerate(values):
        if period and (bar >= period):
            item = values[bar - period]
            idx = _search(recs, item)
            del recs[idx]

        _additem(recs, newx)

        begidx = num
        if bar < num - 1:
            begidx = bar + 1

        lastval = recs[-begidx:]

        results.append(lastval)

    return results


def min_values(values, period=None):
    """Returns list of minimum items.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :rtype: list of windowed minimum items.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> min_values(values, 3)  #using 3 period window.
    [34, 30, 29, 29, 29, 25, 25]
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    results = []
    recs = []
    _additem = bisect.insort
    _search = bisect.bisect_left

    for bar, newx in enumerate(values):
        if period and (bar >= period):
            item = values[bar - period]
            idx = _search(recs, item)
            del recs[idx]

        _additem(recs, newx)

        lastval = recs[0]

        results.append(lastval)

    return results


def bottom_values(values, period=None, num=1):
    """Returns list of bottom num items.

    :param values: list of values to iterate and compute stat.
    :param period: (optional) # of values included in computation.
        * None - includes all values in computation.
    :param num: the num in the bottom num items.
    :rtype: list of windowed bottom num items.

    Examples:
    >>> values = [34, 30, 29, 34, 38, 25, 35]
    >>> bottom_values(values, 3, 2)  #3 period window and top 2 items.
    [[34], [30, 34], [29, 30], [29, 30], [29, 34], [25, 34], [25, 35]]
    """
    if period:
        if period < 1:
            raise ValueError("period must be 1 or greater")

        period = int(period)

    if num:
        num = int(num)

    results = []
    recs = []
    _additem = bisect.insort
    _search = bisect.bisect_left

    for bar, newx in enumerate(values):
        if period and (bar >= period):
            item = values[bar - period]
            idx = _search(recs, item)
            del recs[idx]

        _additem(recs, newx)

        endidx = num
        if bar < num - 1:
            endidx = bar + 1

        lastval = recs[0:endidx]

        results.append(lastval)

    return results


def _testit(verbose=None):
    import doctest
    doctest.testmod(verbose=verbose)

if __name__ == "__main__":
    _testit()
