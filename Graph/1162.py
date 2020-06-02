# 1162. As Far from Land as Possible

# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# If no land or water exists in the grid, return -1.

# Example 1:
# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.

# Example 2:
# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
 
# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1

class Solution(object):
    def maxDistance(self, grid):
        n = len(grid)
        
        visited = set()
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            i, j = queue.pop(0)
            ans = max(ans, grid[i][j] - 1)
            for dirr in directions:
                x, y = i + dirr[0], j + dirr[1]
                if x >= 0 and x < n and y >= 0 and y < n and (x, y) not in visited:
                    visited.add((x, y))
                    grid[x][y] = grid[i][j] + 1
                    queue.append((x, y))
        return -1 if ans == 0 else ans