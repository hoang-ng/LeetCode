# 39. Combination Sum

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution:
    def combinationSum(self, candidates, target):
        rs = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], rs)
        return rs
        
    def dfs(self, candidates, index, target, subList, rs):
        if target == 0:
            print(subList)
            rs.append(subList)
            return
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            self.dfs(candidates, i + 1, target - candidates[i], subList + [candidates[i]], rs)

sol = Solution()
sol.combinationSum([2, 3, 4, 6, 7], 7)