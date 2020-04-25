# 169. Majority Element

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in map.keys():
                map[nums[i]] = 0
            map[nums[i]] += 1
            if map[nums[i]] > n / 2:
                return nums[i]
        return 0