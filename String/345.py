# 345. Reverse Vowels of a String

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Input: "hello"
# Output: "holle"

# Example 2:
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        array = list(s)
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'u', 'i', 'o']
        
        while i < j:
            while i < len(array) and not array[i].lower() in vowels:
                i += 1
            while j >= 0 and not array[j].lower() in vowels:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        return ''.join(array)