# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:49:10 2022

@author: patha
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = {k: 1 for k in wordDict}
        if s in wordset.keys():
            return True
        can_flag = [False]*len(s)
        if s[-1] in wordset.keys():
            can_flag[-1] = True
        for i in range(len(s) - 2, -1, -1):
            if s[i:] in wordset.keys():
                can_flag[i] = True
                continue
            curr_can = False
            for j in range(i + 1, len(s)):
                if s[i:j] in wordset.keys():
                    curr_can = curr_can or can_flag[j]
                    if curr_can:
                        break
            can_flag[i] = curr_can
        return can_flag[0]