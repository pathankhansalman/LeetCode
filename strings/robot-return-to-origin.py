class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for char in moves:
            if char == "U":
                y += 1
            elif char == "L":
                x -= 1
            elif char == "D":
                y -= 1
            elif char == "R":
                x += 1
        if x == 0 and y == 0:
            return True
        return False
        