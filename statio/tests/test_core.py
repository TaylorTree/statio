#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, Mike Taylor
#
# This file is part of statio released under MIT license.
# See the LICENSE for more information.
"""

Test the core module.

"""

import sys
import os
import tempfile
import unittest

#Forced to manipulate path - have yet to find alternative built-in method.
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not libpath in sys.path:
    sys.path.insert(1, libpath)
del libpath

from core import sum_values
from core import sma_values
from core import ema_values
from core import wwma_values
from core import varp_values
from core import var_values
from core import stdp_values
from core import std_values
from core import max_values
from core import top_values
from core import min_values
from core import bottom_values


class Sum_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = sum_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, sum_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = sum_values(series, 3.0)
        self.assertEquals(rows, [21, 46, 78, 112, 109])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = sum_values(series)
        self.assertEquals(rows, [21, 46, 78, 133, 155])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = sum_values(series, 3)
        self.assertEquals(rows, [21, 46, 78, 112, 109])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = sum_values(series, 3)
        self.assertEquals(rows, [21.25, 46.75, 79.0])


class Sma_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = sma_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, sma_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = sma_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '37.33', '36.33'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = sma_values(series)
        self.assertEquals(rows, [21, 23.0, 26.0, 33.25, 31.0])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = sma_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '37.33', '36.33'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = sma_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.25', '23.38', '26.33'])


class Ema_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = ema_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, ema_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = ema_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '40.50', '31.25'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = ema_values(series)
        self.assertEquals(rows, [21, 23.0, 26.0, 33.25, 31.0])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = ema_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '40.50', '31.25'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = ema_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.25', '23.38', '26.33'])


class Wwma_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = wwma_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, wwma_values)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = wwma_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '35.67', '31.11'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = wwma_values(series)
        self.assertEquals(rows, [21, 23.0, 26.0, 33.25, 31.0])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = wwma_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.00', '23.00', '26.00', '35.67', '31.11'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = wwma_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.25', '23.38', '26.33'])


class Varp_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = varp_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, varp_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = varp_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '4.00', '20.67', '164.22', '190.89'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = varp_values(series)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '4.00', '20.67', '173.19', '158.80'])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = varp_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '4.00', '20.67', '164.22', '190.89'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = varp_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '4.52', '20.51'])


class Var_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = var_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, var_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = var_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '8.00', '31.00', '246.33', '286.33'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = var_values(series)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '8.00', '31.00', '230.92', '198.50'])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = var_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '8.00', '31.00', '246.33', '286.33'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = var_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '9.03', '30.77'])


class Std_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = stdp_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, stdp_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = stdp_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.00', '4.55', '12.81', '13.82'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = stdp_values(series)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.00', '4.55', '13.16', '12.60'])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = stdp_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.00', '4.55', '12.81', '13.82'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = stdp_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.13', '4.53'])


class Std_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = std_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, std_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = std_values(series, 3.0)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.83', '5.57', '15.70', '16.92'])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = std_values(series)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.83', '5.57', '15.20', '14.09'])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = std_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '2.83', '5.57', '15.70', '16.92'])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = std_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['0.00', '3.01', '5.55'])


class Max_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = max_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, max_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = max_values(series, 3.0)
        self.assertEquals(rows, [21, 25, 32, 55, 55])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = max_values(series)
        self.assertEquals(rows, [21, 25, 32, 55, 55])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = max_values(series, 3)
        self.assertEquals(rows, [21, 25, 32, 55, 55])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = max_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.25', '25.50', '32.25'])


class Top_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = top_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, top_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = top_values(series, 2.0, 2)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_num_float(self):
        series = [21, 25, 32, 55, 22]
        rows = top_values(series, 2, 2.0)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = top_values(series, num=2)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [32, 55]])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = top_values(series, 2, 2)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_calc_no_num(self):
        series = [21, 25, 32, 55, 22]
        rows = top_values(series, 2)
        self.assertEquals(rows, [[21], [25], [32], [55], [55]])


class Min_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = min_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, min_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = min_values(series, 3.0)
        self.assertEquals(rows, [21, 21, 21, 25, 22])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = min_values(series)
        self.assertEquals(rows, [21, 21, 21, 21, 21])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = min_values(series, 3)
        self.assertEquals(rows, [21, 21, 21, 25, 22])

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        rows = min_values(series, 3)
        rows = ['%.2f' % x for x in rows]
        self.assertEquals(rows, ['21.25', '21.25', '21.25'])


class Bottom_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        """
        Should return [] if empty series.
        """
        series = []
        rows = bottom_values(series, 3)
        self.assertEquals(rows, [])

    def test_no_series(self):
        """
        Must pass series of values to calculate.
        """
        series = None
        self.assertRaises(TypeError, bottom_values, series)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        rows = bottom_values(series, 2.0, 2)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_num_float(self):
        series = [21, 25, 32, 55, 22]
        rows = bottom_values(series, 2, 2.0)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        rows = bottom_values(series, num=2)
        self.assertEquals(rows, [[21], [21, 25], [21, 25], [21, 25], [21, 22]])

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        rows = bottom_values(series, 2, 2)
        self.assertEquals(rows, [[21], [21, 25], [25, 32], [32, 55], [22, 55]])

    def test_calc_no_num(self):
        series = [21, 25, 32, 55, 22]
        rows = bottom_values(series, 2)
        self.assertEquals(rows, [[21], [21], [25], [32], [22]])


if __name__ == "__main__":
    unittest.main()
