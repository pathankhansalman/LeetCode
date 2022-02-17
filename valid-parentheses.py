# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:56:59 2022

@author: patha
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mystr = ''
        for char in s:
            if char in ['(', '{', '[']:
                mystr = mystr + char
            if char == ')':
                if mystr == '' or not mystr[-1] == '(':
                    return False
                mystr = mystr[:-1]
            if char == '}':
                if mystr == '' or not mystr[-1] == '{':
                    return False
                mystr = mystr[:-1]
            if char == ']':
                if mystr == '' or not mystr[-1] == '[':
                    return False
                mystr = mystr[:-1]
        if mystr == '':
            return True
        return False


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.isValid('(]'))
