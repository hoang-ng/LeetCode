# 930. Binary Subarrays With Sum

# In an array A of 0s and 1s, how many non-empty subarrays have sum S?

# Example 1:
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
 
# Note:
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.

import collections

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        def atMost(S):
            if S < 0: 
                return 0
            res = i = 0
            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res
        return atMost(S) - atMost(S - 1)

class Solution2(object):
    def numSubarraysWithSum(self, A, S):
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res
        