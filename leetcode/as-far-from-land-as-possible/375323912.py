# title: as-far-from-land-as-possible
# detail: https://leetcode.com/submissions/detail/375323912/
# datetime: Mon Aug  3 15:50:32 2020
# runtime: 456 ms
# memory: 14 MB

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        MAX = 200
        dp = [[0 for i in range(N)] for i in range(N)]
        result = -1
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1] if j >= 1 else MAX, dp[i - 1][j] if i >= 1 else MAX) + 1
        for i in reversed(range(N)):
            for j in reversed(range(N)):
                if grid[i][j] == 0:
                    dp[i][j] = min(dp[i][j], min(dp[i][j + 1] if j <= N - 2 else MAX, dp[i + 1][j] if i <= N - 2 else MAX) + 1)
                    if dp[i][j] < MAX and dp[i][j] > result:
                        result = dp[i][j]
        return result
                