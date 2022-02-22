# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 01:31:05 2022

@author: patha
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def _gen_helper_(arg):
            if arg == 1:
                return ['()']
            retval = ['()' + x for x in _gen_helper_(arg - 1)] +\
                ['(' + x + ')' for x in _gen_helper_(arg - 1)] +\
                [x + '()' for x in _gen_helper_(arg - 1)]
            for i in range(2, arg - 1):
                retval += [x + y for x in _gen_helper_(i) for y in _gen_helper_(arg - i)]
            return retval
        return list(set(_gen_helper_(n)))


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.generateParenthesis(4))
