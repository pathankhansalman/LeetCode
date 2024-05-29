class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left_sum = [0, nums[0]]
        right_sum = [nums[-1], 0]
        for i in range(1, len(nums) - 1):
            left_sum.append(left_sum[-1] + nums[i])
            right_sum = [nums[len(nums) - i - 1] + right_sum[0]] + right_sum
        # print(left_sum, right_sum)
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
