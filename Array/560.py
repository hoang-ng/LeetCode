# 560. Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2

# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums, k):
        dic = {0: 1}
        
        currSum = 0
        rs = 0
        
        for n in nums:
            currSum += n
            rs += dic.get(currSum - k, 0)
            dic[currSum] = dic.get(currSum, 0) + 1
        return rs