# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:00:29 2022

@author: patha
"""

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return len([x for x in words if x.startswith(pref)])