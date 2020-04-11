# 152. Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        currMax = nums[0]
        currMin = nums[0]
        rs = nums[0]
        
        for i in range(1, len(nums)):
            temp = currMax
            currMax = max(max(currMax * nums[i], currMin * nums[i]), nums[i])
            currMin = min(min(temp * nums[i], currMin * nums[i]), nums[i])
            
            rs = max(currMax, rs)
            
        return rs