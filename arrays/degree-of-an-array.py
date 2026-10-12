class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        min_idx = {}
        max_idx = {}
        degree = 0
        for i, num in enumerate(nums):
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            if counts[num] > degree:
                degree = counts[num]
            if num not in min_idx:
                min_idx[num] = i
            max_idx[num] = i
        deg_nums = [k for k in counts.keys() if counts[k] == degree]
        return min([max_idx[num] - min_idx[num] for num in deg_nums]) + 1