# title: minimum-moves-to-reach-target-with-rotations
# detail: https://leetcode.com/submissions/detail/395525214/
# datetime: Mon Sep 14 17:14:26 2020
# runtime: 340 ms
# memory: 24.7 MB

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m = n = len(grid)
        visited = {0}
        @lru_cache(None)
        def move(i, j, k, r):
            if i == m - 1 and j == n - 1 and k == 0:
                return 0
            result = 1e9
            if k == 0:
                if j + 1 < n and grid[i][j + 1] != 1:
                    result = min(result, 1 + move(i, j + 1, k, 0))
                if i + 1 < m and grid[i + 1][j] != 1 and grid[i + 1][j - 1] != 1:
                    result = min(result, 1 + move(i + 1, j, k, 0))
                    if not r:
                        result = min(result, 1 + move(i + 1, j - 1, 1, 1)) 
            else:
                if i + 1 < m and grid[i + 1][j] != 1:
                    result = min(result, 1 + move(i + 1, j, k, 0))
                if j + 1 < n and grid[i][j + 1] != 1 and grid[i - 1][j + 1] != 1:
                    result = min(result, 1 + move(i, j + 1, k, 0))
                    if not r:
                        result = min(result, 1 + move(i - 1, j + 1, 0, 1))
            return result
        
        result = move(0, 1, 0, 0)
        return result if result < 1e9 else -1