# 680. Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000

class Solution(object):
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.validPalindromeUtil(s, left + 1, right) or self.validPalindromeUtil(s, left, right - 1)
            left, right = left + 1, right - 1
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        