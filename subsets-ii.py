# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 22:00:06 2022

@author: patha
"""
import itertools
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retval = []
        for i in range(len(nums) + 1):
            retval += list(itertools.combinations(nums, i))
        return [list(y) for y in list(set([tuple(sorted(x)) for x in retval]))]