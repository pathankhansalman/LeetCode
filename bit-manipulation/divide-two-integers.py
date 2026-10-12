# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:36:22 2022

@author: patha
"""

import numpy as np

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividend_sign = np.sign(dividend)
        divisor_sign = np.sign(divisor)
        dividend_abs = np.abs(dividend)
        divisor_abs = np.abs(divisor)
        if dividend_abs == 0:
            return 0
        if dividend_abs < divisor_abs:
            return 0
        if dividend_abs == divisor_abs:
            return dividend_sign*divisor_sign
        start_mul = 1
        end_mul = 2
        rem_dividend = dividend_abs
        curr_quot = 0
        while 1:
            if rem_dividend < divisor_abs:
                break
            elif rem_dividend < start_mul*divisor_abs:
                start_mul /= 2
                end_mul /= 2
            elif start_mul*divisor_abs <= rem_dividend and\
                    rem_dividend <= end_mul*divisor_abs:
                curr_quot += start_mul
                rem_dividend -= start_mul*divisor_abs
            elif rem_dividend > end_mul*divisor_abs:
                start_mul *= 2
                end_mul *= 2
        return min(2**31 - 1, max(-(2**31), int(dividend_sign*divisor_sign*curr_quot)))



if __name__ == '__main__':
    mysol = Solution()
    print(mysol.divide(7, -3))
