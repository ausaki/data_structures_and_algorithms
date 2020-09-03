# title: maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
# detail: https://leetcode.com/submissions/detail/381257703/
# datetime: Sat Aug 15 23:30:04 2020
# runtime: 324 ms
# memory: 26.8 MB

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxh = 0
        maxw = 0
        prev = 0
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        maxh = max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, len(horizontalCuts)))
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        maxw = max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, len(verticalCuts)))
        M = 10 ** 9 + 7
        return ((maxw %  M) * (maxh % M)) % M