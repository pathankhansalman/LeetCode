class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_str = format(n, "b")
        for i in range(len(bin_str) - 1):
            if bin_str[i] == bin_str[i + 1]:
                return False
        return True