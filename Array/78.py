# 78. Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        rs = []
        self.backTrack(nums, 0, [], rs)
        return rs

    def backTrack(self, nums, index, subList, rs):
        rs.append(subList)
        for i in range(index, len(nums)):
            self.backTrack(nums, i + 1, subList + [nums[i]], rs)

sol = Solution()
sol.subsets([1,2,3])