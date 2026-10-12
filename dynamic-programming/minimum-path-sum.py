# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:25:48 2022

@author: patha
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def _min_path_helper_(arg_x, arg_y):
            nonlocal mem_dict
            if arg_x == m - 1 and arg_y == n - 1:
                return grid[arg_x][arg_y]
            if (arg_x, arg_y) in mem_dict.keys():
                return mem_dict[(arg_x, arg_y)]
            retval = grid[arg_x][arg_y]
            rest_min = 999999999999
            if arg_x < m - 1:
                if (arg_x + 1, arg_y) not in mem_dict.keys():
                    mem_dict[(arg_x + 1, arg_y)] = _min_path_helper_(arg_x + 1, arg_y)
                if mem_dict[(arg_x + 1, arg_y)] < rest_min:
                    rest_min = mem_dict[(arg_x + 1, arg_y)]
            if arg_y < n - 1:
                if (arg_x, arg_y + 1) not in mem_dict.keys():
                    mem_dict[(arg_x, arg_y + 1)] = _min_path_helper_(arg_x, arg_y + 1)
                if mem_dict[(arg_x, arg_y + 1)] < rest_min:
                    rest_min = mem_dict[(arg_x, arg_y + 1)]
            retval += rest_min
            mem_dict[(arg_x, arg_y)] = retval
            return retval
        mem_dict = {}
        m = len(grid)
        n = len(grid[0])
        return _min_path_helper_(0, 0)