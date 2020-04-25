# 1133. Largest Unique Number
# Given an array of integers A, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

# Example 1:
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

# Example 2:
# Input: [9,9,8,8]
# Output: -1
# Explanation: 
# There is no number that occurs only once.
 
# Note:
# 1 <= A.length <= 2000
# 0 <= A[i] <= 1000

class Solution1():
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = [0] * 1001
        for num in A:
            count[num] += 1
        for i in reversed(range(0,1001)):
            if count[i] == 1:
                return i
        return -1

class Solution2():
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        map = {}
        for num in A:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        keys = map.keys()
        rs = -1
        for key in keys:
            if map[key] == 1:
                rs = max(rs, key)
        return rs