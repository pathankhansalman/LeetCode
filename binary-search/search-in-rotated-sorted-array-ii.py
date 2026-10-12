# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:28:04 2022

@author: patha
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 1:
            if nums[0] == target:
                return True
            return False
        if len(nums) == 2:
            if nums[0] == target or nums[1] == target:
                return True
            return False
        pivot_idx = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot_idx = i
                break
        print(pivot_idx)
        if pivot_idx != -1:
            if pivot_idx == 0:
                if nums[0] == target:
                    return True
            else:
                left = 0
                right = pivot_idx
                while 1:
                    if right - left == 1:
                        if target == nums[left] or target == nums[right]:
                            return True
                        break
                    else:
                        mid = (left + right) // 2
                        if nums[mid] == target:
                            return True
                        elif nums[mid] > target:
                            right = mid
                        else:
                            left = mid
        left = pivot_idx + 1
        right = len(nums) - 1
        if left == right:
            if nums[-1] == target:
                return True
            return False
        while 1:
            if right - left == 1:
                if target == nums[left] or target == nums[right]:
                    return True
                return False
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid
        return False