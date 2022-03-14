# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:51:15 2022

@author: patha
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        elif nums[0] == nums[-1]:
            return 2
        curr_num = nums[0]
        curr_ct = 1
        left_idx = 1
        right_idx = 1
        while left_idx < len(nums):
            print(left_idx, nums[left_idx], curr_num, curr_ct)
            print(nums)
            if nums[left_idx] == curr_num:
                if curr_ct == 2:
                    while right_idx < len(nums) and nums[right_idx] == curr_num:
                        right_idx += 1
                    # print(left_idx, curr_num, curr_ct, right_idx)
                    if right_idx == len(nums):
                        return left_idx
                    else:
                        curr_left_idx = left_idx
                        while right_idx < len(nums):
                            temp = nums[curr_left_idx]
                            nums[curr_left_idx] = nums[right_idx]
                            nums[right_idx] = temp
                            curr_left_idx += 1
                            right_idx += 1
                        if nums[left_idx] < curr_num:
                            return left_idx
                        curr_num = nums[left_idx]
                        curr_ct = 1
                        left_idx += 1
                        right_idx = left_idx
                else:
                    curr_ct += 1
                    left_idx += 1
                    right_idx = left_idx
            elif nums[left_idx] < curr_num:
                # print(left_idx)
                return left_idx
            else:
                curr_num = nums[left_idx]
                curr_ct = 1
                left_idx += 1
                right_idx = left_idx
        return left_idx