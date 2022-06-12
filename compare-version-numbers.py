# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:41:49 2022

@author: patha
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = [int(x) for x in version1.split('.')]
        version2_list = [int(x) for x in version2.split('.')]
        while len(version1_list) < len(version2_list):
            version1_list.append(0)
        while len(version2_list) < len(version1_list):
            version2_list.append(0)
        for i in range(len(version1_list)):
            if version1_list[i] > version2_list[i]:
                return 1
            elif version1_list[i] < version2_list[i]:
                return -1
        return 0