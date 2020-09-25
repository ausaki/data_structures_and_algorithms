# title: number-of-ways-to-stay-in-the-same-place-after-some-steps
# detail: https://leetcode.com/submissions/detail/394118277/
# datetime: Fri Sep 11 16:04:24 2020
# runtime: 176 ms
# memory: 23.5 MB

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * arrLen
        dp[0] = 1
        for step in range(1, steps + 1):
            last = 0
            for i in reversed(range(min(step + 1, arrLen))):
                last, dp[i] = dp[i], (dp[i] + (dp[i - 1] if i else 0) + last) % MOD
        return dp[0]