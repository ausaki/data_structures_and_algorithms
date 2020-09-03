# title: super-egg-drop
# detail: https://leetcode.com/submissions/detail/311206839/
# datetime: Tue Mar 10 22:20:52 2020
# runtime: 104 ms
# memory: 19.7 MB

from functools import lru_cache
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
#         @lru_cache(None)
#         def drop(k, n):
#             if k == 1 or n <= 1:
#                 return n
#             return min((max(drop(k, n - i), drop(k - 1, i - 1)) + 1) for i in range(1, n + 1))
#         # if 2 ** K >= N:
#         #     return 
#         # return drop(K, N)
        
#         # dynamic programing
#         dp = [[0 for j in range(N + 1)] for i in range(K + 1)]
#         for i in range(1, N + 1):
#             dp[1][i] = i
#         for i in range(1, K + 1):
#             dp[i][1] = 1
#         for i in range(2, K + 1):
#             for j in range(2, N + 1):
#                 dp[i][j] = min(max(dp[i][j - k], dp[i - 1][k - 1]) + 1 for k in range(1, j + 1))
#         print(dp)
#         return dp[K][N]
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m