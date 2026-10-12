class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        typedict = {}
        for ctype in candyType:
            if ctype not in typedict:
                typedict[ctype] = 0
            typedict[ctype] += 1
        return min(len(typedict), len(candyType)/2)
