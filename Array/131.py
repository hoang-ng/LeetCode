# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example:
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

class Solution(object):
    def partition(self, s):
        rs = []
        self.backtrack(s, 0, [], rs)
        return rs

    def backtrack(self, s, start, tempList, rs):
        if start == len(s):
            rs.append(tempList)
        else:
            for i in range(start, len(s)):
                if self.isPalindrome(s, start, i):
                    self.backtrack(s, i + 1, tempList + [s[start : i + 1]], rs)

    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high += 1
        return True