# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:03:53 2022

@author: patha
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while 1:
            if right - left == 1:
                return nums[right]
            mid = (right + left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[left] > nums[mid]:
                right = mid
            else:
                left = mid