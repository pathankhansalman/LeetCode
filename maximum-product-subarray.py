# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:03:26 2022

@author: patha
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = [0]*len(nums)
        max_prod_start = [0]*len(nums)
        min_prod_start = [0]*len(nums)
        max_prod[-1] = nums[-1]
        max_prod_start[-1] = nums[-1]
        min_prod_start[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_prod_start[i] = max(max(nums[i], nums[i]*max_prod_start[i + 1]),
                                    nums[i]*min_prod_start[i + 1])
            min_prod_start[i] = min(min(nums[i], nums[i]*max_prod_start[i + 1]),
                                    nums[i]*min_prod_start[i + 1])
            max_prod[i] = max(max_prod_start[i], max_prod[i + 1])
        return max_prod[0]