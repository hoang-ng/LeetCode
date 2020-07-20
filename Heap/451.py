# 451. Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

import collections
import heapq


class Solution(object):
    def frequencySort(self, s):
        counter = collections.Counter(s)
        heap = []
        for k, v in counter.items():
            heap.append((-v, k))
        heapq.heapify(heap)

        rs = ''
        while heap:
            v, k = heapq.heappop(heap)
            rs += k * -v

        return rs
