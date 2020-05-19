# 18. 4Sum

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:
# The solution set must not contain duplicate quadruplets.

# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        rs = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.threeSum(nums, target - nums[i], i + 1, rs)
        return rs
        
    def threeSum(self, nums, target, start, result):
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            t = target - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > t:
                    r -= 1
                elif nums[l] + nums[r] < t:
                    l += 1
                else:
                    result.append([nums[start - 1], nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1