# title: number-of-ways-to-stay-in-the-same-place-after-some-steps
# detail: https://leetcode.com/submissions/detail/394124670/
# datetime: Fri Sep 11 16:26:21 2020
# runtime: 188 ms
# memory: 13.8 MB

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (min(steps + 1, arrLen) + 1)
        dp[1] = 1
        for step in range(1, steps + 1):
            last = 0
            for i in reversed(range(min(step + 1, arrLen))):
                last, dp[i + 1] = dp[i + 1], (dp[i + 1] + dp[i] + last) % MOD
        return dp[1]