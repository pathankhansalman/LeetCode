class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def point_between(point, rec):
            if rec[0] < point[0] < rec[2] and rec[1] < point[1] < rec[3]:
                return True
            return False
        if rec1 == rec2:
            return True
        if point_between([rec1[0], rec1[1]], rec2) or point_between([rec1[2], rec1[3]], rec2) or point_between([rec2[0], rec2[1]], rec1) or point_between([rec2[2], rec2[3]], rec1):
            return True
        #if rec1[0] == rec2[0] or rec1[2] == rec2[2]:
        if (rec1[1] < rec2[1] < rec1[3] or rec1[1] < rec2[3] < rec1[3] or rec2[1] < rec1[1] < rec2[3] or rec2[1] < rec1[3] < rec2[3]) and (rec1[0] < rec2[0] < rec1[2] or rec1[0] < rec2[2] < rec1[2] or rec2[0] < rec1[0] < rec2[2] or rec2[0] < rec1[2] < rec2[2]):
            return True
        #if rec1[1] == rec2[1] or rec1[3] == rec2[3]:
        return False
