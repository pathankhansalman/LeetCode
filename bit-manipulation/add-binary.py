# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:04:29 2022

@author: patha
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')