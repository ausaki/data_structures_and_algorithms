# title: profitable-schemes
# detail: https://leetcode.com/submissions/detail/406527626/
# datetime: Fri Oct  9 18:45:55 2020
# runtime: 1620 ms
# memory: 14.4 MB

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (P + 1) for i in range(G + 1)]
        for i in range(G + 1):
            dp[i][0] = 1
        for g, p in zip(group, profit):
            dp2 = [row[:] for row in dp]
            for g1 in range(g, G + 1):
                for p1 in range(P + 1):
                    dp2[g1][p1] = (dp2[g1][p1] + dp[g1 - g][max(0, p1 - p)]) % MOD
            dp = dp2
        return dp[G][P]