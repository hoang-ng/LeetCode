# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution1:
    def findShortestSubArray(self, nums):
        dic = {}
        degree = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
            degree = max(degree, len(dic[nums[i]]))
        if degree == 1:
            return 1
        rs = float("inf")
        for _, v in dic.items():
            if len(v) == degree:
                rs = min(rs, v[len(v) - 1] - v[0] + 1)
        return rs

class Solution2:
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans