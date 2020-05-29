# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic = {}
        for i in range(len(text)):
            count = dic.get(text[i], 0) + 1
            dic[text[i]] = count
        
        st = 'balon'
        rs = float('inf')
        for i in range(len(st)):
            if not st[i] in dic:
                return 0
            count = dic[st[i]]
            if st[i] == 'l':
                if dic[st[i]] >= 2:
                    count = dic[st[i]] / 2
                else:
                    return 0
            if st[i] == 'o':
                if dic[st[i]] >= 2:
                    count = dic[st[i]] / 2
                else:
                    return 0
            rs = min(rs, count)
        return rs
        