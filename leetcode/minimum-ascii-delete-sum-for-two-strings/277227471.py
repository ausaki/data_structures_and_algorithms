# title: minimum-ascii-delete-sum-for-two-strings
# detail: https://leetcode.com/submissions/detail/277227471/
# datetime: Sat Nov  9 13:20:05 2019
# runtime: 1256 ms
# memory: 17.3 MB

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        i = 0
        for j in range(1, M + 1):
            dp[i][j] = ord(s2[j - 1]) + dp[i][j - 1]
        j = 0
        for i in range(1, N + 1):
            dp[i][j] = ord(s1[i - 1]) + dp[i - 1][j]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1]),
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )
        return dp[N][M]
                