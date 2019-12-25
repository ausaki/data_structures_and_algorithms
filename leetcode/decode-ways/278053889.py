# title: decode-ways
# detail: https://leetcode.com/submissions/detail/278053889/
# datetime: Tue Nov 12 10:19:24 2019
# runtime: 32 ms
# memory: 12.7 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        dp[N] = 1
        for i in reversed(range(N)):
            if s[i] == '0':
                continue
            dp[i] = dp[i + 1]
            if i + 2 <= N and int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]
        