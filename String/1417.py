# 1417. Reformat The String

# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# Return the reformatted string or return an empty string if it is impossible to reformat the string.

# Example 1:
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

# Example 2:
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.

# Example 3:
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.

# Example 4:
# Input: s = "covid2019"
# Output: "c2o0v1i9d"

# Example 5:
# Input: s = "ab123"
# Output: "1a2b3"

# Constraints:
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.

class Solution(object):
    def reformat(self, s):
        array1 = []
        array2 = []
        for i in range(len(s)):
            if s[i].isdigit():
                array1.append(s[i])
            else:
                array2.append(s[i])
        if abs(len(array1) - len(array2)) > 1:
            return ''
        array = []
        minLen = min(len(array1), len(array2))
        i = 0
        while i < minLen:
            if len(array1) > len(array2):
                array.append(array1[i])
                array.append(array2[i])
            else:
                array.append(array2[i])
                array.append(array1[i])
            i += 1
        while i < len(array1):
            array.append(array1[i])
            i += 1
        while i < len(array2):
            array.append(array2[i])
            i += 1
        
        return ''.join(array)
        