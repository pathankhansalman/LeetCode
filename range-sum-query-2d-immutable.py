class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.area_mat = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            self.area_mat.append([0]*n)
        self.area_mat[m - 1][n - 1] = matrix[m - 1][n - 1]
        for i in range(n - 2, -1, -1):
            self.area_mat[m - 1][i] = self.area_mat[m - 1][i + 1] + matrix[m - 1][i]
        for j in range(m - 2, -1, -1):
            self.area_mat[j][n - 1] = self.area_mat[j + 1][n - 1] + matrix[j][n - 1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                self.area_mat[i][j] = matrix[i][j] + self.area_mat[i][j + 1] + self.area_mat[i + 1][j] - self.area_mat[i + 1][j + 1]
        # print(self.area_mat)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        m = len(self.area_mat)
        n = len(self.area_mat[0])
        if row2 == m - 1 and col2 == n - 1:
            return self.area_mat[row1][col1]
        elif row2 == m - 1:
            return self.area_mat[row1][col1] - self.area_mat[row1][col2 + 1]
        elif col2 == n - 1:
            return self.area_mat[row1][col1] - self.area_mat[row2 + 1][col1]
        else:
            return self.area_mat[row1][col1] - self.area_mat[row1][col2 + 1] - self.area_mat[row2 + 1][col1] + self.area_mat[row2 + 1][col2 + 1] 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)