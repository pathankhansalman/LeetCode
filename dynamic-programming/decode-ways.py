# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:59:29 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        nums = [0]*len(s)
        nums[-1] = np.sign(int(s[-1]))
        n = len(s)
        for i in range(n-2, -1, -1):
            print(s[i:i+2])
            if s[i] == '0':
                nums[i] = 0
            else:
                if int(s[i:i+2]) < 27 and '0' not in s[i:i+2]:
                    if i < n - 2:
                        nums[i] = nums[i + 2] + nums[i + 1]
                    else:
                        nums[i] = 2
                elif '0' in s[i:i+2]:
                    if i < n - 2:
                        if int(s[i:i+2]) > 27:
                            nums[i] = 0
                        else:
                            nums[i] = nums[i + 2]
                    else:
                        if int(s[i:i+2]) > 27:
                            nums[i] = 0
                        else:
                            nums[i] = 1
                else:
                    if i < n - 2:
                        nums[i] = nums[i + 1]
                    else:
                        nums[i] = 1
        print(nums)
        return nums[0]