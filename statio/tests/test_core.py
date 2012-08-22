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
import unittest

#Forced to manipulate path - have yet to find alternative built-in method.
libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not libpath in sys.path:
    sys.path.insert(1, libpath)
del libpath

from core import *


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


class Sum_Value_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        result = sum_value(series, 3)
        self.assertEquals(result, None)

    def test_no_series(self):
        series = None
        result = sum_value(series, 3)
        self.assertEquals(result, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = sum_value(series, 3.0)
        self.assertEquals(result, 109)

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = sum_value(series)
        self.assertEquals(result, 155)

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = sum_value(series, 3)
        self.assertEquals(result, 109)

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = sum_value(series, 3)
        self.assertEquals(result, 79.0)


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


class Sma_Value_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        result = sma_value(series, 3)
        self.assertEquals(result, None)

    def test_no_series(self):
        """
        """
        result = sma_value(None)
        self.assertEquals(result, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % sma_value(series, 3.0)
        self.assertEquals(result, '36.33')

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % sma_value(series)
        self.assertEquals(result, "31.00")

    def test_period_too_big(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % sma_value(series, 10)
        self.assertEquals(result, "31.00")

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % sma_value(series, 3)
        self.assertEquals(result, "36.33")

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = '%.2f' % sma_value(series, 3)
        self.assertEquals(result, "26.33")


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


class Varp_Value_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        result = varp_value(series, 3)
        self.assertEquals(result, None)

    def test_no_series(self):
        series = None
        result = varp_value(series, 3)
        self.assertEquals(result, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % varp_value(series, 3.0)
        self.assertEquals(result, '190.89')

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % varp_value(series)
        self.assertEquals(result, '158.80')

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % varp_value(series, 3)
        self.assertEquals(result, '190.89')

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = '%.2f' % varp_value(series, 3)
        self.assertEquals(result, '20.51')


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


class Var_Value_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        rows = var_value(series, 3)
        self.assertEquals(rows, None)

    def test_no_series(self):
        series = None
        rows = var_value(series, 3)
        self.assertEquals(rows, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % var_value(series, 3.0)
        self.assertEquals(result, '286.33')

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % var_value(series)
        self.assertEquals(result, '198.50')

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % var_value(series, 3)
        self.assertEquals(result, '286.33')

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = '%.2f' % var_value(series, 3)
        self.assertEquals(result, '30.77')


class Stdp_Values_TestCase(unittest.TestCase):
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


class Stdp_Value_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        result = stdp_value(series, 3)
        self.assertEquals(result, None)

    def test_no_series(self):
        series = None
        result = stdp_value(series, 3)
        self.assertEquals(result, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % stdp_value(series, 3.0)
        self.assertEquals(result, '13.82')

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % stdp_value(series)
        self.assertEquals(result, '12.60')

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % stdp_value(series, 3)
        self.assertEquals(result, '13.82')

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = '%.2f' % stdp_value(series, 3)
        self.assertEquals(result, '4.53')


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


class Std_Values_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_series(self):
        series = []
        result = std_value(series, 3)
        self.assertEquals(result, None)

    def test_no_series(self):
        series = None
        result = std_value(series, 3)
        self.assertEquals(result, None)

    def test_period_float(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % std_value(series, 3.0)
        self.assertEquals(result, '16.92')

    def test_calc_nowindow(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % std_value(series)
        self.assertEquals(result, '14.09')

    def test_calc_window(self):
        series = [21, 25, 32, 55, 22]
        result = '%.2f' % std_value(series, 3)
        self.assertEquals(result, '16.92')

    def test_basic_floats(self):
        series = [21.25, 25.5, 32.25]
        result = '%.2f' % std_value(series, 3)
        self.assertEquals(result, '5.55')


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
