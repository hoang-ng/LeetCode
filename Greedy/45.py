# 45. Jump Game II

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:

# You can assume that you can always reach the last index.

class Solution(object):
    def jump(self, nums):
        reach = 0
        nxt = 0
        cnt = 0
        for i, n in enumerate(nums):
            if i > reach:
                reach = nxt
                cnt += 1
                
            if reach >= len(nums) - 1:
                return cnt
                
            nxt = max(nxt, i + n)
                            
        return -1
        