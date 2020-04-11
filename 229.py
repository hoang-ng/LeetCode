# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution1:
    def majorityElement(self, nums):
        dic = {}
        rs = []
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

        for n in dic:
            if dic[n] > len(nums) / 3:
                rs.append(n)
        return rs

class Solution2:
    def majorityElement(self, nums):
        max1 = 0
        max2 = 1
        count1 = 0
        count2 = 0
        for n in nums:
            if n == max1:
                count1 += 1
            elif n == max2:
                count2 += 1
            elif count1 == 0:
                max1 = n
                count1 = 1
            elif count2 == 0:
                max2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for n in nums:
            if n == max1:
                count1 += 1
            elif n == max2:
                count2 += 1
        rs = []
        if count1 > len(nums) / 3:
            rs.append(max1)
        if count2 > len(nums) / 3:
            rs.append(max2)
        return rs
        