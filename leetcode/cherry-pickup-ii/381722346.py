# title: cherry-pickup-ii
# detail: https://leetcode.com/submissions/detail/381722346/
# datetime: Sun Aug 16 21:25:06 2020
# runtime: 920 ms
# memory: 45.6 MB

from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def pick(i, c1, c2):
            if i == n or c1 < 0 or c1 >= m or c2 < 0 or c2 >= m:
                return 0
            result = 0
            for j in [-1, 0, 1]:
                for k in [-1, 0, 1]:
                    result = max(result, pick(i + 1, c1 + j, c2 + k))
            return result + grid[i][c1] + (grid[i][c2] if c1 != c2 else 0)
        
        n = len(grid)
        m = len(grid[0])
        return pick(0, 0, m - 1)