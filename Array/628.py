# 628. Maximum Product of Three Numbers

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6
 

# Example 2:
# Input: [1,2,3,4]
# Output: 24
 

# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

class Solution1:
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        
        return max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])

class Solution2:
    def maximumProduct(self, nums):
        max1 = max2 = max3 = -float("inf")
        min1 = min2 = float("inf")
        for n in nums:
            if n >= max1:
                max3, max2, max1 = max2, max1, n
            elif n >= max2:
                max3, max2 = max2, n
            elif n > max3:
                max3 = n
            
            if n <= min1:
                min2, min1 = min1, n
            elif n < min2:
                min2 = n
        return max(max1 * max2 * max3, max1 * min1 * min2)