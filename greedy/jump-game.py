# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 23:52:04 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        pos_arr = np.zeros(n).astype(bool)
        pos_arr[n - 1] = True
        i = n - 2
        while i >= 0:
            pos_arr[i] = pos_arr[i + 1 : i + nums[i] + 1].any()
            i -= 1
        print(pos_arr)
        return pos_arr[0]
