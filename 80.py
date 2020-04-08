# 80. Remove Duplicates from Sorted Array II

# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,1,2,3,3],
# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# It doesn't matter what values are set beyond the returned length.

class Solution1:
    def removeDuplicates(self, nums):
        i = 1
        count = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
                count = 0
            elif nums[j] == nums[j - 1]:
                count += 1
                if count == 1:
                    nums[i] = nums[j]
                    i += 1
        return i

class Solution2:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n != nums[i-2]:
                nums[i] = n
                i += 1
        return i