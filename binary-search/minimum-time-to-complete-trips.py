# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:02:23 2022

@author: patha
"""

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        if len(time) == 1:
            return time[0]*totalTrips
        max_int = min(time)*totalTrips
        left = 0
        right = max_int
        while left < right:
            mid = (left + right) // 2
            curr_sum = sum(mid // t for t in time)
            if curr_sum < totalTrips:
                left = mid + 1
            else:
                right = mid
        return left