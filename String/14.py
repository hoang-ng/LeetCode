# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.

class Solution1:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        return self.helper(strs, 0, len(strs) - 1)
    
    def helper(self, strs, l, r):
        if l == r:
            return strs[l]
        else:
            mid = (l + r) / 2
            lcpLeft = self.helper(strs, l, mid)
            lcpRight = self.helper(strs, mid + 1, r)
            return self.commonPrefix(lcpLeft, lcpRight)
    
    def commonPrefix(self, left, right):
        length = min(len(left), len(right))
        for i in range(length):
            if left[i] != right[i]:
                return left[:i]
        return left[:length]

class Solution2:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        minLen = float('inf')
        for st in strs:
            minLen = min(minLen, len(st))
        
        low = 1
        high = minLen
        
        while low <= high:
            mid = (low + high) / 2
            if self.isCommonPrefix(strs, mid):
                low += 1
            else:
                high -= 1
        return strs[0][:((low + high) / 2)]
        
    def isCommonPrefix(self, strs, length):
        str1 = strs[0][:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True