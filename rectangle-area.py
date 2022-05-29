class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if bx1 >= ax2 or bx2 <= ax1 or ay1 >= by2 or by1 >= ay2:
            return (ax2 - ax1)*(ay2 - ay1) + (bx2 - bx1)*(by2 - by1)
        sx1 = max(ax1, bx1)
        sx2 = min(ax2, bx2)
        sy1 = max(ay1, by1)
        sy2 = min(ay2, by2)
        return (ax2 - ax1)*(ay2 - ay1) + (bx2 - bx1)*(by2 - by1) - (sx2 - sx1)*(sy2 - sy1)