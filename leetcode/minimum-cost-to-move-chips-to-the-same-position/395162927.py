# title: minimum-cost-to-move-chips-to-the-same-position
# detail: https://leetcode.com/submissions/detail/395162927/
# datetime: Mon Sep 14 01:18:41 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)
        s = sum(p % 2 for p in position)
        return min(s, n - s)
                