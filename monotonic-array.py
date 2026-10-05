class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        dirn = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] < 0:
                if dirn == 1:
                    return False
                dirn = -1
            if nums[i] - nums[i - 1] > 0:
                if dirn == -1:
                    return False
                dirn = 1
        return True