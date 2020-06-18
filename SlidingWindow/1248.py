# 1248. Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.

# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

# Constraints:
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

class Solution(object):
    def numberOfSubarrays(self, A, k):
        def atMost(k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
        
class Solution2(object):
    def numberOfSubarrays(self, A, k):
        i = count = res = 0
        for j in range(len(A)):
            if A[j] % 2 == 1:
                k -= 1
                count = 0
            while k == 0:
                k += A[i] & 1
                i += 1
                count += 1
            res += count
        return res