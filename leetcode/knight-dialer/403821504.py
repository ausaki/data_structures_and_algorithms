# title: knight-dialer
# detail: https://leetcode.com/submissions/detail/403821504/
# datetime: Sat Oct  3 15:34:15 2020
# runtime: 2428 ms
# memory: 45.6 MB

class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if k == 0:
                return 1
            result = 0
            for j in jump[i]:
                result = (result + dp(j, k - 1)) % MOD
            return result
        MOD = 10 ** 9 + 7
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [0, 1, 7], [2, 6], [1, 3], [2, 4], list(range(10))]
        return dp(10, n)
