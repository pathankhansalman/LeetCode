import numpy as np

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m*n
        return np.min(np.array([x[0] for x in ops]))*np.min(np.array([x[1] for x in ops]))
