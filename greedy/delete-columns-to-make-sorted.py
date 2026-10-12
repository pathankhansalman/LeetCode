class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(strs[0])):
            curr_str = [string[i] for string in strs]
            if curr_str != sorted(curr_str):
                count += 1
        return count