class Solution(object):
    def subsetsWithDup(self, nums):
        rs = []
        nums.sort()
        used = [False] * len(nums)
        self.backTrack(nums, 0, [], rs, used)
        return rs
        
    def backTrack(self, nums, index, subList, rs, used):
        rs.append(subList)
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            used[i] = True
            self.backTrack(nums, i + 1, subList + [nums[i]], rs, used)
            used[i] = False

sol = Solution()
sol.subsetsWithDup([1, 2, 2])