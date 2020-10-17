# title: profitable-schemes
# detail: https://leetcode.com/submissions/detail/406525170/
# datetime: Fri Oct  9 18:32:32 2020
# runtime: 2236 ms
# memory: 14.5 MB

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # @lru_cache(None)
        # def dp(i, g, p):
        #     if g < 0:
        #         return 0
        #     if i == n:
        #         return 1 if p == 0 else 0
        #     a = dp(i + 1, max(g - group[i], -1), max(0, p - profit[i]))
        #     b = dp(i + 1, g, p)
        #     return (a + b) % MOD
        dp = [[0] * (P + 1) for i in range(G + 1)]
        for i in range(G + 1):
            dp[i][0] = 1
        for g, p in zip(group, profit):
            dp2 = [[0] * (P + 1) for i in range(G + 1)]
            for g1 in range(G + 1):
                for p1 in range(P + 1):
                    dp2[g1][p1] = dp[g1][p1]
                    if g1 >= g:
                        dp2[g1][p1] = (dp2[g1][p1] + dp[g1 - g][max(0, p1 - p)]) % MOD
            dp = dp2
        return dp[G][P]