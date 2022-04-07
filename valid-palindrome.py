# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:33:40 2022

@author: patha
"""

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = re.sub('[^0-9a-zA-Z]+', '', s.lower())
        # print(new_s)
        if len(new_s) <= 1:
            return True
        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False
        return True