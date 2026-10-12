class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_curr_len = -1
        while i < len(s):
            if i > 0 and i < len(s) - 1:
                if s[i] == s[i + 1]:
                    i += 1
                    continue
            char_set = set()
            j = i
            curr_len = 0
            while j < len(s):
                if s[j] in char_set:
                    if curr_len > max_curr_len:
                        max_curr_len = curr_len
                    i += 1
                    break
                else:
                    char_set.add(s[j])
                    curr_len += 1
                    j += 1
            if j == len(s):
                if curr_len > max_curr_len:
                    max_curr_len = curr_len
                i += 1
        return max_curr_len


if __name__ == '__main__':
    s = 'abcabcabb'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
    s = 'bbbbbbbb'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
    s = 'pwwkew'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
    s = ''
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
    s = 'au'
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
