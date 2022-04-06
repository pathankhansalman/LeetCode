# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:58:14 2022

@author: patha
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        retval = [[1], [1, 1]]
        if numRows == 2:
            return retval
        for i in range(2, numRows):
            curr_arr = [1]
            for j in range(len(retval[-1]) - 1):
                curr_arr.append(retval[-1][j] + retval[-1][j + 1])
            curr_arr.append(1)
            retval.append(curr_arr)
        return retval