class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while 1:
            if i > j:
                return -1
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if i == j:
                return -1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
