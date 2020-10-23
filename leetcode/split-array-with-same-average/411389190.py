# title: split-array-with-same-average
# detail: https://leetcode.com/submissions/detail/411389190/
# datetime: Wed Oct 21 16:02:42 2020
# runtime: 192 ms
# memory: 50.2 MB

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return False
        s = sum(A)
        @lru_cache(None)
        def dp(i, state):
            s, j = divmod(state, n)
            if j == 0 and s == 0:
                return True
            if i == n or j == 0 or s == 0:
                return False
            return dp(i + 1, (s - A[i]) * n + j - 1) or dp(i + 1, state)
        for i in range(1, n // 2 + 1):
            q, r = divmod(i * s, n)
            if r == 0 and dp(0, q * n + i):
                return True
        return False
