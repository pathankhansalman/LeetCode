# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:21:13 2022

@author: patha
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        return haystack.find(needle)