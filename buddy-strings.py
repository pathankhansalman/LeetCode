class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        idxs = []
        count = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                idxs.append(i)
                count += 1
        char_dict = {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
        if count == 0:
            if max([v for _, v in char_dict.items()]) > 1:
                return True
            return False
        if count != 2:
            return False
        if s[idxs[0]] == goal[idxs[1]] and s[idxs[1]] == goal[idxs[0]]:
            return True
        return False