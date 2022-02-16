# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:04:30 2022

@author: patha
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        curr_prefix = ''
        for i in range(len(strs[0])):
            curr_search = strs[0][0:i + 1]
            for mystr in strs:
                if not mystr.startswith(curr_search):
                    return curr_prefix
            curr_prefix = curr_search
        return curr_prefix


if __name__ == '__main__':
    mysol = Solution()
    strs = ["flower","flow","flight"]
    print(mysol.longestCommonPrefix(strs))
