# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:53:29 2022

@author: patha
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if ' ' not in s:
            return len(s)
        return len(s.strip().split(' ')[-1])
        