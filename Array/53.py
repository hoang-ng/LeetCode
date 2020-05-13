# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            tempSum = currSum + nums[i]
            currSum = max(curr, tempSum)
            res = max(res, currSum)
        return res

sol  = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])