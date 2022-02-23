# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:49:26 2022

@author: patha
"""
import numpy as np

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # First, maintain range sums and range bool
        # With ( as 1 and ) as -1, range sum must be 0 for a valid string
        # Rolling range sum can't be negative. Maintain negative or not
        # DP
        # arr[i, j] : range val for int_s starts at i, len j
        # arr[i, 0] = 1
        # arr[i, j] = arr[i, j - 1] + int_s[i + j]
        # arr_bool[i, j]: range bool for int_s starts at i, len j
        # arr_bool[i, 0] = False
        # arr_bool[i, j] = arr_bool[i, j - 1] or (arr[i, j - 1] + int_s[i + j] < 0)
        # Change to one-D array
        if len(s) < 2:
            return 0
        # Can pre-allocate s_int
        s_int = []
        filt_s = ''
        start_add = False
        for mychr in s:
            if mychr == ')':
                if not start_add:
                    continue
            else:
                start_add = True
            filt_s += mychr
        for mychr in filt_s:
            if mychr == '(':
                s_int.append(1)
            else:
                s_int.append(-1)
        s_int = np.array(s_int, dtype=int)
        filt_len = len(filt_s)
        curr_sum = np.empty(filt_len, dtype=int)
        curr_bool = np.empty(filt_len, dtype=bool)
        prev_sum = np.empty(filt_len, dtype=int)
        prev_bool = np.empty(filt_len, dtype=bool)
        prev_sum[:] = 0
        prev_bool[:] = False
        curr_sum[:] = 0
        curr_bool[:] = False
        curr_max_len = 0
        for j in range(1, filt_len + 1):
            curr_sum = np.copy(prev_sum)
            curr_sum[:filt_len - j + 1] += s_int[j - 1:]
            curr_bool = np.copy(prev_bool)
            curr_bool[:filt_len - j + 1] = np.logical_or(curr_bool[:filt_len - j + 1],
                                                              (prev_sum[:filt_len - j + 1] +
                                                               s_int[j - 1:]) < 0)
            inter = np.where((curr_sum[:filt_len - j + 1] == 0) & ~curr_bool[:filt_len - j + 1])
            prev_sum = np.copy(curr_sum)
            prev_bool = np.copy(curr_bool)
            if inter[0].size == 0:
                continue
            curr_max_len = j
        return curr_max_len


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.longestValidParentheses(')()())'))
