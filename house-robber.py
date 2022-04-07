# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:02:59 2022

@author: patha
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        val = [0]*len(nums)
        val[-1] = nums[-1]
        val[-2] = max(nums[-2], nums[-1])
        for i in range(len(nums) - 3, -1, -1):
            val[i] = max(nums[i] + val[i + 2],
                         val[i + 1])
        return val[0]