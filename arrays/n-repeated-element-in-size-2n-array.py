class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return num
            my_dict[num] = 1
