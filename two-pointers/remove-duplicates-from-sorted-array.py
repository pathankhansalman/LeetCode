# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:51:19 2022

@author: patha
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exp_nums = list(set(nums))
        nums[0:len(exp_nums)] = exp_nums
        return len(exp_nums)
