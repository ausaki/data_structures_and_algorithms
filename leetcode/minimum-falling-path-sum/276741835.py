# title: minimum-falling-path-sum
# detail: https://leetcode.com/submissions/detail/276741835/
# datetime: Thu Nov  7 15:25:55 2019
# runtime: 124 ms
# memory: 13.5 MB

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        dp = [[A[i][j] for j in range(N)] for i in range(N)]
        MAX = 101
        for i in reversed(range(N - 1)):
            for j in range(N):
                dp[i][j] = min(
                    dp[i + 1][j - 1] if j - 1 >= 0 else MAX,
                    dp[i + 1][j],
                    dp[i + 1][j + 1] if j + 1 < N else MAX,
                ) + dp[i][j]
        return min(dp[0])