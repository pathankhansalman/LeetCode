# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:18:30 2022

@author: patha
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        exp_nums = [x for x in nums if not x == val]
        nums[0:len(exp_nums)] = exp_nums
        return len(exp_nums)