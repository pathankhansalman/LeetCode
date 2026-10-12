# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:56:22 2022

@author: patha
"""

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        curr_hrs = int(current.split(':')[0])
        corr_hrs = int(correct.split(':')[0])
        curr_mins = int(current.split(':')[1])
        corr_mins = int(correct.split(':')[1])
        diff_hrs = corr_hrs - curr_hrs
        diff_mins = corr_mins - curr_mins
        if diff_mins < 0:
            diff_hrs -= 1
            diff_mins += 60
        diff_mins += (diff_hrs)*60
        num_changes = diff_mins // 60
        diff_mins = diff_mins % 60
        num_changes += diff_mins // 15
        diff_mins = diff_mins % 15
        num_changes += (diff_mins // 5)
        diff_mins = diff_mins % 5
        num_changes += diff_mins
        return num_changes