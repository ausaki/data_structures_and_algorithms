# title: out-of-boundary-paths
# detail: https://leetcode.com/submissions/detail/283412397/
# datetime: Tue Dec  3 16:53:08 2019
# runtime: 76 ms
# memory: 18.7 MB

from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if i == -1 or i == m or j == -1 or j == n:
                return 1
            if k == 0:
                return 0
            p = dfs(i - 1, j, k - 1) + dfs(i + 1, j, k - 1) + dfs(i, j - 1, k - 1) + dfs(i, j + 1, k - 1)
            return p % (10 ** 9 + 7)
        
        return dfs(i, j, N)