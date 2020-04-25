# 1351. Count Negative Numbers in a Sorted Matrix

# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
# Return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

# Example 3:
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3

# Example 4:
# Input: grid = [[-1]]
# Output: 1

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

class Solution1:
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count += 1
        return count

class Solution2:
    def countNegatives(self, grid):
        count = 0
        for array in grid:
            l = 0
            r = len(array) - 1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            count += len(array) - l
        return count