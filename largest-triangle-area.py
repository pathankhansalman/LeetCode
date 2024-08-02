import itertools
import numpy as np

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def _get_dist_(arg):
            return np.sqrt((arg[1][0] - arg[0][0])**2 + (arg[1][1] - arg[0][1])**2)
        def _get_area_(arg):
            print(arg)
            sides = [_get_dist_(x) for x in list(itertools.combinations(arg, 2))]
            a = sides[0]
            b = sides[1]
            c = sides[2]
            s = (a + b + c)/2.0
            return np.sqrt(s*(s - a)*(s - b)*(s - c))
        return max([_get_area_(x) for x in list(itertools.combinations(points, 3))])
