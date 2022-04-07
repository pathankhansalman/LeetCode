# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:45:59 2022

@author: patha
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sorted_nums = list(sorted(list(set(nums))))
        max_seq_len = 1
        curr_seq_len = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                curr_seq_len += 1
            else:
                if curr_seq_len > max_seq_len:
                    max_seq_len = curr_seq_len
                curr_seq_len = 1
        return max(curr_seq_len, max_seq_len)