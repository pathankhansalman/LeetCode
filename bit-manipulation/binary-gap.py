class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = "{0:b}".format(n)
        count_1 = 0
        start_idx = -1
        max_dist = 0
        curr_dist = 0
        for i, char in enumerate(list(bin_str)):
            if char == "1":
                count_1 += 1
                if start_idx != -1:
                    curr_dist = i - start_idx
                    if curr_dist > max_dist:
                        max_dist = curr_dist
                start_idx = i
        return max_dist
