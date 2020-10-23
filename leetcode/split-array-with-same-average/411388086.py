# title: split-array-with-same-average
# detail: https://leetcode.com/submissions/detail/411388086/
# datetime: Wed Oct 21 15:58:33 2020
# runtime: 160 ms
# memory: 50.2 MB

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return False
        s = sum(A)
        @lru_cache(None)
        def dp(i, j, s):
            if j == 0 and s == 0:
                return True
            if i == n or j == 0 or s == 0:
                return False
            return dp(i + 1, j - 1, s - A[i]) or dp(i + 1, j, s)
        for i in range(1, n // 2 + 1):
            q, r = divmod(i * s, n)
            if r == 0 and dp(0, i, q):
                return True
        return False
