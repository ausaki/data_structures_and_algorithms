# title: trapping-rain-water
# detail: https://leetcode.com/submissions/detail/311135146/
# datetime: Tue Mar 10 14:59:25 2020
# runtime: 48 ms
# memory: 13.4 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        N = len(height)
        if N <= 2: return 0
        max_height = 0
        m = -1
        for i, h in enumerate(height):
            if h > max_height:
                max_height = h
                m = i
        h = height[0]
        for i in range(m):
            if height[i] < h:
                total += h - height[i]
            elif height[i] > h:
                h = height[i]
        h = height[N - 1]
        for i in range(N - 1, m, -1):
            if height[i] < h:
                total += h - height[i]
            elif height[i] > h:
                h = height[i]
        return total