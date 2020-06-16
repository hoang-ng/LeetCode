# 862. Shortest Subarray with Sum at Least K

# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.

# Example 1:
# Input: A = [1], K = 1
# Output: 1

# Example 2:
# Input: A = [1,2], K = 4
# Output: -1

# Example 3:
# Input: A = [2,-1,2], K = 3
# Output: 3
 
# Note:
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9

import collections

class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        presum = [0] * (n + 1)
        
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + A[i - 1]
        
        deque = collections.deque([])
        res = float("inf")
        
        for i in range(n + 1):
            while deque and presum[i] - presum[deque[0]] >= K:
                res = min(res, i - deque[0])
                deque.popleft()
            while deque and presum[i] <= presum[deque[-1]]:
                deque.pop()
            deque.append(i)
            
        return res if res != float("inf") else -1

class Solution2:
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
        