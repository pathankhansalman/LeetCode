# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:58:42 2022

@author: patha
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        retval = [[1], [1, 1]]
        if rowIndex == 1:
            return retval[-1]
        for i in range(2, rowIndex + 1):
            curr_arr = [1]
            for j in range(len(retval[-1]) - 1):
                curr_arr.append(retval[-1][j] + retval[-1][j + 1])
            curr_arr.append(1)
            retval.append(curr_arr)
        return retval[-1]