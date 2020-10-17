# title: knight-dialer
# detail: https://leetcode.com/submissions/detail/403817764/
# datetime: Sat Oct  3 15:22:19 2020
# runtime: 5836 ms
# memory: 43.7 MB

class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                return 1
            result = 0
            for di in [-2, -1, 1, 2]:
                for dj in [3 - abs(di), abs(di) - 3]:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n and not (ii == 3 and (jj == 0 or jj == 2)):
                        result = (result + dp(ii, jj, k - 1)) % MOD
            return result
        MOD = 10 ** 9 + 7
        k = n
        m, n = 4, 3
        result = 0
        for i in range(m):
            for j in range(n):
                if i == 3 and (j == 0 or j == 2):
                    continue
                result = (result + dp(i, j, k - 1)) % MOD
        return result