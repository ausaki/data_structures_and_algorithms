# title: maximum-non-negative-product-in-a-matrix
# detail: https://leetcode.com/submissions/detail/399173245/
# datetime: Tue Sep 22 19:45:36 2020
# runtime: 60 ms
# memory: 14 MB

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
                m1, m2 = min(dp[j]), max(dp[j])
                if j + 1 < n:
                    m1, m2 = min(m1, min(dp[j + 1])), max(m2, max(dp[j + 1]))
                if a < 0:
                    m1, m2 = m2, m1
                dp[j][:] = a * m1, a * m2
        result = dp[0][1]
        return result % (10 ** 9 + 7) if result >= 0 else -1 