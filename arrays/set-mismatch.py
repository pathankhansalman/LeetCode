class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_dict = {num:0 for num in range(1, len(nums) + 1)}
        for num in nums:
            count_dict[num] += 1
        return [k for k, v in count_dict.items() if v == 2] + [k for k, v in count_dict.items() if v == 0]
