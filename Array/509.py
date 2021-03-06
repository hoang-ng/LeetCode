# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Note:
# 0 ≤ N ≤ 30.

class Solution1():
    def fib(self, N):
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

class Solution2():
    def fib(self, N):
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current

class Solution3():
    
    dict = {0: 0, 1: 1}
    
    def fib(self, N):
        if N < 2:
            return N
        
        if N in self.dict:
            return self.dict[N]
        self.dict[N] = self.fib(N-1) + self.fib(N-2)
        return self.dict[N]

class Solution():
    
    def fib(self, N):
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N):
        cache = {0: 0, 1: 1}

        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]