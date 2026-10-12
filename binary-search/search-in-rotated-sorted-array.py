# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:02:06 2022

@author: patha
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # bin_search for the pivot index first
        # then two bin searches
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        left = 0
        right = len(nums) - 1
        pivot_idx = -1
        while 1:
            if left == right:
                break
            if right - left == 1:
                if nums[right] < nums[left]:
                    pivot_idx = right
                break
            if right - left == 2:
                if nums[left] > nums[left + 1]:
                    pivot_idx = left + 1
                elif nums[left + 1] > nums[right]:
                    pivot_idx = right
                break
            mid = int((left + right)/2)
            if nums[mid - 1] > nums[mid]:
                pivot_idx = mid
                break
            elif nums[mid + 1] < nums[mid]:
                pivot_idx = mid + 1
                break
            else:
                if nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        if pivot_idx == -1:
            search_arr = nums
            pre_val = 0
        elif target <= nums[-1]:
            search_arr = nums[pivot_idx:]
            pre_val = pivot_idx
        else:
            search_arr = nums[:pivot_idx]
            pre_val = 0
        left = 0
        right = len(search_arr) - 1
        while 1:
            # print(left, right)
            if left == right:
                if search_arr[left] == target:
                    return pre_val + left
                return -1
            if right - left == 1:
                if search_arr[left] == target:
                    return pre_val + left
                elif search_arr[right] == target:
                    return pre_val + right
                else:
                    return -1
            mid = int((left + right)/2)
            if search_arr[mid] == target:
                return pre_val + mid
            elif target < search_arr[mid]:
                right = mid
            else:
                left = mid
        return -1

if __name__ == '__main__':
    mysol = Solution()
    print(mysol.search([2,4,5,6,7,0,1], 0))
            