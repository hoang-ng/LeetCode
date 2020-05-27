# 709. To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"

class Solution(object):
    def toLowerCase(self, word):
        arr = list(word)
        for i in range(len(arr)):
            if ord(arr[i]) >= 65 and ord(arr[i]) <= 90:
                arr[i] = chr(ord(arr[i]) + 32)
        return ''.join(arr)

sol = Solution()
a = sol.toLowerCase('HellO')