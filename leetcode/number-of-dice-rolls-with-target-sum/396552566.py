# title: number-of-dice-rolls-with-target-sum
# detail: https://leetcode.com/submissions/detail/396552566/
# datetime: Wed Sep 16 20:09:55 2020
# runtime: 56 ms
# memory: 13.8 MB

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            if target < i:
                break
            t = min(i * f, target)
            dp[t] = sum((dp[t - j] if t - j >= i - 1 else 0) for j in range(1, f + 1)) % MOD
            for t in reversed(range(i,  t)):
                dp[t] = dp[t + 1] - dp[t] + (dp[t - f] if t - f >= i - 1 else 0)
                dp[t] %= MOD
        return dp[target]