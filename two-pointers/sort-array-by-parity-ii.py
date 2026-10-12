class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odds = []
        evens = []
        for num in nums:
            if num %2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        retval = []
        for i in range(len(evens)):
            retval.append(evens[i])
            retval.append(odds[i])
        return retval