# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:22:57 2022

@author: patha
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mydict = {}
        all_tups = []
        if len(nums) < 4:
            return all_tups
        sorted_nums = sorted(nums)
        for i in range(3, len(sorted_nums)):
            mydict[i] = set(sorted_nums[i:])
        for i in range(len(sorted_nums) - 3):
            for j in range(i + 1, len(sorted_nums) - 2):
                for k in range(j + 1, len(sorted_nums) - 1):
                    l = target - sorted_nums[i] - sorted_nums[j] -\
                        sorted_nums[k]
                    if l in mydict[k + 1]:
                        curr_tup = [sorted_nums[i],
                                    sorted_nums[j],
                                    sorted_nums[k],
                                    l]
                        if curr_tup not in all_tups:
                            all_tups.append(curr_tup)
        return all_tups


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.fourSum([1,0,-1,0,-2,2], 0))
