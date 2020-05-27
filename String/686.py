# 686. Repeated String Match

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

# Note:
# The length of A and B will be between 1 and 10000.

class Solution(object):
    def repeatedStringMatch(self, A, B):
        temp = ""
        count = 0
        while len(temp) < len(B):
            temp+=A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        return -1

sol = Solution()
sol.repeatedStringMatch("abcd","cdabcdab")