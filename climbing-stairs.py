# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:04:05 2022

@author: patha
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [1, 2, 3]:
            return n
        f_2_prev = 1
        f_1_prev = 2
        f_curr = f_1_prev + f_2_prev
        for i in range(3, n + 1):
            f_curr = f_2_prev + f_1_prev
            f_2_prev = f_1_prev
            f_1_prev = f_curr
        return f_curr