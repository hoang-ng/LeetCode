# 485. Max Consecutive Ones

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution1:
    def findMaxConsecutiveOnes(self, nums):
        lastZeroIdx = -1
        maxNum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if lastZeroIdx == -1:
                    maxNum = i
                else:
                    maxNum = max(maxNum, i - lastZeroIdx - 1)
                lastZeroIdx = i
        if lastZeroIdx >= 0 and lastZeroIdx < len(nums):
            maxNum = max(maxNum, len(nums) - lastZeroIdx - 1)
        else:
            maxNum = len(nums)
        return maxNum

class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        rs = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                rs = max(count, rs)
            else:
                count = 0
        return rs