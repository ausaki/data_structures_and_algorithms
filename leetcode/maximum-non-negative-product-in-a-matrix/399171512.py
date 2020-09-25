# title: maximum-non-negative-product-in-a-matrix
# detail: https://leetcode.com/submissions/detail/399171512/
# datetime: Tue Sep 22 19:38:26 2020
# runtime: 60 ms
# memory: 13.8 MB

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0, 0] for i in range(n)]
        dp[n - 1] = [grid[m - 1][n - 1], grid[m - 1][n - 1]]
        for j in range(n - 2, -1, -1):
            a, b = grid[m - 1][j] * dp[j + 1][0], grid[m - 1][j] * dp[j + 1][1]
            dp[j][:] = min(a, b), max(a, b)
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                a = grid[i][j]
                if a == 0:
                    dp[j][:] = 0, 0
                b = [a * dp[j][0], a * dp[j][1]]
                if j + 1 < n:
                    b += [a * dp[j + 1][0], a * dp[j + 1][1]]
                dp[j][:] = min(b), max(b)
        result = dp[0][1]
        return result % (10 ** 9 + 7) if result >= 0 else -1 