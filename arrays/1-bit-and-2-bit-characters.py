class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        while 1:
            if bits == [1, 0] or bits == [1, 1]:
                return False
            if len(bits) == 1:
                return True
            if bits[0] == 0:
                bits = bits[1:]
            else:
                bits = bits[2:]
