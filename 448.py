# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]

class Solution1:
    def findDisappearedNumbers(self, nums):
        rs = []
        dic = {}
        for i,v in enumerate(nums):
            dic[v] = i
        for i in range(1, len(nums) + 1):
            if i not in dic:
                rs.append(i)
        return rs

class Solution2:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            n = abs(nums[i]) - 1
            nums[n] = abs(nums[n]) * -1
        rs = []
        for i in range(len(nums)):
            if nums[i] > 0:
                rs.append(i+1)
        return rs

sol = Solution2()
sol.findDisappearedNumbers([1,3,2,7,8,2,3,1])