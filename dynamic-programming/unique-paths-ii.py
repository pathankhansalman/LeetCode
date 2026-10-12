# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 00:14:04 2022

@author: patha
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def _un_path_helper_(arg_x, arg_y):
            nonlocal mem_dict
            if obstacleGrid[arg_x][arg_y] == 1:
                return 0
            if arg_x == m - 1 and arg_y == n - 1:
                return 1
            if (arg_x, arg_y) in mem_dict.keys():
                return mem_dict[(arg_x, arg_y)]
            retval = 0
            if arg_x < m - 1:
                if (arg_x + 1, arg_y) not in mem_dict.keys():
                    mem_dict[(arg_x + 1, arg_y)] = _un_path_helper_(arg_x + 1, arg_y)
                retval += mem_dict[(arg_x + 1, arg_y)]
            if arg_y < n - 1:
                if (arg_x, arg_y + 1) not in mem_dict.keys():
                    mem_dict[(arg_x, arg_y + 1)] = _un_path_helper_(arg_x, arg_y + 1)
                retval += mem_dict[(arg_x, arg_y + 1)]
            return retval
        mem_dict = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return _un_path_helper_(0, 0)