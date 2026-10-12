class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def _self_helper_(arg):
            for char in str(arg):
                if int(char) == 0:
                    return False
                if arg % int(char) != 0:
                    return False
            return True
        retval = []
        for i in range(left, right + 1):
            if _self_helper_(i):
                retval.append(i)
        return retval