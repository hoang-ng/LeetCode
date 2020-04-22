# 46. Permutations

# Given a collection of distinct integers, return all possible permutations.

# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        rs = []
        self.backTrack(rs, [], nums)
        return rs
    
    def backTrack(self, rs, subList, nums):
        if len(subList) == len(nums):
            rs.append(subList)
        else:
            for i in range(len(nums)):
                self.backTrack(rs, subList + [nums[i]], nums)

sol = Solution()
print(sol.permute([1,1,2]))