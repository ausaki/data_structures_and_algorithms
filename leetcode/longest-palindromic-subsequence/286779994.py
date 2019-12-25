# title: longest-palindromic-subsequence
# detail: https://leetcode.com/submissions/detail/286779994/
# datetime: Wed Dec 18 11:43:34 2019
# runtime: 1392 ms
# memory: 29 MB

from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # def find(i, j):
            
        N = len(s)
        dp = [[0] * N for i in range(N)]
        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][N - 1]