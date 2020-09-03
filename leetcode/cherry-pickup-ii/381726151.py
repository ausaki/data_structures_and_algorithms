# title: cherry-pickup-ii
# detail: https://leetcode.com/submissions/detail/381726151/
# datetime: Sun Aug 16 21:38:22 2020
# runtime: 1672 ms
# memory: 21.9 MB

from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
#         @lru_cache(None)
#         def pick(i, c1, c2):
#             if i == n or c1 < 0 or c1 >= m or c2 < 0 or c2 >= m:
#                 return 0
#             result = 0
#             for j in [-1, 0, 1]:
#                 for k in [-1, 0, 1]:
#                     result = max(result, pick(i + 1, c1 + j, c2 + k))
#             return result + grid[i][c1] + (grid[i][c2] if c1 != c2 else 0)
        
        n = len(grid)
        m = len(grid[0])
#         return pick(0, 0, m - 1)
    
        dp = [[[0] * (m + 2) for j in range(m + 2)] for i in range(n + 1)]
        for i in reversed(range(n)):
            for j in range(1, m + 1):
                for k in range(1, m + 1):
                    dp[i][j][k] = max(dp[i + 1][j + dj][k + dk] for dk in [-1, 0, 1] for dj in [-1, 0, 1])
                    dp[i][j][k] += grid[i][j - 1] + (grid[i][k - 1] if j != k else 0)
        return dp[0][1][m]