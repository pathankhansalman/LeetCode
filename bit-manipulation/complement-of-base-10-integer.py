class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(str(format(n, "b")).replace("0", "2").replace("1", "0").replace("2", "1"), base=2)
