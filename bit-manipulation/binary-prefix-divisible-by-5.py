class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        #print([int(''.join([str(c) for c in nums[:i+1]])) for i in range(len(nums))])
        full = ''.join([str(num) for num in nums])
        return [int(full[:i+1], base=2) % 5 == 0 for i in range(len(nums))]
