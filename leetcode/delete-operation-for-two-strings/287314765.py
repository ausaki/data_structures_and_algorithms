# title: delete-operation-for-two-strings
# detail: https://leetcode.com/submissions/detail/287314765/
# datetime: Fri Dec 20 17:40:42 2019
# runtime: 284 ms
# memory: 16.4 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[1] * (N2 + 1) for i in range(N1 + 1)]
        for j in range(N2 + 1):
            dp[N1][j] = N2 - j
        for i in range(N1 + 1):
            dp[i][N2] = N1 - i
        for i in range(N1 - 1, -1, -1):
            for j in range(N2 - 1, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j + 1])
        return dp[0][0]