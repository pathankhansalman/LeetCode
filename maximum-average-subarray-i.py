class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        retval = 0
        for i in range(k):
            retval += nums[i]
        if k == len(nums):
            return retval/(1.0*k)
        max_sum = retval
        for i in range(k, len(nums)):
            max_sum -= nums[i - k]
            max_sum += nums[i]
            if max_sum > retval:
                retval = max_sum
        return retval/(1.0*k)
