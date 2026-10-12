class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            return True
        for i in range(m - 2, -1, -1):
            for j in range(0, n - 1):
                start_x = j
                start_y = i
                start_val = matrix[i][j]
                while 1:
                    if start_x >= n or start_y >= m:
                        break
                    if matrix[start_y][start_x] != start_val:
                        return False
                    start_x += 1
                    start_y += 1
        return True