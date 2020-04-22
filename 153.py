# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Example 1:
# Input: [3,4,5,1,2] 
# Output: 1

# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] > nums[r]:
                l += 1
            else:
                r = mid
        return nums[l]