# title: knight-probability-in-chessboard
# detail: https://leetcode.com/submissions/detail/288455412/
# datetime: Wed Dec 25 21:14:46 2019
# runtime: 132 ms
# memory: 22 MB

from functools import lru_cache
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        positions = [[1, -2], [1, 2], [2, -1], [2, 1], [-1, -2], [-1, 2], [-2, -1], [-2, 1]]
        
        @lru_cache(None)
        def dfs(i, j, k):
            if i < 0 or i >= N or j < 0 or j >= N:
                return 0
            if k == 0:
                return 1
            p = 0
            for ii, jj in positions:
                p += dfs(i + ii, j + jj, k - 1)
            return p / 8
        
        return dfs(r, c, K)