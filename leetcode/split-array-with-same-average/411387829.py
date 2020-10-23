# title: split-array-with-same-average
# detail: https://leetcode.com/submissions/detail/411387829/
# datetime: Wed Oct 21 15:57:38 2020
# runtime: 148 ms
# memory: 49.5 MB

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return False
        s = sum(A)
        candidates = set()
        for i in range(1, n // 2 + 1):
            q, r = divmod(i * s, n)
            if r == 0:
                candidates.add((i, q))
        @lru_cache(None)
        def dp(i, j, s):
            if j == 0 and s == 0:
                return True
            if i == n or j == 0 or s == 0:
                return False
            return dp(i + 1, j - 1, s - A[i]) or dp(i + 1, j, s)
        for i, q in candidates:
            if dp(0, i, q):
                return True
        return False
