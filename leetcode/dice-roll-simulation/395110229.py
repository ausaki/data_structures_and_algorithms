# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395110229/
# datetime: Sun Sep 13 22:47:30 2020
# runtime: 324 ms
# memory: 40.5 MB

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 6 for i in range(n + 1)]
        dp[1] = [1] * 6
        for i in range(2,  n + 1):
            for j in range(6):
                p = dp[i]
                if i - rollMax[j] <= 0:
                    dp[i][j] = sum(dp[i - 1])
                    continue
                if i - rollMax[j] == 1:
                    dp[i][j] = sum(dp[i - 1]) - 1
                    continue
                p = dp[i - rollMax[j] - 1]
                dp[i][j] = sum(dp[i - 1]) - sum(p) + p[j]
        return sum(dp[n]) % MOD
