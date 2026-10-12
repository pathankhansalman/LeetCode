class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if i == 0:
                    area += grid[i][j]
                if i == n - 1:
                    area += grid[i][j]
                if j == 0:
                    area += grid[i][j]
                if j == n - 1:
                    area += grid[i][j]
                if i != 0:
                    area += max(grid[i][j] - grid[i - 1][j], 0)
                if j != 0:
                    area += max(grid[i][j] - grid[i][j - 1], 0)
                if i != n - 1:
                    area += max(grid[i][j] - grid[i + 1][j], 0)
                if j != n - 1:
                    area += max(grid[i][j] - grid[i][j + 1], 0)
                if grid[i][j] != 0:
                    area += 2
        return area
                        
                
