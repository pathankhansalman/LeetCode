# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 01:20:16 2022

@author: patha
"""

import numpy as np

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        arr = np.array([np.array([int(x) for x in ['0' if z == '.' else z for z in y]]) for y in board], dtype=float)
        arr[arr == 0] = np.nan
        # print(arr)
        for i in range(9):
            _, c = np.unique(arr[i, :], return_counts=True)
            if c.max() > 1:
                return False
            # if np.all(np.isnan(arr[i, :])):
            #    return False
            _, c = np.unique(arr[:, i], return_counts=True)
            if c.max() > 1:
                return False
            # if np.all(np.isnan(arr[:, i])):
            #    return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                _, c = np.unique(arr[i:i+3, j:j+3], return_counts=True)
                # print(c)
                if c.max() > 1:
                    return False
        return True