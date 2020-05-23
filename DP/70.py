# 70. Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution1:
    def climbStars(self, n):
        return self.climb_Stars(0, n)

    def climb_Stars(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_Stars(i + 1, n) + self.climb_Stars(i + 2, n)

class Solution2:
    def climbStairs(self, n):
        memo = {}
        return self.climb_start(0, n, memo)
    
    def climb_start(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = self.climb_start(i + 1, n, memo) + self.climb_start(i + 2, n, memo)
        return memo[i]

class Solution3:
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]