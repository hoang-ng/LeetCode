# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.


class Solution(object):
    def isIsomorphic(self, s, t):
        dic1 = {}
        dic2 = {}

        for i in range(len(s)):
            if not s[i] in dic1:
                dic1[s[i]] = i
            if not t[i] in dic2:
                dic2[t[i]] = i

            if len(dic1) != len(dic2):
                return False

            if dic1[s[i]] != dic2[t[i]]:
                return False

        return True
