# 977. Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Example 2:
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Note:
# 1. 1 <= A.length <= 10000
# 2. -10000 <= A[i] <= 10000
# 3. A is sorted in non-decreasing order.

class Solution1:
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        A.sort()
        return A

class Solution2:
    def sortedSquares(self, A):
        N = len(A)
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        ans = []
        while i >= 0 and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1
        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1
        return ans