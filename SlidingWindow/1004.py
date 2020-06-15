# 1004. Max Consecutive Ones III

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s. 

# Example 1:
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

# Example 2:
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

class Solution(object):
    def longestOnes(self, A, K):
        if K == len(A):
            return K
        
        count, j = 0, 0
        res = 0
        
        for i in range(len(A)):
            if A[i] == 0:
                count += 1
                
            while count > K and j < len(A):
                if A[j] == 0:
                    count -= 1
                j += 1
            res = max(res, i - j + 1)
            
        return res

class Solution2(object):
    def longestOnes(self, A, K):
        left = 0
        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
        return right - left + 1