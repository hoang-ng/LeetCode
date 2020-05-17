# 47. Permutations II

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        rs = []
        nums.sort()
        used = [False] * len(nums)
        self.backTrack(nums, [], rs, used)
        return rs
        
    def backTrack(self, nums, subList, rs, used):
        if len(subList) == len(nums):
            rs.append(subList)
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                used[i] = True
                self.backTrack(nums, subList + [nums[i]], rs, used)
                used[i] = False
