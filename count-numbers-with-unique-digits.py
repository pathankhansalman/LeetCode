class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _get_nums_(arg):
            if arg == 0:
                return 1
            if arg == 1:
                return 9
            retval = 9
            for i in range(arg - 1):
                retval *= (9 - i)
            return retval
        retval_out = 0
        for i in range(n + 1):
            retval_out += _get_nums_(i)
        return retval_out