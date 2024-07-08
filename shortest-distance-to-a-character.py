class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        dist_left = [10**5]*len(s)
        dist_right = [10**5]*len(s)
        for i in range(len(s)):
            if s[i] == c:
                dist_left[i] = 0
                dist_right[i] = 0
        if s[0] != c:
            dist_left[0] = 10**5
        if s[-1] != c:
            dist_right[-1] = 10**5
        for i in range(1, len(s)):
            if s[i] != c:
                if dist_left[i - 1] == 10**5:
                    dist_left[i] = 10**5
                else:
                    dist_left[i] = dist_left[i - 1] + 1
            if s[len(s) - i - 1] != c:
                if dist_right[len(s) - i] == 10**5:
                    dist_right[len(s) - i - 1] = 10**5
                else:
                    dist_right[len(s) - i - 1] = dist_right[len(s) - i] + 1
        return [min(dist_left[i], dist_right[i]) for i in range(len(s))]
