# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:07:16 2022

@author: patha
"""
import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mymap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return mymap[digits]
        return [''.join(x) for x in
                list(itertools.product(*[mymap[k] for k in list(digits)]))]
        

if __name__ == '__main__':
    mysol = Solution()
    print(mysol.letterCombinations('2345'))
