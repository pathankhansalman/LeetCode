# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:37:16 2022

@author: patha
"""

import itertools

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list([list(y) for y in set([tuple(x) for x in list(itertools.permutations(nums))])])