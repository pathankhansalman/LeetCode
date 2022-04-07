# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:57:46 2022

@author: patha
"""

import numpy as np
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        rat_dict = {}
        for rectangle in rectangles:
            ratio = rectangle[0]/rectangle[1]
            if ratio not in rat_dict.keys():
                rat_dict[ratio] = 1
            else:
                rat_dict[ratio] += 1
        return int(np.sum([(v * (v - 1))/2 for v in rat_dict.values()]))