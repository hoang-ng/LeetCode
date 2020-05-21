# 59. Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        if not n:
            return []
        
        num = 1
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        rs = [[0 for _ in range(n)] for _ in range(n)]
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                rs[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                rs[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                rs[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                rs[i][left] = num
                num += 1
            left += 1
        return rs