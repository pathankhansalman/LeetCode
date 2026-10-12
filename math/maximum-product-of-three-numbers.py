import numpy as np

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        max_from_last = [0]*len(nums)
        max_from_last[len(nums) - 1] = nums[-1]
        for i in range(2, len(nums) + 1):
            max_from_last[len(nums) - i] = max(nums[len(nums) - i], max_from_last[len(nums) - i + 1])
        min_from_last = [0]*len(nums)
        min_from_last[len(nums) - 1] = nums[-1]
        for i in range(2, len(nums) + 1):
            min_from_last[len(nums) - i] = min(nums[len(nums) - i], min_from_last[len(nums) - i + 1])
        two_prod_val = [0]*len(nums)
        two_prod_val[len(nums) - 2] = nums[len(nums) - 1]*nums[len(nums) - 2]
        for i in range(3, len(nums) + 1):
            two_prod_val[len(nums) - i] = max(two_prod_val[len(nums) - i + 1],
                                              nums[len(nums) - i]*max_from_last[len(nums) - i + 1],
                                              nums[len(nums) - i]*min_from_last[len(nums) - i + 1])
        min_two_prod_val = [0]*len(nums)
        min_two_prod_val[len(nums) - 2] = nums[len(nums) - 1]*nums[len(nums) - 2]
        for i in range(3, len(nums) + 1):
            min_two_prod_val[len(nums) - i] = min(min_two_prod_val[len(nums) - i + 1],
                                                  nums[len(nums) - i]*max_from_last[len(nums) - i + 1],
                                                  nums[len(nums) - i]*min_from_last[len(nums) - i + 1])
        three_prod_val = [0]*len(nums)
        three_prod_val[len(nums) - 3] = nums[len(nums) - 3]*two_prod_val[len(nums) - 2]
        for i in range(4, len(nums) + 1):
            three_prod_val[len(nums) - i] = max(three_prod_val[len(nums) - i + 1],
                                                nums[len(nums) - i]*two_prod_val[len(nums) - i + 1],
                                                nums[len(nums) - i]*min_two_prod_val[len(nums) - i + 1])
        return three_prod_val[0]