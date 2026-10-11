class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_arr = []
        for char in s:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                rev_arr.append(char)
        rev_arr = list(reversed(rev_arr))
        idx = 0
        retval = []
        for char in s:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                retval.append(rev_arr[idx])
                idx += 1
            else:
                retval.append(char)
        return ''.join(retval)