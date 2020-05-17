# 16. 3Sum Closest

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                interimSum = nums[i] + nums[l] + nums[r] - target
                if abs(interimSum) < abs(closest):
                    closest = interimSum
                if interimSum == 0:
                    return target
                elif interimSum > 0:
                    r -= 1
                else:
                    l += 1
        return closest + target