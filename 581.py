# 581. Shortest Unsorted Continuous Subarray

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Note:
# 1. Then length of the input array is in range [1, 10,000].
# 2. The input array may contain duplicates, so ascending order here means <=.

class Solution:
    def findUnsortedSubarray(self, nums):
        a = nums[:]
        a.sort()
        
        start = len(nums)
        end = 0
        for i in range(len(a)):
            if a[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
                
        return end - start + 1 if end > start else 0