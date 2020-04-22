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