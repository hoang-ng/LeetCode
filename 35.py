# 35. Search Insert Position

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

class Solution1:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

class Solution2:
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums) - 1
        while (i <= j):
            mid = (i + j) / 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] > target):
                j = mid - 1
            else:
                i = mid + 1
        return i