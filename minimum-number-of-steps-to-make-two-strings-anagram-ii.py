# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:03:56 2022

@author: patha
"""

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        counts_s = {}
        for k in s:
            if k not in counts_s.keys():
                counts_s[k] = 1
            else:
                counts_s[k] += 1
        counts_t = {}
        for k in t:
            if k not in counts_t.keys():
                counts_t[k] = 1
            else:
                counts_t[k] += 1
        retval = 0
        for k_s in counts_s.keys():
            if k_s not in counts_t.keys():
                retval += counts_s[k_s]
            elif counts_s[k_s] > counts_t[k_s]:
                retval += (counts_s[k_s] - counts_t[k_s])
        for k_t in counts_t.keys():
            if k_t not in counts_s.keys():
                retval += counts_t[k_t]
            elif counts_t[k_t] > counts_s[k_t]:
                retval += (counts_t[k_t] - counts_s[k_t])
        return retval