# title: maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
# detail: https://leetcode.com/submissions/detail/381255053/
# datetime: Sat Aug 15 23:22:07 2020
# runtime: 396 ms
# memory: 26.7 MB

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxh = 0
        maxw = 0
        prev = 0
        horizontalCuts.sort()
        for c in horizontalCuts:
            l, prev = c - prev, c
            maxh = max(maxh, l)
        maxh = max(maxh, h - prev)        
        prev = 0
        verticalCuts.sort()
        for c in verticalCuts:
            l, prev = c - prev, c
            maxw = max(maxw, l)
        maxw = max(maxw, w - prev)
        M = 10 ** 9 + 7
        return ((maxw %  M) * (maxh % M)) % M