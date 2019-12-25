# title: new-21-game
# detail: https://leetcode.com/submissions/detail/283191382/
# datetime: Mon Dec  2 20:31:32 2019
# runtime: 68 ms
# memory: 13.1 MB

from functools import lru_cache
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # @lru_cache(None)
        # def dfs(k):
        #     res = 0
        #     if k <= 0:
        #         if K - k <= N:
        #             res = 1
        #         return res
        #     res = 1 / W * sum(dfs(k - w) for w in reversed(range(1, W + 1)))
        #     return res
        # return dfs(K)
        dp = [0] * (N + W + 1)
        for i in range(K, N + 1):
            dp[i] = 1.0
        p = sum(dp[K:K + W])
        for i in reversed(range(K)):
            dp[i] = 1 / W * p
            p = p - dp[i + W] + dp[i]
        return dp[0]