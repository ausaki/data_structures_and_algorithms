# title: longest-common-subsequence
# detail: https://leetcode.com/submissions/detail/276799213/
# datetime: Thu Nov  7 22:56:51 2019
# runtime: 576 ms
# memory: 23 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        
        # dp[i][j] = dp[i + 1][j + 1] + 1
        for i in reversed(range(N)):
            for j in reversed(range(M)):
                dp[i][j] = max(
                    dp[i + 1][j + 1] + (1 if  text1[i] == text2[j] else 0),
                    dp[i][j + 1],
                    dp[i + 1][j],
                )
        return dp[0][0]