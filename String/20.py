# 20. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        stack = []
        
        for i in range(len(s)):
            if s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack) > 0:
                    char = stack.pop()
                    if s[i] == ')' and char != '(':
                        return False
                    if s[i] == ']' and char != '[':
                        return False
                    if s[i] == '}' and char != '{':
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
            
        return len(stack) == 0