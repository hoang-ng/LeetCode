# 11. Container With Most Water

class Solution(object):
    def maxArea(self, height):
        maxArea = -float('inf')
        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea