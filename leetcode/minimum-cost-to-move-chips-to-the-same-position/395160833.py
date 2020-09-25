# title: minimum-cost-to-move-chips-to-the-same-position
# detail: https://leetcode.com/submissions/detail/395160833/
# datetime: Mon Sep 14 01:13:04 2020
# runtime: 104 ms
# memory: 13.9 MB

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)
        return min(sum(abs(position[j] - position[i]) % 2 for j in range(n)) for i in range(n))
                