import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Without making it a string
        if x < 0:
            return False
        if x < 10:
            return True
        if x < 100:
            if int(x/10) == x % 10:
                return True
            return False
        if x % 10 == 0:
            return False
        revint = 0
        curr = x
        xpow = math.floor(math.log10(curr))
        while curr > 0:
            print(revint, curr, xpow)
            revint += (curr % 10)*(10**xpow)
            curr = math.floor(curr/10)
            xpow -= 1
        if revint == x:
            return True
        return False
