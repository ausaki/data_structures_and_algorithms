# title: largest-rectangle-in-histogram
# detail: https://leetcode.com/submissions/detail/398308807/
# datetime: Sun Sep 20 21:17:59 2020
# runtime: 108 ms
# memory: 15.4 MB

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, -1)
        heights.append(0)
        result = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                hh = heights[stack.pop()]
                k = stack[-1]
                result = max(result, (i - k - 1) * hh)
            stack.append(i)
        return result