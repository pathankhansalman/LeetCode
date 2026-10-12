# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:51:12 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        un_intervals = [list(y) for y in list(set([tuple(x) for x in intervals]))]
        int_arr = np.zeros(max(intervals[-1][1], newInterval[1]) + 1)
        int_arr_sing = np.zeros(max(intervals[-1][1], newInterval[1]) + 1)
        for interval in un_intervals:
            if interval[0] == interval[1]:
                int_arr_sing[interval[0]] = 1
            else:
                int_arr[interval[0]:interval[1]] = 1
        if newInterval[0] == newInterval[1]:
            int_arr_sing[newInterval[0]] = 1
        else:
            int_arr[newInterval[0]:newInterval[1]] = 1
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
        for i in range(len(int_arr_sing)):
            if int_arr_sing[i] == 1:
                if int_arr[i] == 1 or int_arr[max(i - 1, 0)] == 1:
                    continue
                ranges.append([i, i])
        # print(ranges)
        return list(sorted(ranges, key=lambda x:x[0]))