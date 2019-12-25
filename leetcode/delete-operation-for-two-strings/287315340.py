# title: delete-operation-for-two-strings
# detail: https://leetcode.com/submissions/detail/287315340/
# datetime: Fri Dec 20 17:45:57 2019
# runtime: 316 ms
# memory: 16.5 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[1] * (N2 + 1) for i in range(N1 + 1)]
        for j in range(N2 + 1):
            dp[0][j] = j
        for i in range(N1 + 1):
            dp[i][0] = i
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        return dp[N1][N2]