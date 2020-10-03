# title: delete-columns-to-make-sorted-iii
# detail: https://leetcode.com/submissions/detail/403006943/
# datetime: Thu Oct  1 14:35:23 2020
# runtime: 416 ms
# memory: 20.3 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            a = 1 + dp(i + 1, j)
            b = 10 ** 9
            if j == -1 or all(A[k][i] >= A[k][j] for k in range(m)):
                b = dp(i + 1, i)
            return min(a, b)
        
        m, n = len(A), len(A[0])
        return dp(0, -1)