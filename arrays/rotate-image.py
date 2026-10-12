# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 00:40:10 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [np.array(x) for x in matrix]
        matrix[:] = [list(reversed(x)) for x in np.array(matrix).T]
        return None