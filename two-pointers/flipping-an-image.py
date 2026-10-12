class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        retval = []
        for i in range(n):
            curr = [abs(1 - x) for x in reversed(image[i])]
            retval.append(curr)
        return retval