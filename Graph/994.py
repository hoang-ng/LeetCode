# 994. Rotting Oranges

# In a given grid, each cell can have one of three values:
# - the value 0 representing an empty cell;
# - the value 1 representing a fresh orange;
# - the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

# Example 1:
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 
# Note:
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

class Solution(object):
    def orangesRotting(self, grid):
        n,m = len(grid), len(grid[0])
        queue = []
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: count += 1
                if grid[i][j] == 2: queue.append((i,j))
        res = 0
        while queue:
            for _ in range(len(queue)):
                i,j = queue.pop(0)
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0<=x<n and 0<=y<m and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        queue.append((x,y))
            res += 1
        return max(0, res-1) if count == 0 else -1