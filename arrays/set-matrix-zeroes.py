# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 23:07:55 2022

@author: patha
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_idxs = []
        col_idxs = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_idxs.append(i)
                    col_idxs.append(j)
        for i in row_idxs:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in col_idxs:
                matrix[i][j] = 0
        return None