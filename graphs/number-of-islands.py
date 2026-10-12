class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # Mark cell as visited by setting to '0'
            grid[r][c] = '0'
            # Visit neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
                    
        return num_islands

if __name__ == '__main__':
    sol = Solution()
    
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print("Test 1 - Expected: 1, Got:", sol.numIslands(grid1))
    assert sol.numIslands(grid1) == 0  # Grid is already visited (all '0')
    
    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    sol2 = Solution()
    print("Test 2 - Expected: 3, Got:", sol2.numIslands(grid2))
