# 665. Non-decreasing Array

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Example 1:
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.
 
# Constraints:
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5

class Solution1:
    def checkPossibility(self, nums):
        end = len(nums)
        rs = 0
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                if rs == 0:
                    rs = i
                else:
                    return False
        return False if rs < end - 1 and nums[rs + 1] < nums[rs - 1] and 1 < rs and nums[rs -2] > nums[rs] else True

class Solution2:
    def checkPossibility(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count > 1:
                return False
        return True