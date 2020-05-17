# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution1:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                l = mid - 1
                r = mid + 1
                while l >= 0:
                    if target == nums[l]:
                        l -= 1
                    else:
                        break
                while r < len(nums):
                    if target == nums[r]:
                        r += 1
                    else:
                        break
                return [l + 1, r - 1]
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid + 1
        return [-1, -1]

class Solution2:
    def searchRange(self, A, target):
        lmost = self.leftsearch(A,target)
        rmost = self.rightsearch(A,target)
        return[lmost,rmost]

    def leftsearch(self, A, target):
        l = 0
        r = len(A) - 1
        rs = -1
        while l <= r:
            mid = (l + r) / 2
            if target <= A[mid]:
                r = mid - 1
            else:
                l = mid + 1
            if target == A[mid]:
                rs = mid
        return rs


    def rightsearch(self, A, target):
        l = 0
        r = len(A)-1
        rs = -1
        while l <= r:
            mid = (l + r) / 2
            if target >= A[mid]:
                r = mid - 1
            else:
                l = mid + 1
            if target == A[mid]:
                rs = mid
        return rs
