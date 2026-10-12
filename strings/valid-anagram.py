class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
                
        return True

if __name__ == '__main__':
    sol = Solution()
    
    s1, t1 = "anagram", "nagaram"
    print("Test 1 - Expected: True, Got:", sol.isAnagram(s1, t1))
    
    s2, t2 = "rat", "car"
    print("Test 2 - Expected: False, Got:", sol.isAnagram(s2, t2))
