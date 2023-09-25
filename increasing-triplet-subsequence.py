class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        rolling_min = [0]*len(nums)
        rolling_min[0] = nums[0]
        curr_min = nums[0]
        for i, num in enumerate(nums[1:]):
            if num < curr_min:
                curr_min = num
            rolling_min[i + 1] = curr_min
        rolling_max = [0]* len(nums)
        rolling_max[-1] = nums[-1]
        curr_max = nums[-1]
        for i, num in enumerate(list(reversed(nums))[1:]):
            if num > curr_max:
                curr_max = num
            rolling_max[len(nums) - i - 2] = curr_max
        for i in range(1, len(nums) - 1):
            if rolling_min[i - 1] < nums[i] < rolling_max[i + 1]:
                return True
        return False
