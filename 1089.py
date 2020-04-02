# 1089. Duplicate Zeros

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.

# Example 1:
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 
# Note:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

class Solution1:
    def duplicateZeros(self, arr):
        clone = arr[:]
        i = 0
        for j in range(len(arr)):
            if i < len(arr):
                arr[i] = clone[j]
                if clone[j] == 0 and i + 1 < len(arr):
                    arr[i + 1] = 0
                    i += 1
                i += 1

class Solution2:
    def duplicateZeros(self, arr):
        countZero = 0
        for n in arr:
            if n == 0:
                countZero += 1
        if countZero == 0:
            return
        for i in range(len(arr) - 1, -1, -1):
            if i + countZero < len(arr):
                arr[i + countZero] = arr[i]
            if arr[i] == 0:
                countZero -= 1
                if i + countZero < len(arr):
                    arr[i + countZero] = 0