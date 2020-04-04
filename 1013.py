# 1013. Partition Array Into Three Parts With Equal Sum

# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

# Example 1:
# Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: A = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

# Constraints:
# 3 <= A.length <= 50000
# -10^4 <= A[i] <= 10^4

class Solution:
    def canThreePartsEqualSum(self, A):
        s = 0
        for n in A:
            s += n
        if s % 3 != 0:
            return False
        s = s / 3
        currSum = 0
        count = 0
        for i in range(len(A)):
            currSum += A[i]
            if currSum == s:
                count += 1
                currSum = 0
            if count == 2 and i < len(A) - 1:
                return True
        return False