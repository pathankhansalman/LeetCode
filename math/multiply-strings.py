# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:55:53 2022

@author: patha
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1
        return str(int(num1)*int(num2))