# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:25:56 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        un_intervals = [list(y) for y in list(set([tuple(x) for x in intervals]))]
        int_arr = np.zeros(10**4 + 1)
        for interval in un_intervals:
            int_arr[interval[0]:interval[1]] = 1
        ranges = []
        range_start = False
        start_idx = -1
        end_idx = -1
        for i in range(len(int_arr)):
            if int_arr[i] == 1 and not range_start:
                start_idx = i
                range_start = True
                continue
            if int_arr[i] == 0 and range_start:
                end_idx = i
                ranges.append([start_idx, end_idx])
                start_idx = -1
                range_start = False
                continue
        for interval in un_intervals:
            if interval[0] == interval[1] and int_arr[interval[0]] != 1 and int_arr[max(0, interval[0] - 1)] != 1:
                ranges.append(interval)
        return ranges