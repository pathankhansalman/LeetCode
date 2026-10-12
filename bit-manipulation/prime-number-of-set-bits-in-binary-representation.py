class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        retval = 0
        for i in range(left, right + 1):
            str_i = "{0:b}".format(i)
            curr_count = 0
            for char in str_i:
                if char == '1':
                    curr_count += 1
            if curr_count in primes:
                retval += 1
        return retval