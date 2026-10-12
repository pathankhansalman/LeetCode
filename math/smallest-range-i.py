class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = 10**9
        max_val = -10**9
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        return max(max_val - min_val - 2*k, 0)