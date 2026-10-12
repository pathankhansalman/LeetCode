# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 23:58:49 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [x[0] for x in matrix]
        mat_arr = np.array([np.array(x) for x in matrix])
        mylist = []
        while mat_arr.size > 0:
            m = len(mat_arr)
            n = len(mat_arr[0])
            if m == 1:
                mylist += list(mat_arr[0])
                break
            elif n == 1:
                mylist += [x[0] for x in mat_arr]
                break
            count = 2*(m + n) - 4
            i = 0
            idx_col = 0
            idx_row = 0
            curr_max_col = n - 1
            curr_max_row = m - 1
            curr_min_col = 0
            curr_min_row = 0
            while i < count:
                # print(idx_row, idx_col)
                mylist.append(mat_arr[idx_row][idx_col])
                if idx_row == curr_max_row:
                    if idx_col == curr_min_col:
                        curr_max_row -= 1
                        idx_row -= 1
                    else:
                        idx_col -= 1
                elif idx_col == curr_max_col:
                    idx_row += 1
                else:
                    idx_col += 1
                i += 1
            mat_arr = mat_arr[1:-1, 1:-1]
        return mylist