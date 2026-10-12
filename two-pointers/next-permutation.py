# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:50:58 2022

@author: patha
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == list(reversed(sorted(nums))):
            nums[:] = list(sorted(nums))
            print(nums)
            return nums
        start_len = 2
        while 1:
            if nums[-1*start_len:] == list(reversed(sorted(nums[-1*start_len:]))):
                start_len += 1
                continue
            else:
                start_val = nums[-1*start_len:][0]
                j = len(nums) - 1
                for num in reversed(nums[-1*start_len + 1:]):
                    if num > start_val:
                        nums[len(nums) - start_len] = num
                        nums[j] = start_val
                        nums[-1*start_len + 1:] = sorted(nums[-1*start_len +
                                                              1:])
                        return nums
                        break
                    else:
                        j -= 1
                start_len += 1


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.nextPermutation([5, 4, 1, 6, 3, 2]))
