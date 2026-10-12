# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:26:13 2022

@author: patha
"""

import itertools

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))