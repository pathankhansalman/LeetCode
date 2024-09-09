class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        empty_s = ""
        for char in s:
            if char != "#":
                empty_s += char
            else:
                empty_s = empty_s[:-1]
        empty_t = ""
        for char in t:
            if char != "#":
                empty_t += char
            else:
                empty_t = empty_t[:-1]
        return empty_s == empty_t