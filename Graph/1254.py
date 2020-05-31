# 1254. Number of Closed Islands

# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).

# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1

# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
 
# Constraints:
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

class Solution(object):
    def closedIsland(self, grid):
        if len(grid) <= 2 or len(grid[0]) <= 2:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        count += 1
        return count
        
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        top = self.dfs(grid, i + 1, j)
        bottom = self.dfs(grid, i - 1, j)
        left = self.dfs(grid, i, j + 1)
        right = self.dfs(grid, i, j - 1)
        
        return top and bottom and left and right