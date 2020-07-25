# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.

#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 A[j] := false
#     return all i such that A[i] is true.

import math


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        for num in range(2, int(math.sqrt(n)) + 1):
            if primes[num]:
                primes[num**2:n:num] = [False] * len(primes[num**2:n:num])

        return sum(primes)
