class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = list(sorted(nums))
        for i, num in enumerate(nums):
            if num == nums_sorted[-1]:
                break
        if nums_sorted[-1] >= 2*nums_sorted[-2]:
            return i
        return -1
