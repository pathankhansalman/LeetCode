# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:16:28 2022

@author: patha
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mydict = {}
        mydict[0] = 0
        mydict[1] = 0
        mydict[2] = 0
        for num in nums:
            mydict[num] += 1
        for i in range(len(nums)):
            if mydict[0] == 0:
                if mydict[1] == 0:
                    nums[i] = 2
                    mydict[2] -= 1
                else:
                    nums[i] = 1
                    mydict[1] -= 1
            else:
                nums[i] = 0
                mydict[0] -= 1
        return nums