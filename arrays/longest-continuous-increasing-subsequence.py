class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 1
        curr_max_len = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                curr_max_len += 1
            else:
                if curr_max_len > max_len:
                    max_len = curr_max_len
                curr_max_len = 1
        if curr_max_len > max_len:
            max_len = curr_max_len
        return max_len