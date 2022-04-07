# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:57:21 2022

@author: patha
"""

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        idx = word.find(ch)
        return ''.join(list(reversed(list(word[:idx+1])))) + word[idx+1:]