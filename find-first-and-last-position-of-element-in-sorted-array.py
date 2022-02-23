# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:45:05 2022

@author: patha
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
        if nums[0] == target:
            first_idx = 0
        else:
            first_idx = -1
        left = 0
        right = len(nums) - 1
        while first_idx < 0:
            if right - left == 1:
                if nums[right] == target:
                    first_idx = right
                break
            mid = int((left + right)/2)
            if nums[mid - 1] < nums[mid] and nums[mid] == target:
                first_idx = mid
                break
            elif nums[mid + 1] > nums[mid] and nums[mid + 1] == target:
                first_idx = mid + 1
                break
            elif target <= nums[mid]:
                right = mid
            else:
                left = mid
        if nums[-1] == target:
            last_idx = len(nums) - 1
        else:
            last_idx = -1
        left = 0
        right = len(nums) - 1
        while last_idx < 0:
            if right - left == 1:
                if nums[left] == target:
                    last_idx = left
                break
            mid = int((left + right)/2)
            if nums[mid - 1] < nums[mid] and nums[mid - 1] == target:
                last_idx = mid - 1
                break
            elif nums[mid + 1] > nums[mid] and nums[mid] == target:
                last_idx = mid
                break
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        return [first_idx, last_idx]


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.searchRange([1, 2, 3], 1))