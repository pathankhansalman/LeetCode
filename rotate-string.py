class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        mod_s = s
        for i in range(len(s)):
            if mod_s == goal:
                return True
            mod_s = mod_s[1:] + mod_s[0]
        return False