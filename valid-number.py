# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:46:28 2022

@author: patha
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in ['inf', '-inf', '+inf', 'Infinity', '-Infinity', '+Infinity']:
            return False
        try:
            float(s)
            return True
        except:
            return False