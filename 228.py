# Summary Ranges

# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

# Example 2:
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution(object):
    def summaryRanges(self, nums):
        rs = []
        i = 0
        while i < len(nums):
            num = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
                
            if num != nums[i]:
                rs.append(str(num) + '->' + str(nums[i]))
            else:
                rs.append(str(num))
            i += 1
        return rs

sol = Solution()
sol.summaryRanges([0,1,2,4,5,7])