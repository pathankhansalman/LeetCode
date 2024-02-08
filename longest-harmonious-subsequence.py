class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_vals = {}
        for num in nums:
            if num not in count_vals:
                count_vals[num] = 0
            count_vals[num] += 1
        maxlen = 0
        for i in range(len(nums)):
            if max(count_vals.get(nums[i] + 1, 0), count_vals.get(nums[i] - 1, 0)) > 0:
                if count_vals.get(nums[i]) + max(count_vals.get(nums[i] + 1, 0), count_vals.get(nums[i] - 1, 0)) > maxlen:
                    maxlen = count_vals.get(nums[i]) + max(count_vals.get(nums[i] + 1, 0), count_vals.get(nums[i] - 1, 0))
            count_vals[nums[i]] -= 1
        return maxlen
