# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:11:20 2022

@author: patha
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mydict = {}
        all_tups = []
        if len(nums) < 3:
            return all_tups
        sorted_nums = sorted(nums)
        for i in range(2, len(sorted_nums)):
            mydict[i] = set(sorted_nums[i:])
        for i in range(len(sorted_nums) - 2):
            for j in range(i + 1, len(sorted_nums) - 1):
                k = 0 - sorted_nums[i] - sorted_nums[j]
                if k in mydict[j + 1]:
                    curr_tup = [sorted_nums[i],
                                sorted_nums[j],
                                k]
                    if curr_tup not in all_tups:
                        all_tups.append(curr_tup)
        return all_tups


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.threeSum([1, 2, -2, -1]))
