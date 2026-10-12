import numpy as np
from functools import reduce
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) == 1:
            return False
        counts = {}
        for num in deck:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        counts = list(set(list(counts.values())))
        gcd = np.gcd.reduce(counts)
        if gcd > 1:
            return True
        return False