# title: profitable-schemes
# detail: https://leetcode.com/submissions/detail/406520844/
# datetime: Fri Oct  9 18:09:11 2020
# runtime: 4344 ms
# memory: 639.7 MB

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(i, g, p):
            if g < 0:
                return 0
            if i == n:
                return 1 if p == 0 else 0
            a = dp(i + 1, max(g - group[i], -1), max(0, p - profit[i]))
            b = dp(i + 1, g, p)
            return (a + b) % MOD
        
        n = len(group)
        return dp(0, G, P)