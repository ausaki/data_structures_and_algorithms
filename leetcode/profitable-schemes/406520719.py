# title: profitable-schemes
# detail: https://leetcode.com/submissions/detail/406520719/
# datetime: Fri Oct  9 18:08:33 2020
# runtime: 4092 ms
# memory: 669.7 MB

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(i, g, p):
            if g < 0:
                return 0
            if i == n:
                return 1 if p == 0 else 0
            a = dp(i + 1, g - group[i], max(0, p - profit[i]))
            b = dp(i + 1, g, p)
            return (a + b) % MOD
        
        n = len(group)
        return dp(0, G, P)