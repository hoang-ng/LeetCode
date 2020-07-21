# 378. Kth Smallest Element in a Sorted Matrix
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# return 13.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        minHeap = []
        for r in range(min(k, n)):
            minHeap.append((matrix[r][0], r, 0))

        heapq.heapify(minHeap)

        while k:
            element, r, c = heapq.heappop(minHeap)
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            k -= 1

        return element


class Solution2(object):
    def kthSmallest(self, matrix, k):
        l, r = matrix[0][0], matrix[-1][-1]

        while l < r:
            m = (l+r)/2

            count = 0
            i = len(matrix[0]) - 1
            for row in range(len(matrix)):
                while i >= 0 and matrix[row][i] > m:
                    i -= 1
                count += i + 1

            if count >= k:
                r = m
            else:
                l = m + 1

        return l
