# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 00:50:40 2022

@author: patha
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        an_dict = {}
        for mystr in strs:
            sorted_str = ''.join(list(sorted(mystr)))
            if sorted_str in an_dict.keys():
                an_dict[sorted_str].append(mystr)
            else:
                an_dict[sorted_str] = [mystr]
        return list(an_dict.values())