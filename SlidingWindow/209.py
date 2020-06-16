# 209. Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        currSum = 0
        i = 0
        res = float('inf')
        
        for j in range(len(nums)):
            currSum += nums[j]
            
            while currSum >= s:
                res = min(res, j - i + 1)
                currSum -= nums[i]
                i += 1
        
        return res if res != float('inf') else 0
        