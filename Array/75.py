# 75. Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution(object):
    def sortColors(self, nums):
        curr = 0
        l = 0
        r = len(nums) - 1
        while curr <= r:
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                curr += 1
                l += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            else:
                curr += 1

    def sortColors2(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1