# 905. Sort Array By Parity

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Note:
# 1. 1 <= A.length <= 5000
# 2. 0 <= A[i] <= 5000

class Solution:
    def sortArrayByParity(self, A):
        i = 0
        j = len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
            j -= 1
        return A