# title: dice-roll-simulation
# detail: https://leetcode.com/submissions/detail/395117113/
# datetime: Sun Sep 13 23:08:49 2020
# runtime: 1384 ms
# memory: 14 MB

class Solution:
    def dieSimulator(self, n, rollMax):
        mod = 10**9 + 7
        dp = [[0, 1] + [0] * 15 for i in range(6)]
        for _ in range(n - 1):
            dp2 = [[0] * 17 for i in range(6)]
            for i in range(6):
                for k in range(1, rollMax[i] + 1):
                    for j in range(6):
                        if i == j:
                            if k < rollMax[i]:
                                dp2[j][k + 1] += dp[i][k] % mod
                        else:
                            dp2[j][1] += dp[i][k] % mod
            dp = dp2
        return sum(sum(row) for row in dp) % mod