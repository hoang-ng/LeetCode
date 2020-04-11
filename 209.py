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
        ans = float("inf")
        left = 0
        currSum = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            while (currSum >= s):
                ans = min(ans, i + 1 - left)
                currSum -= nums[left]
                left += 1
        return 0 if ans == float("inf") else ans