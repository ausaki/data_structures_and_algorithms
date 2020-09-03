# title: minimum-cost-to-cut-a-stick
# detail: https://leetcode.com/submissions/detail/378844272/
# datetime: Mon Aug 10 20:10:11 2020
# runtime: 1396 ms
# memory: 17.8 MB

from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        MAX_COST = n  / 2 * (n + 1)
        
        @lru_cache(None)
        def cut(cut_l, cut_r, w_l, w_r):
            # print(cut_l, cut_r, w_l, w_r)
            if cut_l > cut_r:
                return 0
            if cut_l == cut_r:
                return w_r - w_l
            cost = MAX_COST
            for i in range(cut_l, cut_r + 1):
                cost = min(cost, cut(cut_l, i - 1, w_l, cuts[i]) + cut(i + 1, cut_r, cuts[i], w_r))
            return cost + w_r - w_l

        cuts.sort()
        return cut(0, len(cuts) - 1, 0, n)