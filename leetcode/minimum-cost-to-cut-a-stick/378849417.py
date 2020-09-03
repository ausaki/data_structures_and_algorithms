# title: minimum-cost-to-cut-a-stick
# detail: https://leetcode.com/submissions/detail/378849417/
# datetime: Mon Aug 10 20:30:25 2020
# runtime: 1068 ms
# memory: 17.5 MB

from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        MAX_COST = n  / 2 * (n + 1)
        
        @lru_cache(None)
        def cut(l, r):
            # print(cut_l, cut_r, w_l, w_r)
            if r - l <= 1:
                return 0
            if r - l == 2:
                return cuts[r] - cuts[l]
            cost = MAX_COST
            for i in range(l + 1, r):
                cost = min(cost, cut(l, i) + cut(i, r))
            return cost + cuts[r] - cuts[l]
        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        return cut(0, len(cuts) - 1)