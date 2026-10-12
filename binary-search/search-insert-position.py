# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:58:37 2022

@author: patha
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            return 1
        if target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while 1:
            if right - left == 1:
                if nums[left] >= target:
                    return left
                return right
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid - 1] < target and target < nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            elif nums[mid] < target and target < nums[mid + 1]:
                return mid + 1
            elif nums[mid] < target:
                left = mid


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.searchInsert([1, 3, 5, 6], 7))
