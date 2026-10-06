class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_copy = [-1]*len(nums)
        even_idx = 0
        odd_idx = len(nums) - 1
        for num in nums:
            if num %2 == 0:
                nums_copy[even_idx] = num
                even_idx += 1
            else:
                nums_copy[odd_idx] = num
                odd_idx -= 1
        return nums_copy