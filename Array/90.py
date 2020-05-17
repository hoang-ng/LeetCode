# 90. Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        rs = []
        nums.sort()
        self.backTrack(nums, 0, [], rs)
        return rs
        
    def backTrack(self, nums, index, subList, rs):
        rs.append(subList)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.backTrack(nums, i + 1, subList + [nums[i]], rs)

sol = Solution()
sol.subsetsWithDup([1, 2, 2])