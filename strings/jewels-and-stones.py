class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        retval = 0
        for char in stones:
            if char in jewels:
                retval += 1
        return retval