# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:25:53 2022

@author: patha
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        if t in s:
            return t
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return s
            else:
                return ''
        dict_t = {}
        for char in t:
            if char not in dict_t.keys():
                dict_t[char] = 1
            else:
                dict_t[char] += 1
        curr_dict = {}
        start = 0
        end = 0
        curr_dict[s[start]] = 1
        min_len = 999999999
        min_str = ''
        while 1:
            valid_substr = True
            for key in dict_t.keys():
                if key not in curr_dict.keys():
                    valid_substr = False
                elif curr_dict[key] < dict_t[key]:
                    valid_substr = False
            if valid_substr:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_str = s[start:end+1]
            inc = False
            if end < len(s) - 1:
                end += 1
                inc = True
                if s[end] not in curr_dict.keys():
                    curr_dict[s[end]] = 1
                else:
                    curr_dict[s[end]] += 1
            dec = False
            while 1:
                if s[start] not in dict_t.keys():
                    if start < end:
                        curr_dict[s[start]] -= 1
                        start += 1
                        dec = True
                        continue
                    else:
                        break
                elif curr_dict[s[start]] > dict_t[s[start]]:
                    if start < end:
                        curr_dict[s[start]] -= 1
                        start += 1
                        dec = True
                        continue
                    else:
                        break
                else:
                    break
            if not (dec or inc):
                break
        return min_str