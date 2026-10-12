# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:08:19 2022

@author: patha
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def _pow_helper_(arg, val):
            if val == 1:
                return arg
            if val == 0:
                return 1
            half = val // 2
            if half not in mydict.keys():
                mydict[half] = _pow_helper_(arg, half)
            if val % 2 == 0:
                return mydict[half]*mydict[half]
            else:
                return arg*mydict[half]*mydict[half]
        mydict = {}
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1/_pow_helper_(x, abs(n))
        else:
            return _pow_helper_(x, abs(n))
