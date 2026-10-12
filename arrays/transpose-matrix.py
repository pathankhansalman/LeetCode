class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        retval = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            curr_arr = []
            for j in range(m):
                curr_arr.append(0)
            retval.append(curr_arr)
        for i in range(m):
            for j in range(n):
                retval[j][i] = matrix[i][j]
        return retval
