# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:38:38 2022

@author: patha
"""

import itertools
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return '1'
        return ''.join([str(y) for y in list(itertools.permutations(list(range(1, n + 1))))[k - 1]])