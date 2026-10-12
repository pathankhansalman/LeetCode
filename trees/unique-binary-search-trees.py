# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:50:15 2022

@author: patha
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        nums = []
        nums.append(1)
        nums.append(1)
        nums.append(2)
        # print(nums)
        for i in range(3, n + 1):
            curr_sum = 0
            for j in range(i):
                # print(j, nums[j])
                curr_sum += nums[j] * nums[i - j - 1]
            nums.append(curr_sum)
            # print(i, curr_sum)
        return nums[n]