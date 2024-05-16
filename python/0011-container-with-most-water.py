class Solution(object):
    def maxArea(self, height):
        l, r, max_area = 0, len(height) - 1, 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            if height[l] < height[r]: l += 1
            else: r -= 1
        return max_area
