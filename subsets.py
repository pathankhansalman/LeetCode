# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:06:33 2022

@author: patha
"""

import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retval = []
        for i in range(len(nums) + 1):
            retval += [list(x) for x in itertools.combinations(nums, i)]
        return retval