# 1020. Number of Enclaves

# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
# A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
# Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

# Example 1:
# Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: 
# There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

# Example 2:
# Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: 
# All 1s are either on the boundary or can reach the boundary.
 
# Note:
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# All rows have the same size.

class Solution(object):
    def numEnclaves(self, A):
        if len(A) == 0:
            return 0
        
        rows = len(A)
        cols = len(A[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    self.dfs(A, i, j)
                    
        count = 0
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    count += 1
        return count
        
        
    def dfs(self, A, i, j):
        if i < 0 or j < 0 or i >= len(A) or j >= len(A[i]):
            return
        if A[i][j] != 1:
            return
        
        A[i][j] = -1
        self.dfs(A, i + 1, j)
        self.dfs(A, i - 1, j)
        self.dfs(A, i, j + 1)
        self.dfs(A, i, j - 1)

sol = Solution()
sol.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])