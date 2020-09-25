# title: minimum-score-triangulation-of-polygon
# detail: https://leetcode.com/submissions/detail/400132131/
# datetime: Thu Sep 24 21:57:14 2020
# runtime: 148 ms
# memory: 14.5 MB

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j < i + 2:
                return 0
            result = 10 ** 9
            for k in range(i + 1, j):
                result = min(result, A[i] * A[k] * A[j] + dfs(i, k) + dfs(k, j))
            return result
        n = len(A)
        return dfs(0, n - 1)