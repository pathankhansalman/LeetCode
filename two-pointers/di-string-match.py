class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if len(s) == 1:
            if s[0] == "I":
                return [0, 1]
            else:
                return [1, 0]
        start = 0
        max_val = len(s)
        perms = []
        for char in s:
            if char == "D":
                perms.append(max_val)
                max_val -= 1
            if char == "I":
                perms.append(start)
                start += 1
        return perms + [start]