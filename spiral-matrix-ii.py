# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:15:07 2022

@author: patha
"""

import numpy as np
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def _gen_mat_(arg, top_left, curr_n):
            # print(arg, curr_n, top_left)
            if curr_n == 2:
                retval = np.array([arg[:-2], list(reversed(arg[-2:]))])
                # print(retval)
                if not top_left:
                    return np.rot90(np.rot90(retval))
                return retval
            # print(top_left)
            retval = _gen_mat_(arg[2*curr_n - 1:], not top_left, curr_n - 1)
            # print(retval)
            # print(np.array(arg[curr_n:2*curr_n - 1]).T)
            if top_left:
                retval = np.hstack((retval, np.array([arg[curr_n:2*curr_n - 1]]).T))
                retval = np.insert(retval, 0, arg[:curr_n], axis=0)
            else:
                retval = np.hstack((np.array([list(reversed(arg[curr_n:2*curr_n - 1]))]).T, retval))
                retval = np.insert(retval, len(retval), list(reversed(arg[:curr_n])), axis=0)
            # if not top_left:
            #     return np.rot90(np.rot90(retval))
            return retval
        if n == 1:
            return [[1]]
        retval = _gen_mat_(list(range(1, n**2 + 1)), True, n)
        return ([list(x) for x in retval])


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.generateMatrix(3))
