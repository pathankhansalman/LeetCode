# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:13:46 2022

@author: patha
"""

import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.comb(m + n - 2, m - 1)