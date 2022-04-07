# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:56:53 2022

@author: patha
"""

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        win_list = [0]*100001
        loss_list = [0]*100001
        for match in matches:
            win_list[match[0]] += 1
            loss_list[match[1]] += 1
        retval = [[], []]
        for k in range(100001):
            if win_list[k] > 0 and loss_list[k] == 0:
                retval[0].append(k)
            elif loss_list[k] == 1:
                retval[1].append(k)
        #retval[0].sort()
        #retval[1].sort()
        return retval