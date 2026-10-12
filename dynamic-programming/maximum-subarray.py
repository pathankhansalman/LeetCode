# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:47:59 2022

@author: patha
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_sum = -100000000000
        max_elem = nums[0]
        i = 0
        n = len(nums)
        cumsum = [0]*n
        cumsum[0] = nums[0]
        for i in range(1, n):
            cumsum[i] = cumsum[i - 1] + nums[i]
        curr_min = cumsum[0]
        curr_max = cumsum[0]
        up_found = False
        for i in range(1, n):
            if nums[i] > max_elem:
                max_elem = nums[i]
            if cumsum[i] > curr_max:
                up_found = True
                curr_max = cumsum[i]
            elif cumsum[i] < curr_min:
                if curr_max - min(curr_min, 0) > max_sum:
                    max_sum = curr_max - min(curr_min, 0)
                curr_min = cumsum[i]
                curr_max = cumsum[i]
        if curr_max - min(curr_min, 0) > max_sum:
            max_sum = curr_max - min(curr_min, 0)
        if not up_found:
            return max_elem
        return max_sum