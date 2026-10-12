class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while 1:
            if s[i] != s[j]:
                str1 = s[:i] + s[i + 1:]
                str2 = s[:j] + s[j + 1:]
                if str1 != ''.join(list(reversed(list(str1)))) and str2 != ''.join(list(reversed(list(str2)))):
                    return False
                else:
                    return True
            i += 1
            j -= 1
            if j < i:
                break
        return True
