class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)*len(mat[0]) != r*c:
            return mat
        retval = []
        for i in range(r):
            retval.append([0]*c)
        i = 0
        j = 0
        k = 0
        l = 0
        while 1:
            retval[k][l] = mat[i][j]
            l += 1
            if l > c - 1:
                k += 1
                l = 0
            if k > r - 1:
                break
            j += 1
            if j > len(mat[0]) - 1:
                i += 1
                j = 0
            if i > len(mat) - 1:
                break
        return retval
