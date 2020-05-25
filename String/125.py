# 125. Valid Palindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

sol = Solution()
rs = sol.isPalindrome("A man, a plan, a canal: Panama")
print(rs)