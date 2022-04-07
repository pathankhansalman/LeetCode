# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:05:54 2022

@author: patha
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print('{0:b}'.format(n))
        return ('{0:b}'.format(n)).count('1')