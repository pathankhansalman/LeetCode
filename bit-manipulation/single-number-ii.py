# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:43:12 2022

@author: patha
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for num in nums:
            if num not in mydict.keys():
                mydict[num] = 1
            else:
                mydict[num] += 1
            if mydict[num] == 3:
                del mydict[num]
        return list(mydict.keys())[0]