# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:00:43 2022

@author: patha
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def _check_(val, arg_row, arg_col):
            if val in arr[arg_row]:
                return False
            for x in arr:
                if x[arg_col] == val:
                    return False
            for i in range(arg_row - arg_row % 3, arg_row - arg_row % 3 + 3):
                for j in range(arg_col - arg_col % 3, arg_col - arg_col % 3 + 3):
                    if arr[i][j] == val:
                        return False
            return True
        def _solve_sudoku_helper_():
            nonlocal board
            for i in range(9):
                for j in range(9):
                    if arr[i][j] == 0:
                        for k in range(1, 10):
                            if _check_(k, i, j):
                                arr[i][j] = k
                                _solve_sudoku_helper_()
                                arr[i][j] = 0
                        return None
            print(arr)
            board[:] = [[str(x) for x in y] for y in arr]
        arr = [[int(x) for x in ['0' if z == '.' else z
                for z in y]] for y in board]
        _solve_sudoku_helper_()
