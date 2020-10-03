# title: tallest-billboard
# detail: https://leetcode.com/submissions/detail/403066991/
# datetime: Thu Oct  1 18:38:23 2020
# runtime: 1288 ms
# memory: 239.4 MB

from functools import lru_cache
class Solution:
    def tallestBillboard(self, rods):
        @lru_cache(None)
        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            return max(dp(i + 1, s),
                       dp(i + 1, s - rods[i]),
                       dp(i + 1, s + rods[i]) + rods[i])

        return dp(0, 0)