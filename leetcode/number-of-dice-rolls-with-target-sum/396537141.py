# title: number-of-dice-rolls-with-target-sum
# detail: https://leetcode.com/submissions/detail/396537141/
# datetime: Wed Sep 16 18:59:54 2020
# runtime: 296 ms
# memory: 13.9 MB

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            for t in reversed(range(i, min(i * f, target) + 1)):
                dp[t] = sum(dp[t - j] for j in range(max(1, t - (i - 1) * f), min(f, t - i + 1) + 1)) % MOD
        return dp[target]