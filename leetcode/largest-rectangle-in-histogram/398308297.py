# title: largest-rectangle-in-histogram
# detail: https://leetcode.com/submissions/detail/398308297/
# datetime: Sun Sep 20 21:15:52 2020
# runtime: 108 ms
# memory: 15.4 MB

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        result = 0
        stack = []
        for i, h in enumerate(heights):
            k = i
            while stack and h < heights[stack[-1]]:
                hh = heights[stack.pop()]
                k = stack[-1] if stack else -1
                result = max(result, (i - k - 1) * hh)
            stack.append(i)
        return result