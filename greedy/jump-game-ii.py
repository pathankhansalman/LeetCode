# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:56:12 2022

@author: patha
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        def _jump_helper_(idx):
            if nums[idx] >= len(nums) - 1 - idx:
                return 1
            if nums[idx] == 0:
                return -1
            min_jumps = 999999999
            for i in range(1, nums[idx] + 1):
                if nums[i + idx] >= len(nums) - 2 - idx:
                    curr_jumps = 1
                else:
                    curr_jumps = _jump_helper_(idx + i)
                    if curr_jumps == -1:
                        continue
                if curr_jumps < min_jumps:
                    min_jumps = curr_jumps
            return 1 + min_jumps
        return _jump_helper_(0)


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.jump([1, 2]))
