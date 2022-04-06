# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:52:40 2022

@author: patha
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        if m == n:
            if s == t:
                return 1
            return 0
        val = []
        for j in range(n):
            val_row = []
            for i in range(m):
                val_row.append(0)
            val.append(val_row)
        for i in range(n - 1, -1, -1):
            # print(val)
            for j in range(m - 1, -1, -1):
                if m - j < n - i:
                    continue
                elif i == n - 1 and j == m - 1:
                    if t[i] == s[j]:
                        val[i][j] = 1
                elif i == n - 1:
                    if t[i] == s[j]:
                        val[i][j] = 1 + val[i][j + 1]
                    else:
                        val[i][j] = val[i][j + 1]
                elif m - j == n - i:
                    # print('here', t[i], s[j])
                    if t[i] == s[j]:
                        # print('here')
                        val[i][j] = val[i + 1][j + 1]
                else:
                    if s[j] == t[i]:
                        val[i][j] = val[i + 1][j + 1] + val[i][j + 1]
                    else:
                        val[i][j] = val[i][j + 1]
        # print(val)
        return val[0][0]