# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:54:49 2022

@author: patha
"""

from copy import deepcopy
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        retval = []
        for i in range(len(triangle) - 1, -1, -1):
            curr_arr = []
            if i == len(triangle) - 1:
                curr_arr = deepcopy(triangle[i])
            else:
                for j in range(len(triangle[i])):
                    curr_arr.append(min(triangle[i][j] + retval[-1][j],
                                        triangle[i][j] + retval[-1][j + 1]))
            retval.append(curr_arr)
            print(curr_arr)
        return retval[-1][0]