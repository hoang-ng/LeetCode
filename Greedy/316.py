# 316. Remove Duplicate Letters

# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:
# Input: "bcabc"
# Output: "abc"

# Example 2:
# Input: "cbacdcbc"
# Output: "acdb"

class Solution(object):
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''
        