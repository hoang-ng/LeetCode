# 242. Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] not in dic:
                return False
            dic[t[i]] -= 1
            if dic[t[i]] < 0:
                return False
            if dic[t[i]] == 0:
                del dic[t[i]]

        return len(dic) == 0
