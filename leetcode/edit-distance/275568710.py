# title: edit-distance
# detail: https://leetcode.com/submissions/detail/275568710/
# datetime: Sun Nov  3 17:55:22 2019
# runtime: 236 ms
# memory: 17.8 MB

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        # if N == 0:
        #     return M
        # if M == 0:
        #     return N
        
        dp = [[0 for j in range(M + 1)] for i in range(N + 1)]
        i = 0
        for j in range(0, M + 1):
            dp[i][j] = j
        j = 0
        for i in range(0, N + 1):
            dp[i][j] = i
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1
        return dp[N][M]        
        