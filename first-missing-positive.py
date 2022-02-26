# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 23:02:36 2022

@author: patha
"""

import numpy as np

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = len(nums)
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > max_num:
                nums[i] = max_num + 1
        #        print(nums)
        for i in range(max_num):
            if np.abs(nums[i]) <= max_num:
                # print(nums[i])
                # print(nums[np.abs(nums[i]) - 1])
                if nums[np.abs(nums[i]) - 1] > 0:
                    nums[np.abs(nums[i]) - 1] = -1*nums[np.abs(nums[i]) - 1]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return max_num + 1
