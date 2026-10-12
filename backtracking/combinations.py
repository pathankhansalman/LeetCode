# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:01:17 2022

@author: patha
"""
import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(x) for x in list(itertools.combinations(list(range(1, n + 1)), k))]