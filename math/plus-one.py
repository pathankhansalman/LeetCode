# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:00:40 2022

@author: patha
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(y) for y in list(str(int(''.join([str(x) for x in digits])) + 1))]