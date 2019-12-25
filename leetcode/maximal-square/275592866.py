# title: maximal-square
# detail: https://leetcode.com/submissions/detail/275592866/
# datetime: Sun Nov  3 21:59:20 2019
# runtime: 204 ms
# memory: 14.8 MB

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        result = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if matrix[i - 1][j - 1] == '0':
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        return result * result
                    