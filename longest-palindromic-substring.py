from copy import deepcopy


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        is_palin_arr = [0]*(len(s))
        curr_arr = [1]*(len(s) - 1)
        is_palin_arr[0] = curr_arr
        curr_len = 2
        while curr_len <= len(s):
            curr_arr = []
            for i in range(len(s) - curr_len + 1):
                j = i + curr_len
                if curr_len == 2:
                    if s[i] == s[j - 1]:
                        curr_arr.append(1)
                    else:
                        curr_arr.append(0)
                else:
                    if (s[i] == s[j - 1]) and\
                            (is_palin_arr[curr_len - 3][i + 1] == 1):
                        curr_arr.append(1)
                    else:
                        curr_arr.append(0)
            is_palin_arr[curr_len - 1] = curr_arr
            curr_len += 1
        substr_found = False
        for i in range(len(is_palin_arr)):
            curr_arr = is_palin_arr[len(is_palin_arr) - i - 1]
            for j, k in enumerate(curr_arr):
                if k == 1:
                    substr = s[j:(j + len(is_palin_arr) - i)]
                    substr_found = True
                    break
            if substr_found:
                break
        return substr


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))
    s = Solution()
    print(s.longestPalindrome('cbbd'))
    s = Solution()
    print(s.longestPalindrome('a'))
    s = Solution()
    print(s.longestPalindrome('ac'))
    s = Solution()
    print(s.longestPalindrome('321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123'))
